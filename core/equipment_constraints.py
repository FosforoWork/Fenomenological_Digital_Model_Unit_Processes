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
    stage_2_5 = result["stage_2_5_ro"]
    stage_3 = result["stage_3"]
    stage_4 = result["stage_4"]
    stage_5 = result["stage_5"]

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
                    f"Volumen requerido {required_tank_0_m3:.2f} m3 excede volumen util "
                    f"{available_tank_0_m3:.2f} m3"
                ),
                recommendation=f"Incrementa stage_0_tank_capacity_m3 a >= {suggested_tank:.2f} m3",
            )
        )

    pump_motor_kw = equipment_specs["stage_0_pump_motor_kw"]
    pump_load_pct = (stage_0["pump_kw"] / pump_motor_kw) * 100.0 if pump_motor_kw > 0 else 0.0
    indicators["stage_0_pump_load_pct"] = pump_load_pct
    if stage_0["pump_kw"] > pump_motor_kw * capacity_limits["pump_max_load_fraction"]:
        suggested_motor_kw = stage_0["pump_kw"] / capacity_limits["pump_max_load_fraction"]
        issues.append(
            _new_issue(
                code="STAGE0_PUMP_POWER",
                equipment="Bomba Etapa 0",
                message=(
                    f"Carga de bomba {stage_0['pump_kw']:.2f} kW excede limite operativo "
                    f"{pump_motor_kw * capacity_limits['pump_max_load_fraction']:.2f} kW"
                ),
                recommendation=f"Incrementa stage_0_pump_motor_kw a >= {suggested_motor_kw:.2f} kW",
            )
        )

    slurry_density = equipment_specs["stage_1_slurry_density_kg_m3"]
    slurry_flow_m3_h = stage_1["slurry_flow_kg_h"] / slurry_density
    required_tank_1_m3 = (
        slurry_flow_m3_h
        * (controls["extraction_residence_min"] / 60.0)
        * equipment_specs["stage_1_tank_reserve_factor"]
    )
    available_tank_1_m3 = equipment_specs["stage_1_tank_capacity_m3"] * capacity_limits["stage_1_tank_max_fill_fraction"]
    tank_1_util = (required_tank_1_m3 / available_tank_1_m3) * 100.0 if available_tank_1_m3 > 0 else 0.0
    indicators["stage_1_tank_utilization_pct"] = tank_1_util
    if required_tank_1_m3 > available_tank_1_m3:
        suggested_tank_1 = required_tank_1_m3 / capacity_limits["stage_1_tank_max_fill_fraction"]
        issues.append(
            _new_issue(
                code="STAGE1_TANK_CAPACITY",
                equipment="Tanque extraccion Etapa 1",
                message=(
                    f"Volumen requerido {required_tank_1_m3:.2f} m3 excede volumen util "
                    f"{available_tank_1_m3:.2f} m3"
                ),
                recommendation=f"Incrementa stage_1_tank_capacity_m3 a >= {suggested_tank_1:.2f} m3",
            )
        )

    required_hex_kw = stage_2["heat_required_mj_h"] * 0.2777777778
    available_hex_kw = (
        equipment_specs["stage_2_hex_u_w_m2k"]
        * equipment_specs["stage_2_hex_area_m2"]
        * equipment_specs["stage_2_hex_lmtd_c"]
    ) / 1000.0
    hex_load_pct = (required_hex_kw / available_hex_kw) * 100.0 if available_hex_kw > 0 else 0.0
    indicators["stage_2_hex_thermal_load_pct"] = hex_load_pct

    hex_area_m2 = equipment_specs["stage_2_hex_area_m2"]
    if hex_area_m2 < capacity_limits["stage_2_hex_min_area_m2"] or hex_area_m2 > capacity_limits["stage_2_hex_max_area_m2"]:
        issues.append(
            _new_issue(
                code="STAGE2_HEX_AREA_EFFICIENCY",
                equipment="Intercambiador Etapa 2",
                message=(
                    f"Area de placas {hex_area_m2:.2f} m2 fuera de banda eficiente "
                    f"[{capacity_limits['stage_2_hex_min_area_m2']:.2f}, {capacity_limits['stage_2_hex_max_area_m2']:.2f}] m2"
                ),
                recommendation="Ajusta stage_2_hex_area_m2 dentro de la banda eficiente configurada",
            )
        )

    if required_hex_kw > available_hex_kw * capacity_limits["stage_2_hex_max_thermal_load_fraction"]:
        numerator = required_hex_kw * 1000.0
        denominator = (
            equipment_specs["stage_2_hex_u_w_m2k"]
            * equipment_specs["stage_2_hex_lmtd_c"]
            * capacity_limits["stage_2_hex_max_thermal_load_fraction"]
        )
        suggested_area = numerator / denominator if denominator > 0 else hex_area_m2
        issues.append(
            _new_issue(
                code="STAGE2_HEX_THERMAL_CAPACITY",
                equipment="Intercambiador Etapa 2",
                message=(
                    f"Carga termica requerida {required_hex_kw:.1f} kW excede limite operativo "
                    f"{available_hex_kw * capacity_limits['stage_2_hex_max_thermal_load_fraction']:.1f} kW"
                ),
                recommendation=(
                    f"Incrementa stage_2_hex_area_m2 a >= {suggested_area:.2f} m2, "
                    "aumenta U o reduce carga termica"
                ),
            )
        )

    membrane_area = equipment_specs["stage_2_5_ro_membrane_area_m2"]
    ro_flux_lmh = (stage_2_5["permeate_flow_m3_h"] * 1000.0) / membrane_area if membrane_area > 0 else 0.0
    indicators["stage_2_5_ro_flux_lmh"] = ro_flux_lmh
    if ro_flux_lmh < capacity_limits["stage_2_5_ro_min_flux_lmh"] or ro_flux_lmh > capacity_limits["stage_2_5_ro_max_flux_lmh"]:
        suggested_area = (stage_2_5["permeate_flow_m3_h"] * 1000.0) / max(capacity_limits["stage_2_5_ro_max_flux_lmh"], 1e-9)
        issues.append(
            _new_issue(
                code="STAGE25_RO_FLUX",
                equipment="OI Etapa 2.5",
                message=(
                    f"Flujo de membrana {ro_flux_lmh:.2f} LMH fuera de rango "
                    f"[{capacity_limits['stage_2_5_ro_min_flux_lmh']:.2f}, {capacity_limits['stage_2_5_ro_max_flux_lmh']:.2f}] LMH"
                ),
                recommendation=(
                    f"Aumenta stage_2_5_ro_membrane_area_m2 a >= {suggested_area:.2f} m2 "
                    "o ajusta TMP/crossflow"
                ),
            )
        )

    evap_capacity = equipment_specs["stage_3_evap_capacity_m3_h"]
    evap_load_pct = (stage_3["evaporator_boiling_removed_m3_h"] / evap_capacity) * 100.0 if evap_capacity > 0 else 0.0
    indicators["stage_3_evap_load_pct"] = evap_load_pct
    if stage_3["evaporator_boiling_removed_m3_h"] > evap_capacity * capacity_limits["stage_3_evap_max_load_fraction"]:
        suggested_evap = stage_3["evaporator_boiling_removed_m3_h"] / capacity_limits["stage_3_evap_max_load_fraction"]
        issues.append(
            _new_issue(
                code="STAGE3_EVAP_CAPACITY",
                equipment="Evaporador Etapa 3",
                message=(
                    f"Carga de evaporacion {stage_3['evaporator_boiling_removed_m3_h']:.2f} m3/h "
                    f"excede limite operativo {evap_capacity * capacity_limits['stage_3_evap_max_load_fraction']:.2f} m3/h"
                ),
                recommendation=f"Incrementa stage_3_evap_capacity_m3_h a >= {suggested_evap:.2f} m3/h",
            )
        )

    centrifuge_capacity = equipment_specs["stage_4_2_centrifuge_capacity_m3_h"]
    centrifuge_load_pct = (stage_4["slurry_precip_m3_h"] / centrifuge_capacity) * 100.0 if centrifuge_capacity > 0 else 0.0
    indicators["stage_4_2_centrifuge_load_pct"] = centrifuge_load_pct
    if stage_4["slurry_precip_m3_h"] > centrifuge_capacity * capacity_limits["stage_4_2_centrifuge_max_load_fraction"]:
        suggested_cent = stage_4["slurry_precip_m3_h"] / capacity_limits["stage_4_2_centrifuge_max_load_fraction"]
        issues.append(
            _new_issue(
                code="STAGE42_CENTRIFUGE_CAPACITY",
                equipment="Centrifuga Etapa 4.2",
                message=(
                    f"Caudal de alimentacion {stage_4['slurry_precip_m3_h']:.2f} m3/h excede limite operativo "
                    f"{centrifuge_capacity * capacity_limits['stage_4_2_centrifuge_max_load_fraction']:.2f} m3/h"
                ),
                recommendation=f"Incrementa stage_4_2_centrifuge_capacity_m3_h a >= {suggested_cent:.2f} m3/h",
            )
        )

    dryer_capacity = equipment_specs["stage_5_dryer_evap_capacity_kg_h"]
    dryer_load_pct = (stage_5["dryer_water_removed_kg_h"] / dryer_capacity) * 100.0 if dryer_capacity > 0 else 0.0
    indicators["stage_5_dryer_load_pct"] = dryer_load_pct
    if stage_5["dryer_water_removed_kg_h"] > dryer_capacity * capacity_limits["stage_5_dryer_max_load_fraction"]:
        suggested_dryer = stage_5["dryer_water_removed_kg_h"] / capacity_limits["stage_5_dryer_max_load_fraction"]
        issues.append(
            _new_issue(
                code="STAGE5_DRYER_CAPACITY",
                equipment="Secador Etapa 5",
                message=(
                    f"Remocion de agua {stage_5['dryer_water_removed_kg_h']:.1f} kg/h excede limite operativo "
                    f"{dryer_capacity * capacity_limits['stage_5_dryer_max_load_fraction']:.1f} kg/h"
                ),
                recommendation=f"Incrementa stage_5_dryer_evap_capacity_kg_h a >= {suggested_dryer:.1f} kg/h",
            )
        )

    chamber_volume = equipment_specs["stage_5_dryer_chamber_volume_m3"]
    specific_powder_load = stage_5["powder_mass_kg_h"] / chamber_volume if chamber_volume > 0 else 0.0
    indicators["stage_5_powder_load_kg_h_m3"] = specific_powder_load
    if specific_powder_load > capacity_limits["stage_5_max_powder_rate_kg_h_m3"]:
        suggested_volume = stage_5["powder_mass_kg_h"] / capacity_limits["stage_5_max_powder_rate_kg_h_m3"]
        issues.append(
            _new_issue(
                code="STAGE5_DRYER_VOLUME",
                equipment="Camara secador Etapa 5",
                message=(
                    f"Carga de polvo {specific_powder_load:.2f} kg/h/m3 excede limite "
                    f"{capacity_limits['stage_5_max_powder_rate_kg_h_m3']:.2f} kg/h/m3"
                ),
                recommendation=f"Incrementa stage_5_dryer_chamber_volume_m3 a >= {suggested_volume:.2f} m3",
            )
        )

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
