"""Configuracion de dimensiones de equipos y umbrales de capacidad."""

from __future__ import annotations

import math


EQUIPMENT_SPEC_DEFAULTS: dict[str, float] = {
    "stage_0_tank_capacity_m3": 15.0,
    "stage_0_tank_reserve_factor": 1.20,
    "stage_0_pump_head_m": 10.7,
    "stage_0_pump_eta_hyd": 0.65,
    "stage_0_pump_eta_motor": 0.90,
    "stage_0_pump_motor_kw": 1.50,
    "stage_1_slurry_density_kg_m3": 1060.0,
    "stage_1_tank_capacity_m3": 16.0,
    "stage_1_tank_reserve_factor": 1.20,
    "stage_1_base_extraction_eff": 0.88,
    "stage_1_2_extract_recovery": 0.965,
    "stage_2_acid_addition_m3_h": 0.02,
    "stage_2_cp_kj_kgk": 4.10,
    "stage_2_hex_area_m2": 40.0,
    "stage_2_hex_u_w_m2k": 3000.0,
    "stage_2_hex_lmtd_c": 20.0,
    "stage_ro_pump_eta": 0.80,
    "stage_3_solids_to_protein_ratio": 1.715,
    "stage_3_steam_economy": 1.85,
    "stage_3_evap_capacity_m3_h": 12.0,
    "stage_4_base_precip_eff": 0.98,
    "stage_4_2_co_solids_kg_h": 0.0,
    "stage_4_2_base_moisture_frac": 0.50,
    "stage_4_2_centrifuge_capacity_m3_h": 3.0,
    "stage_5_dryer_evap_capacity_kg_h": 400.0,
    "stage_5_dryer_chamber_volume_m3": 36.5,
}


EQUIPMENT_SPEC_LIMITS: dict[str, tuple[float, float]] = {
    "stage_0_tank_capacity_m3": (4.0, 80.0),
    "stage_0_tank_reserve_factor": (1.0, 1.6),
    "stage_0_pump_head_m": (5.0, 40.0),
    "stage_0_pump_eta_hyd": (0.45, 0.90),
    "stage_0_pump_eta_motor": (0.60, 0.98),
    "stage_0_pump_motor_kw": (0.50, 30.0),
    "stage_1_slurry_density_kg_m3": (950.0, 1250.0),
    "stage_1_tank_capacity_m3": (4.0, 120.0),
    "stage_1_tank_reserve_factor": (1.0, 1.6),
    "stage_1_base_extraction_eff": (0.70, 0.98),
    "stage_1_2_extract_recovery": (0.85, 0.995),
    "stage_2_acid_addition_m3_h": (0.0, 0.50),
    "stage_2_cp_kj_kgk": (2.0, 6.0),
    "stage_2_hex_area_m2": (5.0, 120.0),
    "stage_2_hex_u_w_m2k": (150.0, 3500.0),
    "stage_2_hex_lmtd_c": (2.0, 60.0),
    "stage_ro_pump_eta": (0.40, 0.95),
    "stage_3_solids_to_protein_ratio": (1.1, 2.5),
    "stage_3_steam_economy": (1.1, 3.0),
    "stage_3_evap_capacity_m3_h": (1.0, 40.0),
    "stage_4_base_precip_eff": (0.80, 0.999),
    "stage_4_2_co_solids_kg_h": (0.0, 200.0),
    "stage_4_2_base_moisture_frac": (0.40, 0.75),
    "stage_4_2_centrifuge_capacity_m3_h": (0.2, 20.0),
    "stage_5_dryer_evap_capacity_kg_h": (20.0, 3000.0),
    "stage_5_dryer_chamber_volume_m3": (3.0, 250.0),
}


CAPACITY_LIMIT_DEFAULTS: dict[str, float] = {
    "tank_max_fill_fraction": 0.96,
    "stage_1_tank_max_fill_fraction": 0.92,
    "pump_max_load_fraction": 0.90,
    "stage_2_hex_max_thermal_load_fraction": 0.90,
    "stage_2_hex_min_area_m2": 15.0,
    "stage_2_hex_max_area_m2": 80.0,
    "stage_3_evap_max_load_fraction": 0.92,
    "stage_4_2_centrifuge_max_load_fraction": 0.90,
    "stage_5_dryer_max_load_fraction": 0.90,
    "stage_5_max_powder_rate_kg_h_m3": 18.0,
}


CAPACITY_LIMIT_BOUNDS: dict[str, tuple[float, float]] = {
    "tank_max_fill_fraction": (0.60, 0.99),
    "stage_1_tank_max_fill_fraction": (0.60, 0.99),
    "pump_max_load_fraction": (0.50, 1.00),
    "stage_2_hex_max_thermal_load_fraction": (0.50, 1.00),
    "stage_2_hex_min_area_m2": (5.0, 120.0),
    "stage_2_hex_max_area_m2": (5.0, 180.0),
    "stage_3_evap_max_load_fraction": (0.50, 1.00),
    "stage_4_2_centrifuge_max_load_fraction": (0.50, 1.00),
    "stage_5_dryer_max_load_fraction": (0.50, 1.00),
    "stage_5_max_powder_rate_kg_h_m3": (2.0, 80.0),
}


def _validate_values(values: dict[str, float], bounds: dict[str, tuple[float, float]], label: str) -> dict[str, float]:
    missing = [key for key in bounds if key not in values]
    if missing:
        raise KeyError(f"Faltan parametros en {label}: {', '.join(missing)}")

    validated: dict[str, float] = {}
    for key, (vmin, vmax) in bounds.items():
        value = values[key]
        if not isinstance(value, (int, float)):
            raise TypeError(f"Parametro '{key}' en {label} debe ser numerico")
        fvalue = float(value)
        if not math.isfinite(fvalue):
            raise ValueError(f"Parametro '{key}' en {label} no es finito")
        if fvalue < vmin or fvalue > vmax:
            raise ValueError(f"Parametro '{key}' en {label} fuera de rango [{vmin}, {vmax}]: {fvalue}")
        validated[key] = fvalue

    return validated


def get_default_equipment_specs() -> dict[str, float]:
    return {key: float(value) for key, value in EQUIPMENT_SPEC_DEFAULTS.items()}


def get_default_capacity_limits() -> dict[str, float]:
    return {key: float(value) for key, value in CAPACITY_LIMIT_DEFAULTS.items()}


def validate_equipment_specs(specs: dict[str, float]) -> dict[str, float]:
    return _validate_values(specs, EQUIPMENT_SPEC_LIMITS, label="equipment_specs")


def validate_capacity_limits(limits: dict[str, float]) -> dict[str, float]:
    validated = _validate_values(limits, CAPACITY_LIMIT_BOUNDS, label="capacity_limits")
    if validated["stage_2_hex_max_area_m2"] <= validated["stage_2_hex_min_area_m2"]:
        raise ValueError("stage_2_hex_max_area_m2 debe ser mayor que stage_2_hex_min_area_m2")
    return validated
