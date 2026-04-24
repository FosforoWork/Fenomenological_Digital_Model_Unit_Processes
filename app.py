"""Gemelo Digital AJAX - Sala de control en tiempo real para proceso de proteina aislada de soya."""

from __future__ import annotations

from pathlib import Path
import random
import re
import time
import unicodedata

import pandas as pd
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
    compute_sales_stage,
)
from core.stage_equations import BASELINE_REFERENCES, run_process_model
from visualizaciones.fluidograma_integrado import build_fluidograma_payload, build_fluidograma_sankey


VISUAL_THEMES = {
    "Contraste Alto": {
        "plot_template": "plotly_dark",
        "bg_start": "#0f172a",
        "bg_end": "#1e293b",
        "bg_glow": "#334155",
        "text": "#f8fafc",
        "muted_text": "#94a3b8",
        "card_bg": "rgba(30, 41, 59, 0.85)",
        "border": "#334155",
        "note_bg": "#1e293b",
        "note_border": "#334155",
        "note_text": "#f8fafc",
        "grid": "rgba(148, 163, 184, 0.20)",
        "stage_colors": {
            "s0": "#38bdf8",
            "s1": "#22c55e",
            "s2": "#f59e0b",
            "s2_5": "#3b82f6",
            "s3": "#fb7185",
            "s4": "#f43f5e",
            "s5": "#ef4444",
        },
        "status": {"verde": "#10b981", "amarillo": "#f59e0b", "rojo": "#ef4444"},
        "aux": ["#38bdf8", "#a78bfa", "#fbbf24"],
    },
    "Brillo Alto": {
        "plot_template": "plotly_white",
        "bg_start": "#fff8ef",
        "bg_end": "#e8f3ff",
        "bg_glow": "#ffe4c4",
        "text": "#0f172a",
        "muted_text": "#334155",
        "card_bg": "rgba(255, 255, 255, 0.92)",
        "border": "#cbd5e1",
        "note_bg": "#fffbeb",
        "note_border": "#fed7aa",
        "note_text": "#7c2d12",
        "grid": "rgba(148, 163, 184, 0.35)",
        "stage_colors": {
            "s0": "#0284c7",
            "s1": "#16a34a",
            "s2": "#d97706",
            "s2_5": "#2563eb",
            "s3": "#db2777",
            "s4": "#dc2626",
            "s5": "#0f766e",
        },
        "status": {"verde": "#059669", "amarillo": "#d97706", "rojo": "#dc2626"},
        "aux": ["#0ea5e9", "#6366f1", "#f59e0b"],
    },
    "Contraste Suave": {
        "plot_template": "plotly_white",
        "bg_start": "#f4f4f5",
        "bg_end": "#e4e4e7",
        "bg_glow": "#d4d4d8",
        "text": "#27272a",
        "muted_text": "#52525b",
        "card_bg": "rgba(250, 250, 250, 0.86)",
        "border": "#a1a1aa",
        "note_bg": "#f5f5f4",
        "note_border": "#d6d3d1",
        "note_text": "#44403c",
        "grid": "rgba(113, 113, 122, 0.22)",
        "stage_colors": {
            "s0": "#64748b",
            "s1": "#4d7c0f",
            "s2": "#b45309",
            "s2_5": "#4f46e5",
            "s3": "#be185d",
            "s4": "#b91c1c",
            "s5": "#0f766e",
        },
        "status": {"verde": "#4d7c0f", "amarillo": "#b45309", "rojo": "#b91c1c"},
        "aux": ["#0284c7", "#7c3aed", "#ca8a04"],
    },
    "Brillo Bajo": {
        "plot_template": "plotly_dark",
        "bg_start": "#0f172a",
        "bg_end": "#1e293b",
        "bg_glow": "#334155",
        "text": "#dbeafe",
        "muted_text": "#94a3b8",
        "card_bg": "rgba(30, 41, 59, 0.85)",
        "border": "#475569",
        "note_bg": "#1e293b",
        "note_border": "#334155",
        "note_text": "#cbd5e1",
        "grid": "rgba(148, 163, 184, 0.20)",
        "stage_colors": {
            "s0": "#0ea5e9",
            "s1": "#22c55e",
            "s2": "#eab308",
            "s2_5": "#60a5fa",
            "s3": "#f472b6",
            "s4": "#fb7185",
            "s5": "#f87171",
        },
        "status": {"verde": "#22c55e", "amarillo": "#eab308", "rojo": "#f87171"},
        "aux": ["#22d3ee", "#818cf8", "#fbbf24"],
    },
}


DEFAULT_CONTROLS = {
    "soy_feed_kg_h": 1000.0,
    "water_flow_m3_h": 12.0,
    "water_temp_c": 25.0,
    "extraction_ph": 8.75,
    "extraction_temp_c": 55.0,
    "extraction_residence_min": 54.0,
    "agitator_rpm": 80.0,
    "solid_liquid_ratio": 12.0,
    "pasteur_temp_c": 80.0,
    "pasteur_retention_s": 22.0,
    "ro_tmp_bar": 24.0,
    "ro_crossflow_ms": 1.5,
    "ro_feed_temp_c": 28.0,
    "ro_feed_ph": 7.0,
    "ro_sdi": 3.0,
    "evap_pressure_bar": 0.40,
    "evap_temp_c": 55.0,
    "precip_ph": 4.5,
    "precip_time_min": 25.0,
    "centrifuge_g": 1800.0,
    "centrifuge_time_min": 20.0,
    "dryer_temp_c": 78.0,
    "dryer_residence_min": 42.0,
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
    ("Etapa 2.5 · Osmosis inversa", [
        "stage_2_5_ro_base_recovery",
        "stage_2_5_ro_membrane_area_m2",
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
    "stage_2_5_ro_base_recovery": "Recuperacion base OI (frac)",
    "stage_2_5_ro_membrane_area_m2": "Area de membrana OI (m2)",
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


CAPACITY_LIMIT_LABELS = {
    "tank_max_fill_fraction": "Maximo llenado tanque Etapa 0",
    "stage_1_tank_max_fill_fraction": "Maximo llenado tanque Etapa 1",
    "pump_max_load_fraction": "Maximo uso motor bomba",
    "stage_2_hex_max_thermal_load_fraction": "Maximo uso termico intercambiador",
    "stage_2_hex_min_area_m2": "Area minima eficiente intercambiador (m2)",
    "stage_2_hex_max_area_m2": "Area maxima eficiente intercambiador (m2)",
    "stage_2_5_ro_min_flux_lmh": "Flujo minimo OI (LMH)",
    "stage_2_5_ro_max_flux_lmh": "Flujo maximo OI (LMH)",
    "stage_3_evap_max_load_fraction": "Maximo uso evaporador",
    "stage_4_2_centrifuge_max_load_fraction": "Maximo uso centrifuga",
    "stage_5_dryer_max_load_fraction": "Maximo uso secador",
    "stage_5_max_powder_rate_kg_h_m3": "Maximo polvo por volumen secador (kg/h/m3)",
}


IMPACT_STAGE_ORDER = [
    "Etapa 0",
    "Etapa 1",
    "Etapa 2",
    "Etapa 2.5",
    "Etapa 3",
    "Etapa 4",
    "Etapa 5",
]


CONTROL_STAGE_LABELS = {
    "soy_feed_kg_h": "Etapa 0",
    "water_flow_m3_h": "Etapa 0",
    "water_temp_c": "Etapa 0",
    "extraction_ph": "Etapa 1",
    "extraction_temp_c": "Etapa 1",
    "extraction_residence_min": "Etapa 1",
    "agitator_rpm": "Etapa 1",
    "solid_liquid_ratio": "Etapa 1",
    "pasteur_temp_c": "Etapa 2",
    "pasteur_retention_s": "Etapa 2",
    "ro_tmp_bar": "Etapa 2.5",
    "ro_crossflow_ms": "Etapa 2.5",
    "ro_feed_temp_c": "Etapa 2.5",
    "ro_feed_ph": "Etapa 2.5",
    "ro_sdi": "Etapa 2.5",
    "evap_pressure_bar": "Etapa 3",
    "evap_temp_c": "Etapa 3",
    "precip_ph": "Etapa 4",
    "precip_time_min": "Etapa 4",
    "centrifuge_g": "Etapa 4",
    "centrifuge_time_min": "Etapa 4",
    "dryer_temp_c": "Etapa 5",
    "dryer_residence_min": "Etapa 5",
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
    "ro_tmp_bar": "TMP OI (bar)",
    "ro_crossflow_ms": "Velocidad cruzada OI (m/s)",
    "ro_feed_temp_c": "Temperatura alimentacion OI (C)",
    "ro_feed_ph": "pH alimentacion OI",
    "ro_sdi": "SDI",
    "evap_pressure_bar": "Presion evaporador (bar abs)",
    "evap_temp_c": "Temperatura evaporacion (C)",
    "precip_ph": "pH de precipitacion",
    "precip_time_min": "Tiempo de precipitacion (min)",
    "centrifuge_g": "Factor G centrifuga",
    "centrifuge_time_min": "Tiempo centrifugacion (min)",
    "dryer_temp_c": "Temperatura de secado (C)",
    "dryer_residence_min": "Residencia en secador (min)",
}


CONTROL_IMPACT_META = {
    "soy_feed_kg_h": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Escala el flujo proteico en toda la cascada de etapas.",
    },
    "water_flow_m3_h": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Modifica dilucion y tiempo de residencia hidraulico global.",
    },
    "water_temp_c": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Se registra como condicion de entrada con efecto indirecto.",
    },
    "extraction_ph": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Cambia fuertemente la eficiencia de extraccion proteica.",
    },
    "extraction_temp_c": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Afecta cinetica y desnaturalizacion en extraccion.",
    },
    "extraction_residence_min": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Controla tiempo de contacto y conversion efectiva.",
    },
    "agitator_rpm": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Influye en mezcla y gradientes de transferencia de masa.",
    },
    "solid_liquid_ratio": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Afecta reologia del lodo y eficiencia de extraccion.",
    },
    "pasteur_temp_c": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Impacta factor de calidad proteica post-tratamiento termico.",
    },
    "pasteur_retention_s": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Define severidad termica y perdida de calidad.",
    },
    "ro_tmp_bar": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Cambia recuperacion OI y carga posterior de evaporacion.",
    },
    "ro_crossflow_ms": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Modula polarizacion y recuperacion de permeado.",
    },
    "ro_feed_temp_c": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Afecta viscosidad del flujo y rendimiento OI.",
    },
    "ro_feed_ph": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Afecta retencion proteica y estabilidad de membrana.",
    },
    "ro_sdi": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Incrementa ensuciamiento y reduce recuperacion efectiva.",
    },
    "evap_pressure_bar": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Ajusta solidos objetivo y agua evaporada equivalente.",
    },
    "evap_temp_c": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Modifica concentracion objetivo y demanda termica.",
    },
    "precip_ph": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Gobierna eficiencia de precipitacion isoelectrica.",
    },
    "precip_time_min": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Define crecimiento de floculo y recuperacion de solidos.",
    },
    "centrifuge_g": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Afecta recuperacion y humedad de pasta en separacion.",
    },
    "centrifuge_time_min": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Ajusta recuperacion y humedad residual en pasta.",
    },
    "dryer_temp_c": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Controla humedad final y masa de polvo producido.",
    },
    "dryer_residence_min": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Define remocion de agua y estabilidad final del polvo.",
    },
}


