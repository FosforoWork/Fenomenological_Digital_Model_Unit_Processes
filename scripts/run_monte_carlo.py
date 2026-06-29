#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Coordinador de Simulacion de Monte Carlo
Ejecuta los 3 escenarios del paper y reporta resultados consolidados.

USO:
    python -m scripts.run_monte_carlo            # Optimizado (default)
    python -m scripts.run_monte_carlo --baseline # Linea base
    python -m scripts.run_monte_carlo --full     # Todos los escenarios
"""

from __future__ import annotations

import argparse
import math
import random
import sys
import time

import numpy as np
from scipy import stats

from core.equipment_constraints import EquipmentCapacityError
from core.equipment_specs import (
    EQUIPMENT_SPEC_LIMITS,
    get_default_capacity_limits,
    get_default_equipment_specs,
)
from core.stage_equations import CONTROL_LIMITS, run_process_model


# --- Configuraciones de los escenarios ---

OPTIMIZED_RANGES = {
    "soy_feed_kg_h": (800.0, 1200.0),
    "water_flow_m3_h": (9.0, 15.0),
    "water_temp_c": (25.0, 95.0),
    "extraction_ph": (7.5, 10.0),
    "extraction_temp_c": (20.0, 95.0),
    "extraction_residence_min": (40.0, 110.0),
    "agitator_rpm": (10.0, 500.0),
    "solid_liquid_ratio": (3.0, 30.0),
    "pasteur_temp_c": (50.0, 140.0),
    "pasteur_retention_s": (2.0, 180.0),
    "evap_pressure_bar": (0.05, 1.20),
    "evap_temp_c": (15.0, 95.0),
    "ro_tmp_bar": (10.0, 45.0),
    "precip_ph": (3.8, 5.2),
    "precip_time_min": (2.0, 120.0),
    "centrifuge_g": (200.0, 5000.0),
    "centrifuge_time_min": (1.0, 120.0),
    "dryer_temp_c": (160.0, 220.0),
    "dryer_residence_min": (1.0, 180.0),
}

BASELINE_RANGES = {
    "soy_feed_kg_h": (500.0, 1800.0),
    "water_flow_m3_h": (5.0, 20.0),
    "water_temp_c": (5.0, 95.0),
    "extraction_ph": (7.0, 10.5),
    "extraction_temp_c": (10.0, 95.0),
    "extraction_residence_min": (20.0, 150.0),
    "agitator_rpm": (10.0, 500.0),
    "solid_liquid_ratio": (2.0, 30.0),
    "pasteur_temp_c": (40.0, 140.0),
    "pasteur_retention_s": (1.0, 200.0),
    "evap_pressure_bar": (0.03, 1.50),
    "evap_temp_c": (15.0, 100.0),
    "ro_tmp_bar": (10.0, 50.0),
    "precip_ph": (3.0, 6.0),
    "precip_time_min": (1.0, 150.0),
    "centrifuge_g": (100.0, 6000.0),
    "centrifuge_time_min": (0.5, 150.0),
    "dryer_temp_c": (100.0, 300.0),
    "dryer_residence_min": (0.5, 200.0),
}

BASELINE_SPECS = {
    "stage_0_tank_capacity_m3": 12.0,
    "stage_0_tank_reserve_factor": 1.20,
    "stage_0_pump_head_m": 10.7,
    "stage_0_pump_eta_hyd": 0.65,
    "stage_0_pump_eta_motor": 0.90,
    "stage_0_pump_motor_kw": 1.50,
    "stage_1_slurry_density_kg_m3": 1050.0,
    "stage_1_tank_capacity_m3": 12.0,
    "stage_1_tank_reserve_factor": 1.20,
    "stage_1_base_extraction_eff": 0.88,
    "stage_1_2_extract_recovery": 0.965,
    "stage_2_acid_addition_m3_h": 0.02,
    "stage_2_cp_kj_kgk": 3.9,
    "stage_2_hex_area_m2": 25.0,
    "stage_2_hex_u_w_m2k": 2000.0,
    "stage_2_hex_lmtd_c": 20.0,
    "stage_ro_pump_eta": 0.80,
    "stage_3_solids_to_protein_ratio": 1.715,
    "stage_3_steam_economy": 1.85,
    "stage_3_evap_capacity_m3_h": 8.0,
    "stage_4_base_precip_eff": 0.98,
    "stage_4_2_co_solids_kg_h": 0.0,
    "stage_4_2_base_moisture_frac": 0.50,
    "stage_4_2_centrifuge_capacity_m3_h": 3.0,
    "stage_5_dryer_evap_capacity_kg_h": 400.0,
    "stage_5_dryer_chamber_volume_m3": 36.5,
}


def run_monte_carlo(
    control_ranges: dict,
    equipment_specs: dict,
    capacity_limits: dict,
    num_batches: int = 30,
    runs_per_batch: int = 10000,
    label: str = "Simulacion",
    bypass_validation: bool = False,
):
    """Ejecuta una campana de Monte Carlo y reporta metricas completas."""
    import core.stage_equations as seq

    # Parchear CONTROL_LIMITS temporalmente si es necesario
    original_limits = dict(seq.CONTROL_LIMITS)
    if bypass_validation:
        seq.CONTROL_LIMITS = {k: (0.0, 1e9) for k in control_ranges}

    batch_success_rates = []
    total_successes = 0
    total_failures = 0
    failure_causes = {}
    validation_errors = 0

    start_time = time.time()

    for idx in range(num_batches):
        batch_seed = 42 + idx
        random.seed(batch_seed)
        batch_ok = 0
        batch_fail = 0

        for _ in range(runs_per_batch):
            controls = {}
            for key, (vmin, vmax) in control_ranges.items():
                controls[key] = random.uniform(vmin, vmax)

            try:
                run_process_model(controls, equipment_specs, capacity_limits)
                batch_ok += 1
            except EquipmentCapacityError as e:
                batch_fail += 1
                for issue in e.issues:
                    code = issue.get("code", "UNKNOWN")
                    failure_causes[code] = failure_causes.get(code, 0) + 1
            except (ValueError, TypeError) as e:
                batch_fail += 1
                validation_errors += 1
                failure_causes["VALIDATION_ERROR"] = (
                    failure_causes.get("VALIDATION_ERROR", 0) + 1
                )
            except Exception as e:
                batch_fail += 1
                failure_causes["OTHER"] = failure_causes.get("OTHER", 0) + 1

        total_successes += batch_ok
        total_failures += batch_fail
        rate = batch_ok / runs_per_batch
        batch_success_rates.append(rate)
        print(
            f"  Batch {idx:02d} (semilla {batch_seed}): "
            f"Exito {rate * 100:6.2f}% | Fallas {batch_fail:,}"
        )

    # Restaurar CONTROL_LIMITS
    seq.CONTROL_LIMITS = original_limits

    end_time = time.time()

    # --- Analisis estadistico ---
    rates = np.array(batch_success_rates)
    mean_rate = np.mean(rates)
    std_dev = np.std(rates, ddof=1)
    total_runs = num_batches * runs_per_batch
    global_rate = total_successes / total_runs

    # Sigma con regla de 3 para tasa perfecta
    if total_failures == 0:
        dpmo_upper = 3.0 / total_runs * 1_000_000
        z_score = stats.norm.ppf(1.0 - dpmo_upper / 1_000_000)
    else:
        dpmo_upper = None
        p_clamped = max(1e-15, min(global_rate, 1.0 - 1e-15))
        z_score = stats.norm.ppf(p_clamped)
    sigma_shifted = z_score + 1.5

    ci95_margin = 1.96 * std_dev / math.sqrt(num_batches)
    ci95_lower = max(0.0, mean_rate - ci95_margin)
    ci95_upper = min(1.0, mean_rate + ci95_margin)

    print()
    print("=" * 70)
    print(f"  RESULTADOS CONSOLIDADOS - {label}")
    print("=" * 70)
    print(f"  Tiempo de ejecucion: {end_time - start_time:.2f} s")
    print(f"  Corridas: {num_batches} x {runs_per_batch:,} = {total_runs:,}")
    print(f"  Exitos: {total_successes:,} / {total_runs:,}")
    print(f"  Tasa de exito promedio: {mean_rate * 100:.4f}%")
    print(f"  Desviacion estandar: {std_dev * 100:.4f}%")
    print(f"  Intervalo de confianza 95%: [{ci95_lower * 100:.4f}%, {ci95_upper * 100:.4f}%]")
    print(f"  Z-score: {z_score:.4f}")
    print(f"  Nivel Sigma (con shift 1.5): {sigma_shifted:.4f} sigma")
    print(f"  Nivel Sigma (sin shift): {z_score:.4f} sigma")
    print()
    print("  Fallas por codigo:")
    if failure_causes:
        for code, cnt in sorted(failure_causes.items(), key=lambda x: -x[1]):
            pct_run = cnt / total_runs * 100
            pct_fail = cnt / total_failures * 100 if total_failures else 0
            print(f"    [{code}]: {cnt:,} ({pct_run:.2f}% de corridas, {pct_fail:.2f}% de fallas)")
    else:
        print("    (Ninguna - estabilidad total)")
    print("=" * 70)

    return mean_rate, std_dev, sigma_shifted


def run_variable_design(runs: int = 200000):
    """Escenario 3: equipamiento variable dentro de limites fisicos."""
    import core.stage_equations as seq

    original_limits = dict(seq.CONTROL_LIMITS)
    seq.CONTROL_LIMITS = dict(CONTROL_LIMITS)

    caps = get_default_capacity_limits()
    total_ok = 0
    total_n = 0
    failure_causes = {}

    print(f"\n--- ESCENARIO 3: ANALISIS DE DISENO DIMENSIONAL ---")
    print(f"  Corridas: {runs:,} con equipamiento aleatorio\n")

    n_batches = 10
    runs_per = runs // n_batches
    random.seed(42)

    for b in range(n_batches):
        batch_ok = 0
        for _ in range(runs_per):
            controls = {}
            for key, (vmin, vmax) in CONTROL_LIMITS.items():
                controls[key] = random.uniform(vmin, vmax)
            specs = {}
            for key, (vmin, vmax) in EQUIPMENT_SPEC_LIMITS.items():
                specs[key] = random.uniform(vmin, vmax)
            try:
                run_process_model(controls, specs, caps)
                batch_ok += 1
            except EquipmentCapacityError as e:
                for issue in e.issues:
                    code = issue.get("code", "UNKNOWN")
                    failure_causes[code] = failure_causes.get(code, 0) + 1
            except Exception:
                failure_causes["OTHER"] = failure_causes.get("OTHER", 0) + 1
        total_ok += batch_ok
        total_n += runs_per
        print(f"  Batch {b:02d}: {batch_ok}/{runs_per} = {batch_ok / runs_per * 100:.2f}%")

    seq.CONTROL_LIMITS = original_limits

    rate = total_ok / total_n
    print(f"\n  Diseno Variable - Total: {total_ok:,}/{total_n:,} = {rate * 100:.4f}%")
    for code, cnt in sorted(failure_causes.items(), key=lambda x: -x[1]):
        print(f"    [{code}]: {cnt:,} ({cnt / total_n * 100:.2f}%)")

    return rate


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monte Carlo Gemelo Digital")
    parser.add_argument("--baseline", action="store_true", help="Ejecutar escenario base")
    parser.add_argument("--variable", action="store_true", help="Ejecutar diseno variable")
    parser.add_argument("--full", action="store_true", help="Ejecutar todos los escenarios")
    args = parser.parse_args()

    limits = get_default_capacity_limits()
    opt_specs = get_default_equipment_specs()

    print("=" * 70)
    print("  GEMELO DIGITAL - CAMPANA DE SIMULACION ESTOCASTICA")
    print("=" * 70)
    print(f"  Especificaciones de equipo optimizadas actuales:")
    for k, v in sorted(opt_specs.items()):
        print(f"    {k}: {v}")
    print()

    escenarios = []
    if args.baseline or args.full:
        escenarios.append(("baseline", True))
    if args.full:
        escenarios.append(("optimizado", True))
    if not args.baseline and not args.variable and not args.full:
        escenarios = [("optimizado", True)]

    for escenario, bypass in escenarios:
        if escenario == "baseline":
            print("#" * 70)
            print("#  ESCENARIO 1: DIAGNOSTICO ESTOCASTICO DE LINEA BASE")
            print("#" * 70)
            run_monte_carlo(
                BASELINE_RANGES,
                BASELINE_SPECS,
                limits,
                num_batches=10,
                runs_per_batch=10000,
                label="LINEA BASE (10x10,000 = 100,000 corridas)",
                bypass_validation=True,
            )
        elif escenario == "optimizado":
            print("#" * 70)
            print("#  ESCENARIO 2: VALIDACION DE ROBUSTEZ POST-OPTIMIZACION")
            print("#" * 70)
            run_monte_carlo(
                OPTIMIZED_RANGES,
                opt_specs,
                limits,
                num_batches=30,
                runs_per_batch=10000,
                label="ROBUSTEZ OPTIMIZADA (30x10,000 = 300,000 corridas)",
                bypass_validation=True,
            )

    if args.variable or args.full:
        run_variable_design(200000)
