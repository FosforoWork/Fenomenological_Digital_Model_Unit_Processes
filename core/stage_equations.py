"""Ecuaciones simplificadas por etapa para la sala de control."""

from __future__ import annotations

import math

from core.equipment_constraints import enforce_capacity_constraints
from core.equipment_specs import (
    get_default_capacity_limits,
    get_default_equipment_specs,
    validate_capacity_limits,
    validate_equipment_specs,
)

# Constantes Fisicoquimicas (Doc 2.2)
RHO_EXTRACT = 1050.0 # kg/m3
CP_EXTRACT = 3.9     # kJ/(kg.K)
F_LOSS = 0.02        # Factor de perdida por etapa (Doc 3.1 - 3.6)

BASELINE_REFERENCES = {
    "ctrl_water_flow_m3_h": {"label": "Caudal de agua", "value": 12.0, "unit": "m3/h"},
    "stage_1_extraction_eff_pct": {"label": "Eficiencia extraccion", "value": 88.0, "unit": "%"},
    "ctrl_pasteur_temp_c": {"label": "Temperatura pasteurizacion", "value": 80.0, "unit": "C"},
    "ctrl_pasteur_retention_s": {"label": "Retencion termica", "value": 22.0, "unit": "s"},
    "ctrl_evap_pressure_bar": {"label": "Presion evaporador", "value": 0.40, "unit": "bar"},
    "stage_3_evaporated_water_m3_h": {"label": "Agua evaporada", "value": 9.42, "unit": "m3/h"},
    "stage_4_protein_precip_kg_h": {"label": "Proteina precipitada", "value": 292.3, "unit": "kg/h"},
    "stage_4_2_paste_mass_kg_h": {"label": "Pasta post-centrifuga", "value": 584.7, "unit": "kg/h"},
    "stage_5_powder_mass_kg_h": {"label": "Polvo final", "value": 301.6, "unit": "kg/h"},
    "stage_5_protein_final_kg_h": {"label": "Proteina final", "value": 286.5, "unit": "kg/h"},
    "stage_5_overall_yield_pct": {"label": "Rendimiento global", "value": 76.4, "unit": "%"},
}


CONTROL_LIMITS: dict[str, tuple[float, float]] = {
    "soy_feed_kg_h": (100.0, 8000.0),
    "water_flow_m3_h": (2.0, 30.0),
    "water_temp_c": (5.0, 90.0),
    "extraction_ph": (6.0, 12.0),
    "extraction_temp_c": (20.0, 95.0),
    "extraction_residence_min": (5.0, 180.0),
    "agitator_rpm": (10.0, 500.0),
    "solid_liquid_ratio": (4.0, 30.0),
    "pasteur_temp_c": (50.0, 130.0),
    "pasteur_retention_s": (2.0, 180.0),
    "evap_pressure_bar": (0.05, 1.20),
    "evap_temp_c": (20.0, 95.0),
    "ro_tmp_bar": (15.0, 40.0),
    "precip_ph": (2.5, 7.0),
    "precip_time_min": (2.0, 120.0),
    "centrifuge_g": (200.0, 5000.0),
    "centrifuge_time_min": (1.0, 120.0),
    "dryer_temp_c": (40.0, 220.0),
    "dryer_residence_min": (1.0, 180.0),
}


def _clip(value: float, vmin: float, vmax: float) -> float:
    return max(vmin, min(value, vmax))


def validate_controls(controls: dict) -> None:
    """Valida presencia, tipo y rango fisico de variables de control."""
    missing = [key for key in CONTROL_LIMITS if key not in controls]
    if missing:
        raise KeyError(f"Faltan controles obligatorios: {', '.join(missing)}")

    for key, (vmin, vmax) in CONTROL_LIMITS.items():
        value = controls[key]
        if not isinstance(value, (int, float)):
            raise TypeError(f"Control '{key}' debe ser numerico, recibido {type(value).__name__}")
        if not math.isfinite(value):
            raise ValueError(f"Control '{key}' no es finito")
        if value < vmin or value > vmax:
            raise ValueError(f"Control '{key}' fuera de rango [{vmin}, {vmax}]: {value}")


