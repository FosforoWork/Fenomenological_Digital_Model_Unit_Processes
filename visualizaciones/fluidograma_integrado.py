"""Construccion de fluidograma integrado y metricas de balance para Streamlit."""

from __future__ import annotations

from typing import Mapping

import plotly.graph_objects as go

KG_PER_M3_WATER = 1000.0


def _safe_float(container: Mapping[str, float], key: str) -> float:
    value = container.get(key, 0.0)
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _kg_from_m3(container: Mapping[str, float], key: str) -> float:
    return max(0.0, _safe_float(container, key) * KG_PER_M3_WATER)


def _hex_to_rgba(hex_color: str, alpha: float) -> str:
    color = (hex_color or "#64748b").lstrip("#")
    if len(color) != 6:
        return f"rgba(100, 116, 139, {alpha:.3f})"

    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)
    return f"rgba({red}, {green}, {blue}, {alpha:.3f})"


def build_fluidograma_payload(result: Mapping[str, Mapping[str, float]]) -> dict:
    """Aplana resultados del modelo a una estructura apta para Sankey y KPIs."""
    stage_0 = result.get("stage_0", {})
    stage_1 = result.get("stage_1", {})
    stage_1_2 = result.get("stage_1_2", {})
    stage_2 = result.get("stage_2", {})
    stage_2_5 = result.get("stage_2_5_ro", {})
    stage_3 = result.get("stage_3", {})
    stage_4 = result.get("stage_4", {})
    stage_4_2 = result.get("stage_4_2", {})
    stage_5 = result.get("stage_5", {})
    integrity = result.get("integrity", {})

    mass_in_kg_h = _safe_float(integrity, "mass_in_kg_h")
    if mass_in_kg_h <= 0.0:
        mass_in_kg_h = _safe_float(stage_0, "soy_feed_kg_h") + _safe_float(stage_0, "water_kg_h")

    mass_out_kg_h = _safe_float(integrity, "mass_out_kg_h")

    feed_total_kg_h = max(0.0, _safe_float(stage_1, "slurry_flow_kg_h"))
    extract_to_pasteur_kg_h = _kg_from_m3(stage_1_2, "extract_flow_m3_h")
    okara_wet_kg_h = max(0.0, _safe_float(stage_1_2, "okara_wet_kg_h"))

    neutralized_kg_h = _kg_from_m3(stage_2, "neutralized_flow_m3_h")
    retentate_kg_h = _kg_from_m3(stage_2_5, "retentate_flow_m3_h")
    permeate_kg_h = _kg_from_m3(stage_2_5, "permeate_flow_m3_h")

    concentrate_kg_h = _kg_from_m3(stage_3, "concentrate_flow_m3_h")
    evaporated_kg_h = _kg_from_m3(stage_3, "evaporator_boiling_removed_m3_h")

    paste_mass_kg_h = max(0.0, _safe_float(stage_4_2, "paste_mass_kg_h"))
    whey_kg_h = _kg_from_m3(stage_4_2, "whey_flow_m3_h")

    powder_kg_h = max(0.0, _safe_float(stage_5, "powder_mass_kg_h"))
    dryer_removed_kg_h = max(0.0, _safe_float(stage_5, "dryer_water_removed_kg_h"))

    nodes = [
        "Alimentacion total",
        "Extraccion y separacion",
        "Pasteurizacion",
        "OI",
        "Evaporacion",
        "Precipitacion y centrifuga",
        "Secado",
        "Producto final",
        "Okara",
        "Permeado OI",
        "Agua evaporada",
        "Suero residual",
        "Agua removida secado",
    ]

    links = [
        {"source": 0, "target": 1, "value": mass_in_kg_h or feed_total_kg_h, "label": "Entrada global"},
        {"source": 1, "target": 2, "value": extract_to_pasteur_kg_h, "label": "Extracto a pasteurizacion"},
        {"source": 1, "target": 8, "value": okara_wet_kg_h, "label": "Okara"},
        {"source": 2, "target": 3, "value": neutralized_kg_h, "label": "Flujo neutralizado"},
        {"source": 3, "target": 4, "value": retentate_kg_h, "label": "Retentado OI"},
        {"source": 3, "target": 9, "value": permeate_kg_h, "label": "Permeado OI"},
        {"source": 4, "target": 5, "value": concentrate_kg_h, "label": "Concentrado"},
        {"source": 4, "target": 10, "value": evaporated_kg_h, "label": "Agua evaporada"},
        {"source": 5, "target": 6, "value": paste_mass_kg_h, "label": "Pasta humeda"},
        {"source": 5, "target": 11, "value": whey_kg_h, "label": "Suero residual"},
        {"source": 6, "target": 7, "value": powder_kg_h, "label": "Polvo final"},
        {"source": 6, "target": 12, "value": dryer_removed_kg_h, "label": "Agua removida en secado"},
    ]

    for link in links:
        link["value"] = max(0.0, float(link["value"]))

    rendimientos = [
        {"label": "Extraccion proteica", "value_pct": max(0.0, _safe_float(stage_1, "extraction_eff_pct"))},
        {"label": "Recuperacion separacion", "value_pct": max(0.0, _safe_float(stage_1_2, "extract_recovery_pct"))},
        {"label": "Calidad post pasteurizacion", "value_pct": max(0.0, _safe_float(stage_2, "protein_quality_factor") * 100.0)},
        {"label": "Recuperacion OI", "value_pct": max(0.0, _safe_float(stage_2_5, "ro_recovery_pct"))},
        {"label": "Retencion proteica OI", "value_pct": max(0.0, _safe_float(stage_2_5, "protein_retention_pct"))},
        {"label": "Eficiencia precipitacion", "value_pct": max(0.0, _safe_float(stage_4, "precip_eff_pct"))},
        {"label": "Recuperacion centrifuga", "value_pct": max(0.0, _safe_float(stage_4_2, "solids_recovery_pct"))},
        {"label": "Rendimiento global", "value_pct": max(0.0, _safe_float(stage_5, "overall_yield_pct"))},
    ]

    desperdicios = [
        {"label": "Okara humedo", "value_kg_h": okara_wet_kg_h},
        {"label": "Permeado OI", "value_kg_h": permeate_kg_h},
        {"label": "Agua evaporada", "value_kg_h": evaporated_kg_h},
        {"label": "Suero residual", "value_kg_h": whey_kg_h},
        {"label": "Agua removida en secado", "value_kg_h": dryer_removed_kg_h},
        {"label": "Proteina perdida en okara", "value_kg_h": max(0.0, _safe_float(stage_1, "protein_lost_okara_kg_h"))},
    ]

    waste_total_kg_h = sum(item["value_kg_h"] for item in desperdicios if item["label"] != "Proteina perdida en okara")

    balance = {
        "mass_in_kg_h": mass_in_kg_h,
        "mass_out_kg_h": mass_out_kg_h,
        "mass_balance_error_pct": _safe_float(integrity, "mass_balance_error_pct"),
        "mass_balance_closure_pct": _safe_float(integrity, "mass_balance_closure_pct"),
        "product_powder_kg_h": powder_kg_h,
        "waste_total_kg_h": waste_total_kg_h,
    }

    return {
        "nodes": nodes,
        "links": links,
        "rendimientos": rendimientos,
        "desperdicios": desperdicios,
        "balance": balance,
    }


