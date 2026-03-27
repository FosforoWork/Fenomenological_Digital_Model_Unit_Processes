"""Calculos economicos de la etapa de ventas para la sala de control."""

from __future__ import annotations

DOC_EXCHANGE_RATE_BS_PER_USD = 6.96
DOC_ANNUAL_OPERATING_HOURS = 8000.0
DOC_OPEX_TOTAL_ANNUAL_USD = 4_959_920.0
# Valor fijado segun el resumen documental (tabla 7.4).
DOC_OPEX_TOTAL_ANNUAL_BS = 34_521_043.0
DEFAULT_SALES_PRICE_BS_PER_KG = 18.10


def compute_sales_stage(
    powder_mass_kg_h: float,
    selling_price_bs_kg: float,
    opex_annual_bs: float = DOC_OPEX_TOTAL_ANNUAL_BS,
    annual_hours: float = DOC_ANNUAL_OPERATING_HOURS,
) -> dict[str, float]:
    """Calcula KPIs economicos de la etapa de ventas."""
    powder_mass_kg_h = max(0.0, float(powder_mass_kg_h))
    selling_price_bs_kg = max(0.0, float(selling_price_bs_kg))
    opex_annual_bs = max(0.0, float(opex_annual_bs))
    annual_hours = max(1.0, float(annual_hours))

    sales_hourly_bs = powder_mass_kg_h * selling_price_bs_kg
    sales_annual_bs = sales_hourly_bs * annual_hours

    opex_hourly_bs = opex_annual_bs / annual_hours

    operating_profit_hourly_bs = sales_hourly_bs - opex_hourly_bs
    operating_profit_annual_bs = sales_annual_bs - opex_annual_bs

    cost_per_kg_bs = 0.0
    if powder_mass_kg_h > 0.0:
        cost_per_kg_bs = opex_hourly_bs / powder_mass_kg_h

    revenue_per_kg_bs = selling_price_bs_kg
    profit_per_kg_bs = revenue_per_kg_bs - cost_per_kg_bs

    operating_margin_pct = 0.0
    if sales_annual_bs > 0.0:
        operating_margin_pct = (operating_profit_annual_bs / sales_annual_bs) * 100.0

    return {
        "selling_price_bs_kg": selling_price_bs_kg,
        "powder_mass_kg_h": powder_mass_kg_h,
        "opex_annual_bs": opex_annual_bs,
        "opex_hourly_bs": opex_hourly_bs,
        "sales_hourly_bs": sales_hourly_bs,
        "sales_annual_bs": sales_annual_bs,
        "operating_profit_hourly_bs": operating_profit_hourly_bs,
        "operating_profit_annual_bs": operating_profit_annual_bs,
        "operating_margin_pct": operating_margin_pct,
        "cost_per_kg_bs": cost_per_kg_bs,
        "revenue_per_kg_bs": revenue_per_kg_bs,
        "profit_per_kg_bs": profit_per_kg_bs,
    }
