"""Calculos economicos de la etapa de ventas para la sala de control."""

from __future__ import annotations

DOC_EXCHANGE_RATE_BS_PER_USD = 6.96
DOC_ANNUAL_OPERATING_HOURS = 7500.0
# OPEX antiguo
DOC_OPEX_TOTAL_ANNUAL_BS = 34_521_043.0
DEFAULT_SALES_PRICE_BS_PER_KG = 24.36 # ~3.5 USD/kg

class FinancialModeler:
    def __init__(self, powder_mass_kg_h: float = 301.6, sales_price_usd_kg: float = 3.50, annual_hours: float = 7500.0):
        self.powder_mass_kg_h = max(0.0, float(powder_mass_kg_h))
        self.sales_price_usd_kg = max(0.0, float(sales_price_usd_kg))
        self.annual_hours = max(1.0, float(annual_hours))
        
        # CAPEX details from document
        self.capex_direct_usd = 3_493_000.0
        self.capex_indirect_usd = 698_600.0
        self.capex_total_usd = self.capex_direct_usd + self.capex_indirect_usd
        self.working_capital_usd = 450_000.0
        self.total_initial_investment_usd = self.capex_total_usd + self.working_capital_usd
        
        # OPEX base details
        self.opex_variable_usd = 4_761_550.0 # at nominal 7500h and 301.6 kg/h
        self.opex_fixed_usd = 751_925.0
        self.depreciation_usd = 377_244.0
        self.circularity_offset_usd = 143_200.0
        
    def run_financial_simulation(self) -> dict[str, float]:
        # Ajustar OPEX variable al ratio de produccion actual (escalado lineal simple)
        ratio = self.powder_mass_kg_h / 301.6 if self.powder_mass_kg_h > 0 else 0
        adj_opex_variable = self.opex_variable_usd * ratio
        
        opex_total_net_usd = adj_opex_variable + self.opex_fixed_usd - self.circularity_offset_usd
        
        annual_production_kg = self.powder_mass_kg_h * self.annual_hours
        gross_revenue_usd = annual_production_kg * self.sales_price_usd_kg
        
        ebitda_usd = gross_revenue_usd - opex_total_net_usd
        
        # Taxes and simple NPV
        ebit_usd = ebitda_usd - self.depreciation_usd
        taxes_usd = max(0.0, ebit_usd * 0.25) # 25% tax
        net_income_usd = ebit_usd - taxes_usd
        operating_cash_flow_usd = net_income_usd + self.depreciation_usd
        
        npv_usd = -self.total_initial_investment_usd
        wacc = 0.12
        for year in range(1, 11):
            npv_usd += operating_cash_flow_usd / ((1 + wacc) ** year)
            
        payback_years = 0.0
        if operating_cash_flow_usd > 0:
            payback_years = self.total_initial_investment_usd / operating_cash_flow_usd
            
        return {
            "capex_total_usd": self.capex_total_usd,
            "total_investment_usd": self.total_initial_investment_usd,
            "opex_variable_usd": adj_opex_variable,
            "opex_fixed_usd": self.opex_fixed_usd,
            "circularity_offset_usd": self.circularity_offset_usd,
            "opex_total_net_usd": opex_total_net_usd,
            "gross_revenue_usd": gross_revenue_usd,
            "ebitda_usd": ebitda_usd,
            "net_income_usd": net_income_usd,
            "operating_cash_flow_usd": operating_cash_flow_usd,
            "npv_usd": npv_usd,
            "payback_years": payback_years,
        }

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
