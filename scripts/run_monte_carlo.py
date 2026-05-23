#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Coordinador de Simulación de Monte Carlo
Analiza la estabilidad estocástica del Gemelo Digital AJAX tras optimizar rangos.
"""

from __future__ import annotations

import time
import random
import math
import numpy as np
from scipy import stats

from core.stage_equations import run_process_model, CONTROL_LIMITS
from core.equipment_specs import get_default_equipment_specs, get_default_capacity_limits
from core.equipment_constraints import EquipmentCapacityError


def run_monte_carlo_simulation(num_batches: int = 30, runs_per_batch: int = 10000):
    print("======================================================================")
    print("           INICIANDO SIMULACIÓN DE MONTE CARLO - GEMELO DIGITAL        ")
    print("======================================================================")
    print(f"Configuración:")
    print(f"  - Batches independientes: {num_batches}")
    print(f"  - Corridas por batch: {runs_per_batch:,}")
    print(f"  - Corridas totales: {num_batches * runs_per_batch:,}")
    print("----------------------------------------------------------------------")

    # Cargar especificaciones y límites por defecto (con las mejoras aplicadas)
    specs = get_default_equipment_specs()
    limits = get_default_capacity_limits()

    batch_success_rates = []
    total_successes = 0
    total_failures = 0

    # Diccionario para rastrear los motivos de falla (códigos de restricción)
    failure_causes = {}
    validation_errors = 0

    start_time = time.time()

    for idx in range(num_batches):
        batch_seed = 42 + idx
        random.seed(batch_seed)
        np.random.seed(batch_seed)

        batch_successes = 0
        batch_failures = 0

        for run in range(runs_per_batch):
            # Generar controles aleatorios uniformes dentro de CONTROL_LIMITS
            controls = {}
            for key, (vmin, vmax) in CONTROL_LIMITS.items():
                controls[key] = random.uniform(vmin, vmax)

            try:
                run_process_model(controls, equipment_specs=specs, capacity_limits=limits)
                batch_successes += 1
                total_successes += 1
            except EquipmentCapacityError as e:
                batch_failures += 1
                total_failures += 1
                # Registrar causas de falla
                for issue in e.issues:
                    code = issue.get("code", "UNKNOWN")
                    failure_causes[code] = failure_causes.get(code, 0) + 1
            except ValueError as e:
                batch_failures += 1
                total_failures += 1
                validation_errors += 1
                err_str = str(e)
                failure_causes[err_str] = failure_causes.get(err_str, 0) + 1
            except Exception as e:
                batch_failures += 1
                total_failures += 1
                err_name = type(e).__name__
                failure_causes[err_name] = failure_causes.get(err_name, 0) + 1

        success_rate = batch_successes / runs_per_batch
        batch_success_rates.append(success_rate)
        print(f"Batch {idx:02d} (Semilla: {batch_seed}) -> Éxito: {success_rate * 100:6.2f}% | Fallas: {batch_failures:,}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # --- ANÁLISIS ESTADÍSTICO ---
    batch_success_rates = np.array(batch_success_rates)
    mean_success_rate = np.mean(batch_success_rates)
    
    # Desviación estándar muestral (ddof=1)
    std_dev = np.std(batch_success_rates, ddof=1)

    # Nivel Sigma Global
    # En Six Sigma, el nivel Sigma = Z-score + 1.5 (con el shift estándar de 1.5 Sigma para variación a largo plazo)
    # Z-score = ppf(tasa de éxito)
    global_success_rate = total_successes / (num_batches * runs_per_batch)
    
    # Prevenir divisiones o infinitos si la tasa es exactamente 0 o 1
    p_clamped = max(1e-10, min(global_success_rate, 1 - 1e-10))
    z_score = stats.norm.ppf(p_clamped)
    sigma_level_shifted = z_score + 1.5
    sigma_level_raw = z_score

    # Intervalo de confianza de la media al 95% usando la distribución Z (Normal Estándar)
    # IC = mean +- Z_0.025 * (s / sqrt(N))
    confidence_levels = [0.90, 0.95, 0.99]
    intervals = {}
    for cl in confidence_levels:
        alpha = 1 - cl
        z_val = stats.norm.ppf(1 - alpha / 2)
        margin_of_error = z_val * (std_dev / math.sqrt(num_batches))
        intervals[cl] = (mean_success_rate - margin_of_error, mean_success_rate + margin_of_error)

    print("\n" + "=" * 70)
    print("                     RESULTADOS CONSOLIDADOS                          ")
    print("=" * 70)
    print(f"Tiempo de ejecución total: {elapsed_time:.2f} segundos")
    print(f"Corridas Exitosas Totales: {total_successes:,} / {num_batches * runs_per_batch:,}")
    print(f"Tasa de Éxito Promedio (Media): {mean_success_rate * 100:.4f}%")
    print(f"Desviación Estándar Muestral (s): {std_dev * 100:.4f}% ({std_dev:.6f})")
    print("-" * 70)
    
    print("Nivel de Calidad Six Sigma:")
    print(f"  - Valor Z (Desviación Normal Estándar): {z_score:.4f}")
    print(f"  - Nivel Sigma Global (con desplazamiento de 1.5σ): {sigma_level_shifted:.4f} σ")
    print(f"  - Nivel Sigma Global (sin desplazamiento): {sigma_level_raw:.4f} σ")
    print("-" * 70)

    print("Intervalos de Confianza (Distribución Z para la media):")
    for cl, (lower, upper) in intervals.items():
        print(f"  - {cl * 100:.0f}% CI: [{lower * 100:.4f}%, {upper * 100:.4f}%] (Margen de error: { (upper-lower)/2*100:.4f}%)")
    print("-" * 70)

    print("Análisis de Fallas por Restricción Activa:")
    sorted_failures = sorted(failure_causes.items(), key=lambda item: item[1], reverse=True)
    if not sorted_failures:
        print("  Ninguna falla registrada. ¡Estabilidad estocástica perfecta (100% de éxito)!")
    else:
        for cause, count in sorted_failures:
            percentage_of_total_runs = (count / (num_batches * runs_per_batch)) * 100
            percentage_of_failures = (count / total_failures) * 100 if total_failures > 0 else 0
            print(f"  - [{cause}]: {count:,} veces ({percentage_of_total_runs:.3f}% de corridas totales | {percentage_of_failures:.2f}% de fallas)")
    print("======================================================================\n")


if __name__ == "__main__":
    run_monte_carlo_simulation()
