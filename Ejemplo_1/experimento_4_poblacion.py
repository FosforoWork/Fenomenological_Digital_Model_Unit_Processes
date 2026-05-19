"""
EXPERIMENTO 4 - Efecto del tamaño de población (con cronometraje)

Para experimentar
- Empujá los POP_SIZES más lejos (5, 200, 500) y observá cómo se curvan
  las gráficas.
- Reemplazá el objetivo analítico barato por uno deliberadamente lento
  (poné un time.sleep(0.001) dentro de _evaluate) para *sentir* el tipo
  de escalamiento que aparece.
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

from problem import TwoPointSquared, purity, coverage


# ----- Parámetros ajustables --------------------------------------------------
POP_SIZES = [10, 200]
N_SEEDS   = 1
N_GEN     = 30
PC        = 0.9
PM        = 0.1
# ------------------------------------------------------------------------------


def run_one(pop_size, seed):
    problem = TwoPointSquared()
    algorithm = NSGA2(pop_size=pop_size)
    algorithm.mating.crossover.prob = PC
    algorithm.mating.mutation.prob = PM
    t0 = time.perf_counter()
    res = minimize(problem, algorithm, ("n_gen", N_GEN), seed=seed, verbose=False)
    elapsed = time.perf_counter() - t0
    return res.F, elapsed


def main():
    times_mean, times_std = [], []
    pur_mean, pur_std = [], []
    cov_mean, cov_std = [], []

    print(f"{'pob':>5} | {'tiempo (s)':>14} | {'pureza':>14} | {'cobertura':>14}")
    print("-" * 60)

    for pop in POP_SIZES:
        ts, purs, covs = [], [], []
        for s in range(N_SEEDS):
            F, dt = run_one(pop, seed=s + 1)
            ts.append(dt)
            purs.append(purity(F))
            covs.append(coverage(F))
        times_mean.append(np.mean(ts));   times_std.append(np.std(ts))
        pur_mean.append(np.mean(purs));   pur_std.append(np.std(purs))
        cov_mean.append(np.mean(covs));   cov_std.append(np.std(covs))
        print(f"{pop:>5} | {np.mean(ts):>6.3f} +- {np.std(ts):>4.3f} | "
              f"{np.mean(purs):>6.2f} +- {np.std(purs):>4.2f} | "
              f"{np.mean(covs):>6.2f} +- {np.std(covs):>4.2f}")

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.2))
    fig.suptitle(f"Experimento 4: barrido del tamaño de población  "
                 f"(gen={N_GEN}, pc={PC}, pm={PM}, {N_SEEDS} semilla(s) por valor)")

    axes[0].errorbar(POP_SIZES, times_mean, yerr=times_std, marker="o", capsize=3)
    axes[0].set_xlabel("tamaño de población")
    axes[0].set_ylabel("tiempo de pared (s)")
    axes[0].set_title("Costo")
    axes[0].grid(alpha=0.3)

    axes[1].errorbar(POP_SIZES, pur_mean, yerr=pur_std, marker="o", capsize=3, color="tab:red")
    axes[1].axhline(1.0, color="k", lw=0.8, ls="--", label="perfecto = 1.0")
    axes[1].set_xlabel("tamaño de población")
    axes[1].set_ylabel("pureza")
    axes[1].set_title("Calidad (fracción sobre el frente verdadero)")
    axes[1].set_ylim(-0.05, 1.1)
    axes[1].legend()
    axes[1].grid(alpha=0.3)

    axes[2].errorbar(POP_SIZES, cov_mean, yerr=cov_std, marker="o", capsize=3, color="tab:green")
    axes[2].axhline(1.0, color="k", lw=0.8, ls="--", label="frente completo = 1.0")
    axes[2].set_xlabel("tamaño de población")
    axes[2].set_ylabel("cobertura")
    axes[2].set_title("Extensión (fracción del frente cubierta)")
    axes[2].set_ylim(-0.05, 1.1)
    axes[2].legend()
    axes[2].grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("experimento_4_poblacion.png", dpi=120)
    plt.show()


if __name__ == "__main__":
    main()
