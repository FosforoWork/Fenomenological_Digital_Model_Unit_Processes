"""Mapeo de variables tecnicas a nombres amigables para el operador."""

from __future__ import annotations

EQUIPMENT_SPEC_LABELS = {
    "stage_0_tank_capacity_m3": "Capacidad tanque agua (m3)",
    "stage_0_tank_reserve_factor": "Factor reserva tanque agua",
    "stage_0_pump_head_m": "Altura manometrica bomba (m)",
    "stage_0_pump_eta_hyd": "Eficiencia hidraulica bomba",
    "stage_0_pump_eta_motor": "Eficiencia motor bomba",
    "stage_0_pump_motor_kw": "Potencia nominal bomba (kW)",
    "stage_1_slurry_density_kg_m3": "Densidad lodo extraccion (kg/m3)",
    "stage_1_tank_capacity_m3": "Capacidad tanque extraccion (m3)",
    "stage_1_tank_reserve_factor": "Factor reserva tanque extraccion",
    "stage_1_base_extraction_eff": "Eficiencia base extraccion (frac)",
    "stage_1_2_extract_recovery": "Recuperacion base separacion primaria (frac)",
    "stage_2_acid_addition_m3_h": "Dosificacion acido (m3/h)",
    "stage_2_cp_kj_kgk": "Cp mezcla (kJ/kgK)",
    "stage_2_hex_area_m2": "Area de placas intercambiador (m2)",
    "stage_2_hex_u_w_m2k": "Coeficiente U intercambiador (W/m2K)",
    "stage_2_hex_lmtd_c": "LMTD diseno intercambiador (C)",
    "stage_2_5_ro_base_recovery": "Recuperacion base OI (frac)",
    "stage_2_5_ro_membrane_area_m2": "Area de membrana OI (m2)",
    "stage_3_solids_to_protein_ratio": "Relacion solidos/proteina evaporador",
    "stage_3_steam_economy": "Economia de vapor",
    "stage_3_evap_capacity_m3_h": "Capacidad evaporador (m3/h)",
    "stage_4_base_precip_eff": "Eficiencia base precipitacion (frac)",
    "stage_4_2_co_solids_kg_h": "Co-solidos post centrifuga (kg/h)",
    "stage_4_2_base_moisture_frac": "Humedad base pasta (frac)",
    "stage_4_2_centrifuge_capacity_m3_h": "Capacidad centrifuga (m3/h)",
    "stage_5_dryer_evap_capacity_kg_h": "Capacidad evaporativa secador (kg/h)",
    "stage_5_dryer_chamber_volume_m3": "Volumen camara secador (m3)",
}

CAPACITY_LIMIT_LABELS = {
    "tank_max_fill_fraction": "Maximo llenado tanque Etapa 0",
    "stage_1_tank_max_fill_fraction": "Maximo llenado tanque Etapa 1",
    "pump_max_load_fraction": "Maximo uso motor bomba",
    "stage_2_hex_max_thermal_load_fraction": "Maximo uso termico intercambiador",
    "stage_2_hex_min_area_m2": "Area minima eficiente intercambiador (m2)",
    "stage_2_hex_max_area_m2": "Area maxima eficiente intercambiador (m2)",
    "stage_2_5_ro_min_flux_lmh": "Flujo minimo OI (LMH)",
    "stage_2_5_ro_max_flux_lmh": "Flujo maximo OI (LMH)",
    "stage_3_evap_max_load_fraction": "Maximo uso evaporador",
    "stage_4_2_centrifuge_max_load_fraction": "Maximo uso centrifuga",
    "stage_5_dryer_max_load_fraction": "Maximo uso secador",
    "stage_5_max_powder_rate_kg_h_m3": "Maximo polvo por volumen secador (kg/h/m3)",
}

CONTROL_LABELS = {
    "soy_feed_kg_h": "Alimentacion de soya (kg/h)",
    "water_flow_m3_h": "Caudal de agua (m3/h)",
    "water_temp_c": "Temperatura de agua (C)",
    "extraction_ph": "pH extraccion",
    "extraction_temp_c": "Temperatura extraccion (C)",
    "extraction_residence_min": "Tiempo residencia (min)",
    "agitator_rpm": "Velocidad agitacion (RPM)",
    "solid_liquid_ratio": "Ratio solido/liquido (1:x)",
    "pasteur_temp_c": "Temperatura de pasteurizacion (C)",
    "pasteur_retention_s": "Retencion termica (s)",
    "ro_tmp_bar": "TMP OI (bar)",
    "ro_crossflow_ms": "Velocidad cruzada OI (m/s)",
    "ro_feed_temp_c": "Temperatura alimentacion OI (C)",
    "ro_feed_ph": "pH alimentacion OI",
    "ro_sdi": "SDI",
    "evap_pressure_bar": "Presion evaporador (bar abs)",
    "evap_temp_c": "Temperatura evaporacion (C)",
    "precip_ph": "pH de precipitacion",
    "precip_time_min": "Tiempo de precipitacion (min)",
    "centrifuge_g": "Factor G centrifuga",
    "centrifuge_time_min": "Tiempo centrifugacion (min)",
    "dryer_temp_c": "Temperatura de secado (C)",
    "dryer_residence_min": "Residencia en secador (min)",
}

ALL_LABELS = {**EQUIPMENT_SPEC_LABELS, **CAPACITY_LIMIT_LABELS, **CONTROL_LABELS}

def get_friendly_name(key: str) -> str:
    """Retorna el nombre amigable de una variable tecnica."""
    return ALL_LABELS.get(key, key)
