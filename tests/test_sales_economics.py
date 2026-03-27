"""Pruebas de regresion para los KPIs economicos de ventas."""

from __future__ import annotations

import unittest

from core.sales_economics import (
    DEFAULT_SALES_PRICE_BS_PER_KG,
    DOC_OPEX_TOTAL_ANNUAL_BS,
    compute_sales_stage,
)


class SalesEconomicsTests(unittest.TestCase):
    def test_documented_base_case_matches_expected_magnitude(self) -> None:
        # Caso base documental: 364.6 kg/h de polvo y 18.10 Bs/kg.
        stage = compute_sales_stage(
            powder_mass_kg_h=364.6,
            selling_price_bs_kg=DEFAULT_SALES_PRICE_BS_PER_KG,
        )

        self.assertAlmostEqual(stage["opex_annual_bs"], DOC_OPEX_TOTAL_ANNUAL_BS, places=6)
        self.assertAlmostEqual(stage["sales_annual_bs"], 52_794_080.0, delta=1.0)
        self.assertAlmostEqual(stage["operating_profit_annual_bs"], 18_273_037.0, delta=1.0)

    def test_price_change_impacts_sales_and_profit(self) -> None:
        low = compute_sales_stage(powder_mass_kg_h=364.6, selling_price_bs_kg=15.31)
        high = compute_sales_stage(powder_mass_kg_h=364.6, selling_price_bs_kg=20.88)

        self.assertGreater(high["sales_annual_bs"], low["sales_annual_bs"])
        self.assertGreater(high["operating_profit_annual_bs"], low["operating_profit_annual_bs"])

    def test_zero_sales_returns_negative_profit_by_opex(self) -> None:
        stage = compute_sales_stage(powder_mass_kg_h=0.0, selling_price_bs_kg=18.10)

        self.assertEqual(stage["sales_annual_bs"], 0.0)
        self.assertAlmostEqual(stage["operating_profit_annual_bs"], -DOC_OPEX_TOTAL_ANNUAL_BS, places=6)
        self.assertEqual(stage["operating_margin_pct"], 0.0)

    def test_per_kg_metrics_are_consistent(self) -> None:
        stage = compute_sales_stage(powder_mass_kg_h=364.6, selling_price_bs_kg=18.10)

        self.assertAlmostEqual(stage["revenue_per_kg_bs"], 18.10, places=6)
        self.assertAlmostEqual(stage["cost_per_kg_bs"], stage["opex_hourly_bs"] / 364.6, places=6)
        self.assertAlmostEqual(
            stage["profit_per_kg_bs"],
            stage["revenue_per_kg_bs"] - stage["cost_per_kg_bs"],
            places=6,
        )


if __name__ == "__main__":
    unittest.main()