def build_fluidograma_sankey(payload: Mapping[str, object], theme: Mapping[str, object] = None) -> go.Figure:
    """Genera figura Sankey para el fluidograma integrado."""
    text_color = "#f8fafc"
    card_bg = "#1e293b"
    accent = "#38bdf8"
    danger = "#ef4444"
    success = "#10b981"

    node_palette = [
        _hex_to_rgba("#94a3b8", 0.85), # Alimentacion
        _hex_to_rgba("#22c55e", 0.90), # S1
        _hex_to_rgba("#f59e0b", 0.90), # S2
        _hex_to_rgba("#3b82f6", 0.90), # S2.5
        _hex_to_rgba("#fb7185", 0.90), # S3
        _hex_to_rgba("#f43f5e", 0.90), # S4
        _hex_to_rgba("#ef4444", 0.90), # S5
        _hex_to_rgba(success, 0.95),   # Producto
        _hex_to_rgba("#b45309", 0.90), # Okara
        _hex_to_rgba("#0284c7", 0.90), # Permeado
        _hex_to_rgba("#475569", 0.88), # Evaporada
        _hex_to_rgba("#7c3aed", 0.88), # Suero
        _hex_to_rgba("#0ea5e9", 0.88), # Agua Secado
    ]

    links = payload.get("links", [])
    sources = [int(item["source"]) for item in links]
    targets = [int(item["target"]) for item in links]
    values = [float(item["value"]) for item in links]
    labels = [str(item["label"]) for item in links]

    link_colors = []
    for item in links:
        target = int(item["target"])
        if target >= 8:
            link_colors.append(_hex_to_rgba(danger, 0.35))
        elif target == 7:
            link_colors.append(_hex_to_rgba(success, 0.40))
        else:
            link_colors.append(_hex_to_rgba(accent, 0.28))

    link_custom = [[label, value] for label, value in zip(labels, values)]

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",
                valueformat=".1f",
                valuesuffix=" kg/h",
                node=dict(
                    pad=16,
                    thickness=16,
                    line=dict(color=_hex_to_rgba("#0f172a", 0.45), width=0.7),
                    label=list(payload.get("nodes", [])),
                    color=node_palette,
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                    color=link_colors,
                    customdata=link_custom,
                    hovertemplate="%{customdata[0]}<br>%{customdata[1]:,.1f} kg/h<extra></extra>",
                ),
            )
        ]
    )

    fig.update_layout(
        margin=dict(l=8, r=8, t=16, b=8),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=str(text_color), size=13),
        template="plotly_dark"
    )

    fig.update_traces(textfont=dict(color=str(text_color), size=13), selector=dict(type="sankey"))
    fig.update_layout(hoverlabel=dict(bgcolor=str(card_bg), font_color=str(text_color)))

    return fig


