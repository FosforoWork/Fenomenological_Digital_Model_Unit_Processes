"""Restricciones de capacidad para equipos de etapas 0-5."""

from __future__ import annotations


class EquipmentCapacityError(ValueError):
    """Error de bloqueo cuando una restriccion de capacidad no se cumple."""

    def __init__(self, issues: list[dict], indicators: dict[str, float]) -> None:
        self.issues = issues
        self.indicators = indicators
        header = "Restricciones de capacidad incumplidas:"
        body = "\n".join(
            f"- [{issue['equipment']}] {issue['message']} Recomendacion: {issue['recommendation']}"
            for issue in issues
        )
        super().__init__(f"{header}\n{body}")


def _new_issue(code: str, equipment: str, message: str, recommendation: str) -> dict:
    return {
        "code": code,
        "equipment": equipment,
        "message": message,
        "recommendation": recommendation,
    }


def evaluate_capacity_constraints(
    controls: dict,
    equipment_specs: dict,
    capacity_limits: dict,
    result: dict,
) -> tuple[dict[str, float], list[dict]]:
    indicators: dict[str, float] = {}
    issues: list[dict] = []

    stage_0 = result["stage_0"]
    stage_1 = result["stage_1"]
    stage_2 = result["stage_2"]
    stage_3 = result["stage_3"]
    stage_4 = result["stage_4"]
    stage_5 = result["stage_5"]

    # --- ETAPA 0: CAPTACION ---
    required_tank_0_m3 = controls["water_flow_m3_h"] * equipment_specs["stage_0_tank_reserve_factor"]
    available_tank_0_m3 = equipment_specs["stage_0_tank_capacity_m3"] * capacity_limits["tank_max_fill_fraction"]
    tank_0_util = (required_tank_0_m3 / available_tank_0_m3) * 100.0 if available_tank_0_m3 > 0 else 0.0
    indicators["stage_0_tank_utilization_pct"] = tank_0_util
    if required_tank_0_m3 > available_tank_0_m3:
        suggested_tank = required_tank_0_m3 / capacity_limits["tank_max_fill_fraction"]
        issues.append(
            _new_issue(
                code="STAGE0_TANK_CAPACITY",
                equipment="Tanque agua Etapa 0",
                message=(
                    f"Inundacion hidraulica: Volumen requerido {required_tank_0_m3:.2f} m3 excede volumen util "
                    f"{available_tank_0_m3:.2f} m3"
                ),
                recommendation=f"Incrementa stage_0_tank_capacity_m3 a >= {suggested_tank:.2f} m3",
            )
        )

    # --- ETAPA 1: LIXIVIACION (BOTTLENECK PRIMARIO - TOC Doc 10.1) ---
    slurry_density = equipment_specs["stage_1_slurry_density_kg_m3"]
    slurry_flow_m3_h = stage_1["slurry_flow_kg_h"] / slurry_density
    # Restriccion cinetica: tau >= 60 min
    required_tank_1_m3 = (
        slurry_flow_m3_h
        * (controls["extraction_residence_min"] / 60.0)
        * equipment_specs["stage_1_tank_reserve_factor"]
    )
    available_tank_1_m3 = equipment_specs["stage_1_tank_capacity_m3"] * capacity_limits["stage_1_tank_max_fill_fraction"]
    tank_1_util = (required_tank_1_m3 / available_tank_1_m3) * 100.0 if available_tank_1_m3 > 0 else 0.0
    indicators["stage_1_tank_utilization_pct"] = tank_1_util
    
    # Doc 10.1: TK-101 es el cuello de botella cinetico principal
    if required_tank_1_m3 > available_tank_1_m3:
        suggested_tank_1 = required_tank_1_m3 / capacity_limits["stage_1_tank_max_fill_fraction"]
        issues.append(
            _new_issue(
                code="STAGE1_TANK_CAPACITY",
                equipment="Tanque extraccion TK-101",
                message=(
                    f"Restriccion Cinetica Cruda: El caudal excede la capacidad de residencia (tau < 60min). "
                    f"Requerido {required_tank_1_m3:.2f} m3 vs disponible {available_tank_1_m3:.2f} m3"
                ),
                recommendation=f"Aumenta dimensiones del TK-101 a >= {suggested_tank_1:.2f} m3 para asegurar solubilizacion.",
            )
        )

    # --- ETAPA 2: PASTEURIZACION ---
    required_hex_kw = stage_2["heat_required_mj_h"] * 0.2777777778
    available_hex_kw = (
        equipment_specs["stage_2_hex_u_w_m2k"]
        * equipment_specs["stage_2_hex_area_m2"]
        * equipment_specs["stage_2_hex_lmtd_c"]
    ) / 1000.0
    hex_load_pct = (required_hex_kw / available_hex_kw) * 100.0 if available_hex_kw > 0 else 0.0
    indicators["stage_2_hex_thermal_load_pct"] = hex_load_pct

    if required_hex_kw > available_hex_kw * capacity_limits["stage_2_hex_max_thermal_load_fraction"]:
        issues.append(
            _new_issue(
                code="STAGE2_HEX_THERMAL_CAPACITY",
                equipment="Intercambiador HX-201",
                message="Falla de Pasteurizacion: Carga termica excede limite fisico del equipo. Riesgo HACCP.",
                recommendation="Aumenta area de intercambio o reduce caudal de alimentacion.",
            )
        )

    # --- ETAPA 3: EVAPORACION (BOTTLENECK SECUNDARIO - TOC Doc 10.1) ---
    evap_capacity = equipment_specs["stage_3_evap_capacity_m3_h"]
    evap_load_pct = (stage_3["evaporator_boiling_removed_m3_h"] / evap_capacity) * 100.0 if evap_capacity > 0 else 0.0
    indicators["stage_3_evap_load_pct"] = evap_load_pct
    if stage_3["evaporator_boiling_removed_m3_h"] > evap_capacity * capacity_limits["stage_3_evap_max_load_fraction"]:
        suggested_evap = stage_3["evaporator_boiling_removed_m3_h"] / capacity_limits["stage_3_evap_max_load_fraction"]
        issues.append(
            _new_issue(
                code="STAGE3_EVAP_CAPACITY",
                equipment="Evaporador EV-301",
                message=(
                    f"Restriccion Termodinamica: Inundacion de calandria. Evaporacion req. {stage_3['evaporator_boiling_removed_m3_h']:.2f} m3/h "
                    f"excede limite {evap_capacity * capacity_limits['stage_3_evap_max_load_fraction']:.2f} m3/h"
                ),
                recommendation=f"Implementa RO (Innovacion Doc 5.0) o aumenta capacidad a >= {suggested_evap:.2f} m3/h",
            )
        )

    # --- ETAPA 4: CENTRIFUGACION ---
    centrifuge_capacity = equipment_specs["stage_4_2_centrifuge_capacity_m3_h"]
    centrifuge_load_pct = (stage_4["slurry_precip_m3_h"] / centrifuge_capacity) * 100.0 if centrifuge_capacity > 0 else 0.0
    indicators["stage_4_2_centrifuge_load_pct"] = centrifuge_load_pct
    if stage_4["slurry_precip_m3_h"] > centrifuge_capacity * capacity_limits["stage_4_2_centrifuge_max_load_fraction"]:
        issues.append(
            _new_issue(
                code="STAGE42_CENTRIFUGE_CAPACITY",
                equipment="Centrifuga CF-401",
                message="Sobrecarga Hidraulica: Caudal de lodo excede capacidad de clarificacion.",
                recommendation="Aumenta capacidad centrifuga o reduce tiempo de residencia en tanque previo.",
            )
        )

    # --- ETAPA 5: SECADO (BUFFER - TOC Doc 10.1) ---
    dryer_capacity = equipment_specs["stage_5_dryer_evap_capacity_kg_h"]
    dryer_load_pct = (stage_5["dryer_water_removed_kg_h"] / dryer_capacity) * 100.0 if dryer_capacity > 0 else 0.0
    indicators["stage_5_dryer_load_pct"] = dryer_load_pct
    
    chamber_volume = equipment_specs["stage_5_dryer_chamber_volume_m3"]
    specific_powder_load = stage_5["powder_mass_kg_h"] / chamber_volume if chamber_volume > 0 else 0.0
    indicators["stage_5_powder_load_kg_h_m3"] = specific_powder_load

    # --- IDENTIFICACION DEL CUELLO DE BOTELLA (TOC) ---
    utilizations = {
        "TK-101": tank_1_util,
        "HX-201": hex_load_pct,
        "EV-301": evap_load_pct,
        "CF-401": centrifuge_load_pct,
        "SD-501": dryer_load_pct
    }
    
    bottleneck_equipment = max(utilizations, key=utilizations.get)
    bottleneck_utilization = utilizations[bottleneck_equipment]
    
    indicators["toc_bottleneck_equipment"] = 0.0 # Placeholder for string
    indicators["toc_bottleneck_utilization_pct"] = bottleneck_utilization
    
    # Metadatos para el Gemelo Digital
    result["toc_metadata"] = {
        "primary_bottleneck": bottleneck_equipment,
        "utilization_pct": bottleneck_utilization,
        "is_critical": bottleneck_utilization > 95.0,
        "all_utils": utilizations
    }

    return indicators, issues


def enforce_capacity_constraints(
    controls: dict,
    equipment_specs: dict,
    capacity_limits: dict,
    result: dict,
) -> dict[str, float]:
    indicators, issues = evaluate_capacity_constraints(
        controls=controls,
        equipment_specs=equipment_specs,
        capacity_limits=capacity_limits,
        result=result,
    )
    if issues:
        raise EquipmentCapacityError(issues=issues, indicators=indicators)
    return indicators
