from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "PROYECTO_3ER BLOQUE" / "media" / "images"


def ensure_output_dir() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_ell_binodal() -> None:
    # Binodal and tie-line points from the consolidated worksheet.
    x_binodal = np.array([0, 5, 15, 28, 45, 65, 85, 95], dtype=float)
    y_binodal = np.array([0, 6, 13, 19, 24, 20, 7, 0], dtype=float)

    tie_lines = [
        ((3.0, 11.0), (57.0, 20.0)),
        ((2.0, 7.0), (70.0, 11.0)),
        ((1.5, 2.5), (85.0, 3.0)),
        ((0.5, 0.5), (92.0, 1.0)),
    ]

    key_points = {
        "M": (35.484, 1.813),
        "E": (88.0961, 2.1154),
        "R": (1.0577, 1.6154),
    }

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x_binodal,
            y=y_binodal,
            mode="lines+markers",
            name="Curva binodal",
            line={"color": "#1f77b4", "width": 3},
            marker={"size": 7},
        )
    )

    for idx, ((x1, y1), (x2, y2)) in enumerate(tie_lines, start=1):
        fig.add_trace(
            go.Scatter(
                x=[x1, x2],
                y=[y1, y2],
                mode="lines",
                name=f"Linea de reparto {idx}",
                line={"color": "#7f7f7f", "width": 1.5, "dash": "dash"},
                showlegend=(idx == 1),
                legendgroup="reparto",
            )
        )

    fig.add_trace(
        go.Scatter(
            x=[key_points["R"][0], key_points["E"][0]],
            y=[key_points["R"][1], key_points["E"][1]],
            mode="lines",
            name="Recta de palanca",
            line={"color": "#2ca02c", "width": 2},
        )
    )

    for label, (x, y) in key_points.items():
        fig.add_trace(
            go.Scatter(
                x=[x],
                y=[y],
                mode="markers+text",
                name=f"Punto {label}",
                text=[label],
                textposition="top center",
                marker={"size": 10, "symbol": "diamond", "color": "#d62728"},
            )
        )

    fig.update_layout(
        title="ELL: Curva binodal y lineas de reparto",
        xaxis_title="X (% p/p en fase rica en solvente)",
        yaxis_title="Y (% p/p de soluto)",
        width=1000,
        height=700,
        template="plotly_white",
        legend={"orientation": "h", "y": -0.2},
    )
    fig.update_xaxes(range=[0, 100])
    fig.update_yaxes(range=[0, 26])

    ell_html = OUT_DIR / "ell_binodal_reparto.html"
    fig.write_html(ell_html, include_plotlyjs="cdn")

    plt.figure(figsize=(10, 7), dpi=160)
    plt.plot(x_binodal, y_binodal, "-o", color="#1f77b4", linewidth=2.5, label="Curva binodal")

    for i, ((x1, y1), (x2, y2)) in enumerate(tie_lines):
        plt.plot([x1, x2], [y1, y2], "--", color="#7f7f7f", linewidth=1.4, label="Lineas de reparto" if i == 0 else None)

    plt.plot(
        [key_points["R"][0], key_points["E"][0]],
        [key_points["R"][1], key_points["E"][1]],
        color="#2ca02c",
        linewidth=1.8,
        label="Recta de palanca",
    )

    for label, (x, y) in key_points.items():
        plt.scatter(x, y, color="#d62728", s=60, marker="D")
        plt.text(x, y + 0.8, label, ha="center", fontsize=10)

    plt.xlim(0, 100)
    plt.ylim(0, 26)
    plt.xlabel("X (% p/p en fase rica en solvente)")
    plt.ylabel("Y (% p/p de soluto)")
    plt.title("ELL: Curva binodal y lineas de reparto")
    plt.grid(alpha=0.25)
    plt.legend(loc="upper left")
    plt.tight_layout()

    ell_png = OUT_DIR / "ell_binodal_reparto.png"
    plt.savefig(ell_png)
    plt.close()