EQUIPMENT_IMPACT_META = {
    "stage_0_tank_capacity_m3": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Afecta autonomia y bloqueos por capacidad, no la cinetica base.",
    },
    "stage_0_tank_reserve_factor": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Margen de diseno que ajusta volumen requerido de tanque.",
    },
    "stage_0_pump_head_m": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Afecta potencia de bombeo mas que calidad de proceso.",
    },
    "stage_0_pump_eta_hyd": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Impacta eficiencia energetica del bombeo.",
    },
    "stage_0_pump_eta_motor": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Impacta consumo electrico del bombeo.",
    },
    "stage_0_pump_motor_kw": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Actua como limite de carga y bloqueo.",
    },
    "stage_1_slurry_density_kg_m3": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Ajusta conersion caudal masico-volumetrico para capacidad.",
    },
    "stage_1_tank_capacity_m3": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Define holdup disponible y bloqueo por llenado.",
    },
    "stage_1_tank_reserve_factor": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Margen de diseno en tiempo de residencia objetivo.",
    },
    "stage_1_base_extraction_eff": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Parametro base multiplicativo de extraccion global.",
    },
    "stage_1_2_extract_recovery": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Modifica flujo recuperado y balance hacia neutralizacion.",
    },
    "stage_2_acid_addition_m3_h": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Ajusta levemente el caudal y dilucion.",
    },
    "stage_2_cp_kj_kgk": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Impacta deber termico calculado en pasteurizacion.",
    },
    "stage_2_hex_area_m2": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Variable de capacidad termica del intercambiador.",
    },
    "stage_2_hex_u_w_m2k": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Define limite de transferencia de calor disponible.",
    },
    "stage_2_hex_lmtd_c": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Ajusta capacidad termica por gradiente efectivo.",
    },
    "stage_2_5_ro_base_recovery": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Define base de recuperacion OI y carga a evaporacion.",
    },
    "stage_2_5_ro_membrane_area_m2": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Controla flujo especifico y cumplimiento de limites LMH.",
    },
    "stage_3_solids_to_protein_ratio": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Afecta concentracion, evaporacion y balance de masa.",
    },
    "stage_3_steam_economy": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Impacta utilidades de vapor mas que el rendimiento masico.",
    },
    "stage_3_evap_capacity_m3_h": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Umbral de capacidad que bloquea fuera de rango.",
    },
    "stage_4_base_precip_eff": {
        "impact": "ALTO",
        "significant": True,
        "reason": "Parametro base de recuperacion proteica en precipitacion.",
    },
    "stage_4_2_co_solids_kg_h": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Aporta masa seca adicional y afecta flujo al secador.",
    },
    "stage_4_2_base_moisture_frac": {
        "impact": "MEDIO",
        "significant": True,
        "reason": "Determina masa de pasta y agua a remover en secado.",
    },
    "stage_4_2_centrifuge_capacity_m3_h": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Limite de capacidad de separacion por carga.",
    },
    "stage_5_dryer_evap_capacity_kg_h": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Define carga maxima de evaporacion del secador.",
    },
    "stage_5_dryer_chamber_volume_m3": {
        "impact": "BAJO/CONDICIONAL",
        "significant": False,
        "reason": "Ajusta carga volumetrica permitida del secado.",
    },
}


IMPACT_PRIORITY = {
    "ALTO": 0,
    "MEDIO": 1,
    "BAJO/CONDICIONAL": 2,
}


def _get_equipment_stage_labels() -> dict[str, str]:
    stage_map: dict[str, str] = {}
    for group_label, keys in EQUIPMENT_GROUPS:
        stage = group_label.split("·", maxsplit=1)[0].strip()
        for key in keys:
            stage_map[key] = stage
    return stage_map


def _build_variable_impact_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for key in DEFAULT_CONTROLS:
        meta = CONTROL_IMPACT_META[key]
        rows.append({
            "Etapa": CONTROL_STAGE_LABELS[key],
            "Tipo": "Control",
            "Variable": CONTROL_LABELS[key],
            "Clave": key,
            "Impacto temporal": meta["impact"],
            "Significativa": "SI" if meta["significant"] else "NO",
            "Justificacion": meta["reason"],
        })

    stage_map = _get_equipment_stage_labels()
    for key in EQUIPMENT_SPEC_DEFAULTS:
        meta = EQUIPMENT_IMPACT_META[key]
        rows.append({
            "Etapa": stage_map[key],
            "Tipo": "Dimensionamiento",
            "Variable": EQUIPMENT_SPEC_LABELS.get(key, key),
            "Clave": key,
            "Impacto temporal": meta["impact"],
            "Significativa": "SI" if meta["significant"] else "NO",
            "Justificacion": meta["reason"],
        })

    stage_rank = {stage: idx for idx, stage in enumerate(IMPACT_STAGE_ORDER)}
    rows.sort(
        key=lambda item: (
            stage_rank.get(item["Etapa"], 999),
            0 if item["Tipo"] == "Control" else 1,
            IMPACT_PRIORITY.get(item["Impacto temporal"], 99),
            item["Variable"],
        )
    )
    return rows