def calc_stage_0(controls: dict, equipment_specs: dict) -> dict:
    soy_feed_kg_h = controls["soy_feed_kg_h"]
    water_flow_m3_h = controls["water_flow_m3_h"]
    water_temp_c = controls["water_temp_c"]

    water_kg_h = water_flow_m3_h * 1000.0
    tank_volume_m3 = water_flow_m3_h * equipment_specs["stage_0_tank_reserve_factor"]

    rho = 1000.0
    g = 9.81
    q_m3_s = water_flow_m3_h / 3600.0
    head_m = equipment_specs["stage_0_pump_head_m"]
    eta_total = equipment_specs["stage_0_pump_eta_hyd"] * equipment_specs["stage_0_pump_eta_motor"]
    pump_kw = (rho * g * q_m3_s * head_m) / (1000.0 * eta_total)

    protein_in_kg_h = soy_feed_kg_h * 0.375

    return {
        "soy_feed_kg_h": soy_feed_kg_h,
        "water_flow_m3_h": water_flow_m3_h,
        "water_temp_c": water_temp_c,
        "water_kg_h": water_kg_h,
        "tank_volume_m3": tank_volume_m3,
        "tank_capacity_m3": equipment_specs["stage_0_tank_capacity_m3"],
        "pump_kw": pump_kw,
        "protein_in_kg_h": protein_in_kg_h,
    }


def calc_stage_1(controls: dict, stage_0: dict, equipment_specs: dict) -> dict:
    ph = controls["extraction_ph"]
    temp_c = controls["extraction_temp_c"]
    residence_min = controls["extraction_residence_min"]
    rpm = controls["agitator_rpm"]
    ratio = controls["solid_liquid_ratio"]

    # --- FRONTERAS DE FALLA (Doc 10.2) ---
    # pH < 8.0: Falla masiva de hidratacion. pH > 9.5: Hidrolisis severa y toxicidad.
    if ph < 8.0:
        ph_factor = _clip(0.50 + (ph - 6.0) * 0.15, 0.10, 0.70)
    elif ph > 9.5:
        ph_factor = _clip(0.95 - (ph - 9.5) * 0.30, 0.40, 0.95)
    else:
        ph_factor = _clip(1.0 - 0.05 * abs(ph - 8.75), 0.90, 1.0)

    # Temp < 40C: Cinetica lenta. Temp > 75C: Desnaturalizacion prematura.
    if temp_c < 45.0:
        temp_factor = _clip(0.60 + (temp_c - 20.0) * 0.015, 0.30, 0.90)
    elif temp_c > 75.0:
        temp_factor = _clip(0.90 - (temp_c - 75.0) * 0.04, 0.20, 0.90)
    else:
        temp_factor = _clip(1.0 - 0.005 * abs(temp_c - 55.0), 0.95, 1.0)

    # TOC: tau < 60 min reduce drásticamente el rendimiento (Doc 10.1)
    if residence_min < 60.0:
        time_factor = _clip(residence_min / 60.0, 0.10, 1.0)
    else:
        time_factor = _clip(1.0 + (residence_min - 60.0) * 0.001, 1.0, 1.05)

    ratio_factor = _clip(1.0 - 0.05 * abs(ratio - 12.0), 0.50, 1.0)
    
    base_eff = equipment_specs["stage_1_base_extraction_eff"]
    extraction_eff = _clip(base_eff * ph_factor * temp_factor * time_factor * ratio_factor, 0.05, 0.98)

    protein_solubilized_theory_kg_h = stage_0["protein_in_kg_h"] * extraction_eff
    
    # Doc 3.1: Aplicacion de realismo F_LOSS en protein solubilized
    protein_solubilized_real_kg_h = protein_solubilized_theory_kg_h * (1.0 - F_LOSS)
    protein_lost_okara_kg_h = stage_0["protein_in_kg_h"] - protein_solubilized_real_kg_h
    
    # Doc 3.7: Inyeccion de NaOH 20% p/p (60 kg/h para 1000 kg/h soya) en TK-101
    soy_ref = 1000.0
    naoh_sol_ref = 60.0
    soy_feed = stage_0["soy_feed_kg_h"]
    naoh_solution_mass_kg_h = naoh_sol_ref * (soy_feed / soy_ref)

    total_in_kg_h = stage_0["soy_feed_kg_h"] + stage_0["water_kg_h"] + naoh_solution_mass_kg_h
    # Doc 3.1: Perdida del 2% por retencion
    merma_kg_h = total_in_kg_h * F_LOSS
    slurry_flow_kg_h = total_in_kg_h - merma_kg_h

    return {
        "extraction_eff_pct": extraction_eff * 100.0,
        "protein_extracted_kg_h": protein_solubilized_real_kg_h,
        "protein_lost_okara_kg_h": protein_lost_okara_kg_h,
        "slurry_flow_kg_h": slurry_flow_kg_h,
        "naoh_solution_mass_kg_h": naoh_solution_mass_kg_h,
        "merma_kg_h": merma_kg_h,
    }


