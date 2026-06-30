"""Generate batch distribution plot with KDE overlay for the paper."""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Data from the 30-batch run
batch_rates = np.array([
    99.86, 99.89, 99.95, 99.88, 99.83, 99.85, 99.87, 99.91, 99.92, 99.87,
    99.90, 99.87, 99.88, 99.90, 99.88, 99.88, 99.89, 99.85, 99.88, 99.87,
    99.83, 99.85, 99.86, 99.89, 99.87, 99.85, 99.91, 99.86, 99.90, 99.88,
])

mean_rate = np.mean(batch_rates)
std_rate = np.std(batch_rates, ddof=1)

fig, ax = plt.subplots(1, 1, figsize=(7, 3.8))

# Histogram (semi-transparent background)
ax.hist(batch_rates, bins=12, color="#2c3e50", edgecolor="white",
        alpha=0.25, density=False, zorder=3)

# KDE curve (Gaussian bell)
x_grid = np.linspace(mean_rate - 4*std_rate, mean_rate + 4*std_rate, 500)
kde = stats.gaussian_kde(batch_rates)
density = kde(x_grid)
density_scaled = density * len(batch_rates) * np.diff(np.histogram_bin_edges(batch_rates, bins=12))[0]
ax.fill_between(x_grid, density_scaled, alpha=0.15, color="#2980b9", zorder=2)
ax.plot(x_grid, density_scaled, color="#2980b9", linewidth=1.8, zorder=5,
        label="Densidad KDE (campana de Gauss)")

# Rug marks for each batch
ax.plot(batch_rates, np.full_like(batch_rates, -0.15), "|", color="#2c3e50",
        markersize=6, markeredgewidth=0.8, zorder=6, label="Lotes individuales")

# Mean line
ax.axvline(mean_rate, color="#c0392b", linestyle="--", linewidth=1.2,
           label=f"Media: ${mean_rate:.2f}\\%$", zorder=4)

# IC95% lines
ci95 = 1.96 * std_rate / np.sqrt(30)
ax.axvline(mean_rate - ci95, color="#7f8c8d", linestyle=":", linewidth=0.9, zorder=2)
ax.axvline(mean_rate + ci95, color="#7f8c8d", linestyle=":", linewidth=0.9, zorder=2,
           label=f"IC 95\\%: $\\pm${ci95:.3f}\\%")

# Labels
ax.set_xlabel("Tasa de Éxito por Lote (%)", fontsize=9)
ax.set_ylabel("Frecuencia (lotes)", fontsize=9)
ax.set_title("Distribución de Tasas de Éxito — 30 lotes × 10,000 corridas", fontsize=10)
ax.legend(fontsize=8, framealpha=0.8, loc="upper left")
ax.grid(True, alpha=0.3, zorder=0)
ax.set_xlim(99.78, 100.0)

plt.tight_layout()
plt.savefig("docs/figures/monte_carlo_dist.pdf", bbox_inches="tight", dpi=200)
plt.savefig("docs/figures/monte_carlo_dist.png", bbox_inches="tight", dpi=200)
print(f"Saved. Mean={mean_rate:.4f}%, Std={std_rate:.4f}%, CI95=[{mean_rate-ci95:.4f}, {mean_rate+ci95:.4f}]")