def render_variable_impact_matrix() -> None:
    with st.expander("Fase 1 · Impacto de variables en el registro temporal", expanded=False):
        st.caption(
            "Clasificacion basada en el modelo del repo y el Proyecto Final. "
            "ALTO/MEDIO se considera impacto significativo en el registro temporal."
        )

        c1, c2, c3 = st.columns([1.0, 1.0, 1.2])
        selected_stage = c1.selectbox(
            "Etapa",
            options=["Todas", *IMPACT_STAGE_ORDER],
            key="impact_filter_stage",
        )
        selected_type = c2.selectbox(
            "Tipo de variable",
            options=["Ambas", "Control", "Dimensionamiento"],
            key="impact_filter_type",
        )
        only_significant = c3.checkbox(
            "Mostrar solo variables significativas",
            value=True,
            key="impact_filter_only_significant",
        )

        rows = _build_variable_impact_rows()
        if selected_stage != "Todas":
            rows = [row for row in rows if row["Etapa"] == selected_stage]
        if selected_type != "Ambas":
            rows = [row for row in rows if row["Tipo"] == selected_type]
        if only_significant:
            rows = [row for row in rows if row["Significativa"] == "SI"]

        total_rows = len(rows)
        sig_rows = sum(1 for row in rows if row["Significativa"] == "SI")
        st.caption(f"Variables mostradas: {total_rows} | Significativas: {sig_rows}")
        st.dataframe(rows, width="stretch", hide_index=True)


