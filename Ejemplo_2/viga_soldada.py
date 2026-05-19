"""
EJERCICIO 2 - Optimización multiobjetivo de una viga soldada

INSTRUCCIONES PARA EL EJERCICIO

1. Escribí tus iniciales abajo (variable INICIALES).
2. Elegí tu RECETA de parámetros: POBLACION, N_GEN, PC, PM, SEMILLA.
   No copiés la del compañero. Defendé la tuya.
3. Corré el script. Vas a obtener:
     - un gráfico de tu frente de Pareto en (costo, deflexión)
     - un CSV con los puntos de tu frente
     - un resumen de info en la pantalla (tomar captura)
4. Comparen entre todos.

"""

import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize


# ============================================================================
# TU RECETA - editá estos valores
# ============================================================================
INICIALES = "XYZ"
POBLACION =
N_GEN     = 
PC        =
PM        =
SEMILLA   = 
# ============================================================================


# --- Constantes físicas (SI, no tocar) ---------------------------------------
P       = 26_700.0     # N, carga aplicada
L       = 0.356       # m, distancia al extremo libre
E       = 207e9        # Pa, módulo de elasticidad del acero
G       = 82.7e9       # Pa, módulo de cortante
TAU_MAX = 93.8e6       # Pa, cortante admisible en la soldadura
SIG_MAX = 207e6        # Pa, flexión admisible en la barra

# Costos unitarios (USD por m^3 de material depositado).
C_SOLD = 67400.0      # USD/m^3, costo de soldadura
C_MAT  = 2940.0       # USD/m^3, costo del material base


def tension_cortante(h, l, t):
    """Tensión cortante combinada en la soldadura (primaria + secundaria) [Pa]."""
    tau_p  = P / (np.sqrt(2.0) * h * l)                          # cortante primaria
    M      = P * (L + l / 2.0)                                   # momento aplicado
    R      = np.sqrt(l**2 / 4.0 + ((h + t) / 2.0) ** 2)          # brazo al extremo
    J      = 2.0 * (h * l / np.sqrt(2.0)) * (l**2 / 12.0
                                              + ((h + t) / 2.0) ** 2)
    tau_pp = M * R / J                                           # cortante secundaria
    return np.sqrt(tau_p**2 + 2.0 * tau_p * tau_pp * (l / (2.0 * R)) + tau_pp**2)


def tension_flexion(t, b):
    """Tensión de flexión en la barra [Pa]."""
    return 6.0 * P * L / (b * t**2)


def deflexion(t, b):
    """Deflexión del extremo libre [m]."""
    return 4.0 * P * L**3 / (E * t**3 * b)


def carga_critica(t, b):
    """Carga crítica de pandeo [N]."""
    fac = 4.013 * E * np.sqrt(t**2 * b**6 / 36.0) / L**2
    return fac * (1.0 - (t / (2.0 * L)) * np.sqrt(E / (4.0 * G)))


def costo(h, l, t, b):
    """Costo total: soldadura (volumen ≈ h^2·l) + material (volumen ≈ t·b·(L+l)) [USD]."""
    return C_SOLD * h**2 * l + C_MAT * t * b * (L + l)


# --- Problema NSGA-II --------------------------------------------------------

class VigaSoldada(ElementwiseProblem):
    def __init__(self):
        super().__init__(
            n_var=4, n_obj=2, n_ieq_constr=4,
            xl=np.array([0.003,  0.0025, 0.0025, 0.003]),    # m
            xu=np.array([0.130,  0.250,  0.250,  0.130]),    # m
        )

    def _evaluate(self, x, out, *args, **kwargs):
        h, l, t, b = x

        f1 = costo(h, l, t, b)
        f2 = deflexion(t, b)

        g1 = tension_cortante(h, l, t) - TAU_MAX
        g2 = tension_flexion(t, b)     - SIG_MAX
        g3 = h - b
        g4 = P - carga_critica(t, b)

        out["F"] = [f1, f2]
        out["G"] = [g1, g2, g3, g4]


# --- Corrida y resumen -------------------------------------------------------

def correr_nsga2(pop_size, n_gen, pc, pm, seed):
    problem = VigaSoldada()
    algorithm = NSGA2(pop_size=pop_size)
    algorithm.mating.crossover.prob = pc
    algorithm.mating.mutation.prob = pm
    res = minimize(problem, algorithm, ("n_gen", n_gen),
                   seed=seed, verbose=False, save_history=False)
    return res


