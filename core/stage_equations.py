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


BASELINE_REFERENCES = {
    "ctrl_water_flow_m3_h": {"label": "Caudal de agua", "value": 12.0, "unit": "m3/h"},
    "stage_1_extraction_eff_pct": {"label": "Eficiencia extraccion", "value": 88.0, "unit": "%"},
    "ctrl_pasteur_temp_c": {"label": "Temperatura pasteurizacion", "value": 80.0, "unit": "C"},
    "ctrl_pasteur_retention_s": {"label": "Retencion termica", "value": 22.0, "unit": "s"},
    "stage_2_5_ro_ro_recovery_pct": {"label": "Recuperacion OI", "value": 25.0, "unit": "%"},
    "ctrl_evap_pressure_bar": {"label": "Presion evaporador", "value": 0.40, "unit": "bar"},
    "stage_3_evaporated_water_m3_h": {"label": "Agua evaporada", "value": 9.939, "unit": "m3/h"},
    "stage_4_protein_precip_kg_h": {"label": "Proteina precipitada", "value": 323.4, "unit": "kg/h"},
    "stage_4_2_paste_mass_kg_h": {"label": "Pasta post-centrifuga", "value": 692.8, "unit": "kg/h"},
    "stage_5_powder_mass_kg_h": {"label": "Polvo final", "value": 364.6, "unit": "kg/h"},
    "stage_5_protein_final_kg_h": {"label": "Proteina final", "value": 323.4, "unit": "kg/h"},
    "stage_5_final_moisture_pct": {"label": "Humedad final", "value": 5.0, "unit": "%"},
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
    "ro_tmp_bar": (5.0, 45.0),
    "ro_crossflow_ms": (0.2, 3.0),
    "ro_feed_temp_c": (5.0, 60.0),
    "ro_feed_ph": (3.0, 11.0),
    "ro_sdi": (1.0, 8.0),
    "evap_pressure_bar": (0.05, 1.20),
    "evap_temp_c": (20.0, 95.0),
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

    base_eff = equipment_specs["stage_1_base_extraction_eff"]
    ph_factor = _clip(1.0 - 0.08 * abs(ph - 8.75), 0.85, 1.0)
    temp_factor = _clip(1.0 - 0.015 * abs(temp_c - 55.0), 0.75, 1.0)
    time_factor = _clip(1.0 - 0.008 * abs(residence_min - 54.0), 0.80, 1.0)
    rpm_factor = _clip(1.0 - 0.0015 * abs(rpm - 80.0), 0.80, 1.0)
    ratio_factor = _clip(1.0 - 0.03 * abs(ratio - 12.0), 0.75, 1.0)

    extraction_eff = _clip(
        base_eff * ph_factor * temp_factor * time_factor * rpm_factor * ratio_factor,
        0.70,
        0.95,
    )

    protein_extracted_kg_h = stage_0["protein_in_kg_h"] * extraction_eff
    protein_lost_okara_kg_h = stage_0["protein_in_kg_h"] - protein_extracted_kg_h
    slurry_flow_kg_h = stage_0["soy_feed_kg_h"] + stage_0["water_kg_h"]

    return {
        "extraction_eff_pct": extraction_eff * 100.0,
        "protein_extracted_kg_h": protein_extracted_kg_h,
        "protein_lost_okara_kg_h": protein_lost_okara_kg_h,
        "slurry_flow_kg_h": slurry_flow_kg_h,
    }


def calc_stage_1_2(stage_0: dict, stage_1: dict, equipment_specs: dict) -> dict:
    extract_recovery = equipment_specs["stage_1_2_extract_recovery"]
    extract_flow_m3_h = stage_0["water_flow_m3_h"] * extract_recovery + 0.82
    okara_wet_kg_h = _clip(stage_1["slurry_flow_kg_h"] - (extract_flow_m3_h * 1000.0), 300.0, 2000.0)
    protein_in_extract_kg_h = stage_1["protein_extracted_kg_h"]

    return {
        "extract_recovery_pct": extract_recovery * 100.0,
        "extract_flow_m3_h": extract_flow_m3_h,
        "okara_wet_kg_h": okara_wet_kg_h,
        "protein_in_extract_kg_h": protein_in_extract_kg_h,
    }


def calc_stage_2(controls: dict, stage_1_2: dict, equipment_specs: dict) -> dict:
    pasteur_temp_c = controls["pasteur_temp_c"]
    pasteur_retention_s = controls["pasteur_retention_s"]

    acid_addition_m3_h = equipment_specs["stage_2_acid_addition_m3_h"]
    neutralized_flow_m3_h = stage_1_2["extract_flow_m3_h"] + acid_addition_m3_h

    mass_kg_h = neutralized_flow_m3_h * 1000.0
    cp_kj_kgk = equipment_specs["stage_2_cp_kj_kgk"]
    delta_t = max(0.0, pasteur_temp_c - 25.0)
    heat_mj_h = mass_kg_h * cp_kj_kgk * delta_t / 1000.0

    under_temp_penalty = max(0.0, 78.0 - pasteur_temp_c) * 0.008
    over_temp_penalty = max(0.0, pasteur_temp_c - 90.0) * 0.009
    under_time_penalty = max(0.0, 18.0 - pasteur_retention_s) * 0.010
    over_time_penalty = max(0.0, pasteur_retention_s - 35.0) * 0.004
    quality_factor = _clip(1.0 - under_temp_penalty - over_temp_penalty - under_time_penalty - over_time_penalty, 0.90, 1.0)

    protein_after_pasteur_kg_h = stage_1_2["protein_in_extract_kg_h"] * quality_factor

    return {
        "neutralized_flow_m3_h": neutralized_flow_m3_h,
        "heat_required_mj_h": heat_mj_h,
        "protein_quality_factor": quality_factor,
        "protein_after_pasteur_kg_h": protein_after_pasteur_kg_h,
    }


def calc_stage_2_5_ro(controls: dict, stage_2: dict, equipment_specs: dict) -> dict:
    ro_tmp_bar = controls["ro_tmp_bar"]
    ro_crossflow_ms = controls["ro_crossflow_ms"]
    ro_feed_temp_c = controls["ro_feed_temp_c"]
    ro_feed_ph = controls["ro_feed_ph"]
    ro_sdi = controls["ro_sdi"]

    tmp_factor = _clip(1.0 + (ro_tmp_bar - 24.0) * 0.018, 0.60, 1.50)
    crossflow_factor = _clip(1.0 - abs(ro_crossflow_ms - 1.50) * 0.18, 0.70, 1.10)
    temp_factor = _clip(1.0 + (ro_feed_temp_c - 28.0) * 0.010, 0.80, 1.15)
    ph_factor = _clip(1.0 - abs(ro_feed_ph - 7.00) * 0.06, 0.75, 1.05)
    sdi_factor = _clip(1.0 - max(0.0, ro_sdi - 3.0) * 0.12, 0.50, 1.05)

    base_recovery = equipment_specs["stage_2_5_ro_base_recovery"]
    recovery_frac = _clip(
        base_recovery * tmp_factor * crossflow_factor * temp_factor * ph_factor * sdi_factor,
        0.10,
        0.45,
    )

    feed_flow_m3_h = stage_2["neutralized_flow_m3_h"]
    permeate_flow_m3_h = feed_flow_m3_h * recovery_frac
    retentate_flow_m3_h = feed_flow_m3_h - permeate_flow_m3_h

    retention_penalty = max(0.0, ro_sdi - 4.0) * 0.004 + max(0.0, abs(ro_feed_ph - 7.0) - 1.0) * 0.003
    protein_retention_frac = _clip(1.0 - retention_penalty, 0.970, 1.000)
    protein_to_evap_kg_h = stage_2["protein_after_pasteur_kg_h"] * protein_retention_frac

    heat_relief_kw = permeate_flow_m3_h * 1000.0 * 2257.0 / 3600.0

    return {
        "ro_recovery_pct": recovery_frac * 100.0,
        "permeate_flow_m3_h": permeate_flow_m3_h,
        "retentate_flow_m3_h": retentate_flow_m3_h,
        "protein_retention_pct": protein_retention_frac * 100.0,
        "protein_to_evap_kg_h": protein_to_evap_kg_h,
        "evap_heat_relief_kw": heat_relief_kw,
    }


def calc_stage_3(controls: dict, stage_2_5_ro: dict, equipment_specs: dict) -> dict:
    evap_pressure_bar = controls["evap_pressure_bar"]
    evap_temp_c = controls["evap_temp_c"]

    solids_kg_h = stage_2_5_ro["protein_to_evap_kg_h"] * equipment_specs["stage_3_solids_to_protein_ratio"]

    target_solids_frac = _clip(0.23 + (0.40 - evap_pressure_bar) * 0.05 + (evap_temp_c - 55.0) * 0.001, 0.18, 0.30)
    concentrate_flow_m3_h = solids_kg_h / (target_solids_frac * 1000.0)
    evaporator_boiling_removed_m3_h = _clip(
        stage_2_5_ro["retentate_flow_m3_h"] - concentrate_flow_m3_h,
        0.0,
        stage_2_5_ro["retentate_flow_m3_h"],
    )
    evaporated_water_m3_h = evaporator_boiling_removed_m3_h + stage_2_5_ro["permeate_flow_m3_h"]

    steam_economy = equipment_specs["stage_3_steam_economy"]
    steam_required_kg_h = evaporator_boiling_removed_m3_h * 1000.0 / steam_economy

    return {
        "target_solids_pct": target_solids_frac * 100.0,
        "concentrate_flow_m3_h": concentrate_flow_m3_h,
        "evaporated_water_m3_h": evaporated_water_m3_h,
        "evaporator_boiling_removed_m3_h": evaporator_boiling_removed_m3_h,
        "steam_required_kg_h": steam_required_kg_h,
        "evap_feed_m3_h": stage_2_5_ro["retentate_flow_m3_h"],
    }


def calc_stage_4(controls: dict, stage_2_5_ro: dict, stage_3: dict, equipment_specs: dict) -> dict:
    precip_ph = controls["precip_ph"]
    precip_time_min = controls["precip_time_min"]

    base_eff = equipment_specs["stage_4_base_precip_eff"]
    ph_factor = _clip(1.0 - 0.25 * abs(precip_ph - 4.5), 0.70, 1.0)
    time_factor = _clip(1.0 - 0.01 * abs(precip_time_min - 25.0), 0.75, 1.0)
    precip_eff = _clip(base_eff * ph_factor * time_factor, 0.85, 0.995)

    protein_precip_kg_h = stage_2_5_ro["protein_to_evap_kg_h"] * precip_eff
    floc_um = _clip(320.0 - abs(precip_ph - 4.5) * 110.0 + (precip_time_min - 25.0) * 1.8, 120.0, 500.0)

    return {
        "precip_eff_pct": precip_eff * 100.0,
        "protein_precip_kg_h": protein_precip_kg_h,
        "floc_size_um": floc_um,
        "slurry_precip_m3_h": stage_3["concentrate_flow_m3_h"] * 1.01,
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
    whey_flow_m3_h = _clip(stage_3["concentrate_flow_m3_h"] - (paste_mass_kg_h / 1000.0), 0.2, 10.0)

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
    protein_final_kg_h = stage_4_2["protein_paste_kg_h"]
    powder_mass_kg_h = stage_4_2["dry_solids_paste_kg_h"] / (1.0 - final_moisture)
    dryer_water_removed_kg_h = stage_4_2["paste_mass_kg_h"] - powder_mass_kg_h
    overall_yield_pct = (protein_final_kg_h / stage_0["protein_in_kg_h"]) * 100.0

    return {
        "final_moisture_pct": final_moisture * 100.0,
        "protein_final_kg_h": protein_final_kg_h,
        "powder_mass_kg_h": powder_mass_kg_h,
        "dryer_water_removed_kg_h": dryer_water_removed_kg_h,
        "overall_yield_pct": overall_yield_pct,
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

    stage_0 = calc_stage_0(controls, specs)
    stage_1 = calc_stage_1(controls, stage_0, specs)
    stage_1_2 = calc_stage_1_2(stage_0, stage_1, specs)
    stage_2 = calc_stage_2(controls, stage_1_2, specs)
    stage_2_5_ro = calc_stage_2_5_ro(controls, stage_2, specs)
    stage_3 = calc_stage_3(controls, stage_2_5_ro, specs)
    stage_4 = calc_stage_4(controls, stage_2_5_ro, stage_3, specs)
    stage_4_2 = calc_stage_4_2(controls, stage_3, stage_4, specs)
    stage_5 = calc_stage_5(controls, stage_0, stage_4_2)

    numeric_checks = [
        stage_0["water_kg_h"],
        stage_1["protein_extracted_kg_h"],
        stage_2["protein_after_pasteur_kg_h"],
        stage_2_5_ro["protein_to_evap_kg_h"],
        stage_3["evaporated_water_m3_h"],
        stage_4["protein_precip_kg_h"],
        stage_4_2["paste_mass_kg_h"],
        stage_5["powder_mass_kg_h"],
    ]
    if any((not math.isfinite(val) or val < 0.0) for val in numeric_checks):
        raise ValueError("Integridad invalida: se detectaron valores no finitos o negativos en resultados")

    mass_in_kg_h = stage_0["soy_feed_kg_h"] + stage_0["water_kg_h"]
    mass_out_kg_h = (
        stage_1_2["okara_wet_kg_h"]
        + stage_3["evaporated_water_m3_h"] * 1000.0
        + stage_4_2["whey_flow_m3_h"] * 1000.0
        + stage_5["powder_mass_kg_h"]
        + stage_5["dryer_water_removed_kg_h"]
    )
    mass_balance_error_pct = ((mass_out_kg_h - mass_in_kg_h) / mass_in_kg_h) * 100.0
    mass_balance_closure_pct = 100.0 - abs(mass_balance_error_pct)

    integrity = {
        "mass_in_kg_h": mass_in_kg_h,
        "mass_out_kg_h": mass_out_kg_h,
        "mass_balance_error_pct": mass_balance_error_pct,
        "mass_balance_closure_pct": mass_balance_closure_pct,
    }

    result = {
        "stage_0": stage_0,
        "stage_1": stage_1,
        "stage_1_2": stage_1_2,
        "stage_2": stage_2,
        "stage_2_5_ro": stage_2_5_ro,
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