def calc_stage_1_2(stage_0: dict, stage_1: dict, equipment_specs: dict) -> dict:
    extract_recovery = equipment_specs["stage_1_2_extract_recovery"]
    
    # Doc 3.2: Clarificado extraido (11,095 kg/h para base 1000 soya + 12000 agua)
    # Factor de proporcionalidad
    soy_ref = 1000.0
    extract_ref = 11095.0
    soy_feed = stage_0["soy_feed_kg_h"]
    extract_mass_theoretical_kg_h = extract_ref * (soy_feed / soy_ref)
    
    # Aplicar perdida operacional Doc 3.2
    merma_kg_h = extract_mass_theoretical_kg_h * F_LOSS
    extract_mass_net_kg_h = extract_mass_theoretical_kg_h - merma_kg_h
    
    # Okara es el remanente (Doc 3.2: ~1645 kg/h)
    okara_wet_kg_h = stage_1["slurry_flow_kg_h"] - extract_mass_net_kg_h - merma_kg_h
    
    # Proteina en extracto clarificado (Doc 3.2: 316.9 kg/h)
    # Viene de S1 y sufre otra merma en S1.2
    protein_in_extract_kg_h = stage_1["protein_extracted_kg_h"] * (1.0 - F_LOSS)

    return {
        "extract_recovery_pct": extract_recovery * 100.0,
        "extract_flow_m3_h": extract_mass_net_kg_h / RHO_EXTRACT,
        "extract_mass_net_kg_h": extract_mass_net_kg_h,
        "okara_wet_kg_h": okara_wet_kg_h,
        "protein_in_extract_kg_h": protein_in_extract_kg_h,
        "merma_kg_h": merma_kg_h,
    }


def calc_stage_2(controls: dict, stage_1_2: dict, equipment_specs: dict) -> dict:
    pasteur_temp_c = controls["pasteur_temp_c"]
    pasteur_retention_s = controls["pasteur_retention_s"]

    # --- FRONTERAS DE FALLA (Doc 10.2) ---
    # T < 75C: Peligro HACCP. T > 95C: Desnaturalizacion total.
    if pasteur_temp_c < 75.0:
        quality_penalty = _clip(0.40 + (pasteur_temp_c - 50.0) * 0.02, 0.10, 0.90) # Falla por inocuidad
    elif pasteur_temp_c > 95.0:
        quality_penalty = _clip(0.90 - (pasteur_temp_c - 95.0) * 0.08, 0.05, 0.90) # Falla por daño termico
    else:
        quality_penalty = 1.0

    in_mass_kg_h = stage_1_2["extract_mass_net_kg_h"]
    merma_kg_h = in_mass_kg_h * F_LOSS
    mass_kg_h = in_mass_kg_h - merma_kg_h
    
    cp_kj_kgk = equipment_specs["stage_2_cp_kj_kgk"]
    delta_t = max(0.0, pasteur_temp_c - 25.0)
    heat_mj_h = mass_kg_h * cp_kj_kgk * delta_t / 1000.0

    protein_after_pasteur_kg_h = stage_1_2["protein_in_extract_kg_h"] * quality_penalty * (1.0 - F_LOSS)

    return {
        "mass_kg_h": mass_kg_h,
        "heat_required_mj_h": heat_mj_h,
        "protein_quality_factor": quality_penalty,
        "protein_after_pasteur_kg_h": protein_after_pasteur_kg_h,
        "merma_kg_h": merma_kg_h,
    }


