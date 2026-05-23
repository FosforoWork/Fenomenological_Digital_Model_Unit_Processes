"""Gemelo Digital AJAX - Sala de control en tiempo real para proceso de proteina aislada de soya."""

from __future__ import annotations

import math
import random
import time


import streamlit as st
import plotly.graph_objects as go

from core.equipment_constraints import EquipmentCapacityError
from core.equipment_specs import (
    CAPACITY_LIMIT_BOUNDS,
    CAPACITY_LIMIT_DEFAULTS,
    EQUIPMENT_SPEC_DEFAULTS,
    EQUIPMENT_SPEC_LIMITS,
    get_default_capacity_limits,
    get_default_equipment_specs,
)
from core.process_model import ControlLog, build_snapshot
from core.sales_economics import (
    DEFAULT_SALES_PRICE_BS_PER_KG,
    DOC_OPEX_TOTAL_ANNUAL_BS,
    FinancialModeler,
    compute_sales_stage,
)
from core.stage_equations import run_process_model


VISUAL_THEMES = {
    "Baluarte (CAT)": {
        "plot_template": "plotly_dark",
        "bg_start": "#0a0a0c",
        "bg_end": "#111216",
        "accent": "#00f0ff",
        "text": "#d4d4d8",
        "muted_text": "#71717a",
        "border": "#27272a",
        "glow": "rgba(0, 240, 255, 0.2)",
        "grid": "rgba(255, 255, 255, 0.05)",
        "stage_colors": {
            "s0": "#00f0ff",
            "s1": "#39ff14",
            "s2": "#ffb300",
            "s3": "#4a90e2",
            "s4": "#f44336",
            "s5": "#9c27b0",
        },
        "status": {"verde": "#39ff14", "amarillo": "#ffb300", "rojo": "#ff003c"},
    }
}


DEFAULT_CONTROLS = {
    "soy_feed_kg_h": 1000.0,
    "water_flow_m3_h": 12.0,
    "water_temp_c": 55.0,
    "extraction_ph": 8.75,
    "extraction_temp_c": 55.0,
    "extraction_residence_min": 60.0,
    "agitator_rpm": 80.0,
    "solid_liquid_ratio": 12.0,
    "pasteur_temp_c": 80.0,
    "pasteur_retention_s": 22.0,
    "evap_pressure_bar": 0.40,
    "evap_temp_c": 75.0,
    "precip_ph": 4.5,
    "precip_time_min": 25.0,
    "centrifuge_g": 1800.0,
    "centrifuge_time_min": 20.0,
    "dryer_temp_c": 190.0,
    "dryer_residence_min": 42.0,
    "ro_tmp_bar": 24.0,
}


EQUIPMENT_GROUPS = [
    ("Etapa 0 · Captacion y bombeo", [
        "stage_0_tank_capacity_m3",
        "stage_0_tank_reserve_factor",
        "stage_0_pump_head_m",
        "stage_0_pump_eta_hyd",
        "stage_0_pump_eta_motor",
        "stage_0_pump_motor_kw",
    ]),
    ("Etapa 1 · Extraccion", [
        "stage_1_slurry_density_kg_m3",
        "stage_1_tank_capacity_m3",
        "stage_1_tank_reserve_factor",
        "stage_1_base_extraction_eff",
        "stage_1_2_extract_recovery",
    ]),
    ("Etapa 2 · Pasteurizacion", [
        "stage_2_acid_addition_m3_h",
        "stage_2_cp_kj_kgk",
        "stage_2_hex_area_m2",
        "stage_2_hex_u_w_m2k",
        "stage_2_hex_lmtd_c",
    ]),
    ("Etapa RO · Osmosis Inversa", [
        "stage_ro_pump_eta",
    ]),
    ("Etapa 3 · Evaporacion", [
        "stage_3_solids_to_protein_ratio",
        "stage_3_steam_economy",
        "stage_3_evap_capacity_m3_h",
    ]),
    ("Etapa 4 · Precipitacion y centrifugacion", [
        "stage_4_base_precip_eff",
        "stage_4_2_co_solids_kg_h",
        "stage_4_2_base_moisture_frac",
        "stage_4_2_centrifuge_capacity_m3_h",
    ]),
    ("Etapa 5 · Secado", [
        "stage_5_dryer_evap_capacity_kg_h",
        "stage_5_dryer_chamber_volume_m3",
    ]),
]


CAPACITY_GROUPS = [
    ("Restricciones E0", ["tank_max_fill_fraction", "pump_max_load_fraction"]),
    ("Restricciones E1", ["stage_1_tank_max_fill_fraction"]),
    ("Restricciones E2", ["stage_2_hex_max_thermal_load_fraction", "stage_2_hex_min_area_m2", "stage_2_hex_max_area_m2"]),
    ("Restricciones RO", []),
    ("Restricciones E3", ["stage_3_evap_max_load_fraction"]),
    ("Restricciones E4", ["stage_4_2_centrifuge_max_load_fraction"]),
    ("Restricciones E5", ["stage_5_dryer_max_load_fraction", "stage_5_max_powder_rate_kg_h_m3"]),
]


EQUIPMENT_SPEC_LABELS = {
    "stage_0_tank_capacity_m3": "Capacidad tanque agua (m3)",
    "stage_0_tank_reserve_factor": "Factor reserva tanque agua",
    "stage_0_pump_head_m": "Altura manometrica bomba (m)",
    "stage_0_pump_eta_hyd": "Eficiencia hidraulica bomba",
    "stage_0_pump_eta_motor": "Eficiencia motor bomba",
    "stage_0_pump_motor_kw": "Potencia nominal bomba (kW)",
    "stage_1_slurry_density_kg_m3": "Densidad lodo extraccion (kg/m3)",
    "stage_1_tank_capacity_m3": "Capacidad tanque extraccion (m3)",
    "stage_1_tank_reserve_factor": "Factor reserva tanque extraccion",
    "stage_1_base_extraction_eff": "Eficiencia base extraccion (frac)",
    "stage_1_2_extract_recovery": "Recuperacion base separacion primaria (frac)",
    "stage_2_acid_addition_m3_h": "Dosificacion acido (m3/h)",
    "stage_2_cp_kj_kgk": "Cp mezcla (kJ/kgK)",
    "stage_2_hex_area_m2": "Area de placas intercambiador (m2)",
    "stage_2_hex_u_w_m2k": "Coeficiente U intercambiador (W/m2K)",
    "stage_2_hex_lmtd_c": "LMTD diseno intercambiador (C)",
    "stage_ro_pump_eta": "Eficiencia bomba OI",
    "stage_3_solids_to_protein_ratio": "Relacion solidos/proteina evaporador",
    "stage_3_steam_economy": "Economia de vapor",
    "stage_3_evap_capacity_m3_h": "Capacidad evaporador (m3/h)",
    "stage_4_base_precip_eff": "Eficiencia base precipitacion (frac)",
    "stage_4_2_co_solids_kg_h": "Co-solidos post centrifuga (kg/h)",
    "stage_4_2_base_moisture_frac": "Humedad base pasta (frac)",
    "stage_4_2_centrifuge_capacity_m3_h": "Capacidad centrifuga (m3/h)",
    "stage_5_dryer_evap_capacity_kg_h": "Capacidad evaporativa secador (kg/h)",
    "stage_5_dryer_chamber_volume_m3": "Volumen camara secador (m3)",
}


CONTROL_LABELS = {
    "soy_feed_kg_h": "Alimentacion de soya (kg/h)",
    "water_flow_m3_h": "Caudal de agua (m3/h)",
    "water_temp_c": "Temperatura de agua (C)",
    "extraction_ph": "pH extraccion",
    "extraction_temp_c": "Temperatura extraccion (C)",
    "extraction_residence_min": "Tiempo residencia (min)",
    "agitator_rpm": "Velocidad agitacion (RPM)",
    "solid_liquid_ratio": "Ratio solido/liquido (1:x)",
    "pasteur_temp_c": "Temperatura de pasteurizacion (C)",
    "pasteur_retention_s": "Retencion termica (s)",
    "evap_pressure_bar": "Presion evaporador (bar abs)",
    "evap_temp_c": "Temperatura evaporacion (C)",
    "ro_tmp_bar": "Presion Transmembrana OI (bar)",
    "precip_ph": "pH de precipitacion",
    "precip_time_min": "Tiempo de precipitacion (min)",
    "centrifuge_g": "Factor G centrifuga",
    "centrifuge_time_min": "Tiempo centrifugacion (min)",
    "dryer_temp_c": "Temperatura de secado (C)",
    "dryer_residence_min": "Residencia en secador (min)",
}


