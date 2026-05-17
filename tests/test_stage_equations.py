"""Pruebas de regresion para alinear el caso base con Proyecto Final Unitarios."""

from __future__ import annotations

import math
import unittest

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
    "ro_tmp_bar": 24.0,
    "evap_temp_c": 75.0,
    "precip_ph": 4.5,
    "precip_time_min": 25.0,
    "centrifuge_g": 1800.0,
    "centrifuge_time_min": 20.0,
    "dryer_temp_c": 190.0,
    "dryer_residence_min": 42.0,
}


class StageEquationsTests(unittest.TestCase):
    def test_baseline_matches_project_final(self) -> None:
        result = run_process_model(BASELINE_CONTROLS)

        self.assertAlmostEqual(result["stage_1"]["extraction_eff_pct"], 88.0, places=2)
        # With RO active, stage 3 evaporated water is reduced
        self.assertAlmostEqual(result["stage_3"]["evaporated_water_m3_h"], 5.51, delta=0.1)
        self.assertAlmostEqual(result["stage_4"]["protein_precip_kg_h"], 292.3, delta=0.5)
        self.assertAlmostEqual(result["stage_4_2"]["paste_mass_kg_h"], 584.7, delta=1.0)
        self.assertAlmostEqual(result["stage_5"]["powder_mass_kg_h"], 301.6, delta=1.0)
        self.assertAlmostEqual(result["stage_5"]["protein_final_kg_h"], 286.5, delta=0.5)
        self.assertAlmostEqual(result["stage_5"]["final_moisture_pct"], 5.0, places=2)

        self.assertLessEqual(abs(result["integrity"]["mass_balance_error_pct"]), 0.1)

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
        # Ignore tiny numerical noise near zero for non-negative check
        self.assertTrue(all(value >= -1e-9 for value in values))


if __name__ == "__main__":
    unittest.main()