def imprimir_resumen(res):
    F = res.F
    print()
    print("=" * 60)
    print(f"  Iniciales:    {INICIALES}")
    print(f"  Receta:       pob={POBLACION}, gen={N_GEN}, "
          f"pc={PC}, pm={PM}, semilla={SEMILLA}")
    print(f"  Evaluaciones: {res.algorithm.evaluator.n_eval}")
    print("-" * 60)
    if F is None or len(F) == 0:
        print("  FRENTE VACÍO: ninguna solución factible encontrada.")
        print("  Revisá tu receta. Probá más generaciones o más población.")
    else:
        i_min_costo = int(np.argmin(F[:, 0]))
        i_min_def   = int(np.argmin(F[:, 1]))
        print(f"  Soluciones factibles no dominadas: {len(F)}")
        print(f"  Mínimo costo:     ${F[i_min_costo, 0]:8.3f}  "
              f"(deflexión = {F[i_min_costo, 1]*1000:.3f} mm)")
        print(f"  Mínima deflexión: {F[i_min_def, 1]*1000:8.3f} mm  "
              f"(costo = ${F[i_min_def, 0]:.3f})")
    print("=" * 60)


def guardar_csv(res):
    if res.F is None or len(res.F) == 0:
        print(f"\n[no se guardó CSV: frente vacío]")
        return None
    nombre = f"frente_{INICIALES}.csv"
    encabezado = ("# Frente de Pareto - viga soldada (SI)\n"
                  f"# iniciales={INICIALES}, pob={POBLACION}, gen={N_GEN}, "
                  f"pc={PC}, pm={PM}, semilla={SEMILLA}\n"
                  "costo_USD,deflexion_m")
    np.savetxt(nombre, res.F, delimiter=",", header=encabezado, comments="")
    print(f"\n[guardado: {nombre}]")
    return nombre


# --- Gráfico -----------------------------------------------------------------

def graficar(res, mostrar_referencia=False):
    fig, ax = plt.subplots(figsize=(8, 6))

    # Población final completa, separada en factible / infactible.
    # Mostramos deflexión en mm para que los números sean legibles.
    pop_F = res.pop.get("F")
    pop_G = res.pop.get("G")
    factibles = np.all(pop_G <= 0, axis=1)

    if np.any(~factibles):
        ax.scatter(pop_F[~factibles, 0], pop_F[~factibles, 1] * 1000,
                   c="lightgray", s=15, alpha=0.5,
                   label="población final infactible")

    if res.F is not None and len(res.F) > 0:
        ax.scatter(res.F[:, 0], res.F[:, 1] * 1000,
                   c="tab:blue", s=30, alpha=0.85,
                   edgecolor="navy", linewidth=0.5,
                   label=f"tu frente ({INICIALES})")

    if mostrar_referencia:
        ruta_ref = os.path.join(os.path.dirname(__file__) or ".", "referencia.npy")
        if os.path.exists(ruta_ref):
            ref = np.load(ruta_ref)
            ax.scatter(ref[:, 0], ref[:, 1] * 1000,
                       c="tab:red", s=8, alpha=0.6,
                       label="referencia (pop=200, gen=500)")
        else:
            print(f"[advertencia: no se encontró {ruta_ref}; "
                  "no se puede mostrar la referencia]")

    ax.set_xlabel("Costo (USD)")
    ax.set_ylabel("Deflexión (mm)")
    ax.set_title(f"Frente de Pareto - viga soldada (SI)\n"
                 f"receta: pob={POBLACION}, gen={N_GEN}, "
                 f"pc={PC}, pm={PM}, semilla={SEMILLA}")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)
    #ax.set_xscale("log")
    #ßax.set_yscale("log")

    nombre = f"frente_{INICIALES}.png"
    plt.tight_layout()
    plt.savefig(nombre, dpi=120)
    plt.show()
    print(f"[guardado: {nombre}]")


# --- Punto de entrada --------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Optimización multiobjetivo de una viga soldada (SI)."
    )
    parser.add_argument("--mostrar-referencia", action="store_true",
                        help="superpone el frente de referencia escondido")
    args = parser.parse_args()

    if INICIALES == "XYZ":
        print("ATENCIÓN: editá la variable INICIALES en el script "
              "antes de correr.\n")

    res = correr_nsga2(POBLACION, N_GEN, PC, PM, SEMILLA)
    imprimir_resumen(res)
    guardar_csv(res)
    graficar(res, mostrar_referencia=args.mostrar_referencia)


if __name__ == "__main__":
    main()