def calc_stage_ro(controls: dict, stage_2: dict, equipment_specs: dict) -> dict:
    """Etapa de Osmosis Inversa (OI) - Salto Innovador Doc 5.0."""
    ro_tmp_bar = controls.get("ro_tmp_bar", 24.0)
    
    # Doc 5.2: Permeado extraido: 2,718.3 kg/h para 1000 kg/h soya a 24 bar
    # Simplificacion: Permeado proporcional a presion (TMP) y flujo de alimentacion
    soy_ref = 1000.0
    permeate_ref = 2718.3
    tmp_ref = 24.0
    
    soy_feed = stage_2.get("soy_feed_kg_h", 1000.0)
    
    # Capacidad proporcional a TMP (lineal para fines del gemelo)
    tmp_factor = _clip(ro_tmp_bar / tmp_ref, 0.5, 1.5)
    permeate_theoretical_kg_h = permeate_ref * (soy_feed / soy_ref) * tmp_factor
    
    # Limitar permeado a la masa disponible (maximo 60% de extraccion de agua)
    in_mass_kg_h = stage_2["mass_kg_h"]
    permeate_kg_h = min(permeate_theoretical_kg_h, in_mass_kg_h * 0.60)
    
    retentate_mass_kg_h = in_mass_kg_h - permeate_kg_h
    
    # Consumo bomba OI: Q * dP / eta
    # Q in m3/s, dP in Pa
    q_m3_h = in_mass_kg_h / 1050.0  # Approx density
    q_m3_s = q_m3_h / 3600.0
    dp_pa = ro_tmp_bar * 100000.0
    eta_pump = equipment_specs.get("stage_ro_pump_eta", 0.80)
    pump_power_kw = (q_m3_s * dp_pa) / (1000.0 * eta_pump)
    
    # Ahorro termico: Calor latente del agua evaporada que nos evitamos
    # ~2260 kJ/kg = 2.26 MJ/kg / 3.6 = 0.627 kW/(kg/h) -> approx 1000 kW for 2718 kg/h
    thermal_saved_kw = permeate_kg_h * (2260.0 / 3600.0)
    
    return {
        "permeate_kg_h": permeate_kg_h,
        "retentate_mass_kg_h": retentate_mass_kg_h,
        "pump_power_kw": pump_power_kw,
        "thermal_saved_kw": thermal_saved_kw,
        "ro_tmp_bar": ro_tmp_bar,
    }


