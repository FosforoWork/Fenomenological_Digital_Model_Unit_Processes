"""Pruebas para restricciones de capacidad y configuracion editable de equipos."""

from __future__ import annotations

import unittest

from core.equipment_constraints import EquipmentCapacityError
from core.equipment_specs import get_default_capacity_limits, get_default_equipment_specs
from core.stage_equations import run_process_model


BASELINE_CONTROLS = {
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
    "enable_ro": 0.0,
    "ro_tmp_bar": 24.0,
    "evap_temp_c": 75.0,
    "precip_ph": 4.5,
    "precip_time_min": 25.0,
    "centrifuge_g": 1800.0,
    "centrifuge_time_min": 20.0,
    "dryer_temp_c": 190.0,
    "dryer_residence_min": 42.0,
}


class EquipmentConstraintsTests(unittest.TestCase):
    def test_baseline_capacity_passes(self) -> None:
        result = run_process_model(BASELINE_CONTROLS)
        self.assertIn("capacity", result)
        self.assertGreater(result["capacity"]["stage_2_hex_thermal_load_pct"], 0.0)

    def test_interchanger_capacity_too_small_blocks(self) -> None:
        specs = get_default_equipment_specs()
        specs["stage_2_hex_area_m2"] = 5.0

        with self.assertRaises(EquipmentCapacityError) as ctx:
            run_process_model(BASELINE_CONTROLS, equipment_specs=specs)

        codes = {issue["code"] for issue in ctx.exception.issues}
        self.assertIn("STAGE2_HEX_THERMAL_CAPACITY", codes)

    def test_dryer_capacity_blocks(self) -> None:
        specs = get_default_equipment_specs()
        specs["stage_5_dryer_evap_capacity_kg_h"] = 200.0

        with self.assertRaises(EquipmentCapacityError) as ctx:
            run_process_model(BASELINE_CONTROLS, equipment_specs=specs)

        codes = {issue["code"] for issue in ctx.exception.issues}
        self.assertIn("STAGE5_DRYER_CAPACITY", codes)


if __name__ == "__main__":
    unittest.main()
