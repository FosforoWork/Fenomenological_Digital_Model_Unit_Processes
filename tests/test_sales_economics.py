"""Pruebas de regresion para los KPIs economicos de ventas y el Gemelo Digital Financiero."""

from __future__ import annotations

import unittest

from core.sales_economics import (
    DEFAULT_SALES_PRICE_BS_PER_KG,
    DOC_OPEX_TOTAL_ANNUAL_BS,
    FinancialModeler,
    compute_sales_stage,
)


class SalesEconomicsTests(unittest.TestCase):
    def test_documented_base_case_matches_expected_magnitude(self) -> None:
        # Se inyecta explicitamente el OPEX antiguo para compatibilidad con la verificacion documental.
        stage = compute_sales_stage(
            powder_mass_kg_h=364.6,
            selling_price_bs_kg=DEFAULT_SALES_PRICE_BS_PER_KG,
            opex_annual_bs=DOC_OPEX_TOTAL_ANNUAL_BS
        )

        self.assertAlmostEqual(stage["opex_annual_bs"], DOC_OPEX_TOTAL_ANNUAL_BS, places=6)
        self.assertAlmostEqual(stage["sales_annual_bs"], 66_612_420.0, delta=100.0)

    def test_price_change_impacts_sales_and_profit(self) -> None:
        low = compute_sales_stage(powder_mass_kg_h=364.6, selling_price_bs_kg=15.31, opex_annual_bs=DOC_OPEX_TOTAL_ANNUAL_BS)
        high = compute_sales_stage(powder_mass_kg_h=364.6, selling_price_bs_kg=20.88, opex_annual_bs=DOC_OPEX_TOTAL_ANNUAL_BS)

        self.assertGreater(high["sales_annual_bs"], low["sales_annual_bs"])
        self.assertGreater(high["operating_profit_annual_bs"], low["operating_profit_annual_bs"])

    def test_zero_sales_returns_negative_profit_by_opex(self) -> None:
        stage = compute_sales_stage(powder_mass_kg_h=0.0, selling_price_bs_kg=18.10, opex_annual_bs=DOC_OPEX_TOTAL_ANNUAL_BS)

        self.assertEqual(stage["sales_annual_bs"], 0.0)
        self.assertAlmostEqual(stage["operating_profit_annual_bs"], -DOC_OPEX_TOTAL_ANNUAL_BS, places=6)
        self.assertEqual(stage["operating_margin_pct"], 0.0)

    def test_per_kg_metrics_are_consistent(self) -> None:
        stage = compute_sales_stage(powder_mass_kg_h=364.6, selling_price_bs_kg=18.10, opex_annual_bs=DOC_OPEX_TOTAL_ANNUAL_BS)

        self.assertAlmostEqual(stage["revenue_per_kg_bs"], 18.10, places=6)
        self.assertAlmostEqual(stage["cost_per_kg_bs"], stage["opex_hourly_bs"] / 364.6, places=6)
        self.assertAlmostEqual(
            stage["profit_per_kg_bs"],
            stage["revenue_per_kg_bs"] - stage["cost_per_kg_bs"],
            places=6,
        )

    def test_advanced_financial_modeler_structure(self) -> None:
        # Prueba del nuevo motor de simulacion financiera
        model = FinancialModeler(powder_mass_kg_h=301.6)
        results = model.run_financial_simulation()

        self.assertIn("capex_total_usd", results)
        self.assertGreater(results["capex_total_usd"], 3_000_000.0)
        
        self.assertIn("npv_usd", results)
        self.assertIn("payback_years", results)
        self.assertIn("circularity_offset_usd", results)

        # La monetización de subproductos (Okara/Suero) debe reducir el OPEX neto
        self.assertGreater(results["circularity_offset_usd"], 0.0)
        self.assertLess(results["opex_total_net_usd"], results["opex_variable_usd"] + results["opex_fixed_usd"])

if __name__ == "__main__":
    unittest.main()
