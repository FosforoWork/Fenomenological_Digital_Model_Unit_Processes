"""
EXPERIMENTO 1 - Efecto de la semilla aleatoria

Para experimentar
- Modificá la lista SEEDS y volvé a correr.
- Probá con una configuración exigente (POBLACION pequeña, pocas N_GEN)
  y observá cómo crece la variación entre semillas.
"""

import matplotlib.pyplot as plt
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

from problem import TwoPointSquared, make_overlay_axes, purity, coverage


# ----- Parámetros ajustables --------------------------------------------------
SEEDS     = [2]
POBLACION = 40
N_GEN     = 30
PC        = 0.9     # probabilidad de cruce
PM        = 0.5     # probabilidad de mutación (por individuo)
# ------------------------------------------------------------------------------


def run_one(seed):
    problem = TwoPointSquared()
    algorithm = NSGA2(pop_size=POBLACION)
    algorithm.mating.crossover.prob = PC
    algorithm.mating.mutation.prob = PM
    res = minimize(problem, algorithm, ("n_gen", N_GEN), seed=seed, verbose=False)
    return res.X, res.F


def main():
    fig, ax_dec, ax_obj = make_overlay_axes(
        f"Experimento 1: mismos parámetros, distintas semillas  "
        f"(pob={POBLACION}, gen={N_GEN}, pc={PC}, pm={PM})"
    )

    cmap = plt.get_cmap("tab10")
    print(f"{'semilla':>7} | {'|frente|':>8} | {'pureza':>7} | {'cobertura':>9}")
    print("-" * 44)
    for i, seed in enumerate(SEEDS):
        X, F = run_one(seed)
        c = cmap(i % 10)
        ax_dec.scatter(X[:, 0], X[:, 1], color=c, s=20, alpha=0.7, label=f"semilla={seed}")
        ax_obj.scatter(F[:, 0], F[:, 1], color=c, s=20, alpha=0.7, label=f"semilla={seed}")
        print(f"{seed:>7} | {len(F):>8} | {purity(F):>7.2f} | {coverage(F):>9.2f}")

    # Acercamos la vista del espacio de decisión para ver bien el segmento A-B
    ax_dec.set_xlim(-1.0, 3.0)
    ax_dec.set_ylim(-1.0, 3.0)

    ax_dec.legend(loc="best", fontsize=8)
    ax_obj.legend(loc="best", fontsize=8)
    plt.tight_layout()
    plt.savefig("experimento_1_semilla.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
