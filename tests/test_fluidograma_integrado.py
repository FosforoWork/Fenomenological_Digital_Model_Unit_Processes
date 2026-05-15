"""Pruebas de transformacion para fluidograma integrado."""

from __future__ import annotations

import unittest

from core.stage_equations import run_process_model
from visualizaciones.fluidograma_integrado import build_fluidograma_payload


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
    "evap_pressure_bar": 0.40,
    "enable_ro": 0.0,
    "ro_tmp_bar": 24.0,
    "evap_temp_c": 55.0,
    "precip_ph": 4.5,
    "precip_time_min": 25.0,
    "centrifuge_g": 1800.0,
    "centrifuge_time_min": 20.0,
    "dryer_temp_c": 78.0,
    "dryer_residence_min": 42.0,
}


class FluidogramaIntegradoTests(unittest.TestCase):
    def test_payload_sections_exist(self) -> None:
        result = run_process_model(BASELINE_CONTROLS)
        payload = build_fluidograma_payload(result)

        self.assertIn("nodes", payload)
        self.assertIn("links", payload)
        self.assertIn("rendimientos", payload)
        self.assertIn("desperdicios", payload)
        self.assertIn("balance", payload)

        self.assertGreater(len(payload["nodes"]), 0)
        self.assertGreater(len(payload["links"]), 0)

    def test_balance_is_consistent_with_model_integrity(self) -> None:
        result = run_process_model(BASELINE_CONTROLS)
        payload = build_fluidograma_payload(result)

        self.assertAlmostEqual(
            payload["balance"]["mass_in_kg_h"],
            result["integrity"]["mass_in_kg_h"],
            places=6,
        )
        self.assertAlmostEqual(
            payload["balance"]["mass_out_kg_h"],
            result["integrity"]["mass_out_kg_h"],
            places=6,
        )
        self.assertAlmostEqual(
            payload["balance"]["mass_balance_closure_pct"],
            result["integrity"]["mass_balance_closure_pct"],
            places=6,
        )

    def test_link_values_are_non_negative(self) -> None:
        result = run_process_model(BASELINE_CONTROLS)
        payload = build_fluidograma_payload(result)

        for link in payload["links"]:
            self.assertGreaterEqual(float(link["value"]), 0.0)

    def test_all_rendimientos_are_non_negative(self) -> None:
        result = run_process_model(BASELINE_CONTROLS)
        payload = build_fluidograma_payload(result)

        for metric in payload["rendimientos"]:
            self.assertGreaterEqual(float(metric["value_pct"]), 0.0)


if __name__ == "__main__":
    unittest.main()