def render_svg_pfd(payload: Mapping[str, object], theme: Mapping[str, object] = None) -> str:
    """Genera un diagrama de flujo de proceso (PFD) en SVG dinamico."""
    if theme is None:
        theme = {
            "text": "#f8fafc",
            "border": "#334155",
            "accent": "#38bdf8",
            "status": {"rojo": "#ef4444", "verde": "#10b981"},
            "stage_colors": {"s0": "#38bdf8"}
        }

    # Extraer flujos del balance
    links = {link["label"]: link["value"] for link in payload.get("links", [])}

    # Escalamiento de grosores (max ~10px)
    max_flow = max([l["value"] for l in payload.get("links", [])] or [1.0])
    def get_width(flow_name):
        val = links.get(flow_name, 0.0)
        return max(1.5, (val / max_flow) * 12.0)

    # Colores
    c_main = theme.get("accent", "#38bdf8")
    c_waste = theme.get("status", {}).get("rojo", "#ef4444")
    c_product = theme.get("status", {}).get("verde", "#10b981")
    c_text = theme.get("text", "#f8fafc")

    svg = f"""
    <svg viewBox="0 0 950 300" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family: 'Inter', sans-serif;">
        <!-- Definicion de flechas -->
        <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="{c_main}" />
            </marker>
            <marker id="arrowhead-waste" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="{c_waste}" />
            </marker>
            <marker id="arrowhead-product" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="{c_product}" />
            </marker>
            <style>
                .stage-box {{ fill: #1e293b; stroke: {theme.get('border', '#334155')}; stroke-width: 1.5; }}
                .stage-text {{ fill: {c_text}; font-size: 10px; font-weight: 600; text-anchor: middle; }}
                .flow-label {{ fill: {c_text}; font-size: 8px; opacity: 0.8; }}
                .flow-line {{ fill: none; stroke-linecap: round; transition: stroke-width 0.5s ease; }}
                @keyframes dash {{
                    to {{ stroke-dashoffset: -20; }}
                }}
                .animated-flow {{
                    stroke-dasharray: 4, 2;
                    animation: dash 1s linear infinite;
                }}
            </style>
        </defs>

        <!-- Etapa 0: Alimentacion -->
        <rect x="20" y="130" width="60" height="40" rx="4" class="stage-box" />
        <text x="50" y="155" class="stage-text">E0: Ingreso</text>

        <!-- E0 -> E1 -->
        <path d="M 80 150 L 120 150" stroke="{c_main}" stroke-width="{get_width('Entrada global')}" class="flow-line" marker-end="url(#arrowhead)" />
        <text x="85" y="140" class="flow-label">Alimentacion</text>

        <!-- Etapa 1: Extraccion -->
        <rect x="120" y="130" width="70" height="40" rx="4" class="stage-box" />
        <text x="155" y="155" class="stage-text">E1: Extraccion</text>

        <!-- E1 -> E1.2 -->
        <path d="M 190 150 L 230 150" stroke="{c_main}" stroke-width="{get_width('Extracto a pasteurizacion')}" class="flow-line" marker-end="url(#arrowhead)" />

        <!-- Etapa 1.2: Separacion -->
        <circle cx="250" cy="150" r="25" class="stage-box" />
        <text x="250" y="153" class="stage-text">E1.2: Sep.</text>

        <!-- E1.2 -> Okara (Desperdicio) -->
        <path d="M 250 175 L 250 220" stroke="{c_waste}" stroke-width="{get_width('Okara')}" class="flow-line" marker-end="url(#arrowhead-waste)" />
        <text x="255" y="210" class="flow-label" style="fill:{c_waste}">Okara</text>

        <!-- E1.2 -> E2 -->
        <path d="M 275 150 L 320 150" stroke="{c_main}" stroke-width="{get_width('Extracto a pasteurizacion')}" class="flow-line" marker-end="url(#arrowhead)" />

        <!-- Etapa 2: Pasteurizacion -->
        <rect x="320" y="130" width="70" height="40" rx="4" class="stage-box" />
        <text x="355" y="155" class="stage-text">E2: Past.</text>

        <!-- E2 -> E2.5 -->
        <path d="M 390 150 L 430 150" stroke="{c_main}" stroke-width="{get_width('Flujo neutralizado')}" class="flow-line" marker-end="url(#arrowhead)" />

        <!-- Etapa 2.5: OI -->
        <rect x="430" y="130" width="60" height="40" rx="4" class="stage-box" />
        <text x="460" y="155" class="stage-text">E2.5: OI</text>

        <!-- E2.5 -> Permeado (Desperdicio) -->
        <path d="M 460 170 L 460 220" stroke="{c_waste}" stroke-width="{get_width('Permeado OI')}" class="flow-line" marker-end="url(#arrowhead-waste)" />
        <text x="465" y="210" class="flow-label" style="fill:{c_waste}">Permeado</text>

        <!-- E2.5 -> E3 -->
        <path d="M 490 150 L 530 150" stroke="{c_main}" stroke-width="{get_width('Retentado OI')}" class="flow-line" marker-end="url(#arrowhead)" />

        <!-- Etapa 3: Evaporacion -->
        <rect x="530" y="120" width="70" height="60" rx="4" class="stage-box" />
        <text x="565" y="155" class="stage-text">E3: Evap.</text>

        <!-- E3 -> Vapor (Desperdicio) -->
        <path d="M 565 120 L 565 80" stroke="{c_waste}" stroke-width="{get_width('Agua evaporada')}" class="flow-line" marker-end="url(#arrowhead-waste)" />
        <text x="570" y="90" class="flow-label" style="fill:{c_waste}">Vapor</text>

        <!-- E3 -> E4 -->
        <path d="M 600 150 L 640 150" stroke="{c_main}" stroke-width="{get_width('Concentrado')}" class="flow-line" marker-end="url(#arrowhead)" />

        <!-- Etapa 4: Precipitacion y Centrifuga -->
        <rect x="640" y="130" width="80" height="40" rx="4" class="stage-box" />
        <text x="680" y="155" class="stage-text">E4: Ppt/Cf</text>

        <!-- E4 -> Suero (Desperdicio) -->
        <path d="M 680 170 L 680 220" stroke="{c_waste}" stroke-width="{get_width('Suero residual')}" class="flow-line" marker-end="url(#arrowhead-waste)" />
        <text x="685" y="210" class="flow-label" style="fill:{c_waste}">Suero</text>

        <!-- E4 -> E5 -->
        <path d="M 720 150 L 760 150" stroke="{c_main}" stroke-width="{get_width('Pasta humeda')}" class="flow-line" marker-end="url(#arrowhead)" />

        <!-- Etapa 5: Secado -->
        <rect x="760" y="120" width="70" height="60" rx="4" class="stage-box" />
        <text x="795" y="155" class="stage-text">E5: Secado</text>

        <!-- E5 -> Vapor (Desperdicio) -->
        <path d="M 795 120 L 795 80" stroke="{c_waste}" stroke-width="{get_width('Agua removida en secado')}" class="flow-line" marker-end="url(#arrowhead-waste)" />
        <text x="800" y="95" class="flow-label" style="fill:{c_waste}">H2O</text>

        <!-- E5 -> Producto Final -->
        <path d="M 830 150 L 870 150" stroke="{c_product}" stroke-width="{get_width('Polvo final')}" class="flow-line" marker-end="url(#arrowhead-product)" />

        <!-- Producto Final -->
        <polygon points="870,130 930,150 870,170" fill="{c_product}" opacity="0.8" />
        <text x="900" y="153" class="stage-text" style="fill: #1e293b;">FINAL</text>

        <!-- Valores dinamicos -->
        <text x="50" y="185" class="flow-label" text-anchor="middle">{links.get('Entrada global', 0):.0f} kg/h</text>
        <text x="900" y="185" class="flow-label" text-anchor="middle" style="fill:{c_product}; font-weight:bold;">{links.get('Polvo final', 0):.1f} kg/h</text>
    </svg>
    """
    return svg