CAPACITY_LIMIT_LABELS = {
    "tank_max_fill_fraction": "Maximo llenado tanque Etapa 0",
    "stage_1_tank_max_fill_fraction": "Maximo llenado tanque Etapa 1",
    "pump_max_load_fraction": "Maximo uso motor bomba",
    "stage_2_hex_max_thermal_load_fraction": "Maximo uso termico intercambiador",
    "stage_2_hex_min_area_m2": "Area minima eficiente intercambiador (m2)",
    "stage_2_hex_max_area_m2": "Area maxima eficiente intercambiador (m2)",
    "stage_3_evap_max_load_fraction": "Maximo uso evaporador",
    "stage_4_2_centrifuge_max_load_fraction": "Maximo uso centrifuga",
    "stage_5_dryer_max_load_fraction": "Maximo uso secador",
    "stage_5_max_powder_rate_kg_h_m3": "Maximo polvo por volumen secador (kg/h/m3)",
}


STAGE_KPI_CONFIG = [
    {
        "tab": "Etapa 0",
        "title": "KPIs de captacion y acondicionamiento",
        "metrics": [
            {"key": "stage_0_pump_kw", "label": "Bomba Etapa 0", "unit": "kW", "decimals": 2},
            {"key": "capacity_stage_0_tank_utilization_pct", "label": "Uso tanque agua", "unit": "%", "decimals": 1},
            {"key": "stage_0_kpi_soy_moisture_pct", "label": "Humedad grano", "unit": "%", "decimals": 1},
            {"key": "stage_0_kpi_grinding_size_mesh", "label": "Molienda", "unit": "mesh", "decimals": 0},
        ],
    },
    {
        "tab": "Etapa 1",
        "title": "KPIs de lixiviacion y clarificacion",
        "metrics": [
            {"key": "stage_1_extraction_eff_pct", "label": "Eficiencia extraccion", "unit": "%", "decimals": 2},
            {"key": "stage_1_2_extract_recovery_pct", "label": "Recuperacion centrifuga 1", "unit": "%", "decimals": 2},
            {"key": "stage_1_protein_extracted_kg_h", "label": "Proteina extraida", "unit": "kg/h", "decimals": 2},
            {"key": "stage_1_kpi_protein_concentration_gl", "label": "Proteina disuelta", "unit": "g/L", "decimals": 2},
            {"key": "stage_1_kpi_slurry_viscosity_cp", "label": "Viscosidad lodo", "unit": "cP", "decimals": 1},
            {"key": "stage_1_kpi_naoh_conc_pct_pv", "label": "Conc. NaOH", "unit": "% p/v", "decimals": 2},
        ],
    },
    {
        "tab": "Etapa 2",
        "title": "KPIs de pasteurizacion y sanitizacion",
        "metrics": [
            {"key": "stage_2_heat_required_mj_h", "label": "Calor pasteurizacion", "unit": "MJ/h", "decimals": 2},
            {"key": "capacity_stage_2_hex_thermal_load_pct", "label": "Uso termico HEX", "unit": "%", "decimals": 1},
            {"key": "stage_2_kpi_reynolds_number", "label": "Reynolds", "unit": "-", "decimals": 0},
            {"key": "stage_2_protein_quality_factor", "label": "Calidad (Inocuidad)", "unit": "frac", "decimals": 2},
        ],
    },
    {
        "tab": "Osmosis Inversa",
        "title": "Salto Innovador: Pre-concentracion por OI",
        "metrics": [
            {"key": "stage_ro_permeate_kg_h", "label": "Agua removida (Permeado)", "unit": "kg/h", "decimals": 1},
            {"key": "stage_ro_thermal_saved_kw", "label": "Ahorro termico estimado", "unit": "kW", "decimals": 1},
            {"key": "stage_ro_pump_power_kw", "label": "Consumo bomba OI", "unit": "kW", "decimals": 2},
        ],
    },
    {
        "tab": "Etapa 3",
        "title": "KPIs de evaporacion y concentracion",
        "metrics": [
            {"key": "stage_3_evaporated_water_m3_h", "label": "Agua evaporada", "unit": "m3/h", "decimals": 3},
            {"key": "stage_3_target_solids_pct", "label": "Solidos objetivo", "unit": "%", "decimals": 2},
            {"key": "stage_3_kpi_concentrate_viscosity_cp", "label": "Visc. concentrado", "unit": "cP", "decimals": 1},
            {"key": "stage_3_kpi_u_global_w_m2k", "label": "Coeficiente U", "unit": "W/m2K", "decimals": 1},
        ],
    },
    {
        "tab": "Etapa 4",
        "title": "KPIs de precipitacion e isoelectrico",
        "metrics": [
            {"key": "stage_4_precip_eff_pct", "label": "Eficiencia precipitacion", "unit": "%", "decimals": 2},
            {"key": "stage_4_2_solids_recovery_pct", "label": "Recuperacion centrifuga 2", "unit": "%", "decimals": 2},
            {"key": "stage_4_protein_precip_kg_h", "label": "Proteina precipitada", "unit": "kg/h", "decimals": 2},
            {"key": "stage_4_kpi_residual_protein_whey_kg_m3", "label": "Prot. en suero", "unit": "kg/m3", "decimals": 2},
            {"key": "stage_4_kpi_zeta_potential_mv", "label": "Potencial Zeta", "unit": "mV", "decimals": 2},
        ],
    },
    {
        "tab": "Etapa 5",
        "title": "KPIs de secado y despacho",
        "metrics": [
            {"key": "stage_5_final_moisture_pct", "label": "Humedad final", "unit": "%", "decimals": 2},
            {"key": "stage_5_powder_mass_kg_h", "label": "Polvo final", "unit": "kg/h", "decimals": 1},
            {"key": "stage_5_overall_yield_pct", "label": "Rendimiento global", "unit": "%", "decimals": 2},
            {"key": "stage_5_kpi_water_activity_aw", "label": "Actividad agua", "unit": "aw", "decimals": 3},
        ],
    },
    {
        "tab": "Vista Integrada",
        "title": "KPIs integrados de proteina",
        "metrics": [
            {"key": "stage_1_protein_extracted_kg_h", "label": "Proteina extraida", "unit": "kg/h", "decimals": 2},
            {"key": "stage_4_protein_precip_kg_h", "label": "Proteina precipitada", "unit": "kg/h", "decimals": 2},
            {"key": "stage_5_protein_final_kg_h", "label": "Proteina final", "unit": "kg/h", "decimals": 2},
        ],
    },
]


DEFAULT_ERROR_BASE_PCT = 1.0
ERROR_BAND_FACTOR = 1.5
STABILITY_WINDOW_POINTS = 12

KPI_ERROR_BASE_PCT = {
    "stage_0_pump_kw": 1.2,
    "stage_1_extraction_eff_pct": 0.8,
    "stage_1_2_extract_recovery_pct": 0.9,
    "stage_2_heat_required_mj_h": 1.4,
    "stage_ro_permeate_kg_h": 1.1,
    "stage_ro_thermal_saved_kw": 1.2,
    "stage_ro_pump_power_kw": 1.0,
    "stage_3_evaporated_water_m3_h": 1.5,
    "stage_3_steam_required_kg_h": 1.5,
    "stage_3_target_solids_pct": 1.0,
    "stage_4_precip_eff_pct": 0.9,
    "stage_4_2_solids_recovery_pct": 1.0,
    "stage_4_2_paste_mass_kg_h": 1.2,
    "stage_5_final_moisture_pct": 0.8,
    "stage_5_powder_mass_kg_h": 1.2,
    "stage_5_overall_yield_pct": 1.0,
    "capacity_stage_0_tank_utilization_pct": 1.0,
    "capacity_stage_2_hex_thermal_load_pct": 1.0,
    "stage_ventas_cost_per_kg_bs": 0.4,
    "stage_ventas_revenue_per_kg_bs": 0.4,
    "stage_ventas_profit_per_kg_bs": 0.7,
    "stage_ventas_opex_annual_bs": 0.3,
    "stage_ventas_opex_hourly_bs": 0.3,
    "stage_ventas_sales_annual_bs": 1.0,
    "stage_ventas_sales_hourly_bs": 1.0,
    "stage_ventas_operating_profit_annual_bs": 1.2,
    "stage_ventas_operating_profit_hourly_bs": 1.2,
    "stage_1_protein_extracted_kg_h": 1.1,
    "stage_4_protein_precip_kg_h": 1.1,
    "stage_5_protein_final_kg_h": 1.0,
}