def calc_stage_3(controls: dict, stage_ro: dict, equipment_specs: dict) -> dict:
    evap_pressure_bar = controls["evap_pressure_bar"]
    evap_temp_c = controls["evap_temp_c"]

    # --- FRONTERAS DE FALLA (Doc 10.2) ---
    # P > 0.60 bar abs: Reaccion de Maillard (Pardeamiento)
    if evap_pressure_bar > 0.60:
        maillard_penalty = _clip(1.0 - (evap_pressure_bar - 0.60) * 1.5, 0.10, 1.0)
    else:
        maillard_penalty = 1.0

    evap_feed_mass_kg_h = stage_ro["retentate_mass_kg_h"]
    merma_kg_h = evap_feed_mass_kg_h * F_LOSS
    evap_feed_mass_net_kg_h = evap_feed_mass_kg_h - merma_kg_h
    
    protein_to_evap_kg_h = stage_ro.get("protein_after_pasteur_kg_h", 0.0) * maillard_penalty * (1.0 - F_LOSS)
    solids_kg_h = protein_to_evap_kg_h * equipment_specs["stage_3_solids_to_protein_ratio"]

    target_solids_frac = _clip(0.23 + (0.40 - evap_pressure_bar) * 0.05 + (evap_temp_c - 55.0) * 0.001, 0.18, 0.30)
    concentrate_flow_m3_h = solids_kg_h / (target_solids_frac * 1000.0)

    evaporator_boiling_removed_m3_h = _clip(
        (evap_feed_mass_net_kg_h / 1000.0) - concentrate_flow_m3_h,
        0.0,
        evap_feed_mass_net_kg_h / 1000.0,
    )
    evaporated_water_m3_h = evaporator_boiling_removed_m3_h

    steam_economy = equipment_specs["stage_3_steam_economy"]
    steam_required_kg_h = evaporator_boiling_removed_m3_h * 1000.0 / steam_economy

    return {
        "target_solids_pct": target_solids_frac * 100.0,
        "concentrate_flow_m3_h": concentrate_flow_m3_h,
        "evaporated_water_m3_h": evaporated_water_m3_h,
        "evaporator_boiling_removed_m3_h": evaporator_boiling_removed_m3_h,
        "steam_required_kg_h": steam_required_kg_h,
        "evap_feed_m3_h": evap_feed_mass_net_kg_h / 1000.0,
        "protein_to_evap_kg_h": protein_to_evap_kg_h,
        "merma_kg_h": merma_kg_h,
    }


def calc_stage_4(controls: dict, stage_3: dict, equipment_specs: dict) -> dict:
    precip_ph = controls["precip_ph"]
    precip_time_min = controls["precip_time_min"]

    # --- FRONTERAS DE FALLA (Doc 10.2) ---
    # pI 4.5 es el pozo matematico. Desviacion > 0.4 unidades re-disuelve proteina.
    if abs(precip_ph - 4.5) > 0.4:
        precip_penalty = _clip(1.0 - (abs(precip_ph - 4.5) - 0.4) * 2.0, 0.05, 1.0)
    else:
        precip_penalty = 1.0

    soy_ref = 1000.0
    hcl_sol_ref = 110.0
    soy_feed = stage_3.get("soy_feed_kg_h", 1000.0)
    hcl_solution_mass_kg_h = hcl_sol_ref * (soy_feed / soy_ref)

    base_eff = equipment_specs["stage_4_base_precip_eff"]
    precip_eff = _clip(base_eff * precip_penalty, 0.05, 0.995)

    protein_precip_kg_h = stage_3["protein_to_evap_kg_h"] * precip_eff * (1.0 - F_LOSS)
    
    total_feed_kg_h = stage_3["concentrate_flow_m3_h"] * 1000.0 + hcl_solution_mass_kg_h
    merma_kg_h = total_feed_kg_h * F_LOSS
    
    floc_um = _clip(320.0 - abs(precip_ph - 4.5) * 250.0 + (precip_time_min - 25.0) * 1.8, 20.0, 500.0)

    return {
        "precip_eff_pct": precip_eff * 100.0,
        "protein_precip_kg_h": protein_precip_kg_h,
        "floc_size_um": floc_um,
        "slurry_precip_m3_h": (total_feed_kg_h - merma_kg_h) / 1000.0,
        "hcl_solution_mass_kg_h": hcl_solution_mass_kg_h,
        "merma_kg_h": merma_kg_h,
    }


