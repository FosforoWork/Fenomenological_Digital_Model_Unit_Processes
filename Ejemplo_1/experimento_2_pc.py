"""
EXPERIMENTO 2 - Efecto de la probabilidad de cruce pc

- 'pureza'    = fracción de puntos devueltos que efectivamente caen sobre
                el frente analítico (con tolerancia 1e-2).
- 'cobertura' = rango cubierto, normalizado de modo que 1.0 = frente
                completo.

Para experimentar
- Modificá PC_VALUES.
- Bajá aún más N_GEN (a 5, por ejemplo) para acentuar las diferencias.
"""

import numpy as np
import matplotlib.pyplot as plt
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

from problem import TwoPointSquared, decorate_panel, purity, coverage


# ----- Parámetros ajustables --------------------------------------------------
PC_VALUES = [0.1, 1]
N_SEEDS   = 1
POBLACION = 40
N_GEN     = 10
PM        = 0.1
# ------------------------------------------------------------------------------


def run_one(pc, seed):
    problem = TwoPointSquared()
    algorithm = NSGA2(pop_size=POBLACION)
    algorithm.mating.crossover.prob = pc
    algorithm.mating.mutation.prob = PM
    res = minimize(problem, algorithm, ("n_gen", N_GEN), seed=seed, verbose=False)
    return res.X, res.F


def main():
    fig, axes = plt.subplots(2, len(PC_VALUES), figsize=(4 * len(PC_VALUES), 8))
    fig.suptitle(f"Experimento 2: barrido de la probabilidad de cruce  "
                 f"(pob={POBLACION}, gen={N_GEN}, pm={PM}, {N_SEEDS} semilla(s) por valor)")
    cmap = plt.get_cmap("tab10")

    print(f"{'pc':>5} | {'pureza (por semilla)':<35} | {'cobertura (por semilla)'}")
    print("-" * 90)

    for col, pc in enumerate(PC_VALUES):
        ax_dec = axes[0, col]
        ax_obj = axes[1, col]
        decorate_panel(ax_dec, ax_obj)

        # Acercamos la vista del espacio de decisión para ver bien el segmento A-B
        ax_dec.set_xlim(-1.0, 3.0)
        ax_dec.set_ylim(-1.0, 3.0)

        purs, covs = [], []
        for s in range(N_SEEDS):
            X, F = run_one(pc, seed=s + 1)
            c = cmap(s)
            ax_dec.scatter(X[:, 0], X[:, 1], color=c, s=15, alpha=0.6)
            ax_obj.scatter(F[:, 0], F[:, 1], color=c, s=15, alpha=0.6)
            purs.append(purity(F))
            covs.append(coverage(F))

        ax_dec.set_title(f"pc = {pc}")
        if col != 0:
            ax_dec.set_ylabel(""); ax_obj.set_ylabel("")

        purs_str = "[" + ", ".join(f"{p:.2f}" for p in purs) + "]"
        covs_str = "[" + ", ".join(f"{c:.2f}" for c in covs) + "]"
        print(f"{pc:>5} | {purs_str:<35} | {covs_str}")

    plt.tight_layout()
    plt.savefig("experimento_2_pc.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