STAGE_KPI_CONFIG = [
    {
        "tab": "Etapa 0-1",
        "title": "KPIs de preparacion y extraccion",
        "metrics": [
            {"key": "stage_0_pump_kw", "label": "Bomba Etapa 0", "unit": "kW", "decimals": 2},
            {"key": "stage_1_extraction_eff_pct", "label": "Eficiencia Etapa 1", "unit": "%", "decimals": 2},
            {"key": "stage_1_2_extract_recovery_pct", "label": "Recuperacion Etapa 1.2", "unit": "%", "decimals": 2},
        ],
    },
    {
        "tab": "Etapa 2 + OI",
        "title": "KPIs de pasteurizacion y OI",
        "metrics": [
            {"key": "stage_2_heat_required_mj_h", "label": "Calor pasteurizacion", "unit": "MJ/h", "decimals": 2},
            {"key": "stage_2_5_ro_ro_recovery_pct", "label": "Recuperacion OI", "unit": "%", "decimals": 2},
            {"key": "stage_2_5_ro_permeate_flow_m3_h", "label": "Permeado OI", "unit": "m3/h", "decimals": 3},
        ],
    },
    {
        "tab": "Etapa 3",
        "title": "KPIs de evaporacion",
        "metrics": [
            {"key": "stage_3_evaporated_water_m3_h", "label": "Agua evaporada", "unit": "m3/h", "decimals": 3},
            {"key": "stage_3_steam_required_kg_h", "label": "Vapor requerido", "unit": "kg/h", "decimals": 1},
            {"key": "stage_3_target_solids_pct", "label": "Solidos objetivo", "unit": "%", "decimals": 2},
        ],
    },
    {
        "tab": "Etapa 4",
        "title": "KPIs de precipitacion y centrifugacion",
        "metrics": [
            {"key": "stage_4_precip_eff_pct", "label": "Recuperacion precipitacion", "unit": "%", "decimals": 2},
            {"key": "stage_4_2_solids_recovery_pct", "label": "Recuperacion centrifuga", "unit": "%", "decimals": 2},
            {"key": "stage_4_2_paste_mass_kg_h", "label": "Pasta humeda", "unit": "kg/h", "decimals": 1},
        ],
    },
    {
        "tab": "Etapa 5",
        "title": "KPIs de secado y rendimiento",
        "metrics": [
            {"key": "stage_5_final_moisture_pct", "label": "Humedad final", "unit": "%", "decimals": 2},
            {"key": "stage_5_powder_mass_kg_h", "label": "Polvo final", "unit": "kg/h", "decimals": 1},
            {"key": "stage_5_overall_yield_pct", "label": "Rendimiento global", "unit": "%", "decimals": 2},
        ],
    },
    {
        "tab": "Ventas",
        "title": "KPIs economicos por kilogramo de producto",
        "metrics": [
            {
                "key": "stage_ventas_cost_per_kg_bs",
                "label": "Gasto en producir",
                "unit": "Bs/kg",
                "decimals": 2,
                "compact": True,
            },
            {
                "key": "stage_ventas_revenue_per_kg_bs",
                "label": "Lo que se gana",
                "unit": "Bs/kg",
                "decimals": 2,
                "compact": True,
            },
            {
                "key": "stage_ventas_profit_per_kg_bs",
                "label": "Utilidades",
                "unit": "Bs/kg",
                "decimals": 2,
                "compact": True,
            },
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
    "stage_2_5_ro_ro_recovery_pct": 1.0,
    "stage_2_5_ro_permeate_flow_m3_h": 1.3,
    "stage_3_evaporated_water_m3_h": 1.5,
    "stage_3_steam_required_kg_h": 1.5,
    "stage_3_target_solids_pct": 1.0,
    "stage_4_precip_eff_pct": 0.9,
    "stage_4_2_solids_recovery_pct": 1.0,
    "stage_4_2_paste_mass_kg_h": 1.2,
    "stage_5_final_moisture_pct": 0.8,
    "stage_5_powder_mass_kg_h": 1.2,
    "stage_5_overall_yield_pct": 1.0,
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


PROJECT_FINAL_ROOT = Path(__file__).resolve().parent / "PROYECTO_FINAL_UNITARIOS"
PROJECT_FINAL_README_PATH = PROJECT_FINAL_ROOT / "readme.md"
PROJECT_FINAL_IMAGES_DIR = PROJECT_FINAL_ROOT / "media" / "images"
SUPPORTED_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
IMAGE_PROCESS_SEQUENCE = [
    ("planta industrial", "Vista general de planta"),
    ("silaje soja", "Etapa 0 - Recepcion y almacenamiento"),
    ("tamizado y molienda", "Etapa 0 - Molienda y tamizado"),
    ("tanque agitado", "Etapa 1 - Extraccion alcalina"),
    ("decantador centrifugo", "Etapa 2A - Separacion solido-liquido"),
    ("intercambiador de calor", "Etapa 2B - Neutralizacion y pasteurizacion"),
    ("osmosis inversa", "Etapa 2C - Preconcentracion por osmosis inversa"),
    ("evaporador de doble efecto", "Etapa 3 - Concentracion por evaporacion"),
    ("precipitador isoelectrico", "Etapa 4 - Precipitacion isoelectrica"),
    ("spray dryer", "Etapa 5 - Secado por atomizacion"),
    ("secado y palletizado", "Etapa 6 - Envasado y palletizado"),
    ("formato de venta", "Producto final - Presentacion comercial"),
]


@st.cache_data(show_spinner=False)
def load_project_final_readme() -> str:
    try:
        return PROJECT_FINAL_README_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "No se encontro el README del Proyecto Final en PROYECTO_FINAL_UNITARIOS/readme.md."
    except OSError as exc:
        return f"No fue posible leer el README del Proyecto Final: {exc}"


def list_project_final_images() -> list[Path]:
    if not PROJECT_FINAL_IMAGES_DIR.exists():
        return []

    image_paths = [
        path
        for path in PROJECT_FINAL_IMAGES_DIR.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_IMAGE_SUFFIXES
    ]
    return sorted(image_paths, key=lambda path: (_image_process_rank(path), path.name.lower()))


def _normalize_text(value: str) -> str:
    # Normaliza acentos y puntuacion para hacer matching robusto de nombres de archivo.
    ascii_text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", ascii_text.lower())).strip()


def _image_process_rank(path: Path) -> int:
    stem = _normalize_text(path.stem)
    for idx, (token, _) in enumerate(IMAGE_PROCESS_SEQUENCE):
        if _normalize_text(token) in stem:
            return idx
    return len(IMAGE_PROCESS_SEQUENCE)


def _image_process_label(path: Path) -> str:
    stem = _normalize_text(path.stem)
    for token, label in IMAGE_PROCESS_SEQUENCE:
        if _normalize_text(token) in stem:
            return label
    return "Equipo complementario"


def _build_image_caption(path: Path) -> str:
    normalized = " ".join(path.stem.replace("_", " ").replace("-", " ").split())
    name = normalized if normalized else path.name
    return f"{_image_process_label(path)} | {name}"


st.set_page_config(
    page_title="Gemelo Digital AJAX",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

def get_active_theme() -> dict:
    mode = st.session_state.get("visual_mode", "Contraste Alto")
    return VISUAL_THEMES.get(mode, VISUAL_THEMES["Contraste Alto"])


def apply_visual_theme_css() -> None:
    # Palette definition
    bg_deep = "#0f172a"
    bg_surface = "#1e293b"
    text_main = "#f8fafc"
    text_muted = "#94a3b8"
    accent = "#38bdf8"
    border = "#334155"

    st.markdown(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

            :root {{
                --bg-deep: {bg_deep};
                --bg-surface: {bg_surface};
                --text-main: {text_main};
                --text-muted: {text_muted};
                --accent: {accent};
                --border: {border};
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
            }}

            /* Custom Cards for KPIs */
            div[data-testid="stMetric"] {{
                background-color: var(--bg-surface);
                border: 1px solid var(--border);
                border-radius: 12px;
                padding: 1rem !important;
                transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            }}

            .kpi-meta {{
                font-size: 0.75rem;
                color: var(--text-muted);
                margin-top: 4px;
            }}

            .kpi-status {{
                font-size: 0.75rem;
                font-weight: 600;
                margin-top: 4px;
                padding: 2px 8px;
                border-radius: 4px;
                display: inline-block;
            }}

            .kpi-stable {{
                background-color: rgba(16, 185, 129, 0.1);
                color: #10b981;
            }}

            .kpi-unstable {{
                background-color: rgba(239, 68, 68, 0.1);
                color: #ef4444;
            }}

            div[data-testid="stMetric"]:hover {{
                transform: translateY(-5px);
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2), 0 10px 10px -5px rgba(0, 0, 0, 0.1);
                border-color: var(--accent);
            }}

            /* Buttons */
            .stButton > button {{
                width: 100%;
                background-color: var(--bg-surface);
                color: var(--text-main);
                border: 1px solid var(--border);
                border-radius: 8px;
                padding: 0.5rem 1rem;
                font-weight: 600;
                transition: all 0.2s ease;
            }}

            .stButton > button:hover {{
                border-color: var(--accent);
                color: var(--accent);
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(56, 189, 248, 0.2);
            }}

            .stButton > button:active {{
                transform: translateY(0);
            }}

            /* Inputs and Sliders */
            div[data-baseweb="input"], div[data-baseweb="select"], div[data-baseweb="textarea"] {{
                background-color: var(--bg-deep) !important;
                border-radius: 8px !important;
                border: 1px solid var(--border) !important;
            }}

            div[data-baseweb="input"] input {{
                color: var(--text-main) !important;
                font-family: var(--font-mono) !important;
            }}

            div[role="slider"] {{
                background-color: var(--accent) !important;
            }}

            div[data-testid="stExpander"] {{
                background-color: var(--bg-surface) !important;
                border: 1px solid var(--border) !important;
                border-radius: 12px !important;
                margin-bottom: 1rem !important;
            }}

            div[data-testid="stExpander"] summary:hover {{
                color: var(--accent) !important;
            }}

            div[data-testid="stDataFrame"] {{
                background-color: var(--bg-surface) !important;
                border: 1px solid var(--border) !important;
                border-radius: 12px !important;
            }}

            /* Hero Panel & Chips */
            .hero-panel {{
                background: linear-gradient(135deg, var(--bg-surface) 0%, var(--bg-deep) 100%);
                border: 1px solid var(--border);
                border-left: 4px solid var(--accent);
                border-radius: 12px;
                padding: 1.5rem;
                margin-bottom: 2rem;
            }}

            .note-chip {{
                background-color: rgba(56, 189, 248, 0.1);
                border: 1px solid rgba(56, 189, 248, 0.2);
                color: var(--accent);
                border-radius: 8px;
                padding: 0.75rem 1rem;
                margin-bottom: 1.5rem;
                font-size: 0.9rem;
            }}

            /* Tabs Custom Styling (for where still used) */
            div[data-baseweb="tab-list"] {{
                background-color: transparent !important;
                gap: 1rem !important;
            }}

            div[data-baseweb="tab"] {{
                background-color: var(--bg-surface) !important;
                border: 1px solid var(--border) !important;
                border-radius: 8px 8px 0 0 !important;
                color: var(--text-muted) !important;
                padding: 0.5rem 1.5rem !important;
            }}

            div[data-baseweb="tab"][aria-selected="true"] {{
                border-color: var(--accent) !important;
                color: var(--accent) !important;
                background-color: rgba(56, 189, 248, 0.05) !important;
            }}

            /* Scrollbar */
            ::-webkit-scrollbar {{
                width: 8px;
                height: 8px;
            }}
            ::-webkit-scrollbar-track {{
                background: var(--bg-deep);
            }}
            ::-webkit-scrollbar-thumb {{
                background: var(--border);
                border-radius: 4px;
            }}
            ::-webkit-scrollbar-thumb:hover {{
                background: var(--text-muted);
            }}

            /* Animations */
            @keyframes slideUp {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}

            .stMarkdown, div[data-testid="stMetric"], .stButton {{
                animation: slideUp 0.4s ease-out forwards;
            }}

            /* Status Indicators */
            .status-pill {{
                width: 10px;
                height: 10px;
                border-radius: 50%;
                display: inline-block;
                margin-right: 8px;
            }}
            .status-running {{ background-color: #10b981; box-shadow: 0 0 8px #10b981; }}
            .status-paused {{ background-color: #ef4444; }}

            .semaphore-container {{
                display: flex;
                align-items: center;
                gap: 8px;
                margin-top: 4px;
            }}
            .semaphore-dot {{
                width: 12px;
                height: 12px;
                border-radius: 50%;
            }}
            .bg-verde {{ background-color: #10b981; box-shadow: 0 0 8px #10b981; }}
            .bg-amarillo {{ background-color: #f59e0b; box-shadow: 0 0 8px #f59e0b; }}
            .bg-rojo {{ background-color: #ef4444; box-shadow: 0 0 8px #ef4444; }}

            /* Range Bar Styling */
            .range-container {{
                position: relative;
                height: 24px;
                width: 100%;
                margin-top: 8px;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
            }}
            .range-bar {{
                height: 8px;
                background: var(--border);
                border-radius: 4px;
                flex-grow: 1;
                display: flex;
                overflow: hidden;
                position: relative;
            }}
            .range-ideal {{ background: #10b981; }}
            .range-warning {{ background: #f59e0b; }}
            .range-danger {{ background: #ef4444; }}

            .range-pointer {{
                position: absolute;
                top: -6px;
                width: 4px;
                height: 20px;
                background: var(--text-main);
                border-radius: 2px;
                border: 1px solid var(--bg-deep);
                box-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
                z-index: 10;
                transition: left 0.3s ease-out;
            }}

            .range-label-container {{
                display: flex;
                justify-content: space-between;
                font-size: 0.7rem;
                color: var(--text-muted);
                margin-top: 4px;
            }}

        </style>
        """,
        unsafe_allow_html=True,
    )


def _append_sales_stage(result: dict) -> dict:
    powder_mass_kg_h = float(result["stage_5"]["powder_mass_kg_h"])
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
        st.session_state.interval_s = 3
    else:
        st.session_state.interval_s = int(max(1, min(5, st.session_state.interval_s)))
    if "visual_mode" not in st.session_state:
        st.session_state.visual_mode = "Contraste Alto"
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
    if st.session_state.get("pending_full_reset", False):
        _apply_full_reset()
        st.session_state.pending_full_reset = False


def sync_controls_from_widgets() -> None:
    st.session_state.controls = {
        "soy_feed_kg_h": st.session_state.w_soy_feed_kg_h,
        "water_flow_m3_h": st.session_state.w_water_flow_m3_h,
        "water_temp_c": st.session_state.w_water_temp_c,
        "extraction_ph": st.session_state.w_extraction_ph,
        "extraction_temp_c": st.session_state.w_extraction_temp_c,
        "extraction_residence_min": st.session_state.w_extraction_residence_min,
        "agitator_rpm": st.session_state.w_agitator_rpm,
        "solid_liquid_ratio": st.session_state.w_solid_liquid_ratio,
        "pasteur_temp_c": st.session_state.w_pasteur_temp_c,
        "pasteur_retention_s": st.session_state.w_pasteur_retention_s,
        "ro_tmp_bar": st.session_state.w_ro_tmp_bar,
        "ro_crossflow_ms": st.session_state.w_ro_crossflow_ms,
        "ro_feed_temp_c": st.session_state.w_ro_feed_temp_c,
        "ro_feed_ph": st.session_state.w_ro_feed_ph,
        "ro_sdi": st.session_state.w_ro_sdi,
        "evap_pressure_bar": st.session_state.w_evap_pressure_bar,
        "evap_temp_c": st.session_state.w_evap_temp_c,
        "precip_ph": st.session_state.w_precip_ph,
        "precip_time_min": st.session_state.w_precip_time_min,
        "centrifuge_g": st.session_state.w_centrifuge_g,
        "centrifuge_time_min": st.session_state.w_centrifuge_time_min,
        "dryer_temp_c": st.session_state.w_dryer_temp_c,
        "dryer_residence_min": st.session_state.w_dryer_residence_min,
    }


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
    updated: dict[str, float] = {}
    for key, default in EQUIPMENT_SPEC_DEFAULTS.items():
        widget_key = f"w_eq_{key}"
        updated[key] = float(st.session_state.get(widget_key, st.session_state.equipment_specs.get(key, default)))
    st.session_state.equipment_specs = updated


def sync_capacity_limits_from_widgets() -> None:
    updated: dict[str, float] = {}
    for key, default in CAPACITY_LIMIT_DEFAULTS.items():
        widget_key = f"w_lim_{key}"
        updated[key] = float(st.session_state.get(widget_key, st.session_state.capacity_limits.get(key, default)))
    st.session_state.capacity_limits = updated


def sync_sales_price_from_widgets() -> None:
    st.session_state.sales_price_bs_kg = float(
        st.session_state.get("w_sales_price_bs_kg", st.session_state.sales_price_bs_kg)
    )


def _get_variable_ranges(key: str, vmin: float, vmax: float) -> tuple[tuple[float, float], tuple[float, float]]:
    default = DEFAULT_CONTROLS.get(key) or EQUIPMENT_SPEC_DEFAULTS.get(key)
    if default is None:
        default = (vmin + vmax) / 2

    # Overrides based on readme.md and process knowledge
    if key == "extraction_ph": return (8.5, 9.5), (7.0, 11.0)
    if key == "pasteur_temp_c": return (75.0, 85.0), (70.0, 100.0)
    if key == "precip_ph": return (4.3, 4.7), (3.5, 5.5)
    if key == "water_flow_m3_h": return (10.0, 14.0), (5.0, 25.0)
    if key == "soy_feed_kg_h": return (800.0, 1200.0), (500.0, 5000.0)
    if key == "ro_tmp_bar": return (20.0, 30.0), (10.0, 40.0)
    if key == "evap_pressure_bar": return (0.3, 0.5), (0.1, 0.8)
    if key == "dryer_temp_c": return (70.0, 90.0), (50.0, 150.0)

    # Generic heuristic
    return (default * 0.9, default * 1.1), (default * 0.7, default * 1.3)


def _render_range_bar(key: str, vmin: float, vmax: float, current_val: float):
    ideal, warning = _get_variable_ranges(key, vmin, vmax)
    i_min, i_max = ideal
    w_min, w_max = warning

    points = [
        (w_min, "danger"),
        (i_min, "warning"),
        (i_max, "ideal"),
        (w_max, "warning"),
        (vmax, "danger")
    ]

    span = max(vmax - vmin, 1e-9)
    # Clip pointer position between 0 and 100%
    pointer_pos = max(0.0, min(100.0, (current_val - vmin) / span * 100))

    html = '<div class="range-container"><div class="range-bar">'
    prev = vmin
    for end_val, ztype in points:
        actual_end = max(prev, min(end_val, vmax))
        width = (actual_end - prev) / span * 100
        if width > 0.01:
            html += f'<div class="range-segment range-{ztype}" style="width: {width}%"></div>'
        prev = actual_end

    html += f'</div><div class="range-pointer" style="left: calc({pointer_pos}% - 2px);"></div></div>'
    html += f'<div class="range-label-container"><span>{vmin}</span><span>{vmax}</span></div>'

    st.markdown(html, unsafe_allow_html=True)


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
                _render_range_bar(key, float(vmin), float(vmax), val)

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
            "Fuente documental: escenario base 18.10 Bs/kg | "
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


def render_controls() -> None:
    controls = st.session_state.controls
    with st.expander("Etapa 0 · Preparacion", expanded=True):
        val01 = st.number_input("Alimentacion de soya (kg/h)", 100.0, 8000.0, value=controls["soy_feed_kg_h"], step=100.0, key="w_soy_feed_kg_h")
        _render_range_bar("soy_feed_kg_h", 100.0, 8000.0, val01)
        val02 = st.number_input("Caudal de agua (m3/h)", 2.0, 30.0, value=controls["water_flow_m3_h"], step=0.1, key="w_water_flow_m3_h")
        _render_range_bar("water_flow_m3_h", 2.0, 30.0, val02)
        val03 = st.number_input("Temperatura de agua (C)", 5.0, 90.0, value=controls["water_temp_c"], step=0.5, key="w_water_temp_c")
        _render_range_bar("water_temp_c", 5.0, 90.0, val03)

    with st.expander("Etapa 1 · Extraccion", expanded=False):
        val11 = st.number_input("pH extraccion", 6.0, 12.0, value=controls["extraction_ph"], step=0.01, key="w_extraction_ph")
        _render_range_bar("extraction_ph", 6.0, 12.0, val11)
        val12 = st.number_input("Temperatura extraccion (C)", 20.0, 95.0, value=controls["extraction_temp_c"], step=0.5, key="w_extraction_temp_c")
        _render_range_bar("extraction_temp_c", 20.0, 95.0, val12)
        val13 = st.number_input("Tiempo residencia (min)", 5.0, 180.0, value=controls["extraction_residence_min"], step=1.0, key="w_extraction_residence_min")
        _render_range_bar("extraction_residence_min", 5.0, 180.0, val13)
        val14 = st.number_input("Velocidad agitacion (RPM)", 10.0, 500.0, value=controls["agitator_rpm"], step=1.0, key="w_agitator_rpm")
        _render_range_bar("agitator_rpm", 10.0, 500.0, val14)
        val15 = st.number_input("Ratio solido/liquido (1:x)", 4.0, 30.0, value=controls["solid_liquid_ratio"], step=0.1, key="w_solid_liquid_ratio")
        _render_range_bar("solid_liquid_ratio", 4.0, 30.0, val15)

    with st.expander("Etapa 2 · Pasteurizacion", expanded=False):
        val21 = st.number_input("Temperatura de pasteurizacion (C)", 50.0, 130.0, value=controls["pasteur_temp_c"], step=0.5, key="w_pasteur_temp_c")
        _render_range_bar("pasteur_temp_c", 50.0, 130.0, val21)
        val22 = st.number_input("Retencion termica (s)", 2.0, 180.0, value=controls["pasteur_retention_s"], step=1.0, key="w_pasteur_retention_s")
        _render_range_bar("pasteur_retention_s", 2.0, 180.0, val22)

    with st.expander("Etapa 2.5 · Osmosis inversa", expanded=False):
        val251 = st.number_input("TMP OI (bar)", 5.0, 45.0, value=controls["ro_tmp_bar"], step=0.1, key="w_ro_tmp_bar")
        _render_range_bar("ro_tmp_bar", 5.0, 45.0, val251)
        val252 = st.number_input("Velocidad cruzada OI (m/s)", 0.2, 3.0, value=controls["ro_crossflow_ms"], step=0.05, key="w_ro_crossflow_ms")
        _render_range_bar("ro_crossflow_ms", 0.2, 3.0, val252)
        val253 = st.number_input("Temperatura alimentacion OI (C)", 5.0, 60.0, value=controls["ro_feed_temp_c"], step=0.5, key="w_ro_feed_temp_c")
        _render_range_bar("ro_feed_temp_c", 5.0, 60.0, val253)
        val254 = st.number_input("pH alimentacion OI", 3.0, 11.0, value=controls["ro_feed_ph"], step=0.01, key="w_ro_feed_ph")
        _render_range_bar("ro_feed_ph", 3.0, 11.0, val254)
        val255 = st.number_input("SDI", 1.0, 8.0, value=controls["ro_sdi"], step=0.1, key="w_ro_sdi")
        _render_range_bar("ro_sdi", 1.0, 8.0, val255)

    with st.expander("Etapa 3 · Evaporacion", expanded=False):
        val31 = st.number_input("Presion evaporador (bar abs)", 0.05, 1.20, value=controls["evap_pressure_bar"], step=0.01, key="w_evap_pressure_bar")
        _render_range_bar("evap_pressure_bar", 0.05, 1.20, val31)
        val32 = st.number_input("Temperatura evaporacion (C)", 20.0, 95.0, value=controls["evap_temp_c"], step=0.5, key="w_evap_temp_c")
        _render_range_bar("evap_temp_c", 20.0, 95.0, val32)

    with st.expander("Etapa 4 · Precipitacion y centrifugacion", expanded=False):
        val41 = st.number_input("pH de precipitacion", 2.5, 7.0, value=controls["precip_ph"], step=0.01, key="w_precip_ph")
        _render_range_bar("precip_ph", 2.5, 7.0, val41)
        val42 = st.number_input("Tiempo de precipitacion (min)", 2.0, 120.0, value=controls["precip_time_min"], step=1.0, key="w_precip_time_min")
        _render_range_bar("precip_time_min", 2.0, 120.0, val42)
        val43 = st.number_input("Factor G centrifuga", 200.0, 5000.0, value=controls["centrifuge_g"], step=10.0, key="w_centrifuge_g")
        _render_range_bar("centrifuge_g", 200.0, 5000.0, val43)
        val44 = st.number_input("Tiempo centrifugacion (min)", 1.0, 120.0, value=controls["centrifuge_time_min"], step=1.0, key="w_centrifuge_time_min")
        _render_range_bar("centrifuge_time_min", 1.0, 120.0, val44)

    with st.expander("Etapa 5 · Secado", expanded=False):
        val51 = st.number_input("Temperatura de secado (C)", 40.0, 220.0, value=controls["dryer_temp_c"], step=1.0, key="w_dryer_temp_c")
        _render_range_bar("dryer_temp_c", 40.0, 220.0, val51)
        val52 = st.number_input("Residencia en secador (min)", 1.0, 180.0, value=controls["dryer_residence_min"], step=1.0, key="w_dryer_residence_min")
        _render_range_bar("dryer_residence_min", 1.0, 180.0, val52)

    sync_controls_from_widgets()


def run_step() -> None:
    # Verificacion de rangos para paro del sistema
    danger_vars = []

    # Chequeo de Controles
    for key, value in st.session_state.controls.items():
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
        result = run_process_model(
            st.session_state.controls,
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

    snapshot = build_snapshot(
        st.session_state.controls,
        result,
        equipment_specs=st.session_state.equipment_specs,
        capacity_limits=st.session_state.capacity_limits,
    )

    # Generate actual and predicted (both with noise for realism as requested)
    actual_noisy = _inject_independent_error(snapshot)
    predicted_noisy = _inject_independent_error(snapshot)

    st.session_state.log.append(actual_noisy)

    # Update sparkline history (last 60 seconds)
    # snapshot is flattened by build_snapshot, so we can iterate top-level keys
    max_points = 60 // st.session_state.interval_s
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


def _compute_kpi_window_stats(df, key: str) -> dict | None:
    if key not in df.columns:
        return None

    all_series = df[key].dropna()
    if all_series.empty:
        return None

    series = all_series.tail(STABILITY_WINDOW_POINTS)

    current = float(all_series.iloc[-1])
    previous = float(all_series.iloc[-2]) if len(all_series) > 1 else current

    # Promedio dinámico basado en la corrida actual completa
    average = float(all_series.mean())

    # Desviación estándar de los puntos recientes para estabilidad
    std_dev = float(series.std(ddof=0)) if len(series) > 1 else 0.0

    base_error_pct = _error_base_pct_for_key(key)
    error_abs = abs(current) * (base_error_pct / 100.0)
    band_pct = base_error_pct * ERROR_BAND_FACTOR
    lower_limit = average * (1.0 - (band_pct / 100.0))
    upper_limit = average * (1.0 + (band_pct / 100.0))
    if lower_limit > upper_limit:
        lower_limit, upper_limit = upper_limit, lower_limit

    if abs(previous) > 1e-9:
        delta_pct = ((current - previous) / abs(previous)) * 100.0
    else:
        delta_pct = 0.0

    if abs(average) > 1e-9:
        relative_std_pct = (std_dev / abs(average)) * 100.0
    else:
        relative_std_pct = 0.0

    # Sigma Calculation vs Baseline
    # Convert app key to baseline key if necessary
    # Example: stage_1_extraction_eff_pct is same in both
    # Some baseline keys might be different, but let's try direct match first
    baseline_info = BASELINE_REFERENCES.get(key)
    sigma_deviation = 0.0
    semaphore = "verde"

    if baseline_info:
        setpoint = baseline_info["value"]
        # Use relative deviation for sigma if not enough points, or fixed sigma
        # Requirement says "calculen desviación vs. setpoint usando desviación estándar (1σ, 2σ)"
        # Let's use the running std_dev or a default if std_dev is 0
        effective_sigma = std_dev if std_dev > 0.001 else (abs(setpoint) * (base_error_pct / 100.0))

        diff = abs(current - setpoint)
        sigma_deviation = diff / effective_sigma if effective_sigma > 0 else 0.0

        if sigma_deviation <= 1.0:
            semaphore = "verde"
        elif sigma_deviation <= 2.0:
            semaphore = "amarillo"
        else:
            semaphore = "rojo"

    return {
        "current": current,
        "average": average,
        "lower_limit": lower_limit,
        "upper_limit": upper_limit,
        "delta_pct": delta_pct,
        "error_abs": error_abs,
        "relative_std_pct": relative_std_pct,
        "stable": relative_std_pct <= base_error_pct,
        "sigma_deviation": sigma_deviation,
        "semaphore": semaphore,
        "has_baseline": baseline_info is not None
    }


def _format_kpi_value(value: float, unit: str, decimals: int) -> str:
    number = _format_number_es(value, decimals)
    if unit:
        return f"{number} {unit}"
    return number


def _render_kpi_chart(key: str, stats: dict, theme: dict, chart_key: str | None = None) -> None:
    """Renderiza un mini gráfico de líneas (sparkline) para el KPI con modo exploratorio."""
    history = st.session_state.get("sparkline_history", {}).get(key, [])
    if len(history) < 2:
        return

    actual_values = [h["actual"] for h in history]
    predicted_values = [h["predicted"] for h in history]

    fig = go.Figure()

    # Predicción del modelo (línea punteada) - Modo Exploratorio
    fig.add_trace(go.Scatter(
        y=predicted_values,
        mode="lines",
        name="Predicción",
        line=dict(color=theme["muted_text"], width=1, dash="dot"),
        hoverinfo="skip"
    ))

    # Valor actual (línea sólida)
    # Extract stage (e.g., stage_1 -> s1)
    stage_key = "s0"
    parts = key.split("_")
    if len(parts) > 1 and parts[0] == "stage":
        stage_id = parts[1]
        if stage_id in ["0", "1", "2", "3", "4", "5"]:
            stage_key = f"s{stage_id}"
        elif stage_id == "2" and len(parts) > 2 and parts[2] == "5":
            stage_key = "s2_5"

    color = theme["stage_colors"].get(stage_key, theme["stage_colors"].get("s0", "#38bdf8"))
    fig.add_trace(go.Scatter(
        y=actual_values,
        mode="lines",
        name="Actual",
        line=dict(color=color, width=2),
        hoverinfo="skip"
    ))

    # Bandas de control (límites admisibles)
    fig.add_hline(y=stats["upper_limit"], line_dash="dash", line_color=theme["status"]["rojo"], opacity=0.3)
    fig.add_hline(y=stats["lower_limit"], line_dash="dash", line_color=theme["status"]["rojo"], opacity=0.3)

    fig.update_layout(
        height=60,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        template="plotly_dark",
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False}, key=chart_key or f"spark_{key}")


def _render_kpi_card(
    df,
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
    stats = _compute_kpi_window_stats(df, key)
    theme = get_active_theme()
    if not stats:
        st.metric(label, "Sin datos", delta="0.00%")
        st.caption("Ejecuta la simulacion para activar historico.")
        return

    if compact:
        st.metric(label, _format_kpi_value(stats["current"], unit, decimals))
        return

    with st.container():
        st.metric(
            label,
            _format_kpi_value(stats["current"], unit, decimals),
            delta=_format_pct_delta_es(stats["delta_pct"]),
        )

        # Gráfico de líneas integrado
        _render_kpi_chart(key, stats, theme, chart_key=f"spark_{card_id or key}")

        st.markdown(
            f"<div class='kpi-meta'>Error +/- {_format_kpi_value(stats['error_abs'], unit, decimals)} | Prom: {_format_number_es(stats['average'], decimals)}</div>",
            unsafe_allow_html=True,
        )

        if secondary_key:
            secondary_stats = _compute_kpi_window_stats(df, secondary_key)
            if secondary_stats:
                st.markdown(
                    f"<div class='kpi-meta'>{secondary_label}: {_format_kpi_value(secondary_stats['current'], secondary_unit, secondary_decimals)}</div>",
                    unsafe_allow_html=True,
                )

        status_class = "kpi-stable" if stats["stable"] else "kpi-unstable"
        status_text = "Estable" if stats["stable"] else "Inestable"
        st.markdown(
            f"<div class='kpi-status {status_class}'>{status_text} | Var: {stats['relative_std_pct']:.2f}%</div>",
            unsafe_allow_html=True,
        )

        if stats["has_baseline"]:
            st.markdown(
                f"""
                <div class="semaphore-container">
                    <div class="semaphore-dot bg-{stats['semaphore']}"></div>
                    <div class="kpi-meta">Desviación: {stats['sigma_deviation']:.2f}σ</div>
                </div>
                """,
                unsafe_allow_html=True
            )


def render_kpis() -> None:
    df = st.session_state.log.to_dataframe()
    result = st.session_state.last_result
    capacity = result.get("capacity", {})

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        _render_kpi_card(df, "stage_5_protein_final_kg_h", "Proteina final", "kg/h", 1, card_id="top_protein")
    with c2:
        _render_kpi_card(df, "stage_5_overall_yield_pct", "Rendimiento global", "%", 1, card_id="top_yield")
    with c3:
        _render_kpi_card(df, "stage_2_5_ro_ro_recovery_pct", "Recuperacion OI", "%", 1, card_id="top_ro")
    with c4:
        _render_kpi_card(df, "stage_3_evaporated_water_m3_h", "Agua evaporada", "m3/h", 2, card_id="top_evap")

    st.caption("Baselines documentales: extraccion 88%, OI 25%, pasteurizacion 80 C/22 s, evaporacion 0.40 bar.")

    if capacity:
        u1, u2, u3, u4 = st.columns(4)
        with u1:
            _render_kpi_card(df, "capacity_stage_0_tank_utilization_pct", "Uso tanque E0", "%", 1)
        with u2:
            _render_kpi_card(df, "capacity_stage_2_hex_thermal_load_pct", "Uso intercambiador", "%", 1)
        with u3:
            _render_kpi_card(df, "capacity_stage_2_5_ro_flux_lmh", "Flujo OI", "LMH", 1)
        with u4:
            _render_kpi_card(df, "capacity_stage_5_dryer_load_pct", "Uso secador", "%", 1)


def render_stage_panels() -> None:
    df = st.session_state.log.to_dataframe()
    if df.empty:
        st.info("Aun no hay historico. Usa 'Paso' o 'Iniciar' para comenzar el registro.")
        return

    tabs = st.tabs([stage["tab"] for stage in STAGE_KPI_CONFIG])
    for tab, stage in zip(tabs, STAGE_KPI_CONFIG):
        with tab:
            st.caption(stage["title"])
            cols = st.columns(3)
            for idx, metric in enumerate(stage["metrics"]):
                with cols[idx % 3]:
                    _render_kpi_card(
                        df,
                        key=metric["key"],
                        label=metric["label"],
                        unit=metric["unit"],
                        decimals=metric["decimals"],
                        secondary_key=metric.get("secondary_key"),
                        secondary_label=metric.get("secondary_label", "Referencia"),
                        secondary_unit=metric.get("secondary_unit", ""),
                        secondary_decimals=int(metric.get("secondary_decimals", 2)),
                        compact=bool(metric.get("compact", False)),
                    )


def render_corroboration() -> None:
    history_df = st.session_state.log.to_dataframe()
    if history_df.empty:
        st.info("Aun no hay historico suficiente para validar indicadores.")
        return

    st.caption("Indicadores de validacion conservados (sin grafica de corroboracion documental).")
    summary_cols = st.columns(3)
    summary_keys = [
        "stage_1_extraction_eff_pct",
        "stage_2_5_ro_ro_recovery_pct",
        "stage_5_powder_mass_kg_h",
    ]

    for idx, key in enumerate(summary_keys):
        with summary_cols[idx]:
            if key not in history_df.columns or key not in BASELINE_REFERENCES:
                st.caption("Sin datos para resumen estadistico")
                continue

            stats = _compute_kpi_window_stats(history_df, key)
            if not stats:
                continue

            base = BASELINE_REFERENCES[key]["value"]
            current_val = stats["current"]
            dev_pct = ((current_val - base) / base) * 100.0

            st.metric(
                BASELINE_REFERENCES[key]["label"],
                _format_kpi_value(current_val, BASELINE_REFERENCES[key]["unit"], 2),
                delta=f"{dev_pct:+.2f}% vs base",
            )
            st.markdown(f"<div class='kpi-meta'>Promedio actual: {_format_number_es(stats['average'], 2)}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='kpi-meta'>Desviación: {stats['sigma_deviation']:.2f}σ</div>", unsafe_allow_html=True)

            st.markdown(
                f"""
                <div class="semaphore-container">
                    <div class="semaphore-dot bg-{stats['semaphore']}"></div>
                    <div class="kpi-meta">Estado: {stats['semaphore'].upper()}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


def render_production_counters() -> None:
    stage_5 = st.session_state.last_result["stage_5"]

    protein_rate_kg_h = float(stage_5["protein_final_kg_h"])
    powder_rate_kg_h = float(stage_5["powder_mass_kg_h"])
    time_per_kg_h = (1.0 / protein_rate_kg_h) if protein_rate_kg_h > 0 else 0.0
    time_per_kg_min = time_per_kg_h * 60.0

    bags_per_hour = powder_rate_kg_h
    bags_per_day = bags_per_hour * 24.0

    elapsed_s = float(st.session_state.production_elapsed_s)
    observed_bags_h = (st.session_state.production_bags_1kg * 3600.0 / elapsed_s) if elapsed_s > 0 else 0.0
    observed_protein_h = (st.session_state.production_protein_kg * 3600.0 / elapsed_s) if elapsed_s > 0 else 0.0

    st.subheader("Produccion")
    p1, p2, p3 = st.columns(3)
    p1.metric("Tiempo para 1 kg de proteina", f"{time_per_kg_min:.2f} min/kg")
    p2.metric("Bolsas de 1 kg por hora", f"{bags_per_hour:.1f}")
    p3.metric("Bolsas de 1 kg por dia", f"{bags_per_day:.0f}")

    p4, p5, p6 = st.columns(3)
    p4.metric("Bolsas acumuladas corrida", f"{st.session_state.production_bags_1kg:.1f}")
    p5.metric("Proteina acumulada corrida", f"{st.session_state.production_protein_kg:.1f} kg")
    p6.metric("Tasa observada bolsas/h", f"{observed_bags_h:.1f}")

    st.caption(
        f"Tiempo efectivo de corrida: {elapsed_s:.0f} s | Tasa observada proteina: {observed_protein_h:.2f} kg/h"
    )


def render_fluidograma_tab() -> None:
    theme = get_active_theme()
    st.subheader("Fluidograma integrado y balance de masa")
    st.caption(
        "Visualizacion dinamica del tren de proceso con corrientes principales, "
        "desperdicios y cierre de masa en tiempo real."
    )

    result = st.session_state.last_result
    if not isinstance(result, dict) or not result:
        st.info("No hay resultados disponibles aun. Ejecuta la simulacion para activar el fluidograma.")
        return

    payload = build_fluidograma_payload(result)
    fig = build_fluidograma_sankey(payload, theme)

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Rendimiento por proceso")
    rend_icons = {
        "Extraccion proteica": "🧪",
        "Recuperacion separacion": "🔄",
        "Calidad post pasteurizacion": "🌡️",
        "Recuperacion OI": "💧",
        "Retencion proteica OI": "🛡️",
        "Eficiencia precipitacion": "⚖️",
        "Recuperacion centrifuga": "🌀",
        "Rendimiento global": "🏆",
    }

    rendimiento_cols = st.columns(4)
    for idx, item in enumerate(payload["rendimientos"]):
        col = rendimiento_cols[idx % 4]
        icon = rend_icons.get(item["label"], "📊")
        with col:
            st.markdown(
                f"""
                <div style='border: 1px solid {theme["border"]}; border-radius: 12px; padding: 15px; background: {theme["card_bg"]}; margin-bottom: 10px;'>
                    <div style='font-size: 1.5rem; margin-bottom: 5px;'>{icon}</div>
                    <div style='color: {theme["muted_text"]}; font-size: 0.85rem; font-weight: 600;'>{item["label"]}</div>
                    <div style='color: {theme["text"]}; font-size: 1.4rem; font-weight: 700;'>{float(item['value_pct']):.2f}%</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("### Desperdicios y corrientes laterales")
    desp_icons = {
        "Okara humedo": "🌾",
        "Permeado OI": "🚰",
        "Agua evaporada": "☁️",
        "Suero residual": "🧪",
        "Agua removida en secado": "💨",
        "Proteina perdida en okara": "📉",
    }

    desperdicios = payload["desperdicios"]
    disp_cols = st.columns(3)
    for idx, item in enumerate(desperdicios):
        col = disp_cols[idx % 3]
        icon = desp_icons.get(item["label"], "🗑️")
        with col:
            st.markdown(
                f"""
                <div style='border: 1px solid {theme["border"]}; border-radius: 12px; padding: 15px; background: {theme["card_bg"]}; margin-bottom: 10px; border-left: 4px solid {theme["status"]["rojo"]}66;'>
                    <div style='display: flex; align-items: center; gap: 10px;'>
                        <div style='font-size: 1.5rem;'>{icon}</div>
                        <div>
                            <div style='color: {theme["muted_text"]}; font-size: 0.8rem;'>{item["label"]}</div>
                            <div style='color: {theme["text"]}; font-size: 1.1rem; font-weight: 700;'>{_format_number_es(float(item['value_kg_h']), 2)} kg/h</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    balance = payload["balance"]
    st.markdown("### Balance de masa global")
    b1, b2, b3, b4 = st.columns(4)
    b1.metric("Entrada total", f"{_format_number_es(float(balance['mass_in_kg_h']), 1)} kg/h")
    b2.metric("Salida total", f"{_format_number_es(float(balance['mass_out_kg_h']), 1)} kg/h")
    b3.metric("Error de balance", f"{float(balance['mass_balance_error_pct']):+.3f}%")
    b4.metric("Cierre de masa", f"{float(balance['mass_balance_closure_pct']):.3f}%")

    closure = float(balance["mass_balance_closure_pct"])
    if closure >= 99.5:
        st.markdown("<div class='kpi-status kpi-stable'>Cierre de masa dentro del criterio documental (>= 99.5%).</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='kpi-status kpi-unstable'>Advertencia: cierre de masa por debajo del criterio documental.</div>", unsafe_allow_html=True)

    st.caption(
        "Convencion de unidades: corrientes acuosas convertidas a kg/h con densidad 1000 kg/m3, "
        "coherente con el modelo de etapas."
    )


def render_equipment_gallery_tab() -> None:
    st.subheader("Imagenes de equipos y planta")

    image_paths = list_project_final_images()
    if not image_paths:
        st.info("No se encontraron imagenes en PROYECTO_FINAL_UNITARIOS/media/images.")
        return

    st.caption(
        "Orden de visualizacion segun el Informe Simplificado: "
        "Etapa 0 -> Etapa 1 -> Etapa 2A -> Etapa 2B -> Etapa 2C -> Etapa 3 -> Etapa 4 -> Etapa 5 -> Etapa 6 -> Producto final. "
        f"Total de imagenes detectadas: {len(image_paths)}"
    )

    plant_images = [path for path in image_paths if "planta" in path.stem.lower()]
    equipment_images = [path for path in image_paths if path not in plant_images]

    st.markdown("### Vista general de planta")
    if plant_images:
        for path in plant_images:
            st.image(str(path), caption=_build_image_caption(path), width="stretch")
    else:
        st.caption("No se detecto una imagen de planta por nombre; se muestran todas como equipos.")

    st.markdown("### Equipos del proceso")
    if not equipment_images:
        st.caption("No hay imagenes de equipos adicionales disponibles.")
        return

    cols = st.columns(3)
    for idx, path in enumerate(equipment_images):
        with cols[idx % 3]:
            st.image(str(path), caption=_build_image_caption(path), width="stretch")


def render_project_final_tab() -> None:
    st.subheader("Proyecto Final Unitarios")
    st.caption("Resumen tecnico consolidado desde planteamiento, calculos e informe simplificado.")

    result = st.session_state.last_result
    stage_5 = result["stage_5"]
    stage_2_5 = result["stage_2_5_ro"]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Proteina final (kg/h)", f"{float(stage_5['protein_final_kg_h']):.1f}")
    c2.metric("Polvo final (kg/h)", f"{float(stage_5['powder_mass_kg_h']):.1f}")
    c3.metric("Humedad final (%)", f"{float(stage_5['final_moisture_pct']):.2f}")
    c4.metric("Recuperacion OI (%)", f"{float(stage_2_5['ro_recovery_pct']):.1f}")

    st.markdown("---")
    readme_md = load_project_final_readme()
    if readme_md.startswith("No se encontro") or readme_md.startswith("No fue posible"):
        st.warning(readme_md)
    else:
        st.markdown(readme_md)


init_state()
apply_visual_theme_css()

st.title("Gemelo Digital AJAX")
st.markdown(
    "<div class='hero-panel'><strong>Centro de Operacion Integrado:</strong> interfaz orientada al seguimiento operativo y de produccion en tiempo real.</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='note-chip'>Modo exploratorio activo: los rangos de control son amplios para pruebas de sensibilidad; usa los semaforos de corroboracion para identificar condiciones fuera de banda documental.</div>",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
    st.markdown("### Navegación")
    menu = st.radio(
        "Selecciona una sección:",
        ["Operación", "Monitoreo", "Validación", "Fluidograma", "Imágenes", "Proyecto Final"],
        label_visibility="collapsed"
    )

    st.divider()
    st.markdown("### Ejecución")
    st.session_state.interval_s = st.slider("Intervalo (s)", 1, 5, value=int(st.session_state.interval_s), step=1)

    col1, col2 = st.columns(2)
    if col1.button("Iniciar", use_container_width=True):
        st.session_state.running = True
    if col2.button("Pausar", use_container_width=True):
        st.session_state.running = False

    col3, col4 = st.columns(2)
    if col3.button("Paso", use_container_width=True):
        run_step()
    if col4.button("Reset", use_container_width=True):
        st.session_state.pending_full_reset = True
        st.rerun()

    if st.session_state.running:
        st.markdown("<div style='display: flex; align-items: center;'><span class='status-pill status-running'></span> Ejecutando...</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='display: flex; align-items: center;'><span class='status-pill status-paused'></span> Pausado</div>", unsafe_allow_html=True)

    st.divider()
    render_sales_modification_panel()
    render_capacity_issues()

if menu == "Operación":
    left, right = st.columns([1.5, 1.0], gap="large")
    with left:
        st.subheader("Variables de Control")
        st.caption("Afectan la velocidad de cambio en los registros por etapa.")
        render_controls()
    with right:
        st.subheader("Dimensiones y Capacidad")
        st.caption("Parámetros fijos de inercia y tiempo de respuesta.")
        render_equipment_specs_editor()
        render_capacity_limits_editor()
        render_variable_impact_matrix()

elif menu == "Monitoreo":
    st.subheader("Panel de Indicadores en Vivo")
    render_kpis()
    st.divider()
    st.subheader("KPIs por Etapa de Proceso")
    render_stage_panels()

elif menu == "Validación":
    st.subheader("Validación y Rendimiento")
    render_corroboration()
    st.divider()
    render_production_counters()

elif menu == "Fluidograma":
    render_fluidograma_tab()

elif menu == "Imágenes":
    render_equipment_gallery_tab()

elif menu == "Proyecto Final":
    render_project_final_tab()


if st.session_state.running:
    run_step()
    if st.session_state.running:
        time.sleep(st.session_state.interval_s)
    st.rerun()
