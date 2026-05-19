"""
EXPERIMENTO 5 - Cómo evoluciona el frente de Pareto a lo largo de las generaciones

Para experimentar
- Modificá SNAPSHOT_GENS.
- Probá una población muy chica (10) y una grande (200) y comparen
  tanto la velocidad de convergencia como la uniformidad del
  esparcimiento.
"""

import matplotlib.pyplot as plt
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

from problem import TwoPointSquared, decorate_panel


# ----- Parámetros ajustables --------------------------------------------------
SNAPSHOT_GENS = [1, 100]
SEED          = 1
POBLACION     = 40
PC            = 0.9
PM            = 0.1
# ------------------------------------------------------------------------------


def run_until(n_gen):
    problem = TwoPointSquared()
    algorithm = NSGA2(pop_size=POBLACION)
    algorithm.mating.crossover.prob = PC
    algorithm.mating.mutation.prob = PM
    res = minimize(problem, algorithm, ("n_gen", n_gen), seed=SEED, verbose=False)
    # Mostramos la población COMPLETA (no sólo el frente no dominado) para
    # que los estudiantes vean el "enjambre" en cada fotografía.
    pop_X = res.pop.get("X")
    pop_F = res.pop.get("F")
    return pop_X, pop_F


def main():
    fig, axes = plt.subplots(2, len(SNAPSHOT_GENS),
                             figsize=(3.5 * len(SNAPSHOT_GENS), 7))
    fig.suptitle(f"Experimento 5: evolución de la población a lo largo de las generaciones  "
                 f"(semilla={SEED}, pob={POBLACION}, pc={PC}, pm={PM})")

    for col, g in enumerate(SNAPSHOT_GENS):
        X, F = run_until(g)
        ax_d = axes[0, col]
        ax_o = axes[1, col]
        decorate_panel(ax_d, ax_o)

        ax_d.scatter(X[:, 0], X[:, 1], c="tab:blue", s=15, alpha=0.7)
        ax_o.scatter(F[:, 0], F[:, 1], c="tab:blue", s=15, alpha=0.7)

        # Reescalamos automáticamente el espacio de objetivos cuando los
        # puntos caen fuera del cuadro estándar (típicamente en las
        # primeras generaciones, cuando f1, f2 todavía son enormes).
        f_max_here = max(F[:, 0].max(), F[:, 1].max())
        if f_max_here > 9.0:
            lim = f_max_here * 1.05
            ax_o.set_xlim(-0.5, lim)
            ax_o.set_ylim(-0.5, lim)

        ax_d.set_title(f"gen = {g}")
        if col != 0:
            ax_d.set_ylabel(""); ax_o.set_ylabel("")

    plt.tight_layout()
    plt.savefig("experimento_5_generaciones.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