def _build_staircase_points() -> tuple[list[float], list[float]]:
    x_d = 0.90
    y_d = 0.90

    stage_y = [0.900, 0.826, 0.750, 0.698, 0.611, 0.457, 0.259, 0.089]
    stage_x = [0.733, 0.560, 0.443, 0.375, 0.285, 0.169, 0.069, 0.021]

    xs = [x_d]
    ys = [y_d]

    y_current = y_d
    for y_next, x_next in zip(stage_y, stage_x):
        xs.extend([x_next, x_next])
        ys.extend([y_current, y_next])
        y_current = y_next

    return xs, ys


def plot_mccabe_etanol_agua() -> None:
    x_eq = np.array([0.000, 0.050, 0.100, 0.200, 0.300, 0.400, 0.500, 0.600, 0.700, 0.800, 0.900, 0.956])
    y_eq = np.array([0.000, 0.210, 0.340, 0.510, 0.630, 0.720, 0.790, 0.850, 0.890, 0.920, 0.950, 0.956])

    x = np.linspace(0, 1, 500)
    y_diag = x
    y_lor = 0.44 * x + 0.50
    y_loa = 1.70 * x - 0.0282

    stair_x, stair_y = _build_staircase_points()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_eq, y=y_eq, mode="lines+markers", name="Equilibrio", line={"color": "#1f77b4", "width": 3}))
    fig.add_trace(go.Scatter(x=x, y=y_diag, mode="lines", name="Diagonal y=x", line={"color": "#2ca02c", "width": 2}))
    fig.add_trace(go.Scatter(x=x, y=y_lor, mode="lines", name="LOR", line={"color": "#ff7f0e", "width": 2}))
    fig.add_trace(go.Scatter(x=x, y=y_loa, mode="lines", name="LOA", line={"color": "#d62728", "width": 2}))
    fig.add_trace(go.Scatter(x=[0.42, 0.42], y=[0, 1], mode="lines", name="q-line (q=1)", line={"color": "#9467bd", "width": 2, "dash": "dash"}))
    fig.add_trace(go.Scatter(x=stair_x, y=stair_y, mode="lines+markers", name="Escalonamiento", line={"color": "#111111", "width": 2}, marker={"size": 5}))

    fig.update_layout(
        title="McCabe-Thiele etanol-agua",
        xaxis_title="x (fraccion molar de etanol en liquido)",
        yaxis_title="y (fraccion molar de etanol en vapor)",
        width=1000,
        height=800,
        template="plotly_white",
        legend={"orientation": "h", "y": -0.18},
    )
    fig.update_xaxes(range=[0, 1], scaleanchor="y", scaleratio=1)
    fig.update_yaxes(range=[0, 1])

    mc_html = OUT_DIR / "mccabe_etanol_agua.html"
    fig.write_html(mc_html, include_plotlyjs="cdn")

    plt.figure(figsize=(9, 9), dpi=160)
    plt.plot(x_eq, y_eq, "-o", color="#1f77b4", linewidth=2.5, label="Equilibrio")
    plt.plot(x, y_diag, color="#2ca02c", linewidth=1.8, label="Diagonal y=x")
    plt.plot(x, y_lor, color="#ff7f0e", linewidth=1.8, label="LOR")
    plt.plot(x, y_loa, color="#d62728", linewidth=1.8, label="LOA")
    plt.plot([0.42, 0.42], [0, 1], "--", color="#9467bd", linewidth=1.8, label="q-line (q=1)")
    plt.plot(stair_x, stair_y, "-o", color="#111111", linewidth=1.8, markersize=4, label="Escalonamiento")

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel("x (fraccion molar de etanol en liquido)")
    plt.ylabel("y (fraccion molar de etanol en vapor)")
    plt.title("McCabe-Thiele etanol-agua")
    plt.grid(alpha=0.25)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.legend(loc="lower right")
    plt.tight_layout()

    mc_png = OUT_DIR / "mccabe_etanol_agua.png"
    plt.savefig(mc_png)
    plt.close()


def main() -> None:
    ensure_output_dir()
    plot_ell_binodal()
    plot_mccabe_etanol_agua()
    print("Graphs generated:")
    print(f"- {OUT_DIR / 'ell_binodal_reparto.html'}")
    print(f"- {OUT_DIR / 'ell_binodal_reparto.png'}")
    print(f"- {OUT_DIR / 'mccabe_etanol_agua.html'}")
    print(f"- {OUT_DIR / 'mccabe_etanol_agua.png'}")


if __name__ == "__main__":
    main()
