"""Transformación de resultados del modelo a payload de fluidograma integrado.

Genera la estructura de datos para visualización Sankey / diagrama de flujo
del proceso completo de Aislado de Proteína de Soya (ISP).

Ref: Gemelo Digital.md — Sección 3.0 (Balance de Materia Completo)
"""

from __future__ import annotations


def build_fluidograma_payload(result: dict) -> dict:
    """Transforma el resultado de ``run_process_model`` en un payload de fluidograma.

    Parameters
    ----------
    result : dict
        Salida completa de ``core.stage_equations.run_process_model``.

    Returns
    -------
    dict
        Payload con secciones ``nodes``, ``links``, ``rendimientos``,
        ``desperdicios`` y ``balance``.
    """
    s0 = result.get("stage_0", {})
    s1 = result.get("stage_1", {})
    s1_2 = result.get("stage_1_2", {})
    s2 = result.get("stage_2", {})
    s_ro = result.get("stage_ro", {})
    s3 = result.get("stage_3", {})
    s4 = result.get("stage_4", {})
    s4_2 = result.get("stage_4_2", {})
    s5 = result.get("stage_5", {})
    integrity = result.get("integrity", {})

    # ── Nodos ──────────────────────────────────────────────────────
    nodes = [
        {"id": "soya", "label": "Grano de Soya", "stage": "input"},
        {"id": "agua", "label": "Agua de Proceso", "stage": "input"},
        {"id": "naoh", "label": "NaOH 20%", "stage": "input"},
        {"id": "hcl", "label": "HCl 10%", "stage": "input"},
        {"id": "TK-101", "label": "Extracción Alcalina", "stage": "stage_1"},
        {"id": "CF-102", "label": "Decanter Centrífugo", "stage": "stage_1_2"},
        {"id": "HX-201", "label": "Pasteurizador HTST", "stage": "stage_2"},
        {"id": "RO-205", "label": "Ósmosis Inversa", "stage": "stage_ro"},
        {"id": "EV-301", "label": "Evaporador Vacío", "stage": "stage_3"},
        {"id": "TK-401", "label": "Precipitación Isoeléctrica", "stage": "stage_4"},
        {"id": "CF-401", "label": "Centrífuga Separadora", "stage": "stage_4_2"},
        {"id": "SD-501", "label": "Secado Spray", "stage": "stage_5"},
        {"id": "ISP", "label": "ISP Final (Polvo)", "stage": "output"},
        {"id": "okara", "label": "Okara (Subproducto)", "stage": "byproduct"},
        {"id": "suero", "label": "Suero (Subproducto)", "stage": "byproduct"},
        {"id": "permeado", "label": "Permeado RO", "stage": "byproduct"},
        {"id": "vapor_ev", "label": "Vapor Evaporado", "stage": "byproduct"},
        {"id": "vapor_sd", "label": "Agua Evaporada (Secado)", "stage": "byproduct"},
    ]

    # ── Enlaces (flujos de masa en kg/h) ──────────────────────────
    links = [
        # Entradas al extractor
        {
            "source": "soya",
            "target": "TK-101",
            "value": max(0.0, s0.get("soy_feed_kg_h", 0.0)),
            "label": "Grano",
        },
        {
            "source": "agua",
            "target": "TK-101",
            "value": max(0.0, s0.get("water_kg_h", 0.0)),
            "label": "Agua",
        },
        {
            "source": "naoh",
            "target": "TK-101",
            "value": max(0.0, s1.get("naoh_solution_mass_kg_h", 0.0)),
            "label": "NaOH sol.",
        },
        # Extracción → Decanter
        {
            "source": "TK-101",
            "target": "CF-102",
            "value": max(0.0, s1.get("slurry_flow_kg_h", 0.0)),
            "label": "Slurry",
        },
        # Decanter → Extracto + Okara
        {
            "source": "CF-102",
            "target": "HX-201",
            "value": max(0.0, s1_2.get("extract_mass_net_kg_h", 0.0)),
            "label": "Extracto Clarificado",
        },
        {
            "source": "CF-102",
            "target": "okara",
            "value": max(0.0, s1_2.get("okara_wet_kg_h", 0.0)),
            "label": "Okara húmeda",
        },
        # Pasteurizador → RO
        {
            "source": "HX-201",
            "target": "RO-205",
            "value": max(0.0, s2.get("mass_kg_h", 0.0)),
            "label": "Extracto pasteurizado",
        },
        # RO → Evaporador + Permeado
        {
            "source": "RO-205",
            "target": "EV-301",
            "value": max(0.0, s_ro.get("retentate_mass_kg_h", 0.0)),
            "label": "Retenido RO",
        },
        {
            "source": "RO-205",
            "target": "permeado",
            "value": max(0.0, s_ro.get("permeate_kg_h", 0.0)),
            "label": "Permeado",
        },
        # Evaporador → Precipitador + Vapor
        {
            "source": "EV-301",
            "target": "TK-401",
            "value": max(0.0, s3.get("concentrate_flow_m3_h", 0.0) * 1000.0),
            "label": "Concentrado",
        },
        {
            "source": "EV-301",
            "target": "vapor_ev",
            "value": max(0.0, s3.get("evaporated_water_m3_h", 0.0) * 1000.0),
            "label": "Vapor",
        },
        # HCl al precipitador
        {
            "source": "hcl",
            "target": "TK-401",
            "value": max(0.0, s4.get("hcl_solution_mass_kg_h", 0.0)),
            "label": "HCl sol.",
        },
        # Precipitador → Centrífuga
        {
            "source": "TK-401",
            "target": "CF-401",
            "value": max(0.0, s4.get("slurry_precip_m3_h", 0.0) * 1000.0),
            "label": "Slurry precipitado",
        },
        # Centrífuga → Secador + Suero
        {
            "source": "CF-401",
            "target": "SD-501",
            "value": max(0.0, s4_2.get("paste_mass_kg_h", 0.0)),
            "label": "Pasta proteica",
        },
        {
            "source": "CF-401",
            "target": "suero",
            "value": max(0.0, s4_2.get("whey_flow_m3_h", 0.0) * 1000.0),
            "label": "Suero / Whey",
        },
        # Secador → ISP Final + Vapor
        {
            "source": "SD-501",
            "target": "ISP",
            "value": max(0.0, s5.get("powder_mass_kg_h", 0.0)),
            "label": "Polvo ISP",
        },
        {
            "source": "SD-501",
            "target": "vapor_sd",
            "value": max(0.0, s5.get("dryer_water_removed_kg_h", 0.0)),
            "label": "Agua evaporada",
        },
    ]

    # ── Rendimientos (%) ──────────────────────────────────────────
    extraction_eff = s1.get("extraction_eff_pct", 0.0)
    protein_in = s0.get("protein_in_kg_h", 1.0)
    protein_final = s5.get("protein_final_kg_h", 0.0)
    overall_yield = s5.get("overall_yield_pct", 0.0)

    rendimientos = [
        {
            "label": "Eficiencia Extracción (η_ext)",
            "value_pct": max(0.0, extraction_eff),
        },
        {
            "label": "Rendimiento Global Proteína",
            "value_pct": max(0.0, overall_yield),
        },
        {
            "label": "Calidad Pasteurización",
            "value_pct": max(0.0, s2.get("protein_quality_factor", 0.0) * 100.0),
        },
        {
            "label": "Eficiencia Precipitación",
            "value_pct": max(0.0, s4.get("precip_eff_pct", 0.0)),
        },
        {
            "label": "Recuperación Sólidos (Centrífuga)",
            "value_pct": max(0.0, s4_2.get("solids_recovery_pct", 0.0)),
        },
    ]

    # ── Desperdicios / Subproductos ───────────────────────────────
    desperdicios = [
        {
            "label": "Okara (fibra húmeda)",
            "mass_kg_h": max(0.0, s1_2.get("okara_wet_kg_h", 0.0)),
            "destino": "Alimentación animal",
        },
        {
            "label": "Suero / Whey",
            "mass_kg_h": max(0.0, s4_2.get("whey_flow_m3_h", 0.0) * 1000.0),
            "destino": "Porcicultura / Biogás",
        },
        {
            "label": "Permeado RO",
            "mass_kg_h": max(0.0, s_ro.get("permeate_kg_h", 0.0)),
            "destino": "Reutilización CIP",
        },
        {
            "label": "Mermas acumuladas",
            "mass_kg_h": max(0.0, integrity.get("total_mermas_kg_h", 0.0)),
            "destino": "Pérdidas operacionales (2% por etapa)",
        },
    ]

    # ── Balance de masa ───────────────────────────────────────────
    balance = {
        "mass_in_kg_h": integrity.get("mass_in_kg_h", 0.0),
        "mass_out_kg_h": integrity.get("mass_out_kg_h", 0.0),
        "mass_balance_error_pct": integrity.get("mass_balance_error_pct", 0.0),
        "mass_balance_closure_pct": integrity.get("mass_balance_closure_pct", 0.0),
        "total_mermas_kg_h": integrity.get("total_mermas_kg_h", 0.0),
    }

    return {
        "nodes": nodes,
        "links": links,
        "rendimientos": rendimientos,
        "desperdicios": desperdicios,
        "balance": balance,
    }
