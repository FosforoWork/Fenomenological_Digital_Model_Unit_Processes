"""Pruebas de regresion para alinear el caso base con Proyecto Final Unitarios."""

from __future__ import annotations

import math
import unittest

from core.stage_equations import run_process_model


BASELINE_CONTROLS = {
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


class StageEquationsTests(unittest.TestCase):
    def test_baseline_matches_project_final(self) -> None:
        result = run_process_model(BASELINE_CONTROLS)

        self.assertAlmostEqual(result["stage_1"]["extraction_eff_pct"], 88.0, places=2)
        self.assertAlmostEqual(result["stage_2_5_ro"]["ro_recovery_pct"], 25.0, places=2)
        self.assertAlmostEqual(result["stage_3"]["evaporated_water_m3_h"], 9.939, delta=0.05)
        self.assertAlmostEqual(result["stage_4"]["protein_precip_kg_h"], 323.4, delta=0.1)
        self.assertAlmostEqual(result["stage_4_2"]["paste_mass_kg_h"], 692.8, delta=0.2)
        self.assertAlmostEqual(result["stage_5"]["powder_mass_kg_h"], 364.6, delta=0.3)
        self.assertAlmostEqual(result["stage_5"]["protein_final_kg_h"], 323.4, delta=0.1)
        self.assertAlmostEqual(result["stage_5"]["final_moisture_pct"], 5.0, places=2)

        self.assertLessEqual(abs(result["integrity"]["mass_balance_error_pct"]), 0.5)

    def test_invalid_control_range_raises(self) -> None:
        controls = BASELINE_CONTROLS.copy()
        controls["water_flow_m3_h"] = 0.0

        with self.assertRaises(ValueError):
            run_process_model(controls)

    def test_non_finite_control_raises(self) -> None:
        controls = BASELINE_CONTROLS.copy()
        controls["evap_temp_c"] = float("nan")

        with self.assertRaises(ValueError):
            run_process_model(controls)

    def test_outputs_are_finite_and_non_negative(self) -> None:
        result = run_process_model(BASELINE_CONTROLS)

        values = []
        for stage_data in result.values():
            if not isinstance(stage_data, dict):
                continue
            for value in stage_data.values():
                if isinstance(value, (int, float)):
                    values.append(float(value))

        self.assertTrue(values)
        self.assertTrue(all(math.isfinite(value) for value in values))
        self.assertTrue(all(value >= 0.0 for value in values))


if __name__ == "__main__":
    unittest.main()
