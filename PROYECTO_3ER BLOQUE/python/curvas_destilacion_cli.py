"""Script CLI para visualizar curvas de destilacion (McCabe-Thiele).

Lee parametros y tabla de equilibrio desde archivos de calculos en Markdown,
calcula lineas de operacion y genera una grafica interactiva con Plotly.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import plotly.graph_objects as go


@dataclass
class DistillationCase:
    feed_flow_kmol_h: float
    x_f: float
    x_d: float
    x_b: float
    reflux_ratio: float
    q: float
    x_eq: np.ndarray
    y_eq: np.ndarray


@dataclass
class StageResult:
    stage: int
    y_op: float
    x_eq: float
    section: str


def _extract_float(text: str, pattern: str, default: float) -> float:
    match = re.search(pattern, text, flags=re.IGNORECASE)
    if not match:
        return default
    return float(match.group(1))


def _parse_equilibrium_table(markdown_text: str) -> tuple[np.ndarray, np.ndarray]:
    lines = markdown_text.splitlines()
    rows: list[tuple[float, float]] = []
    in_table = False

    for line in lines:
        if "| x (liquido) | y (vapor) |" in line.lower():
            in_table = True
            continue

        if not in_table:
            continue

        if not line.strip().startswith("|"):
            break

        matches = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", line)
        if len(matches) >= 2:
            x_val = float(matches[0])
            y_val = float(matches[1])
            rows.append((x_val, y_val))

    if len(rows) < 3:
        raise ValueError(
            "No se encontro una tabla valida de equilibrio en el archivo de calculos."
        )

    rows = sorted(rows, key=lambda item: item[0])
    x_vals = np.array([item[0] for item in rows], dtype=float)
    y_vals = np.array([item[1] for item in rows], dtype=float)

    x_unique, unique_idx = np.unique(x_vals, return_index=True)
    y_unique = y_vals[unique_idx]

    if np.any(np.diff(x_unique) <= 0) or np.any(np.diff(y_unique) < 0):
        raise ValueError("La tabla de equilibrio debe ser monotona en x e y.")

    return x_unique, y_unique


def load_case_from_markdown(file_path: Path) -> DistillationCase:
    text = file_path.read_text(encoding="utf-8")

    x_eq, y_eq = _parse_equilibrium_table(text)

    case = DistillationCase(
        feed_flow_kmol_h=_extract_float(text, r"F\s*=\s*([0-9]+(?:\.[0-9]+)?)", 100.0),
        x_f=_extract_float(text, r"x_F\s*=\s*([0-9]+(?:\.[0-9]+)?)", 0.42),
        x_d=_extract_float(text, r"x_D\s*=\s*([0-9]+(?:\.[0-9]+)?)", 0.90),
        x_b=_extract_float(text, r"x_B\s*=\s*([0-9]+(?:\.[0-9]+)?)", 0.04),
        reflux_ratio=_extract_float(text, r"R\s*=\s*([0-9]+(?:\.[0-9]+)?)", 2.0),
        q=_extract_float(text, r"q\s*=\s*([0-9]+(?:\.[0-9]+)?)", 1.0),
        x_eq=x_eq,
        y_eq=y_eq,
    )

    return case


def _clip01(value: float) -> float:
    return float(np.clip(value, 0.0, 1.0))


def _rectifying_line(x: np.ndarray | float, r: float, x_d: float) -> np.ndarray | float:
    return (r / (r + 1.0)) * x + x_d / (r + 1.0)


def _q_line(x: np.ndarray | float, q: float, x_f: float) -> np.ndarray | float:
    if np.isclose(q, 1.0):
        if np.isscalar(x):
            return float("nan")
        return np.full_like(x, fill_value=np.nan, dtype=float)
    return (q / (q - 1.0)) * x - x_f / (q - 1.0)


def _q_intersection(r: float, x_d: float, q: float, x_f: float) -> tuple[float, float]:
    if np.isclose(q, 1.0):
        x_int = x_f
        y_int = _rectifying_line(x_int, r, x_d)
        return _clip01(x_int), _clip01(y_int)

    m_r = r / (r + 1.0)
    b_r = x_d / (r + 1.0)
    m_q = q / (q - 1.0)
    b_q = -x_f / (q - 1.0)

    x_int = (b_q - b_r) / (m_r - m_q)
    y_int = m_r * x_int + b_r
    return _clip01(x_int), _clip01(y_int)


def _stripping_line_coeffs(x_b: float, x_int: float, y_int: float) -> tuple[float, float]:
    if np.isclose(x_int, x_b):
        return 1.0, 0.0
    m_s = (y_int - x_b) / (x_int - x_b)
    b_s = x_b - m_s * x_b
    return m_s, b_s


def compute_stages(case: DistillationCase, max_stages: int) -> tuple[list[StageResult], list[tuple[float, float]], float, float]:
    x_int, y_int = _q_intersection(case.reflux_ratio, case.x_d, case.q, case.x_f)
    m_s, b_s = _stripping_line_coeffs(case.x_b, x_int, y_int)

    def y_strip(x: float) -> float:
        return m_s * x + b_s

    def y_rect(x: float) -> float:
        return _rectifying_line(x, case.reflux_ratio, case.x_d)

    def x_from_y(y_target: float) -> float:
        return float(np.interp(_clip01(y_target), case.y_eq, case.x_eq))

    y_current = case.x_d
    stage_rows: list[StageResult] = []
    stair_points: list[tuple[float, float]] = [(case.x_d, case.x_d)]

    for stage in range(1, max_stages + 1):
        x_eq = x_from_y(y_current)
        section = "Enriquecimiento" if x_eq >= x_int else "Agotamiento"
        y_next = y_rect(x_eq) if section == "Enriquecimiento" else y_strip(x_eq)
        y_next = _clip01(y_next)

        stage_rows.append(StageResult(stage=stage, y_op=y_current, x_eq=x_eq, section=section))

        stair_points.append((x_eq, y_current))
        stair_points.append((x_eq, y_next))

        y_current = y_next

        if x_eq <= case.x_b:
            break

    if not stage_rows:
        return stage_rows, stair_points, x_int, 0.0

    n_theoretical = float(len(stage_rows))
    if len(stage_rows) >= 2 and stage_rows[-1].x_eq < case.x_b < stage_rows[-2].x_eq:
        x_hi = stage_rows[-2].x_eq
        x_lo = stage_rows[-1].x_eq
        frac = (x_hi - case.x_b) / (x_hi - x_lo)
        frac = float(np.clip(frac, 0.0, 1.0))
        n_theoretical = (len(stage_rows) - 1) + frac

    return stage_rows, stair_points, x_int, n_theoretical


def build_figure(
    case: DistillationCase,
    x_int: float,
    stage_points: list[tuple[float, float]],
) -> go.Figure:
    x_grid = np.linspace(0.0, 1.0, 400)

    y_eq_interp = np.interp(x_grid, case.x_eq, case.y_eq)
    y_diag = x_grid
    y_rect = _rectifying_line(x_grid, case.reflux_ratio, case.x_d)

    _, y_int = _q_intersection(case.reflux_ratio, case.x_d, case.q, case.x_f)
    m_s, b_s = _stripping_line_coeffs(case.x_b, x_int, y_int)
    y_strip = m_s * x_grid + b_s

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x_grid,
            y=y_eq_interp,
            mode="lines",
            name="Curva de equilibrio",
            line=dict(color="#0f766e", width=3),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x_grid,
            y=y_diag,
            mode="lines",
            name="Diagonal y=x",
            line=dict(color="#64748b", width=2, dash="dash"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x_grid,
            y=np.clip(y_rect, 0.0, 1.0),
            mode="lines",
            name="Linea de enriquecimiento",
            line=dict(color="#1d4ed8", width=2.5),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x_grid,
            y=np.clip(y_strip, 0.0, 1.0),
            mode="lines",
            name="Linea de agotamiento",
            line=dict(color="#b45309", width=2.5),
        )
    )

    if np.isclose(case.q, 1.0):
        fig.add_trace(
            go.Scatter(
                x=[case.x_f, case.x_f],
                y=[0.0, 1.0],
                mode="lines",
                name="q-line (q=1)",
                line=dict(color="#7c3aed", width=2, dash="dot"),
            )
        )
    else:
        y_q = _q_line(x_grid, case.q, case.x_f)
        fig.add_trace(
            go.Scatter(
                x=x_grid,
                y=np.clip(y_q, 0.0, 1.0),
                mode="lines",
                name="q-line",
                line=dict(color="#7c3aed", width=2, dash="dot"),
            )
        )

    if stage_points:
        x_stage = [point[0] for point in stage_points]
        y_stage = [point[1] for point in stage_points]
        fig.add_trace(
            go.Scatter(
                x=x_stage,
                y=y_stage,
                mode="lines+markers",
                name="Escalones McCabe-Thiele",
                line=dict(color="#ef4444", width=2),
                marker=dict(size=5, color="#ef4444"),
            )
        )

    fig.add_trace(
        go.Scatter(
            x=[case.x_f, case.x_d, case.x_b],
            y=[case.x_f, case.x_d, case.x_b],
            mode="markers+text",
            name="Puntos de diseno",
            text=["xF", "xD", "xB"],
            textposition="top center",
            marker=dict(size=9, color="#111827"),
        )
    )

    fig.update_layout(
        title=(
            "Curvas de destilacion (McCabe-Thiele)"
            f"<br><sup>R={case.reflux_ratio:.3f}, xF={case.x_f:.3f}, xD={case.x_d:.3f}, xB={case.x_b:.3f}, q={case.q:.3f}</sup>"
        ),
        xaxis_title="x (fraccion molar en liquido)",
        yaxis_title="y (fraccion molar en vapor)",
        template="plotly_white",
        width=1050,
        height=760,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    fig.update_xaxes(range=[0.0, 1.0])
    fig.update_yaxes(range=[0.0, 1.0], scaleanchor="x", scaleratio=1)
    return fig


def _print_stage_table(stage_rows: list[StageResult], n_theoretical: float) -> None:
    print("\nEscalonamiento aproximado:")
    print(f"{'Etapa':>6} {'y_op':>10} {'x_eq':>10} {'Seccion':>18}")
    for row in stage_rows:
        print(f"{row.stage:6d} {row.y_op:10.4f} {row.x_eq:10.4f} {row.section:>18}")
    print(f"\nEtapas teoricas estimadas (sin rehervidor): {n_theoretical:.3f}")
    print(f"Etapas teoricas estimadas (con rehervidor): {n_theoretical + 1.0:.3f}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Visualiza curvas de destilacion con base en archivos de calculos (McCabe-Thiele)."
    )
    default_source = Path(__file__).resolve().parent.parent / "docs" / "Calculos Proyecto 3er Bloque.md"

    parser.add_argument(
        "--source",
        type=Path,
        default=default_source,
        help="Archivo markdown con parametros y tabla de equilibrio.",
    )
    parser.add_argument("--R", type=float, default=None, help="Override de razon de reflujo.")
    parser.add_argument("--xF", type=float, default=None, help="Override de composicion de alimentacion.")
    parser.add_argument("--xD", type=float, default=None, help="Override de composicion en destilado.")
    parser.add_argument("--xB", type=float, default=None, help="Override de composicion en fondos.")
    parser.add_argument("--q", type=float, default=None, help="Override de parametro termico q.")
    parser.add_argument("--max-stages", type=int, default=100, help="Maximo de etapas a iterar.")
    parser.add_argument("--html", type=Path, default=None, help="Ruta para exportar HTML interactivo.")
    parser.add_argument("--png", type=Path, default=None, help="Ruta para exportar PNG.")
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="No abre ventana interactiva; util para ejecucion en servidores.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.source.exists():
        raise FileNotFoundError(f"No existe el archivo fuente: {args.source}")

    case = load_case_from_markdown(args.source)

    if args.R is not None:
        case.reflux_ratio = args.R
    if args.xF is not None:
        case.x_f = args.xF
    if args.xD is not None:
        case.x_d = args.xD
    if args.xB is not None:
        case.x_b = args.xB
    if args.q is not None:
        case.q = args.q

    for attr_name in ("x_f", "x_d", "x_b"):
        value = getattr(case, attr_name)
        if not (0.0 <= value <= 1.0):
            raise ValueError(f"{attr_name} debe estar entre 0 y 1. Recibido: {value}")

    if case.reflux_ratio <= 0:
        raise ValueError("R debe ser mayor que cero.")

    stage_rows, stage_points, x_int, n_theoretical = compute_stages(case, max_stages=args.max_stages)

    if len(stage_rows) >= args.max_stages and stage_rows[-1].x_eq > case.x_b:
        print(
            "Advertencia: se alcanzo el maximo de etapas sin llegar a xB. "
            "Aumenta --max-stages o revisa parametros."
        )

    _print_stage_table(stage_rows, n_theoretical)
    fig = build_figure(case, x_int, stage_points)

    if args.html is not None:
        args.html.parent.mkdir(parents=True, exist_ok=True)
        fig.write_html(str(args.html))
        print(f"\nHTML exportado en: {args.html}")

    if args.png is not None:
        args.png.parent.mkdir(parents=True, exist_ok=True)
        try:
            fig.write_image(str(args.png), width=1400, height=1000, scale=2)
            print(f"PNG exportado en: {args.png}")
        except Exception as exc:  # pragma: no cover - depende de motor de render.
            print("No se pudo exportar PNG. Instala kaleido para habilitar fig.write_image().")
            print(f"Detalle: {exc}")

    if not args.no_show:
        fig.show()


if __name__ == "__main__":
    main()
