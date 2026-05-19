"""
EXPERIMENTO 3 - Efecto de la probabilidad de mutación pm

Para experimentar
- Modificá PM_VALUES, sobre todo probá valores muy pequeños y 1.0.
- Mirá tanto el espacio de decisión (fila superior) como el espacio de
  objetivos (fila inferior) en los resultados. A veces pm cambia uno pero no el otro.
"""

import matplotlib.pyplot as plt
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

from problem import TwoPointSquared, decorate_panel, purity, coverage


# ----- Parámetros ajustables --------------------------------------------------
PM_VALUES = [0.0, 1.0]
N_SEEDS   = 1
POBLACION = 40
N_GEN     = 10
PC        = 0.9
# ------------------------------------------------------------------------------


def run_one(pm, seed):
    problem = TwoPointSquared()
    algorithm = NSGA2(pop_size=POBLACION)
    algorithm.mating.crossover.prob = PC
    algorithm.mating.mutation.prob = pm
    res = minimize(problem, algorithm, ("n_gen", N_GEN), seed=seed, verbose=False)
    return res.X, res.F


def main():
    fig, axes = plt.subplots(2, len(PM_VALUES), figsize=(4 * len(PM_VALUES), 8))
    fig.suptitle(f"Experimento 3: barrido de la probabilidad de mutación  "
                 f"(pob={POBLACION}, gen={N_GEN}, pc={PC}, {N_SEEDS} semillas por valor)")
    cmap = plt.get_cmap("tab10")

    print(f"{'pm':>5} | {'pureza (por semilla)':<35} | {'cobertura (por semilla)'}")
    print("-" * 90)

    for col, pm in enumerate(PM_VALUES):
        ax_dec = axes[0, col]
        ax_obj = axes[1, col]
        decorate_panel(ax_dec, ax_obj)

        # Acercamos la vista del espacio de decisión para ver bien el segmento A-B
        ax_dec.set_xlim(-1.0, 3.0)
        ax_dec.set_ylim(-1.0, 3.0)

        purs, covs = [], []
        for s in range(N_SEEDS):
            X, F = run_one(pm, seed=s + 1)
            c = cmap(s)
            ax_dec.scatter(X[:, 0], X[:, 1], color=c, s=15, alpha=0.6)
            ax_obj.scatter(F[:, 0], F[:, 1], color=c, s=15, alpha=0.6)
            purs.append(purity(F))
            covs.append(coverage(F))

        ax_dec.set_title(f"pm = {pm}")
        if col != 0:
            ax_dec.set_ylabel(""); ax_obj.set_ylabel("")

        purs_str = "[" + ", ".join(f"{p:.2f}" for p in purs) + "]"
        covs_str = "[" + ", ".join(f"{c:.2f}" for c in covs) + "]"
        print(f"{pm:>5} | {purs_str:<35} | {covs_str}")

    plt.tight_layout()
    plt.savefig("experimento_3_pm.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
