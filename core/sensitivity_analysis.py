"""Analisis de sensibilidad y gradientes para el Gemelo Digital."""

from __future__ import annotations

import copy
from core.stage_equations import run_process_model


def perform_sensitivity_analysis(
    controls: dict,
    equipment_specs: dict,
    capacity_limits: dict,
    target_variable: str = "stage_5_overall_yield_pct",
    perturbation_pct: float = 1.0,
) -> dict[str, float]:
    """
    Calcula el impacto de variar cada control en un % sobre una variable objetivo.
    Retorna un diccionario de 'sensibilidad' (dTarget / dControl * (Control/Target)).
    """
    base_result = run_process_model(controls, equipment_specs, capacity_limits)
    
    # Flatten results for easy access
    def get_val(res, target):
        parts = target.split("_", 1)
        if len(parts) == 2 and parts[0] in res:
            return res[parts[0]].get(parts[1], 0.0)
        return 0.0

    base_val = get_val(base_result, target_variable)
    if base_val == 0:
        return {}

    sensitivities = {}
    
    # Analizar controles
    for key, value in controls.items():
        if not isinstance(value, (int, float)) or value == 0:
            continue
            
        perturbed_controls = copy.deepcopy(controls)
        delta = value * (perturbation_pct / 100.0)
        perturbed_controls[key] = value + delta
        
        try:
            perturbed_result = run_process_model(perturbed_controls, equipment_specs, capacity_limits)
            perturbed_val = get_val(perturbed_result, target_variable)
            
            # Sensibilidad normalizada: (% cambio en target) / (% cambio en control)
            sensitivity = ((perturbed_val - base_val) / base_val) / (perturbation_pct / 100.0)
            sensitivities[f"ctrl_{key}"] = sensitivity
        except Exception:
            # Si la perturbacion causa un error de capacidad, la sensibilidad es 'infinita' o alta
            sensitivities[f"ctrl_{key}"] = float('nan')

    return sensitivities


def analyze_equipment_sensitivity(
    controls: dict,
    equipment_specs: dict,
    capacity_limits: dict,
    target_variable: str = "stage_5_powder_mass_kg_h",
    perturbation_pct: float = 5.0,
) -> dict[str, float]:
    """
    Analiza como afectan las dimensiones de los equipos a la capacidad productiva.
    """
    base_result = run_process_model(controls, equipment_specs, capacity_limits)
    
    def get_val(res, target):
        parts = target.split("_", 1)
        if len(parts) == 2 and parts[0] in res:
            return res[parts[0]].get(parts[1], 0.0)
        return 0.0

    base_val = get_val(base_result, target_variable)
    
    sensitivities = {}
    
    # Analizar especificaciones de equipo (dimensiones)
    for key, value in equipment_specs.items():
        if "capacity" not in key and "area" not in key and "volume" not in key and "kw" not in key:
            continue
            
        if not isinstance(value, (int, float)) or value == 0:
            continue
            
        perturbed_specs = copy.deepcopy(equipment_specs)
        delta = value * (perturbation_pct / 100.0)
        perturbed_specs[key] = value + delta
        
        try:
            perturbed_result = run_process_model(controls, perturbed_specs, capacity_limits)
            perturbed_val = get_val(perturbed_result, target_variable)
            
            sensitivity = ((perturbed_val - base_val) / base_val) / (perturbation_pct / 100.0)
            sensitivities[f"eq_{key}"] = sensitivity
        except Exception:
            sensitivities[f"eq_{key}"] = 0.0 # No afecta directamente al valor, quiza solo a la viabilidad

    return sensitivities