def calc_stage_4_2(controls: dict, stage_3: dict, stage_4: dict, equipment_specs: dict) -> dict:
    centrifuge_g = controls["centrifuge_g"]
    centrifuge_time_min = controls["centrifuge_time_min"]

    g_factor = _clip(1.0 - abs(centrifuge_g - 1800.0) / 3000.0, 0.70, 1.0)
    time_factor = _clip(1.0 - abs(centrifuge_time_min - 20.0) * 0.01, 0.75, 1.0)
    solids_recovery = _clip(1.0 * g_factor * time_factor, 0.90, 1.000)

    protein_paste_kg_h = stage_4["protein_precip_kg_h"] * solids_recovery
    co_solids_kg_h = equipment_specs["stage_4_2_co_solids_kg_h"]
    dry_solids_paste_kg_h = protein_paste_kg_h + co_solids_kg_h
    
    base_moisture_frac = equipment_specs["stage_4_2_base_moisture_frac"]
    paste_moisture_frac = _clip(
        base_moisture_frac - (centrifuge_g - 1800.0) * 0.00002 - (centrifuge_time_min - 20.0) * 0.001,
        0.45,
        0.60,
    )
    paste_mass_kg_h = dry_solids_paste_kg_h / (1.0 - paste_moisture_frac)
    whey_flow_m3_h = _clip(stage_4["slurry_precip_m3_h"] - (paste_mass_kg_h / 1000.0), 0.2, 10.0)

    return {
        "solids_recovery_pct": solids_recovery * 100.0,
        "protein_paste_kg_h": protein_paste_kg_h,
        "co_solids_kg_h": co_solids_kg_h,
        "dry_solids_paste_kg_h": dry_solids_paste_kg_h,
        "paste_moisture_pct": paste_moisture_frac * 100.0,
        "paste_mass_kg_h": paste_mass_kg_h,
        "whey_flow_m3_h": whey_flow_m3_h,
    }


def calc_stage_5(controls: dict, stage_0: dict, stage_4_2: dict) -> dict:
    dryer_temp_c = controls["dryer_temp_c"]
    dryer_residence_min = controls["dryer_residence_min"]

    final_moisture = _clip(0.05 - (dryer_temp_c - 78.0) * 0.0007 - (dryer_residence_min - 42.0) * 0.0006, 0.03, 0.14)
    
    # Doc 3.6: operational loss (2%) in spray drying
    protein_final_kg_h = stage_4_2["protein_paste_kg_h"] * (1.0 - F_LOSS)
    powder_mass_theoretical_kg_h = stage_4_2["dry_solids_paste_kg_h"] / (1.0 - final_moisture)
    
    merma_kg_h = powder_mass_theoretical_kg_h * F_LOSS
    powder_mass_kg_h = powder_mass_theoretical_kg_h - merma_kg_h
    
    dryer_water_removed_kg_h = stage_4_2["paste_mass_kg_h"] - powder_mass_theoretical_kg_h
    overall_yield_pct = (protein_final_kg_h / stage_0["protein_in_kg_h"]) * 100.0

    return {
        "final_moisture_pct": final_moisture * 100.0,
        "protein_final_kg_h": protein_final_kg_h,
        "powder_mass_kg_h": powder_mass_kg_h,
        "dryer_water_removed_kg_h": dryer_water_removed_kg_h,
        "overall_yield_pct": overall_yield_pct,
        "merma_kg_h": merma_kg_h,
    }