st.set_page_config(
    page_title="Gemelo Digital AJAX",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

def get_active_theme() -> dict:
    mode = st.session_state.get("visual_mode", "Baluarte (CAT)")
    return VISUAL_THEMES.get(mode, VISUAL_THEMES["Baluarte (CAT)"])


@st.cache_data
def get_visual_theme_css(mode: str) -> str:
    theme = VISUAL_THEMES.get(mode, VISUAL_THEMES["Baluarte (CAT)"])
    bg_deep = theme["bg_start"]
    bg_surface = theme["bg_end"]
    text_main = theme["text"]
    text_muted = theme["muted_text"]
    accent = theme["accent"]
    border = theme["border"]
    glow = theme["glow"]

    return f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=JetBrains+Mono:wght@400;600;700&display=swap');

            :root {{
                --bg-deep: {bg_deep};
                --bg-surface: {bg_surface};
                --text-main: {text_main};
                --text-muted: {text_muted};
                --accent: {accent};
                --border: {border};
                --glow: {glow};
                --font-sans: 'Inter', sans-serif;
                --font-mono: 'JetBrains Mono', monospace;
            }}

            /* Base App Styling */
            .stApp {{
                background-color: var(--bg-deep);
                color: var(--text-main);
                font-family: var(--font-sans);
            }}

            [data-testid="stSidebar"] {{
                background-color: var(--bg-surface);
                border-right: 1px solid var(--border);
            }}

            /* Typography */
            h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {{
                font-family: var(--font-sans) !important;
                color: var(--text-main) !important;
            }}

            div[data-testid="stMetricValue"] > div {{
                font-family: var(--font-mono) !important;
                font-weight: 700 !important;
                color: var(--accent) !important;
                text-shadow: 0 0 8px var(--glow);
            }}

            /* Custom Cards for KPIs */
            div[data-testid="stMetric"] {{
                background-color: var(--bg-surface);
                border: 1px solid var(--border);
                border-radius: 4px;
                padding: 1rem !important;
                transition: border-color 0.15s ease, box-shadow 0.15s ease;
            }}

            .kpi-meta {{
                font-family: var(--font-mono) !important;
                font-size: 0.75rem;
                color: var(--text-muted);
                margin-top: 4px;
                text-transform: uppercase;
            }}

            .kpi-status {{
                font-family: var(--font-mono) !important;
                font-size: 0.75rem;
                font-weight: 600;
                margin-top: 4px;
                padding: 2px 6px;
                border-radius: 2px;
                display: inline-block;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}

            .kpi-stable {{
                background-color: rgba(57, 255, 20, 0.1);
                color: #39ff14;
                border: 1px solid rgba(57, 255, 20, 0.3);
            }}

            .kpi-unstable {{
                background-color: rgba(255, 0, 60, 0.1);
                color: #ff003c;
                border: 1px solid rgba(255, 0, 60, 0.3);
            }}

            div[data-testid="stMetric"]:hover {{
                border-color: var(--accent);
                box-shadow: 0 0 12px var(--glow), inset 0 0 8px var(--glow);
            }}

            /* Buttons */
            .stButton > button {{
                width: 100%;
                background-color: var(--bg-deep);
                color: var(--accent);
                border: 1px solid var(--border);
                border-radius: 4px;
                padding: 0.5rem 1rem;
                font-family: var(--font-mono);
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                transition: all 0.15s ease;
            }}

            .stButton > button:hover {{
                border-color: var(--accent);
                background-color: rgba(0, 240, 255, 0.05);
                box-shadow: 0 0 8px var(--glow);
            }}

            .stButton > button:active {{
                transform: scale(0.98);
            }}

            /* Inputs and Sliders */
            div[data-baseweb="input"], div[data-baseweb="select"], div[data-baseweb="textarea"] {{
                background-color: var(--bg-deep) !important;
                border-radius: 2px !important;
                border: 1px solid var(--border) !important;
                transition: border-color 0.15s ease, box-shadow 0.15s ease;
            }}
            
            div[data-baseweb="input"]:focus-within {{
                border-color: var(--accent) !important;
                box-shadow: 0 0 8px var(--glow) !important;
            }}

            div[data-baseweb="input"] input {{
                color: var(--accent) !important;
                font-family: var(--font-mono) !important;
            }}

            div[role="slider"] {{
                background-color: var(--accent) !important;
                box-shadow: 0 0 6px var(--glow) !important;
            }}

            div[data-testid="stExpander"] {{
                background-color: var(--bg-surface) !important;
                border: 1px solid var(--border) !important;
                border-radius: 4px !important;
                margin-bottom: 1rem !important;
            }}

            div[data-testid="stExpander"] summary:hover {{
                color: var(--accent) !important;
            }}
            
            div[data-testid="stExpander"] summary {{
                font-family: var(--font-mono) !important;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}

            div[data-testid="stDataFrame"] {{
                background-color: var(--bg-surface) !important;
                border: 1px solid var(--border) !important;
                border-radius: 4px !important;
            }}

            /* Hero Panel & Chips */
            .hero-panel {{
                background: linear-gradient(135deg, var(--bg-surface) 0%, var(--bg-deep) 100%);
                border: 1px solid var(--border);
                border-left: 2px solid var(--accent);
                border-radius: 4px;
                padding: 1.5rem;
                margin-bottom: 2rem;
                box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
            }}

            .note-chip {{
                background-color: rgba(0, 240, 255, 0.05);
                border: 1px solid rgba(0, 240, 255, 0.2);
                color: var(--accent);
                border-radius: 2px;
                padding: 0.75rem 1rem;
                margin-bottom: 1.5rem;
                font-size: 0.85rem;
                font-family: var(--font-mono);
            }}

            /* Tabs Custom Styling */
            div[data-baseweb="tab-list"] {{
                background-color: transparent !important;
                gap: 0.5rem !important;
            }}

            div[data-baseweb="tab"] {{
                background-color: var(--bg-deep) !important;
                border: 1px solid var(--border) !important;
                border-bottom: none !important;
                border-radius: 4px 4px 0 0 !important;
                color: var(--text-muted) !important;
                padding: 0.5rem 1rem !important;
                font-family: var(--font-mono) !important;
                text-transform: uppercase;
                font-size: 0.8rem !important;
            }}

            div[data-baseweb="tab"][aria-selected="true"] {{
                border-color: var(--accent) !important;
                color: var(--accent) !important;
                background-color: var(--bg-surface) !important;
                box-shadow: inset 0 4px 0 var(--accent);
            }}

            /* Scrollbar */
            ::-webkit-scrollbar {{
                width: 6px;
                height: 6px;
            }}
            ::-webkit-scrollbar-track {{
                background: var(--bg-deep);
            }}
            ::-webkit-scrollbar-thumb {{
                background: var(--border);
                border-radius: 0;
            }}
            ::-webkit-scrollbar-thumb:hover {{
                background: var(--accent);
            }}

            /* Animations - disabled for faster updates */
            .stMarkdown, .stButton {{
                animation: none !important;
            }}

            div[data-testid="stMetric"] {{
                animation: none !important;
            }}

            /* Status Indicators */
            .status-pill {{
                width: 8px;
                height: 8px;
                border-radius: 50%;
                display: inline-block;
                margin-right: 8px;
            }}
            .status-running {{ background-color: #39ff14; box-shadow: 0 0 8px #39ff14; }}
            .status-paused {{ background-color: #ff003c; box-shadow: 0 0 8px #ff003c; }}

        </style>
"""

def apply_visual_theme_css() -> None:
    mode = st.session_state.get("visual_mode", "Baluarte (CAT)")
    st.markdown(get_visual_theme_css(mode), unsafe_allow_html=True)



def _append_sales_stage(result: dict) -> dict:
    stage_5 = result.get("stage_5", {})
    powder_mass_kg_h = float(stage_5.get("powder_mass_kg_h", 0.0))
    result["stage_ventas"] = compute_sales_stage(
        powder_mass_kg_h=powder_mass_kg_h,
        selling_price_bs_kg=float(st.session_state.sales_price_bs_kg),
    )
    return result


def _format_number_es(value: float, decimals: int) -> str:
    abs_text = f"{abs(float(value)):,.{decimals}f}"
    normalized = abs_text.replace(",", "_").replace(".", ",").replace("_", ".")
    if value < 0:
        return f"-{normalized}"
    return normalized


def _format_pct_delta_es(value: float) -> str:
    sign = "+" if value >= 0 else "-"
    return f"{sign}{_format_number_es(abs(value), 2)}%"


def _apply_full_reset() -> None:
    st.session_state.running = False
    st.session_state.controls = DEFAULT_CONTROLS.copy()
    st.session_state.equipment_specs = get_default_equipment_specs()
    st.session_state.capacity_limits = get_default_capacity_limits()
    st.session_state.sales_price_bs_kg = float(DEFAULT_SALES_PRICE_BS_PER_KG)

    for key, value in st.session_state.controls.items():
        st.session_state[f"w_{key}"] = float(value)
    for key, value in st.session_state.equipment_specs.items():
        st.session_state[f"w_eq_{key}"] = float(value)
    for key, value in st.session_state.capacity_limits.items():
        st.session_state[f"w_lim_{key}"] = float(value)
    st.session_state.w_sales_price_bs_kg = float(st.session_state.sales_price_bs_kg)

    st.session_state.log = ControlLog(max_points=1000)
    st.session_state.last_result = _append_sales_stage(run_process_model(
        st.session_state.controls,
        equipment_specs=st.session_state.equipment_specs,
        capacity_limits=st.session_state.capacity_limits,
    ))
    st.session_state.capacity_issues = []
    st.session_state.last_run_error = ""
    st.session_state.production_elapsed_s = 0.0
    st.session_state.production_protein_kg = 0.0
    st.session_state.production_bags_1kg = 0.0
    st.session_state.sparkline_history = {}
    st.session_state.pv_controls = st.session_state.controls.copy()


def init_state() -> None:
    if "controls" not in st.session_state:
        st.session_state.controls = DEFAULT_CONTROLS.copy()
    if "equipment_specs" not in st.session_state:
        st.session_state.equipment_specs = get_default_equipment_specs()
    if "capacity_limits" not in st.session_state:
        st.session_state.capacity_limits = get_default_capacity_limits()
    if "log" not in st.session_state:
        st.session_state.log = ControlLog(max_points=1000)
    if "running" not in st.session_state:
        st.session_state.running = False
    if "interval_s" not in st.session_state:
        st.session_state.interval_s = 3.0
    else:
        st.session_state.interval_s = float(max(0.5, min(5, st.session_state.interval_s)))
    if "visual_mode" not in st.session_state:
        st.session_state.visual_mode = "Baluarte (CAT)"
    elif st.session_state.visual_mode != "Baluarte (CAT)":
        st.session_state.visual_mode = "Baluarte (CAT)"
    if "sales_price_bs_kg" not in st.session_state:
        st.session_state.sales_price_bs_kg = float(DEFAULT_SALES_PRICE_BS_PER_KG)
    if "w_sales_price_bs_kg" not in st.session_state:
        st.session_state.w_sales_price_bs_kg = float(st.session_state.sales_price_bs_kg)
    if "last_result" not in st.session_state:
        st.session_state.last_result = _append_sales_stage(run_process_model(
            st.session_state.controls,
            equipment_specs=st.session_state.equipment_specs,
            capacity_limits=st.session_state.capacity_limits,
        ))
    elif "stage_ventas" not in st.session_state.last_result:
        st.session_state.last_result = _append_sales_stage(st.session_state.last_result)
    if "capacity_issues" not in st.session_state:
        st.session_state.capacity_issues = []
    if "last_run_error" not in st.session_state:
        st.session_state.last_run_error = ""
    if "production_elapsed_s" not in st.session_state:
        st.session_state.production_elapsed_s = 0.0
    if "production_protein_kg" not in st.session_state:
        st.session_state.production_protein_kg = 0.0
    if "production_bags_1kg" not in st.session_state:
        st.session_state.production_bags_1kg = 0.0
    if "sparkline_history" not in st.session_state:
        st.session_state.sparkline_history = {}
    if "pv_controls" not in st.session_state:
        st.session_state.pv_controls = st.session_state.controls.copy()
    if st.session_state.get("pending_full_reset", False):
        _apply_full_reset()
        st.session_state.pending_full_reset = False


def sync_controls_from_widgets() -> None:
    # Solo actualizamos los valores si el widget existe en el estado de sesion actual (esta renderizado)
    for key in DEFAULT_CONTROLS:
        widget_key = f"w_{key}"
        if widget_key in st.session_state:
            st.session_state.controls[key] = st.session_state[widget_key]


def _get_widget_step(vmin: float, vmax: float) -> float:
    span = float(vmax - vmin)
    if span >= 1000.0:
        return 1.0
    if span >= 100.0:
        return 0.5
    if span >= 10.0:
        return 0.1
    if span >= 1.0:
        return 0.01
    return 0.001


def sync_equipment_specs_from_widgets() -> None:
    for key in EQUIPMENT_SPEC_DEFAULTS:
        widget_key = f"w_eq_{key}"
        if widget_key in st.session_state:
            st.session_state.equipment_specs[key] = float(st.session_state[widget_key])


def sync_capacity_limits_from_widgets() -> None:
    for key in CAPACITY_LIMIT_DEFAULTS:
        widget_key = f"w_lim_{key}"
        if widget_key in st.session_state:
            st.session_state.capacity_limits[key] = float(st.session_state[widget_key])


def sync_sales_price_from_widgets() -> None:
    st.session_state.sales_price_bs_kg = float(
        st.session_state.get("w_sales_price_bs_kg", st.session_state.sales_price_bs_kg)
    )


def _get_variable_ranges(key: str, vmin: float, vmax: float) -> tuple[tuple[float, float], tuple[float, float]]:
    default = DEFAULT_CONTROLS.get(key) or EQUIPMENT_SPEC_DEFAULTS.get(key)
    if default is None:
        default = (vmin + vmax) / 2

    # Overrides alineados con Doc 10.2 — Rangos de Operabilidad (Gemelo Digital.md)
    # Formato: return (rango_estable), (frontera_de_fallo)
    if key == "extraction_ph": return (8.65, 8.85), (8.00, 9.50)
    if key == "pasteur_temp_c": return (80.0, 85.0), (76.0, 95.0)
    if key == "precip_ph": return (4.45, 4.55), (4.10, 4.90)
    if key == "evap_pressure_bar": return (0.38, 0.42), (0.30, 0.60)
    if key == "solid_liquid_ratio": return (11.5, 12.5), (9.0, 14.0)
    if key == "water_flow_m3_h": return (11.5, 12.5), (10.5, 14.0)
    if key == "soy_feed_kg_h": return (950.0, 1050.0), (680.0, 1746.50)
    if key == "dryer_temp_c": return (188.0, 192.0), (160.0, 210.0)
    if key == "agitator_rpm": return (75.0, 85.0), (50.0, 150.0)
    if key == "centrifuge_g": return (1750.0, 1850.0), (1000.0, 3000.0)
    if key == "extraction_residence_min": return (60.0, 75.0), (58.0, 120.0)
    if key == "pasteur_retention_s": return (20.0, 25.0), (15.0, 60.0)
    if key == "extraction_temp_c": return (50.0, 60.0), (40.0, 75.0)
    if key == "ro_tmp_bar": return (22.0, 26.0), (15.0, 40.0)
    if key == "evap_temp_c": return (73.0, 77.0), (60.0, 85.0)
    if key == "precip_time_min": return (20.0, 30.0), (10.0, 60.0)
    if key == "centrifuge_time_min": return (18.0, 22.0), (10.0, 40.0)
    if key == "dryer_residence_min": return (38.0, 46.0), (20.0, 90.0)
    if key == "water_temp_c": return (50.0, 60.0), (40.0, 75.0)

    # Generic heuristic
    return (default * 0.9, default * 1.1), (default * 0.7, default * 1.3)


def render_equipment_specs_editor() -> None:
    specs = st.session_state.equipment_specs

    for idx, (group_label, keys) in enumerate(EQUIPMENT_GROUPS):
        with st.expander(f"Dimensiones · {group_label}", expanded=(idx == 0)):
            for key in keys:
                vmin, vmax = EQUIPMENT_SPEC_LIMITS[key]
                val = st.number_input(
                    EQUIPMENT_SPEC_LABELS.get(key, key),
                    min_value=float(vmin),
                    max_value=float(vmax),
                    value=float(specs[key]),
                    step=_get_widget_step(vmin, vmax),
                    key=f"w_eq_{key}",
                )

    sync_equipment_specs_from_widgets()


def render_capacity_limits_editor() -> None:
    limits = st.session_state.capacity_limits
    with st.expander("Restricciones avanzadas · Capacidad/Eficiencia", expanded=False):
        st.caption("Estos umbrales gobiernan el bloqueo duro cuando una capacidad de equipo es excedida.")
        for key in CAPACITY_LIMIT_DEFAULTS:
            vmin, vmax = CAPACITY_LIMIT_BOUNDS[key]
            st.number_input(
                CAPACITY_LIMIT_LABELS.get(key, key),
                min_value=float(vmin),
                max_value=float(vmax),
                value=float(limits[key]),
                step=_get_widget_step(vmin, vmax),
                key=f"w_lim_{key}",
            )

    sync_capacity_limits_from_widgets()


def render_sales_modification_panel() -> None:
    with st.expander("Modificacion comercial", expanded=True):
        st.number_input(
            "Costo de venta (Bs/kg)",
            min_value=0.0,
            max_value=200.0,
            value=float(st.session_state.sales_price_bs_kg),
            step=0.05,
            key="w_sales_price_bs_kg",
        )
        sync_sales_price_from_widgets()
        st.caption(
            f"Fuente documental: escenario base {DEFAULT_SALES_PRICE_BS_PER_KG:.2f} Bs/kg (~3.50 USD/kg) | "
            f"OPEX anual fijo: {_format_number_es(DOC_OPEX_TOTAL_ANNUAL_BS, 0)} Bs"
        )


def render_capacity_issues() -> None:
    if st.session_state.capacity_issues:
        st.error("Simulacion bloqueada por capacidad de equipos.")
        for issue in st.session_state.capacity_issues:
            st.warning(
                f"[{issue['equipment']}] {issue['message']}\n\n"
                f"Recomendacion: {issue['recommendation']}"
            )
    elif st.session_state.last_run_error:
        st.error(st.session_state.last_run_error)


def _render_control_with_pv(label: str, key: str, vmin: float, vmax: float, step: float) -> float:
    pv = st.session_state.pv_controls.get(key, st.session_state.controls[key])

    col_sp, col_pv = st.columns([3, 1])
    with col_sp:
        val = st.number_input(label, vmin, vmax, value=st.session_state.controls[key], step=step, key=f"w_{key}")
    with col_pv:
        st.markdown(f"<div style='margin-top: 32px;'><small>PV:</small><br><b>{pv:.2f}</b></div>", unsafe_allow_html=True)

    return val





def apply_process_inertia(dt: float) -> None:
    """Aplica inercia de primer orden a las variables de proceso (PV) hacia los Setpoints (SP)."""
    specs = st.session_state.equipment_specs
    controls = st.session_state.controls

    # Inercia calculada segun capacidad (Residencia Hidraulica Escalada)
    v0 = specs.get("stage_0_tank_capacity_m3", 15.0)
    q0 = max(controls.get("water_flow_m3_h", 12.0), 1.0)
    tau_water = max(10.0, (v0 / q0) * 10.0) # Escalado para realismo en app

    v1 = specs.get("stage_1_tank_capacity_m3", 15.0)
    q1 = q0 + (controls.get("soy_feed_kg_h", 1000.0) / 1000.0)
    tau_ext = max(15.0, (v1 / q1) * 12.0)

    # Constantes de tiempo (tau) en segundos
    TAUS = {
        "soy_feed_kg_h": 12.0,
        "water_flow_m3_h": 8.0,
        "water_temp_c": tau_water,
        "extraction_ph": tau_ext * 0.6,
        "extraction_temp_c": tau_ext,
        "extraction_residence_min": 60.0,
        "agitator_rpm": 4.0,
        "solid_liquid_ratio": 15.0,
        "pasteur_temp_c": 35.0,
        "pasteur_retention_s": 3.0,
        "evap_pressure_bar": 25.0,
        "evap_temp_c": 45.0,  # Inercia termica del evaporador en segundos (no confundir con temperatura)
        "precip_ph": 22.0,
        "precip_time_min": 8.0,
        "centrifuge_g": 12.0,
        "centrifuge_time_min": 4.0,
        "dryer_temp_c": 60.0,  # Inercia termica del secador en segundos (no confundir con temperatura)
        "dryer_residence_min": 8.0,
        "ro_tmp_bar": 15.0,  # Respuesta de presion de membrana RO
    }

    for key, sp in st.session_state.controls.items():
        pv_old = st.session_state.pv_controls.get(key, sp)
        tau = TAUS.get(key, 20.0)
        # PV_new = PV_old + (SP - PV_old) * (1 - exp(-dt / tau))
        # Si dt >> tau, PV_new aproxima SP.
        alpha = 1.0 - math.exp(-dt / tau)
        pv_new = pv_old + (sp - pv_old) * alpha
        st.session_state.pv_controls[key] = pv_new


def run_step() -> None:
    cycle_s = float(st.session_state.interval_s)

    # Aplicar inercia antes de correr el modelo
    apply_process_inertia(cycle_s)

    # Verificacion de rangos para paro del sistema usando PVs
    danger_vars = []

    # Chequeo de Controles
    for key, value in st.session_state.pv_controls.items():
        # Obtenemos los rangos de seguridad (ideal, warning)
        _, warning = _get_variable_ranges(key, 0, 100) # vmin/vmax no afectan al warning en esta funcion
        w_min, w_max = warning
        if value < w_min or value > w_max:
            danger_vars.append(f"Control: {CONTROL_LABELS.get(key, key)} ({value:.2f} fuera del rango documental [{w_min}, {w_max}])")

    # Chequeo de Dimensionamiento
    for key, value in st.session_state.equipment_specs.items():
        _, warning = _get_variable_ranges(key, 0, 100)
        w_min, w_max = warning
        if value < w_min or value > w_max:
            danger_vars.append(f"Equipo: {EQUIPMENT_SPEC_LABELS.get(key, key)} ({value:.2f} fuera del rango documental [{w_min}, {w_max}])")

    if danger_vars:
        st.session_state.running = False
        st.session_state.last_run_error = "PARO DEL SISTEMA: Variables en rango de peligro."
        st.session_state.capacity_issues = [{"equipment": "SEGURIDAD", "message": v, "recommendation": "Ajuste la variable al rango ideal."} for v in danger_vars]
        return

    try:
        # El modelo ahora corre con los PVs calculados con inercia
        result = run_process_model(
            st.session_state.pv_controls,
            equipment_specs=st.session_state.equipment_specs,
            capacity_limits=st.session_state.capacity_limits,
        )
        result = _append_sales_stage(result)
    except EquipmentCapacityError as exc:
        st.session_state.running = False
        st.session_state.capacity_issues = exc.issues
        st.session_state.last_run_error = str(exc)
        return
    except (ValueError, TypeError, KeyError) as exc:
        st.session_state.running = False
        st.session_state.capacity_issues = []
        st.session_state.last_run_error = f"Error de validacion: {exc}"
        return

    st.session_state.capacity_issues = []
    st.session_state.last_run_error = ""
    st.session_state.last_result = result

    cycle_s = float(st.session_state.interval_s)
    protein_rate_kg_h = float(result["stage_5"]["protein_final_kg_h"])
    powder_rate_kg_h = float(result["stage_5"]["powder_mass_kg_h"])
    st.session_state.production_elapsed_s += cycle_s
    st.session_state.production_protein_kg += protein_rate_kg_h * (cycle_s / 3600.0)
    st.session_state.production_bags_1kg += powder_rate_kg_h * (cycle_s / 3600.0)

    # El snapshot debe registrar tanto SP como PV para telemetría
    snapshot = build_snapshot(
        st.session_state.pv_controls,
        result,
        equipment_specs=st.session_state.equipment_specs,
        capacity_limits=st.session_state.capacity_limits,
    )
    # Añadimos los setpoints explicitamente con prefijo sp_
    for k, v in st.session_state.controls.items():
        snapshot[f"sp_{k}"] = float(v)

    # Generate actual and predicted (both with noise for realism as requested)
    actual_noisy = _inject_independent_error(snapshot)
    predicted_noisy = _inject_independent_error(snapshot)

    st.session_state.log.append(actual_noisy)

    # Update sparkline history (last 60 seconds)
    # snapshot is flattened by build_snapshot, so we can iterate top-level keys
    max_points = int(60 / st.session_state.interval_s)
    for key in actual_noisy:
        if not (key.startswith("stage_") or key.startswith("capacity_")) or not isinstance(actual_noisy[key], (int, float)):
            continue

        if key not in st.session_state.sparkline_history:
            st.session_state.sparkline_history[key] = []

        st.session_state.sparkline_history[key].append({
            "actual": actual_noisy[key],
            "predicted": predicted_noisy[key]
        })

        if len(st.session_state.sparkline_history[key]) > max_points:
            st.session_state.sparkline_history[key] = st.session_state.sparkline_history[key][-max_points:]


def _error_base_pct_for_key(key: str) -> float:
    return KPI_ERROR_BASE_PCT.get(key, DEFAULT_ERROR_BASE_PCT)


def _inject_independent_error(snapshot: dict) -> dict:
    """Inyecta ruido independiente por ciclo para evitar valores planos en monitoreo."""
    noisy_snapshot = snapshot.copy()
    for key, value in snapshot.items():
        # Inject error only for process and capacity variables
        if not (key.startswith("stage_") or key.startswith("capacity_")) or not isinstance(value, (int, float)):
            continue

        base_error_pct = _error_base_pct_for_key(key)
        amplitude = max(abs(float(value)) * (base_error_pct / 100.0), base_error_pct * 0.01)
        noisy_value = float(value) + random.uniform(-amplitude, amplitude)
        if key.startswith("stage_ventas_operating_profit") or key.startswith("stage_ventas_profit_per_kg"):
            noisy_snapshot[key] = noisy_value
        else:
            noisy_snapshot[key] = max(0.0, noisy_value)

    return noisy_snapshot


def _compute_kpi_window_stats(key: str) -> dict | None:
    rows = st.session_state.log.rows
    if not rows:
        return None

    values = [r[key] for r in rows if key in r and r[key] is not None]
    if not values:
        return None

    current = float(values[-1])
    previous = float(values[-2]) if len(values) > 1 else current

    average = sum(values) / len(values)
    max_val = max(values)
    min_val = min(values)

    recent_values = values[-STABILITY_WINDOW_POINTS:]
    n_recent = len(recent_values)
    
    if n_recent > 1:
        mean_recent = sum(recent_values) / n_recent
        variance = sum((x - mean_recent) ** 2 for x in recent_values) / n_recent
        std_dev = math.sqrt(variance)
    else:
        std_dev = 0.0

    base_error_pct = _error_base_pct_for_key(key)
    error_abs = abs(current) * (base_error_pct / 100.0)
    band_pct = base_error_pct * ERROR_BAND_FACTOR
    lower_limit = average * (1.0 - (band_pct / 100.0))
    upper_limit = average * (1.0 + (band_pct / 100.0))
    if lower_limit > upper_limit:
        lower_limit, upper_limit = upper_limit, lower_limit

    delta_pct = ((current - previous) / abs(previous)) * 100.0 if abs(previous) > 1e-9 else 0.0
    relative_std_pct = (std_dev / abs(average)) * 100.0 if abs(average) > 1e-9 else 0.0

    return {
        "current": current,
        "average": average,
        "max": max_val,
        "min": min_val,
        "lower_limit": lower_limit,
        "upper_limit": upper_limit,
        "delta_pct": delta_pct,
        "error_abs": error_abs,
        "relative_std_pct": relative_std_pct,
        "stable": relative_std_pct <= base_error_pct,
    }


def _format_kpi_value(value: float, unit: str, decimals: int) -> str:
    number = _format_number_es(value, decimals)
    if unit:
        return f"{number} {unit}"
    return number


def _render_kpi_chart(key: str, stats: dict, theme: dict, chart_key: str | None = None) -> None:
    history = st.session_state.get("sparkline_history", {}).get(key, [])
    if len(history) < 2:
        return

    actual_values = [h["actual"] for h in history]

    stage_key = "s0"
    parts = key.split("_")
    if len(parts) > 1 and parts[0] == "stage":
        stage_id = parts[1]
        if stage_id in ["0", "1", "2", "3", "4", "5"]:
            stage_key = f"s{stage_id}"

    color = theme["stage_colors"].get(stage_key, theme["stage_colors"].get("s0", "#4a90e2"))
    
    y_min = stats["min"]
    y_max = stats["max"]
    y_range = y_max - y_min
    padding = abs(y_min) * 0.1 if y_range < 1e-6 and abs(y_min) > 1e-6 else (0.5 if y_range < 1e-6 else y_range * 0.1)

    fig_dict = {
        "data": [{
            "type": "scatter",
            "y": actual_values,
            "mode": "lines",
            "fill": "tozeroy",
            "name": "Actual",
            "line": {"color": color, "width": 3},
            "fillcolor": f"rgba({int(color[1:3],16)}, {int(color[3:5],16)}, {int(color[5:7],16)}, 0.1)",
            "hoverinfo": "y"
        }],
        "layout": {
            "height": 220,
            "margin": {"l": 10, "r": 10, "t": 30, "b": 10},
            "xaxis": {"showgrid": True, "gridcolor": theme["grid"], "showticklabels": False},
            "yaxis": {
                "showgrid": True,
                "gridcolor": theme["grid"],
                "tickfont": {"size": 10, "color": theme["muted_text"]},
                "range": [y_min - padding, y_max + padding]
            },
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "showlegend": False,
            "template": "plotly_dark",
            "shapes": [
                {"type": "line", "y0": stats["max"], "y1": stats["max"], "x0": 0, "x1": 1, "xref": "paper", "line": {"color": theme["status"]["rojo"], "width": 1, "dash": "dash"}},
                {"type": "line", "y0": stats["min"], "y1": stats["min"], "x0": 0, "x1": 1, "xref": "paper", "line": {"color": theme["status"]["amarillo"], "width": 1, "dash": "dash"}},
                {"type": "line", "y0": stats["average"], "y1": stats["average"], "x0": 0, "x1": 1, "xref": "paper", "line": {"color": theme["accent"], "width": 2}},
                {"type": "rect", "y0": stats["lower_limit"], "y1": stats["upper_limit"], "x0": 0, "x1": 1, "xref": "paper", "fillcolor": theme["grid"], "opacity": 0.2, "line": {"width": 0}}
            ]
        }
    }
    
    st.plotly_chart(go.Figure(fig_dict), use_container_width=True, config={"displayModeBar": False}, key=chart_key or f"spark_{key}")


def _render_kpi_card(
    key: str,
    label: str,
    unit: str,
    decimals: int,
    secondary_key: str | None = None,
    secondary_label: str = "Referencia",
    secondary_unit: str = "",
    secondary_decimals: int = 2,
    compact: bool = False,
    card_id: str | None = None,
) -> None:
    stats = _compute_kpi_window_stats(key)
    theme = get_active_theme()
    if not stats:
        st.metric(label, "Sin datos", delta="0.00%")
        return

    if compact:
        st.metric(label, _format_kpi_value(stats["current"], unit, decimals))
        return

    with st.container():
        # Arriba: Título, Valor y Varianza (Delta)
        st.metric(
            label,
            _format_kpi_value(stats["current"], unit, decimals),
            delta=_format_pct_delta_es(stats["delta_pct"]),
        )

        # En medio: Error Porcentual y Status
        error_pct = (stats['error_abs'] / abs(stats['current'])) * 100 if stats['current'] != 0 else 0.0
        status_class = "kpi-stable" if stats["stable"] else "kpi-unstable"
        status_text = "Estable" if stats["stable"] else "Inestable"
        
        st.markdown(
            f"<div style='margin-top: -10px; margin-bottom: 10px; display: flex; flex-direction: column; gap: 4px;'>"
            f"<div class='kpi-meta'><b>Error:</b> ±{error_pct:.2f}% ({_format_kpi_value(stats['error_abs'], unit, decimals)})</div>"
            f"<div class='kpi-status {status_class}' style='width: fit-content;'>{status_text} | Var: {stats['relative_std_pct']:.2f}%</div>"
            f"</div>",
            unsafe_allow_html=True,
        )

        if secondary_key:
            secondary_stats = _compute_kpi_window_stats(secondary_key)
            if secondary_stats:
                st.markdown(
                    f"<div class='kpi-meta' style='margin-bottom: 10px;'>{secondary_label}: {_format_kpi_value(secondary_stats['current'], secondary_unit, secondary_decimals)}</div>",
                    unsafe_allow_html=True,
                )

        # Abajo: Gráfico de líneas/Sparkline
        _render_kpi_chart(key, stats, theme, chart_key=f"spark_{card_id or key}")


def render_kpis() -> None:
    result = st.session_state.last_result
    capacity = result.get("capacity", {})

    c1, c2, c3 = st.columns(3)
    with c1:
        _render_kpi_card("stage_5_protein_final_kg_h", "Proteina final", "kg/h", 1, card_id="top_protein")
    with c2:
        _render_kpi_card("stage_5_overall_yield_pct", "Rendimiento global", "%", 1, card_id="top_yield")
    with c3:
        _render_kpi_card("stage_3_evaporated_water_m3_h", "Agua evaporada", "m3/h", 2, card_id="top_evap")

    st.caption("Baselines documentales: extraccion 88% (pH 8.75), pasteurizacion 80 C / 22 s, evaporacion 0.40 bar / 75 C, precipitacion pH 4.5.")

    if capacity:
        u1, u2, u3 = st.columns(3)
        with u1:
            _render_kpi_card("capacity_stage_0_tank_utilization_pct", "Uso tanque E0", "%", 1)
        with u2:
            _render_kpi_card("capacity_stage_2_hex_thermal_load_pct", "Uso intercambiador", "%", 1)
        with u3:
            _render_kpi_card("capacity_stage_5_dryer_load_pct", "Uso secador", "%", 1)






def render_stage_tab(stage_idx: int) -> None:
    has_data = bool(st.session_state.log)
    
    # Mapeo de controles por etapa
    stage_controls = {
        0: [
            ("Alimentacion de soya (kg/h)", "soy_feed_kg_h", 900.0, 1100.0, 100.0),
            ("Caudal de agua (m3/h)", "water_flow_m3_h", 11.0, 13.0, 0.1),
            ("Temperatura de agua (C)", "water_temp_c", 5.0, 90.0, 0.5),
        ],
        1: [
            ("pH extraccion", "extraction_ph", 8.0, 9.5, 0.01),
            ("Temperatura extraccion (C)", "extraction_temp_c", 20.0, 95.0, 0.5),
            ("Tiempo residencia (min)", "extraction_residence_min", 58.0, 90.0, 1.0),
            ("Velocidad agitacion (RPM)", "agitator_rpm", 10.0, 500.0, 1.0),
            ("Ratio solido/liquido (1:x)", "solid_liquid_ratio", 4.0, 30.0, 0.1),
        ],
        2: [
            ("Temperatura de pasteurizacion (C)", "pasteur_temp_c", 50.0, 130.0, 0.5),
            ("Retencion termica (s)", "pasteur_retention_s", 2.0, 180.0, 1.0),
        ],
        3: [
            ("Presion Transmembrana OI (bar)", "ro_tmp_bar", 15.0, 40.0, 0.5),
        ],
        4: [
            ("Presion evaporador (bar abs)", "evap_pressure_bar", 0.05, 1.20, 0.01),
            ("Temperatura evaporacion (C)", "evap_temp_c", 20.0, 95.0, 0.5),
        ],
        5: [
            ("pH de precipitacion", "precip_ph", 4.1, 4.9, 0.01),
            ("Tiempo de precipitacion (min)", "precip_time_min", 2.0, 120.0, 1.0),
            ("Factor G centrifuga", "centrifuge_g", 200.0, 5000.0, 10.0),
            ("Tiempo centrifugacion (min)", "centrifuge_time_min", 1.0, 120.0, 1.0),
        ],
        6: [
            ("Temperatura de secado (C)", "dryer_temp_c", 170.0, 210.0, 1.0),
            ("Residencia en secador (min)", "dryer_residence_min", 1.0, 180.0, 1.0),
        ]
    }

    # Mapeo de KPIs por etapa (heredado de STAGE_KPI_CONFIG)
    
    left, right = st.columns([1, 2], gap="large")
    
    with left:
        st.subheader("Controles de Proceso")
        if stage_idx in stage_controls:
            for label, key, vmin, vmax, step in stage_controls[stage_idx]:
                _render_control_with_pv(label, key, vmin, vmax, step)
        
        st.divider()
        st.subheader("Especificaciones de Equipo")
        if stage_idx < len(EQUIPMENT_GROUPS):
            group_label, keys = EQUIPMENT_GROUPS[stage_idx]
            st.caption(group_label)
            for key in keys:
                vmin, vmax = EQUIPMENT_SPEC_LIMITS[key]
                val = st.number_input(
                    EQUIPMENT_SPEC_LABELS.get(key, key),
                    min_value=float(vmin),
                    max_value=float(vmax),
                    value=float(st.session_state.equipment_specs[key]),
                    step=_get_widget_step(vmin, vmax),
                    key=f"w_eq_{key}",
                )
        
        sync_equipment_specs_from_widgets()
        
        st.divider()
        st.subheader("Restricciones de Capacidad")
        if stage_idx < len(CAPACITY_GROUPS):
            c_group_label, c_keys = CAPACITY_GROUPS[stage_idx]
            st.caption(c_group_label)
            for key in c_keys:
                vmin, vmax = CAPACITY_LIMIT_BOUNDS[key]
                st.number_input(
                    CAPACITY_LIMIT_LABELS.get(key, key),
                    min_value=float(vmin),
                    max_value=float(vmax),
                    value=float(st.session_state.capacity_limits[key]),
                    step=_get_widget_step(vmin, vmax),
                    key=f"w_lim_{key}",
                )
        
        sync_capacity_limits_from_widgets()
        sync_controls_from_widgets()

    with right:
        st.subheader("Monitoreo en Tiempo Real")
        if not has_data:
            st.info("Sin datos de telemetria.")
        else:
            kpi_idx = stage_idx
            
            if kpi_idx < len(STAGE_KPI_CONFIG):
                config = STAGE_KPI_CONFIG[kpi_idx]
                st.caption(config["title"])
                cols_per_row = 2
                for i in range(0, len(config["metrics"]), cols_per_row):
                    k_cols = st.columns(cols_per_row, gap="medium")
                    for j in range(cols_per_row):
                        m_idx = i + j
                        if m_idx < len(config["metrics"]):
                            metric = config["metrics"][m_idx]
                            with k_cols[j]:
                                _render_kpi_card(
                                    key=metric["key"],
                                    label=metric["label"],
                                    unit=metric["unit"],
                                    decimals=metric["decimals"],
                                    card_id=f"tab_{stage_idx}_{metric['key']}"
                                )
                    st.write("") # Espaciado vertical entre filas
            
            # Visuales Técnicos por Etapa (Data-Driven)
            st.markdown("---")
            STAGE_IMAGES = {
                0: ("assets/image/tamizado_y_molienda.png", "Sistema de Limpieza y Molienda M-100"),
                1: ("assets/image/tanque_agitado.png", "Tanque Agitado TK-101 (Lixiviacion Alcalina)"),
                2: ("assets/image/intercambiador_de_calor.png", "Intercambiador HX-201 (Pasteurizacion HTST)"),
                3: ("assets/image/osmosis_inversa.png", "Osmosis Inversa RO-205 (Membranas TFC)"),
                4: ("assets/image/evaporador_de_doble_efecto.png", "Evaporador Doble Efecto EV-301"),
                5: ("assets/image/precipitador_isoelectrico.png", "Precipitacion Isoelectrica TK-401"),
                6: ("assets/image/spray_dryer.png", "Secador Spray SD-501 (Atomizacion Rotativa)"),
            }
            if stage_idx in STAGE_IMAGES:
                img_path, img_caption = STAGE_IMAGES[stage_idx]
                try:
                    st.image(img_path, caption=img_caption, use_container_width=True)
                except Exception:
                    st.caption(f"Imagen no disponible: {img_path}")

init_state()
apply_visual_theme_css()

# HEADER CON CONTROLES TOP-RIGHT
head_left, head_right = st.columns([2, 1])

with head_left:
    st.title("Gemelo Digital AJAX")
    st.markdown(
        "<div class='hero-panel'><strong>Consola Unificada:</strong> Operacion y monitoreo integrado por etapas.</div>",
        unsafe_allow_html=True,
    )

with head_right:
    st.markdown("### Panel de Control")
    c1, c2, c3, c4 = st.columns(4)
    if c1.button("▶", help="Iniciar Simulación"):
        st.session_state.running = True
    if c2.button("⏸", help="Pausar Simulación"):
        st.session_state.running = False
    if c3.button("⏭", help="Paso"):
        run_step()
    if c4.button("🔄", help="Reiniciar"):
        st.session_state.pending_full_reset = True
        st.rerun()
    
    st.session_state.interval_s = st.slider("Ciclo (s)", 0.5, 5.0, value=float(st.session_state.interval_s), step=0.1)
    
    if st.session_state.running:
        st.markdown("<small><span class='status-pill status-running'></span> SISTEMA EN LINEA</small>", unsafe_allow_html=True)
    else:
        st.markdown("<small><span class='status-pill status-paused'></span> SISTEMA EN ESPERA</small>", unsafe_allow_html=True)

# DASHBOARD PRINCIPAL
render_capacity_issues()

# ... (dentro de los tabs)

tab_labels = ["E0: Captacion", "E1: Extraccion", "E2: Pasteurizacion", "E-RO: Osmosis Inversa", "E3: Evaporacion", "E4: Precipitacion", "E5: Secado", "Vista Global"]
main_tabs = st.tabs(tab_labels)

for i, tab in enumerate(main_tabs):
    with tab:
        if i < 7:
            render_stage_tab(i)
        elif i == 7:
            # Vista Global — Dashboard Integrado del Gemelo Digital
            result = st.session_state.last_result

            # ─── 1) INTEGRIDAD DEL BALANCE DE MASA ───────────────────
            st.subheader("Integridad del Balance de Masa")
            integrity = result.get("integrity", {})
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                closure = integrity.get("mass_balance_closure_pct", 0.0)
                st.metric("Cierre de Balance", f"{closure:.2f}%")
            with m2:
                st.metric("Masa Entrada", f"{integrity.get('mass_in_kg_h', 0.0):,.1f} kg/h")
            with m3:
                st.metric("Masa Salida", f"{integrity.get('mass_out_kg_h', 0.0):,.1f} kg/h")
            with m4:
                st.metric("Mermas Totales", f"{integrity.get('total_mermas_kg_h', 0.0):,.1f} kg/h")

            st.divider()

            # ─── 2) KPIs PRINCIPALES ──────────────────────────────────
            st.subheader("KPIs de Produccion")
            render_kpis()

            st.divider()

            # ─── 3) PRODUCCION ACUMULADA ──────────────────────────────
            st.subheader("Produccion Acumulada (Sesion)")
            elapsed_h = st.session_state.production_elapsed_s / 3600.0
            p1, p2, p3, p4 = st.columns(4)
            with p1:
                st.metric("Tiempo Operativo", f"{elapsed_h:.2f} h")
            with p2:
                st.metric("Proteina Producida", f"{st.session_state.production_protein_kg:,.1f} kg")
            with p3:
                bags = st.session_state.production_bags_1kg
                st.metric("Polvo ISP Producido", f"{bags:,.1f} kg")
            with p4:
                sacks_20kg = bags / 20.0
                st.metric("Sacos (20 kg)", f"{sacks_20kg:,.0f}")

            st.divider()

            # ─── 4) PANEL FINANCIERO AVANZADO ─────────────────────────
            col_fin, col_eco = st.columns([1, 1])
            with col_fin:
                st.subheader("Simulacion Financiera")
                powder_kg_h = result.get("stage_5", {}).get("powder_mass_kg_h", 301.6)
                fm = FinancialModeler(powder_mass_kg_h=powder_kg_h)
                fin = fm.run_financial_simulation()

                f1, f2 = st.columns(2)
                with f1:
                    st.metric("CAPEX Total", f"${fin['capex_total_usd']:,.0f} USD")
                    st.metric("NPV (10a, 12%)", f"${fin['npv_usd']:,.0f} USD")
                    st.metric("Offset Circular", f"${fin['circularity_offset_usd']:,.0f} USD/a")
                with f2:
                    st.metric("Payback Period", f"{fin['payback_years']:.2f} a")
                    st.metric("EBITDA", f"${fin['ebitda_usd']:,.0f} USD/a")
                    st.metric("OPEX Neto", f"${fin['opex_total_net_usd']:,.0f} USD/a")

            with col_eco:
                render_sales_modification_panel()

            st.divider()

            # ─── 5) MATRIZ DE CRITICIDAD FMEA (Doc 10.2) ─────────────
            st.subheader("Matriz de Criticidad FMEA")

            fmea_data = [
                {"var": "pH Precipitacion TK-401", "falla": "pH fuera 4.5+-0.2", "s": 8, "o": 6, "d": 3, "npr": 144, "nivel": "CRITICO", "ck": "precip_ph"},
                {"var": "Humedad Final SD-501", "falla": "Humedad >6%", "s": 9, "o": 4, "d": 3, "npr": 108, "nivel": "ALTA", "ck": "dryer_temp_c"},
                {"var": "Vacio Evaporador EV-301", "falla": "P >0.6 bar", "s": 7, "o": 5, "d": 2, "npr": 70, "nivel": "ALTA", "ck": "evap_pressure_bar"},
                {"var": "pH Extraccion TK-101", "falla": "pH <8.0", "s": 8, "o": 4, "d": 2, "npr": 64, "nivel": "ALTA", "ck": "extraction_ph"},
                {"var": "T Past. HX-201", "falla": "T <75C", "s": 9, "o": 3, "d": 1, "npr": 27, "nivel": "MEDIA", "ck": "pasteur_temp_c"},
            ]

            pv = st.session_state.pv_controls
            fmea_md = "| Variable | Modo de Falla | S | O | D | NPR | Nivel | Estado |\n"
            fmea_md += "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |\n"
            for row in fmea_data:
                current_pv = pv.get(row["ck"], 0.0)
                ideal, fail = _get_variable_ranges(row["ck"], 0, 100)
                if ideal[0] <= current_pv <= ideal[1]:
                    status = "OK"
                elif fail[0] <= current_pv <= fail[1]:
                    status = "ALERTA"
                else:
                    status = "FALLO"
                npr_str = f"**{row['npr']}**" if row["npr"] >= 100 else str(row["npr"])
                fmea_md += f"| {row['var']} | {row['falla']} | {row['s']} | {row['o']} | {row['d']} | {npr_str} | {row['nivel']} | {status} |\n"

            st.markdown(fmea_md)
            st.caption("NPR = Severidad x Ocurrencia x Deteccion. Niveles >= 100 requieren accion inmediata.")

            st.divider()
            st.image("assets/image/planta_industrial_soja.png", caption="Gemelo Digital: Topologia de Planta Integrada", use_container_width=True)

if st.session_state.running:
    run_step()
    if st.session_state.running:
        time.sleep(st.session_state.interval_s)
    st.rerun()
