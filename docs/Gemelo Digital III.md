# Gemelo Digital y Diseño Integral de Planta: Producción de Proteína Aislada de Soya
## (Integración con Gemelo Digital, Cálculos Profundos y Normativa Internacional)
**Ingeniería de Procesos Senior - PARTE III**

---

## 8. Ingeniería Financiera y Estructura de Costos (Estimación Clase 3 AACE)

### 8.1. Estructura de Inversión de Capital (CAPEX)
**A. CAPEX Directo:**
1. Maquinaria Principal: $1,960,000 USD.
2. Utilidades: $450,000 USD.
3. Robótica/AMMRs: $185,000 USD.
4. Instrumentación/DCS: $320,000 USD.
5. Obras Civiles/Piping: $588,000 USD.
- *Subtotal Directo:* $3,493,000 USD.

**B. CAPEX Indirecto (20%):** $698,600 USD.
- **CAPEX TOTAL:** **$4,191,600 USD**.

### 8.2. Capital de Trabajo (OWC)
- Cobertura de 30 días de materia prima, inventario ISP y cuentas por cobrar/pagar.
- **Inversión OWC:** **$\approx $450,000 USD**.
- **INVERSIÓN TOTAL INICIAL:** **$4,641,600 USD**.

### 8.3. Estructura de OPEX (7,500 hrs/año)
**A. OPEX Variable:** $4,761,550 USD/año (Soya @ 430 USD/ton).
**B. OPEX Fijo:** $751,925 USD/año (Salarios, Mantenimiento 2.5%, Seguros).
**C. Depreciación (10 años):** $377,244 USD/año.
**D. Offset por Circularidad:** $\approx$ $143,200 USD/año.

### 8.4. Indicadores de Rentabilidad
- **Producción Anual:** 2,262,000 kg/año ISP.
- **Costo Unitario Neto:** **$\approx 2.37 \text{ USD/kg}$**.
- **Revenue Anual (@ 3.50 USD/kg):** $7,917,000 USD/año.
- **EBITDA Anual:** **$\approx $2,546,725 USD/año** (Margen 32.1%).
- **Payback Period:** **$\approx 2.15 \text{ años}$**.

---

## 9. Datasheets Técnicos de Equipamiento

### 9.1. DS-101: Tanque de Extracción (TK-101 + AG-101)
- **Capacidad:** 14.0 m³.
- **Agitador:** EKATO PBT 6 palas, 7.5 kW.
- **Material:** AISI 316L, $Ra \le 0.4 \mu\text{m}$.

### 9.2. DS-102: Decanters (CF-102A/B)
- **Proveedor:** Alfa Laval Foodec.
- **Capacidad:** 2 x 8 m³/h.
- **Factor G:** 1800 - 2000 g.

### 9.3. DS-201: Pasteurizador (HX-201)
- **Carga Útil:** 310 kW (55% HR).
- **Área:** 39.6 m² (GEA/Alfa Laval).

### 9.4. DS-301: Evaporador (EV-301)
- **Tipo:** Película Descendente, Doble Efecto.
- **Economía:** $E = 1.85$.
- **Vacío:** 0.40 bar abs.

### 9.5. DS-501: Spray Dryer (SD-501)
- **Capacidad:** 400 kg/h polvo.
- **Atomizador:** Rotativo (18,000 rpm).
- **Seguridad:** NFPA 68 (Venteo explosión).

---

## 10. Análisis de Cuello de Botella y Sensibilidad (TOC)

### 10.1. Identificación de Restricciones
- **TK-101 (Lixiviación):** 96.5% utilización. **Cuello de Botella Primario.** Limitado por cinética de difusión (tiempo de residencia).
- **EV-301 (Evaporador):** 89.6% utilización. Restricción térmica secundaria.
- **Spray Dryer SD-501:** 70.8% utilización. Buffer de seguridad.

### 10.2. Rangos de Operabilidad
- **Ratio Agua:Soya:** $< 1:9$ causa saturación; $> 1:14$ inunda evaporador.
- **pH Extracción:** $< 8.0$ falla rendimiento; $> 9.5$ causa hidrólisis y toxicidad.
- **Vacío Evaporador:** $> 0.6$ bar detona Reacción de Maillard (oscurecimiento).

### 10.3. Límites y Escalabilidad
- **Punto de Equilibrio:** Mínimo $680 \text{ kg/h}$ de soya para viabilidad térmica.
- **Escalabilidad:** Aumentar a $1,500 \text{ kg/h}$ es posible mediante un segundo reactor TK-101B e integración plena de Ósmosis Inversa (RO-205).