def run_process_model(
    controls: dict,
    equipment_specs: dict | None = None,
    capacity_limits: dict | None = None,
) -> dict:
    """Ejecuta todas las etapas en cascada (0 -> 5)."""
    validate_controls(controls)
    specs = validate_equipment_specs(equipment_specs or get_default_equipment_specs())
    limits = validate_capacity_limits(capacity_limits or get_default_capacity_limits())

    soy_feed = controls["soy_feed_kg_h"]

    stage_0 = calc_stage_0(controls, specs)
    stage_0["soy_feed_kg_h"] = soy_feed

    stage_1 = calc_stage_1(controls, stage_0, specs)
    stage_1["soy_feed_kg_h"] = soy_feed

    stage_1_2 = calc_stage_1_2(stage_0, stage_1, specs)
    stage_1_2["soy_feed_kg_h"] = soy_feed

    stage_2 = calc_stage_2(controls, stage_1_2, specs)
    stage_2["soy_feed_kg_h"] = soy_feed

    stage_ro = calc_stage_ro(controls, stage_2, specs)
    stage_ro["soy_feed_kg_h"] = soy_feed
    # Ensure protein carries over
    stage_ro["protein_after_pasteur_kg_h"] = stage_2["protein_after_pasteur_kg_h"]

    stage_3 = calc_stage_3(controls, stage_ro, specs)
    stage_3["soy_feed_kg_h"] = soy_feed

    stage_4 = calc_stage_4(controls, stage_3, specs)
    stage_4["soy_feed_kg_h"] = soy_feed

    stage_4_2 = calc_stage_4_2(controls, stage_3, stage_4, specs)
    stage_4_2["soy_feed_kg_h"] = soy_feed

    stage_5 = calc_stage_5(controls, stage_0, stage_4_2)
    stage_5["soy_feed_kg_h"] = soy_feed

    numeric_checks = [
        stage_0["water_kg_h"],
        stage_1["protein_extracted_kg_h"],
        stage_2["protein_after_pasteur_kg_h"],
        stage_3["protein_to_evap_kg_h"],
        stage_4["protein_precip_kg_h"],
        stage_4_2["paste_mass_kg_h"],
        stage_5["powder_mass_kg_h"],
    ]
    if any((not math.isfinite(val) or val < 0.0) for val in numeric_checks):
        raise ValueError("Integridad invalida: se detectaron valores no finitos o negativos en resultados")

    # Accurate mass balance closure including chemical additions (Doc 3.7)
    mass_in_kg_h = (
        stage_0["soy_feed_kg_h"] 
        + stage_0["water_kg_h"] 
        + stage_1.get("naoh_solution_mass_kg_h", 0.0) 
        + stage_4.get("hcl_solution_mass_kg_h", 0.0)
    )
    
    # Cumulative losses
    total_mermas_kg_h = (
        stage_1["merma_kg_h"]
        + stage_1_2["merma_kg_h"]
        + stage_2["merma_kg_h"]
        + stage_3["merma_kg_h"]
        + stage_4["merma_kg_h"]
        + stage_5["merma_kg_h"]
    )
    
    mass_out_kg_h = (
        stage_1_2["okara_wet_kg_h"]
        + stage_ro["permeate_kg_h"]
        + stage_3["evaporated_water_m3_h"] * 1000.0
        + stage_4_2["whey_flow_m3_h"] * 1000.0
        + stage_5["powder_mass_kg_h"]
        + stage_5["dryer_water_removed_kg_h"]
        + total_mermas_kg_h
    )
    
    mass_balance_error_pct = ((mass_out_kg_h - mass_in_kg_h) / mass_in_kg_h) * 100.0
    mass_balance_closure_pct = 100.0 - abs(mass_balance_error_pct)

    integrity = {
        "mass_in_kg_h": mass_in_kg_h,
        "mass_out_kg_h": mass_out_kg_h,
        "mass_balance_error_pct": mass_balance_error_pct,
        "mass_balance_closure_pct": mass_balance_closure_pct,
        "total_mermas_kg_h": total_mermas_kg_h,
    }

    result = {
        "stage_0": stage_0,
        "stage_1": stage_1,
        "stage_1_2": stage_1_2,
        "stage_2": stage_2,
        "stage_ro": stage_ro,
        "stage_3": stage_3,
        "stage_4": stage_4,
        "stage_4_2": stage_4_2,
        "stage_5": stage_5,
        "integrity": integrity,
    }

    capacity = enforce_capacity_constraints(
        controls=controls,
        equipment_specs=specs,
        capacity_limits=limits,
        result=result,
    )
    result["capacity"] = capacity

    return result
