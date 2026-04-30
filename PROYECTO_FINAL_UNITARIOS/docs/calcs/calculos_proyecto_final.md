# Calculos del Proyecto Final
## Produccion de proteina aislada de soya (base: 1 ton/h de grano)

> Documento consolidado en formato Markdown, con calculos trazables, unidades consistentes y criterios explicitos para evitar ambiguedades.

---

## Indice

1. [Objetivo](#1-objetivo)
2. [Base de calculo y supuestos](#2-base-de-calculo-y-supuestos)
3. [Calculos Detallados por Etapa (Inputs/Outputs)](#3-calculos-detallados-por-etapa-inputsoutputs)
4. [Investigación de Equipos y Costos (CEPCI 2024)](#4-investigación-de-equipos-y-costos-cepci-2024)
5. [Validación de Consistencia (Doc vs Código)](#5-validación-de-consistencia-doc-vs-código)
6. [Resultados del caso base](#6-resultados-del-caso-base)
7. [Verificaciones globales](#7-verificaciones-globales)
8. [Balance final de rendimiento por etapa](#8-balance-final-de-rendimiento-por-etapa)
9. [Analisis economico preliminar (CAPEX y OPEX)](#9-analisis-economico-preliminar-capex-y-opex)
10. [Resumen ejecutivo de variables](#10-resumen-ejecutivo-de-variables)
11. [Presentacion de ingenieria: Datasheets de equipos](#11-presentacion-de-ingenieria-datasheets-de-equipos)
12. [Presentacion de ingenieria: PFD narrativo y control](#12-presentacion-de-ingenieria-pfd-narrativo-y-control)
13. [Presentacion de ingenieria: Matriz de criticidad](#13-presentacion-de-ingenieria-matriz-de-criticidad)
14. [Presentacion de ingenieria: Riesgos y mitigacion](#14-presentacion-de-ingenieria-riesgos-y-mitigacion)
15. [Especificaciones de envasado y estrategia de entrega](#15-especificaciones-de-envasado-y-estrategia-de-entrega)
16. [Referencias internas](#16-referencias-internas)
17. [Anexo de bibliografia consultada](#17-anexo-de-bibliografia-consultada)

---

## 1. Objetivo

Consolidar una base de calculo unica, coherente y trazable para el proceso de produccion de proteina aislada de soya.

Esta version eleva el realismo del modelo con los siguientes criterios de diseno:

- **Factor de pérdida operacional (f_loss):** 2% por etapa (Cubre mermas mecánicas, suciedad en tuberías y residuos en equipos).
- **Eficiencia global proyectada:** ~75% de recuperación proteica (Alineado con realidades industriales).
- **Evaporacion en multiple efecto:** (2 efectos) para optimización energética.
- **Actualización de costos:** Basada en índice CEPCI 2024 (~800).
- **Sin factor de ensuciamiento:** (Ajustado en margen de área).
- **Inclusion de analisis economico preliminar:** (CAPEX/OPEX).

---

## 2. Base de calculo y supuestos

### 2.1 Alimentacion

| Variable | Valor | Justificación |
|---|---:|---|
| Grano de soya | 1000 kg/h | Escala piloto-industrial base |
| Proteina en grano | 37.5% p/p | Promedio soya regional (36-40%) |
| Proteina de entrada | 375 kg/h | Cálculo directo (1000 * 0.375) |
| Agua de extraccion (1:12) | 12000 kg/h | Relación óptima solubilidad/costo energético |

### 2.2 Supuestos promedio de operacion

| Variable | Valor | Justificacion tecnica |
|---|---:|---|
| Eficiencia de extraccion proteica (Etapa 1) | 88% | Literatura para extraccion alcalina (pH 8.5-9.0): rango 85–92% según FAO/Perry. |
| Recuperacion proteica en precipitacion (Etapa 4) | 98% | Estándar aislado de soya en punto isoeléctrico (pH 4.5); pérdida 2% por solubilidad residual |
| Humedad de pasta post-centrifugacion | 50% | Centrifuga decantadora sanitaria típica; <50% requiere otros métodos |
| Humedad final de polvo | 5% | Estándar comercial para estabilidad microbiológica |
| pH de extraccion | 8.75 | Máxima solubilidad sin hidrólisis excesiva |
| Temperatura de extraccion | 55 C | Optimiza cinética sin desnaturalizar proteína |
| Pasteurizacion | 80 C por 22 s | Proceso HTST para seguridad alimentaria |
| Evaporacion multiple efecto | 2 efectos | Economía de vapor ~1.85 kg/kg |
| Presion de referencia en evaporacion | 0.40 bar abs | T ebullición ~48°C (Protección térmica) |
| Factor de pérdida operacional | 2.0% | **Criterio de Realismo:** Pérdidas por transporte, limpieza y mermas mecánicas |

### 2.3 Criterios de reporte

1. Se reportan dos salidas finales:
  1. Polvo total (kg/h)
  2. Proteina pura recuperada (kg/h)
2. Los reactivos de ajuste de pH (NaOH/HCl) se incluyen en OPEX y se consideran despreciables en el cierre principal de masa.
3. Se aplica un factor de ensuciamiento del 10% en el cálculo de área de intercambiadores.

### 2.4 Criterios generales de diseño y factores de seguridad

| Criterio | Valor/Rango | Justificación |
|---|---|---|
| Margen de diseño bombas | 20% Caudal / 15% TDH | Cubre variaciones de viscosidad y ensuciamiento tuberías |
| Factor de capacidad tanques | 25% Volumen libre | Evita desbordamientos por espuma o agitación |
| Margen área intercambiadores | 10% Adicional | Compensación por fouling industrial |
| Eficiencia electromecánica | 90% | Pérdidas en motores y transmisión |
| Autonomía almacenamiento | 1.25 h | Asegura continuidad ante fallas menores de suministro |

### 2.5 Base hidrica del caso base (red industrial)

Para esta version se fija como caso base el suministro desde red industrial.

| Parametro | Valor |
|---|---:|
| Fuente de agua | Red industrial |
| Caudal de agua de extraccion | 12000 L/h |
| Caudal equivalente | 12.0 m3/h |
| Caudal en SI | 0.00333 m3/s |
| Densidad de agua (25 C) | 1000 kg/m3 |
| Viscosidad cinematica (25 C) | 0.89e-6 m2/s |

Se adopta autonomia minima de 1 hora con reserva operativa del 20% para asegurar continuidad de extraccion y disponibilidad de agua para ajustes operativos.

---

## 3. Calculos Detallados por Etapa (Inputs/Outputs)

A continuación se detallan los balances de masa y energía para cada etapa operativa, asegurando la trazabilidad de las variables y aplicando el factor de pérdida del 2% ($f_{loss} = 0.02$).

### 3.0 Etapa 0: Captación y Almacenamiento
**Objetivo:** Asegurar el suministro hídrico constante para la relación 1:12.

| Variable de Entrada | Valor | Variable de Salida | Valor |
|---|---:|---|---:|
| Grano de soya (Alim.) | 1000 kg/h | Agua a Extracción | 12000 kg/h |
| Agua de Red (Caudal) | 12.0 m3/h | Potencia Bombeo (P-101) | 0.72 kW |
| Temperatura Agua | 25 C | Capacidad Tanque (TK-101) | 15.0 m3 |

*Justificación:* Se aplica un factor de seguridad del 20% sobre la potencia teórica de bombeo.

### 3.1 Etapa 1: Extracción Alcalina
**Objetivo:** Solubilizar la proteína mediante pH alcalino (8.75) y agitación.

| Variable de Entrada | Valor | Variable de Salida | Valor |
|---|---:|---|---:|
| Grano de soya | 1000 kg/h | Masa de Lodo Total | 12740 kg/h |
| Agua de Extracción | 12000 kg/h | Proteína Disuelta | 323.4 kg/h |
| Eficiencia Extracción | 88% | Pérdida Mecánica (2%) | 260 kg/h |

### 3.2 Etapa 1.2: Separación Sólido-Líquido (Centrifugación 1)
**Objetivo:** Clarificar el extracto eliminando la fibra (okara).

| Variable de Entrada | Valor | Variable de Salida | Valor |
|---|---:|---|---:|
| Masa de Lodo | 12740 kg/h | Extracto Clarificado | 10646.7 kg/h |
| Proteína en Lodo | 323.4 kg/h | Okara Húmedo (65% H) | 1876.0 kg/h |

### 3.3 Etapa 2: Pasteurización HTST
**Objetivo:** Inactivación enzimática y microbiológica manteniendo funcionalidad.

| Variable de Entrada | Valor | Variable de Salida | Valor |
|---|---:|---|---:|
| Extracto Clarificado | 10646.7 kg/h | Extracto Pasteurizado | 10433.8 kg/h |
| Temperatura Entrada | 25 C | Carga Térmica Neta | 278.4 kW |
| Temperatura Destino | 80 C | Factor de Pérdida | 2.0% |

### 3.4 Etapa 2.5: Ósmosis Inversa (Concentración por Membrana)
**Objetivo:** Reducir carga térmica retirando agua por vía mecánica (Innovación).

| Variable de Entrada | Valor | Variable de Salida | Valor |
|---|---:|---|---:|
| Extracto Pasteurizado | 10433.8 kg/h | Permeado (Agua) | 2608.5 kg/h |
| Presión (TMP) | 24 bar | Retentado Neto | 7668.8 kg/h |
| Recuperación (Rec) | 25% | Proteína en Retentado | 304.4 kg/h |

### 3.5 Etapa 3: Evaporación de Doble Efecto
**Objetivo:** Alcanzar 23% de sólidos totales.

| Variable de Entrada | Valor | Variable de Salida | Valor |
|---|---:|---|---:|
| Retentado (Alim. EV) | 7668.8 kg/h | Concentrado Neto | 1296.9 kg/h |
| Proteína Alim. | 304.4 kg/h | Agua Evaporada | 6345.4 kg/h |
| Presión de Vacío | 0.40 bar | Proteína en Concentrado | 298.3 kg/h |

### 3.6 Etapa 4: Precipitación y Centrifugación 2
**Objetivo:** Recuperar la proteína aislada en punto isoeléctrico (pH 4.5).

| Variable de Entrada | Valor | Variable de Salida | Valor |
|---|---:|---|---:|
| Concentrado (EV) | 1296.9 kg/h | Pasta Proteica (50% H) | 573.0 kg/h |
| pH Ajuste | 4.5 | Suero Residual | 712.3 kg/h |
| Eficiencia Precip. | 98% | Proteína en Pasta | 286.5 kg/h |

### 3.7 Etapa 5: Secado Spray y Clasificación
**Objetivo:** Obtener polvo fino con 5% de humedad.

| Variable de Entrada | Valor | Variable de Salida | Valor |
|---|---:|---|---:|
| Pasta Proteica | 573.0 kg/h | Polvo Final Neto | 295.5 kg/h |
| Humedad Entrada | 50% | Humedad Final | 5.0% |
| Rendimiento Proteína | 74.87% | Proteína Final Neta | 280.8 kg/h |


---

## 4. Investigación de Equipos y Costos (CEPCI 2024)

### 4.1 Metodología de Estimación de Costos
Se utiliza el método de escalado por capacidad y ajuste por índice de inflación de ingeniería química (CEPCI).
- **CEPCI 2020:** 600 (Referencia)
- **CEPCI 2024:** 795.4 (Actualizado) -> Factor de ajuste: **1.326**

### 4.2 Tabla Detallada de Equipamiento y Materiales

| Equipo | Material | Capacidad Operativa | Costo Base (USD) | Costo Instalado (USD) |
|---|---|---|---:|---:|
| **Tanque Agua (TK-101)** | AISI 304 | 15 m3 | 32,000 | 42,432 |
| **Tanque Extraccion (TK-102)** | AISI 316L | 14 m3 | 45,000 | 59,670 |
| **Decanter 1 (CF-102A/B)** | AISI 316L | 2 x 8 m3/h | 180,000 | 238,680 |
| **Intercambiador (HX-201)** | AISI 316L | 40 m2 | 22,000 | 29,172 |
| **Módulo OI (RO-205)** | Poliamida/316L | 12.5 m3/h | 95,000 | 125,970 |
| **Evaporador (EV-301)** | AISI 316L | 10 t/h evap. | 650,000 | 861,900 |
| **Decanter 2 (CF-401)** | AISI 316L | 3 m3/h | 75,000 | 99,450 |
| **Spray Dryer (SD-501)** | AISI 316L | 400 kg/h polvo | 420,000 | 556,920 |
| **Sistemas Auxiliares** | Varios | 60 kW / 4 MW t | 441,200 | 512,000 |
| **TOTAL CAPEX** | - | - | **1,960,200** | **2,526,200** |

*Nota: El costo instalado incluye factores de montaje y conexión.*

---

## 5. Validación de Consistencia (Doc vs Código)

Se ha auditado la implementación lógica en `core/stage_equations.py` frente a este documento:

1.  **Balance de Masa:** El código utiliza una arquitectura de cascada donde la salida de una etapa alimenta la siguiente. El error de cierre reportado por la función `run_process_model` es de **<0.2%**, validando la precisión de las ecuaciones de balance.
2.  **Eficiencias Variables:** La lógica de `ph_factor`, `temp_factor` y `time_factor` en el código (Etapa 1 y 4) sigue las curvas experimentales citadas en la bibliografía, penalizando el rendimiento fuera de los puntos óptimos (8.75 y 4.5 respectivamente).
3.  **Conversión de Unidades:** El código maneja internamente unidades SI (kg/s, W, m3/s) y convierte a unidades industriales (kg/h, kW, m3/h) para la visualización, asegurando que no haya errores de factor 3600.
4.  **Consistencia Económica:** Los valores en `core/sales_economics.py` (OPEX anual de 34.5M Bs) se derivan directamente de los costos de materia prima y energía detallados en la Sección 9.4 de este informe.

---

## 6. Resultados del caso base

## 6.1 Indicadores de produccion

- **Polvo final total:** 295.5 kg/h
- **Proteina pura recuperada:** 280.8 kg/h

Pureza proteica del polvo:

$$
\%P = \frac{280.8}{295.5} \cdot 100 = 95.0\%
$$

## 6.2 Rendimientos

Rendimiento de recuperacion de proteina (base proteina de entrada):

$$
\eta_{prot,global} = \frac{280.8}{375} \cdot 100 = 74.87\%
$$

Rendimiento masico de polvo (base grano):

$$
\eta_{polvo/grano} = \frac{295.5}{1000} \cdot 100 = 29.6\%
$$

---

## 7. Verificaciones globales

## 7.1 Balance global de masa

Entrada total:

- 13000 kg/h (Soya + Agua)

Salidas principales:

- Okara humedo: 1876.0 kg/h
- Permeado OI: 2608.5 kg/h
- Condensado de evaporador: 6345.4 kg/h
- Suero residual: 712.3 kg/h
- Polvo final: 295.5 kg/h
- Agua removida en spray dryer: 271.4 kg/h
- **Mermas operacionales acumuladas:** 890.9 kg/h

Suma de salidas:

$$
1876.0 + 2608.5 + 6345.4 + 712.3 + 295.5 + 271.4 + 890.9 = 13000.0\ \text{kg/h}
$$

Cierre de masa global: **100.0%** (Las mermas cierran el balance físico real).

## 7.2 Balance energetico del caso base (realista)

- Pasteurizacion (utilidad real): 310 kW (Ajustado por menor flujo de extracto)
- Evaporacion 2 efectos (utilidad real): 3800 kW
- Secado por atomizacion (utilidad real): 300 kW
- Bombas + agitadores + equipos mecanicos (electricidad real): 60 kW

$$
\dot{E}_{total,real} \approx 310 + 3800 + 300 + 60 = 4470\ \text{kW}
$$

Consumo especifico por kg de proteina recuperada:

$$
e_{esp,prot} = \frac{4470}{280.8} = 15.9\ \text{kWh/kg proteina}
$$

Consumo especifico por kg de polvo:

$$
e_{esp,polvo} = \frac{4470}{295.5} = 15.1\ \text{kWh/kg polvo}
$$

## 7.3 Validacion de consistencia de balances y unidades

Checklist de validacion del caso base:

1. Cierre masico global: 100% incluyendo mermas técnicas.
2. Coherencia de potencia total: 4470 kW = suma de bloques de utilidad y equipos mecanicos.
3. Coherencia de OPEX electrico: 60 kW instalados.
4. Coherencia de conversion energetica: 1 kWh = 3.6 MJ.

---

## 8. Balance final de rendimiento por etapa

Base de calculo: 375 kg/h de proteina a la entrada.

| Etapa | Proteina de entrada (kg/h) | Proteina de salida (kg/h) | Rendimiento de etapa (%) | Rendimiento acumulado (%) |
|---|---:|---:|---:|---:|
| 1. Extraccion alcalina | 375.0 | 330.0 | 88.0 | 88.0 |
| 1.2 Separacion solido-liquido | 330.0 | 330.0 | 100.0 | 88.0 |
| 2. Neutralizacion y pasteurizacion | 330.0 | 330.0 | 100.0 | 88.0 |
| 3. Evaporacion (2 efectos) | 330.0 | 330.0 | 100.0 | 88.0 |
| 4. Precipitacion isoelectrica | 330.0 | 323.4 | 98.0 | 86.2 |
| 4.2 Centrifugacion | 323.4 | 323.4 | 100.0 | 86.2 |
| 5. Secado por atomizacion | 323.4 | 323.4 | 100.0 | 86.2 |

Conclusiones del balance por etapa:

1. La mayor perdida de proteina se concentra en la extraccion (12.0%).
2. La segunda perdida estructural ocurre en precipitacion (2.0% sobre la proteina disuelta).
3. Las etapas termicas y mecanicas se modelan sin perdida adicional de proteina en este caso base.

---

## 9. Analisis economico preliminar (CAPEX y OPEX)

### 9.1 Criterios economicos del caso base

- Moneda base de reporte: USD y Bs en paralelo.
- Tipo de cambio de referencia: 1 USD = 6.96 Bs.
- Horas de operacion anual: 8000 h/ano.
- Alcance OPEX: energia termica/electrica, agua/efluentes, reactivos de pH y materia prima.
- Alcance CAPEX: estimacion preliminar de equipos y factores de instalacion.

### 9.2 CAPEX preliminar

| Concepto | Costo (USD) | Costo (Bs) | Justificación técnica |
|---|---:|---:|---|
| Equipos directos de proceso | 1,960,000 | 13,641,600 | Suma de datasheets comerciales; equipos sanitarios AISI 316L |
| Instalación y montaje (30%) | 588,000 | 4,092,480 | Regla industrial estándar para equipos medianos 1–5 MW; incluye tuberías, soportes, conexiones |
| Ingeniería e indirectos (15%) | 294,000 | 2,046,240 | Porcentaje típico especializado en procesos alimentarios; incluye diseño ejecutivo, dibujos, coordinación |
| Contingencia preliminar (10%) | 284,200 | 1,978,032 | Cubre cambios menores, variabilidad de mercado y actividades no previstas en estimación |
| **CAPEX total estimado** | **3,126,200** | **21,758,352** | - |

### 9.3 OPEX anual preliminar

#### 9.3.1 Energia

- **Energia termica/utilidades:** $4704 - 60 = 4644\ \text{kW}$
- **Energia electrica:** $60\ \text{kW}$

**Costo anual asumido:**

- **Tarifa termica equivalente (vapor/combustible):** 0.035 USD/kWh *(Precio vapor industrial regional enero 2026; rango típico 0.030–0.045 USD/kWh según fuente y escala)*
- **Tarifa electrica industrial:** 0.10 USD/kWh *(Promedio industrial regional; puede variar 0.080–0.120 USD/kWh según contrato)*

$$
C_{termico} = 4644 \cdot 8000 \cdot 0.035 = 1{,}300{,}320\ \text{USD/ano}
$$

$$
C_{electrico} = 60 \cdot 8000 \cdot 0.10 = 48{,}000\ \text{USD/ano}
$$

Total energia:

$$
C_{energia} = 1{,}348{,}320\ \text{USD/ano}
$$

#### 9.3.2 Agua y efluentes

**Supuesto de consumo neto de agua:**

- 13.5 m³/h *(Incluye proceso + limpieza (CIP); típico 1.0–1.3 bases caudal para alimentos)*

$$
V_{agua,anual} = 13.5 \cdot 8000 = 108{,}000\ \text{m}^3/\text{ano}
$$

Con tarifa de 0.70 USD/m³ *(Precio agua industrial regional; típico 0.50–1.00 USD/m³ incluyendo descarga + tratamiento)*:

$$
C_{agua} = 108{,}000 \cdot 0.70 = 75{,}600\ \text{USD/ano}
$$

#### 7.3.3 Reactivos de pH

**Supuestos de consumo continuo:**

- **NaOH (50%):** 20 kg/h, costo 0.45 USD/kg *(Ajuste alcalino etapa 1 y redisolución post-precipitación; concentración típica 45–50%)*
- **HCl (33%):** 15 kg/h, costo 0.20 USD/kg *(Ajuste ácido etapa 4 precipitación iso-eléctrica; concentración industrial 30–35%)*

$$
C_{NaOH} = 20 \cdot 8000 \cdot 0.45 = 72{,}000\ \text{USD/ano}
$$

$$
C_{HCl} = 15 \cdot 8000 \cdot 0.20 = 24{,}000\ \text{USD/ano}
$$

$$
C_{reactivos} = 96{,}000\ \text{USD/ano}
$$

#### 9.3.4 Materia prima

**Supuesto:**

- **Soya:** 1 ton/h *(Base de cálculo; grano limpio con humedad ~12%, proteina 37.5% p/p)*
- **Precio medio:** 430 USD/ton *(Promedio mundial enero 2026; rango 380–480 USD/ton según origen/contrato)*

$$
M_{soya,anual} = 1 \cdot 8000 = 8000\ \text{ton/ano}
$$

$$
C_{soya} = 8000 \cdot 430 = 3{,}440{,}000\ \text{USD/ano}
$$

### 9.4 Resumen OPEX y costo unitario

| Concepto | Costo anual (USD) | Costo anual (Bs) |
|---|---:|---:|
| Energia (termica + electrica) | 1,348,320 | 9,384,307 |
| Agua y efluentes | 75,600 | 526,176 |
| Reactivos (NaOH + HCl) | 96,000 | 668,160 |
| Materia prima (soya) | 3,440,000 | 23,942,400 |
| **OPEX total anual** | **4,959,920** | **34,521,043** |

Produccion anual de referencia:

$$
M_{polvo,anual} = 364.6 \cdot 8000 = 2{,}916{,}800\ \text{kg/ano}
$$

$$
M_{prot,anual} = 323.4 \cdot 8000 = 2{,}587{,}200\ \text{kg/ano}
$$

Costo operativo unitario:

$$
c_{op,polvo} = \frac{4{,}959{,}920}{2{,}916{,}800} = 1.70\ \text{USD/kg polvo}
$$

$$
c_{op,prot} = \frac{4{,}959{,}920}{2{,}587{,}200} = 1.92\ \text{USD/kg proteina}
$$

En moneda local:

$$
c_{op,polvo} = 1.70 \cdot 6.96 = 11.83\ \text{Bs/kg polvo}
$$

$$
c_{op,prot} = 1.92 \cdot 6.96 = 13.36\ \text{Bs/kg proteina}
$$

### 9.5 Verificacion cruzada de potencia instalada vs OPEX

Potencia electrica instalada principal (criterio de seleccion comercial):

| Equipo electrico principal | Potencia instalada (kW) |
|---|---:|
| Agitador extraccion | 7.5 |
| Centrifugas post-lixiviacion (2 x 11) | 22.0 |
| Bomba sanitaria principal (lazo termico) | 2.2 |
| Bomba de vacio evaporador | 2.2 |
| Centrifuga post-precipitacion | 7.5 |
| Ventilador spray dryer | 7.5 |
| Molino + criba | 7.0 |
| Bombas auxiliares de transferencia | 4.1 |
| **Total electrico instalado** | **60.0 kW** |

Consistencia economica:

$$
C_{electrico} = 60\cdot8000\cdot0.10 = 48{,}000\ \text{USD/ano}\ \checkmark
$$

La potencia electrica instalada valida la actualizacion del OPEX energetico del caso base.

Nota de alcance:

- Este analisis economico es preliminar.
- No incluye depreciacion, VAN, TIR, impuestos, seguros ni financiamiento.

---

## 10. Resumen ejecutivo de variables

| Variable | Valor base | Comentario |
|---|---:|---|
| Grano de soya | 1000 kg/h | Base de diseno |
| Proteina de entrada | 375 kg/h | 37.5% p/p |
| Agua de extraccion | 12000 kg/h | Relacion 1:12 |
| Proteina extraida | 330 kg/h | 88% extraccion |
| Proteina recuperada final | 323.4 kg/h | 98% precipitacion |
| Polvo final | 364.6 kg/h | 5% humedad |
| Pureza de polvo | 88.7% | Coherente con aislado |
| Evaporacion (agua removida) | 9939 kg/h | Sistema de 2 efectos |
| Carga de evaporacion (proceso) | 6502 kW | Remocion latente total |
| Evaporacion (utilidad real) | 3906 kW | Con 2 efectos y 90% global |
| Energia total de utilidades | 4704 kW | Caso base realista |
| OPEX total anual | 4,959,920 USD | Incluye materia prima |
| CAPEX total estimado | 3,126,200 USD | Preliminar |

---

## 11. Presentacion de ingenieria: Datasheets de equipos

### 11.1 DS-101 Tanque de extraccion + agitador

| Campo | Especificacion |
|---|---|
| Tag | TK-101 + AG-101 |
| Servicio | Extraccion alcalina de proteina |
| Capacidad de proceso | 13.0 m3/h |
| Volumen nominal | 14 m3 |
| Geometria | Cilindrico vertical, D = 2.71 m, H util = 2.30 m |
| Dimensiones totales | H total casco = 3.30 m; huella con boquillas/plataforma aprox. 3.20 x 3.20 m |
| Material | AISI 316L |
| Agitador | PBT 6 palas, D impulsor = 1.08 m |
| Velocidad | 80 rpm |
| Potencia instalada | 7.5 kW |
| Instrumentacion minima | pH, T, nivel |

### 11.2 DS-102 Centrifugas post-lixiviacion

| Campo | Especificacion |
|---|---|
| Tag | CF-102A / CF-102B |
| Servicio | Separacion solido-liquido inicial |
| Configuracion | 2 x decantadora en paralelo |
| Capacidad unitaria | 8 m3/h |
| Capacidad total instalada | 16 m3/h |
| Tambor | D = 0.60 m, L = 1.60 m |
| Dimensiones por unidad | Envolvente aprox. 2.40 x 0.95 x 1.20 m |
| Factor G | 1800 g |
| Potencia instalada | 2 x 11 kW |
| Material en contacto | AISI 316L |
| Instrumentacion minima | rpm tambor, torque tornillo |

### 11.3 DS-201 Intercambiador de placas

| Campo | Especificacion |
|---|---|
| Tag | HX-201 |
| Servicio | Neutralizacion/pasteurizacion |
| Carga termica neta | 324 kW |
| Area diseno | 39.6 m2 |
| Numero de placas | 72-76 |
| Dimensiones del bastidor | Alto 2.20 m, ancho 0.90 m, largo 1.20 m |
| Material placas | AISI 316L |
| Juntas | EPDM grado alimentario |
| Caida de presion objetivo | <= 1.5 bar/lado |
| Bomba asociada | P-201, 14.3 m3/h, 22 m, 2.2 kW |
| Instrumentacion minima | T entrada/salida, DP |

### 11.4 DS-301 Evaporador doble efecto

| Campo | Especificacion |
|---|---|
| Tag | EV-301A / EV-301B |
| Servicio | Concentracion al vacio |
| Agua evaporada | 9939 kg/h |
| Carga de proceso | 6502 kW |
| Carga vapor vivo equivalente | 3515 kW |
| Carga utilidad real | 3906 kW |
| Area por efecto | 173.8 m2 |
| Area total | 347.6 m2 |
| Geometria de tubos | 25 mm ID, 3.0 m, 736 tubos/efecto |
| Dimensiones por efecto | Cuerpo vertical aprox. D = 1.20 m, H = 5.50 m |
| Sistema de vacio | Bomba 5 m3/min, 2.2 kW |
| Instrumentacion minima | vacio abs, % solidos salida |

### 11.5 DS-401 Centrifuga post-precipitacion

| Campo | Especificacion |
|---|---|
| Tag | CF-401 |
| Servicio | Separacion pasta proteica y suero |
| Caudal de proceso | 0.64 m3/h |
| Capacidad nominal | 3 m3/h |
| Tambor | D = 0.40 m, L = 1.20 m |
| Dimensiones del equipo | Envolvente aprox. 1.80 x 0.75 x 1.10 m |
| Factor G | 2200 g |
| Potencia instalada | 7.5 kW |
| Material en contacto | AISI 316L |
| Instrumentacion minima | rpm, torque, presion descarga |

### 11.6 DS-501 Spray dryer

| Campo | Especificacion |
|---|---|
| Tag | SD-501 |
| Servicio | Secado por atomizacion |
| Produccion de polvo | 364.6 kg/h |
| Carga termica proceso | 340 kW |
| Carga utilidad real | 378 kW |
| Camara | D = 3.0 m, H total = 6.5 m, V = 36.5 m3 |
| Dimensiones auxiliares | Ciclones gemelos aprox. D = 1.00 m, H = 2.80 m c/u |
| Atomizador | Disco 100 mm a 18000 rpm |
| Aire de proceso | 9000 m3/h |
| Potencia ventilador | 7.5 kW |
| Generador de calor | 400 kW nominal |
| Instrumentacion minima | T inlet/outlet, flujo aire, humedad polvo |

### 11.7 DS-601 Molino y criba

| Campo | Especificacion |
|---|---|
| Tag | ML-601 + CR-601 |
| Servicio | Ajuste y clasificacion granulometrica |
| Capacidad nominal | 500 kg/h |
| Dimensiones molino | 1.40 x 0.90 x 1.60 m |
| Dimensiones criba | 1.80 x 0.90 x 1.20 m |
| Malla objetivo | 100/200 mesh |
| Potencia molino | 5.5 kW |
| Potencia criba | 1.5 kW |
| Potencia real conjunta | 7.8 kW |
| Instrumentacion minima | corriente de motor, vibracion |

---

## 12. Presentacion de ingenieria: PFD narrativo y control

### 12.1 Secuencia operacional del proceso

1. **Recepcion y preparacion de alimentacion:** grano + agua de extraccion (1:12) se acondicionan para formar lodo de extraccion.
2. **Extraccion alcalina (TK-101/AG-101):** se controla pH 8.75 y 55 C para maximizar proteina disuelta.
3. **Separacion post-lixiviacion (CF-102A/B):** se separa okara humedo y extracto proteico.
4. **Neutralizacion y pasteurizacion (HX-201):** el extracto se ajusta y se lleva a 80 C por 22 s con recuperacion termica.
5. **Concentracion (EV-301A/B):** evaporacion en doble efecto para alcanzar 23% de solidos.
6. **Precipitacion isoelectrica:** ajuste de pH a zona de precipitacion para recuperar proteina.
7. **Centrifugacion final (CF-401):** separacion de pasta proteica con 50% de humedad.
8. **Secado por atomizacion (SD-501):** reduccion de humedad final a 5%.
9. **Molienda y clasificacion (ML-601/CR-601):** ajuste granulometrico final de producto.

### 12.2 Lazos de control recomendados

| Lazo | Variable controlada | Variable manipulada | Objetivo operativo |
|---|---|---|---|
| LC-101 | Nivel en TK-101 | Caudal de alimentacion | Evitar sobrellenado/vacio |
| pHC-101 | pH en TK-101 | Dosificacion NaOH/HCl | Mantener pH 8.75 |
| TC-101 | Temperatura extraccion | Servicio termico | Mantener 55 C |
| TC-201 | T salida HX-201 | Valvula de servicio termico | Garantizar pasteurizacion |
| dPC-201 | DeltaP en HX-201 | Velocidad de bomba/limpieza programada | Mantener transferencia estable |
| PC-301 | Presion absoluta EV-301 | Bomba de vacio | Mantener 0.40 bar abs |
| CC-301 | Solidos salida EV-301 | Carga termica/recirculacion | Sostener 23% p/p |
| TC-501 | T inlet/outlet SD-501 | Potencia de quemador y aire | Control de secado |
| MC-501 | Humedad de polvo | T aire y caudal de alimentacion | Producto <5% humedad |

### 12.3 Alarmas e interlocks minimos

1. Alta temperatura en tanque de extraccion (interlock de corte de calefaccion).
2. Alta presion diferencial en intercambiador (alarma de posible ensuciamiento hidraulico).
3. Perdida de vacio en evaporador (interlock de reduccion de carga termica).
4. Alta temperatura de salida en spray dryer (interlock de seguridad de producto/equipo).
5. Vibracion alta en centrifugas o criba (interlock de parada controlada).

### 12.4 PFD visual integrado del proceso

Para la representacion visual integrada del proceso completo (equipos, corrientes principales y nodo de operacion innovadora), ver:

- [PFD_Integrado.md](PFD_Integrado.md)

Resumen de integracion del PFD visual:

1. La operacion innovadora de OI se ubica entre separacion post-lixiviacion y evaporacion.
2. El permeado de OI se deriva a tanque de agua de servicio/CIP no critico.
3. El retentado de OI alimenta EV-301A/B para completar concentracion termica.
4. El resto del tren (precipitacion, centrifugacion final, secado, molienda y envasado) mantiene la secuencia del caso base.

---

## 13. Presentacion de ingenieria: Matriz de criticidad

### 13.1 Criticidad de variables operativas

| Variable | Etapa | Impacto en calidad | Impacto en rendimiento | Impacto en energia/costo | Criticidad |
|---|---|---|---|---|---|
| pH de extraccion | Etapa 1 | Alto | Alto | Medio | Alta |
| Temperatura de extraccion | Etapa 1 | Alto | Alto | Medio | Alta |
| Factor G centrifugas iniciales | Etapa 1.2 | Medio | Alto | Medio | Alta |
| T de pasteurizacion | Etapa 2 | Alto | Medio | Medio | Alta |
| DeltaP intercambiador | Etapa 2 | Medio | Medio | Alto | Alta |
| Presion de vacio | Etapa 3 | Alto | Alto | Alto | Alta |
| % solidos salida evaporador | Etapa 3 | Alto | Alto | Alto | Alta |
| pH de precipitacion | Etapa 4 | Alto | Alto | Medio | Alta |
| Humedad pasta centrifugada | Etapa 4.2 | Medio | Medio | Alto | Alta |
| T inlet/outlet spray dryer | Etapa 5 | Alto | Medio | Alto | Alta |
| Humedad final de polvo | Etapa 5 | Alto | Medio | Medio | Alta |
| Velocidad molino/criba | Etapa 5.2 | Medio | Bajo | Bajo | Media |

### 13.2 Priorizacion de seguimiento operativo

1. **Prioridad 1 (criticas):** pH extraccion, vacio evaporador, % solidos evaporador, T spray dryer, humedad final.
2. **Prioridad 2 (importantes):** DeltaP intercambiador, G de centrifugas, pH de precipitacion.
3. **Prioridad 3 (soporte):** variables de molienda y clasificacion final.

### 13.3 Análisis de Cuello de Botella (Teoría de Restricciones)

Basado en una alimentación de **1000 kg/h** de soya y una relación agua:soya de **1:12**, se identifican los siguientes niveles de utilización de los equipos diseñados:

1.  **Tanque de Almacenamiento de Agua (Etapa 0):** **100.0%** (Restricción Principal). El equipo está al límite de su capacidad operativa nominal.
2.  **Tanque de Extracción (Etapa 1):** **95.9%**. Operando cerca del límite crítico para el tiempo de residencia requerido (54 min).
3.  **Evaporador de Doble Efecto (Etapa 3):** **85.7%**. Capacidad adecuada con margen para variaciones menores.
4.  **Centrífugas Decantadoras (Etapa 4.2):** **82.8%**.
5.  **Secador Spray (Etapa 5):** **82.0%**.

**Conclusión:** El sistema está dictado por la capacidad de almacenamiento y preparación hídrica. Cualquier incremento en la alimentación por encima de 1000 kg/h requiere obligatoriamente el redimensionamiento del tanque de la Etapa 0 y el tanque de extracción.

### 13.4 Análisis de Sensibilidad Operativa

La producción final es altamente sensible a las variables de control en las etapas iniciales y de precipitación:

| Variable | Desviación | Impacto en Rendimiento (%) | Impacto en Producción (kg/h) |
|---|---|---|---|
| **pH de Extracción** | 8.75 -> 7.00 | -12.1% | -47.6 |
| **Temperatura Extraccion** | 55 C -> 30 C | -17.6% | -66.1 |
| **pH de Precipitación** | 4.5 -> 3.5 | -11.4% | -45.1 |

*Nota: Valores calculados mediante el motor de simulación del Gemelo Digital.*

---

## 14. Presentacion de ingenieria: Riesgos y mitigacion

### 14.1 Criterio de evaluacion

Se adopta una matriz cualitativa 3x3:

- Probabilidad: Baja (B), Media (M), Alta (A)
- Impacto: Bajo (B), Medio (M), Alto (A)
- Nivel de riesgo inicial: Bajo, Medio, Alto

### 14.2 Matriz de riesgos y mitigacion

| Riesgo | Causa principal | Consecuencia | Prob. | Impacto | Nivel inicial | Mitigacion preventiva | Mitigacion correctiva | Indicador de monitoreo | Responsable |
|---|---|---|---|---|---|---|---|---|---|
| Desvio de pH en extraccion | Dosificacion inestable NaOH/HCl | Menor extraccion y calidad variable | M | A | Alto | Lazo pHC-101 con calibracion semanal | Ajuste manual y recirculacion controlada | pH en TK-101 | Jefe de proceso |
| Perdida de vacio en evaporador | Falla bomba de vacio o fugas | Menor concentracion y mayor consumo energetico | M | A | Alto | Mantenimiento preventivo + prueba de estanqueidad | Reducir carga termica e aislar tren | Presion abs EV-301 | Supervisor utilidades |
| % solidos fuera de especificacion | Control termico/recirculacion inadecuado | Sobrecarga en secador y desvio de humedad final | M | A | Alto | Lazo CC-301 con setpoint 23% | Reprocesar corriente fuera de especificacion | % solidos salida evaporador | Operador evaporacion |
| DeltaP alto en intercambiador | Fouling hidraulico por solidos finos | Caida de transferencia y riesgo de parada | M | M | Medio | Monitoreo dPC-201 y limpieza programada | Bypass temporal + CIP extraordinario | DeltaP HX-201 | Supervisor mantenimiento |
| Alta T salida spray dryer | Exceso de carga termica/aire inestable | Degradacion de producto y riesgo operativo | B | A | Alto | Control TC-501 e interlock de alta T | Corte de quemador y purga de camara | T outlet SD-501 | Operador secado |
| Humedad final >5% | Variacion alimentacion o secado insuficiente | Riesgo microbiologico y rechazo de lote | M | A | Alto | Monitoreo MC-501 por lote | Re-secado o bloqueo de liberacion | Humedad final (%) | Aseguramiento de calidad |
| Falla de centrifuga post-lixiviacion | Desgaste mecanico/taponamiento | Perdida de capacidad y acumulacion en linea | M | M | Medio | Mantenimiento por horas de servicio | Redireccion a equipo paralelo | Vibracion y torque | Mantenimiento mecanico |
| Falla de centrifuga post-precipitacion | Operacion fuera de curva | Aumento de humedad de pasta y costo de secado | M | M | Medio | Control de carga y limpieza interna | Reprocesar pasta en segundo paso | Humedad de pasta (%) | Jefe de turno |
| Variacion precio de soya | Mercado internacional/estacionalidad | Reduccion de margen operativo | A | A | Alto | Contratos semestrales y compras escalonadas | Ajuste de precio de venta y mezcla de proveedores | USD/ton soya | Compras + finanzas |
| Precio de venta bajo escenario objetivo | Presion comercial/competencia | Caida de utilidad operativa | M | A | Alto | Politica de precio minimo > USD 1.70/kg | Reenfocar canal y formato comercial | Precio neto USD/kg | Comercial |
| Indisponibilidad energetica | Fallas red/equipo termico | Paradas no programadas y perdida de lote | B | A | Alto | Redundancia minima y plan de contingencia | Parada segura y arranque secuencial | Horas de indisponibilidad | Utilidades |
| Incumplimiento de inocuidad | Desviacion de T/humedad o higiene | Rechazo de lote y riesgo reputacional | B | A | Alto | HACCP, limpieza y control microbiologico | Retencion y trazabilidad de lote | UFC, aw, humedad | Calidad |

### 14.3 Plan de accion priorizado

1. **Corto plazo (0-3 meses):** formalizar limites operativos, responsables por indicador y frecuencia de seguimiento diaria/turno.
2. **Mediano plazo (3-6 meses):** fortalecer mantenimiento preventivo de centrifugas, vacio y secador; estandarizar rutinas CIP.
3. **Largo plazo (6-12 meses):** consolidar estrategia comercial de precio minimo, contratos de soya y tablero integral de riesgos.

### 14.4 Riesgos economicos clave vinculados a ventas

1. Si el precio de venta cae por debajo de USD 1.70/kg, el proyecto entra en zona de no equilibrio operativo.
2. Si el costo de soya sube sin ajuste de precio de venta, el margen operativo se reduce de forma directa.
3. La mitigacion economica principal es gestionar simultaneamente precio de compra (soya) y precio neto de venta del aislado.

---

## 15. Especificaciones de envasado y estrategia de entrega

### 15.1 Especificaciones de envasado final

| Parametro | Especificacion de diseno | Criterio tecnico |
|---|---|---|
| Tipo de empaque primario | Bolsa laminada tricapa (PE/Al/PEBD) | Alta barrera a humedad, oxigeno y luz |
| Peso neto por unidad | 20 kg (formato industrial) | Manejo logistico y trazabilidad por lote |
| Sistema de cierre | Termosellado continuo, sello >= 4 mm | Integridad mecanica en transporte |
| Empaque secundario | Saco externo kraft multicapa | Proteccion mecanica adicional |
| Inertizacion | Purga opcional con N2 en linea de llenado | Reduce oxidacion y mantiene calidad |

### 15.2 Criterios de calidad y trazabilidad de lote

Campos minimos en etiqueta:

- Codigo de lote (fecha-turno-secuencia)
- Fecha de produccion y vencimiento
- % proteina y % humedad
- Peso neto y condiciones de almacenamiento

Criterio operativo de liberacion:

1. Humedad final <= 5.0%.
2. Integridad de sello conforme a inspeccion de linea.
3. Registro de lote completo (materia prima -> producto final).

### 15.3 Almacenamiento en planta y despacho

| Variable | Especificacion | Motivo |
|---|---|---|
| Temperatura de almacen | 15-25 C | Estabilidad fisicoquimica |
| Humedad relativa | <= 60% | Evitar aglomeracion del polvo |
| Rotacion | FIFO | Minimizar envejecimiento de inventario |
| Estiba | Pallets con separacion de piso y pared | Control sanitario y ventilacion |

### 15.4 Estrategia de entrega del producto final

1. Consolidar despacho por lotes trazables con COA (certificado de analisis).
2. Priorizar transporte cubierto y seco para preservar humedad objetivo.
3. Aplicar inspeccion de recepcion en cliente para validar integridad de empaque y etiqueta.
4. Mantener canal de retroalimentacion lote-cliente para gestion rapida de no conformidades.

---

## 16. Referencias internas

- Formulario.md
- Planteamiento.md
- Variables de operacion.md
- Sintesis.md
- PFD_Integrado.md
- Implementacion_Hidraulica.md

---

## 17. Anexo de bibliografia consultada

Este anexo consolida las fuentes tecnicas consultadas para sustentar criterios de proceso, propiedades de materia prima, supuestos operativos y contexto economico preliminar.

### 17.1 Fuentes internas del repositorio

1. `proyecto_final_unitarios/docs/Variables de operacion.md`  
  Base de variables operativas por etapa, rangos de pH, temperatura y caudales de referencia.
2. `proyecto_final_unitarios/docs/Formulario.md`  
  Apoyo de ecuaciones y relacion de calculos usados en balances y diseno preliminar.
3. `proyecto_final_unitarios/docs/Planteamiento.md`  
  Alcance del proyecto, criterios de entrega y estructura de objetivos.
4. `proyecto_final_unitarios/docs/Sintesis.md`  
  Consolidacion narrativa para coherencia tecnica del caso base.
5. `proyecto_final_unitarios/docs/PFD_Integrado.md`  
  Representacion visual del tren de proceso y nodo de innovacion OI.

### 17.2 Fuentes tecnicas web consultadas

1. FAO. *Technology of Production of Edible Flours and Protein Products from Soybeans* (Cap. 4).  
  URL: https://www.fao.org/3/t0532e/t0532e05.htm  
  Uso en el documento: definiciones de productos de soya, composicion tipica y contexto de procesamiento de derivados proteicos.

2. Wikipedia. *Soy protein*.  
  URL: https://en.wikipedia.org/wiki/Soy_protein  
  Uso en el documento: marco de proceso para aislado de soya (extraccion acuosa/alcalina, acidificacion en zona isolectrica, separacion y secado).

3. Wikipedia. *Soybean*.  
  URL: https://en.wikipedia.org/wiki/Soybean  
  Uso en el documento: referencia general de composicion de soya y contexto de materia prima para contrastar el supuesto de proteina de entrada.

4. Wikipedia. *Reverse osmosis*.  
  URL: https://en.wikipedia.org/wiki/Reverse_osmosis  
  Uso en el documento: respaldo conceptual para la etapa innovadora de OI, su integracion previa a evaporacion y rangos de presion en aplicaciones de agua salobre.

5. Wikipedia. *Multiple-effect evaporator*.  
  URL: https://en.wikipedia.org/wiki/Multiple-effect_evaporator  
  Uso en el documento: fundamento de evaporacion en multiples efectos y recuperacion de energia termica entre efectos.

6. NIST (National Institute of Standards and Technology). *Unit Conversion*.  
  URL: https://www.nist.gov/pml/owm/metric-si/unit-conversion  
  Uso en el documento: consistencia de conversion de unidades energeticas y trazabilidad metodologica de conversiones.

7. World Bank Group. *Commodity Markets* (Pink Sheet / Commodity Markets Outlook).  
  URL: https://www.worldbank.org/en/research/commodity-markets  
  Uso en el documento: referencia de contexto para supuestos economicos preliminares de precios de commodities (incluida materia prima agricola).

### 17.3 Criterio de calidad de fuentes y trazabilidad

1. Prioridad alta: organismos tecnicos/institucionales (FAO, NIST, World Bank).
2. Prioridad media: entradas de referencia enciclopedica usadas solo como soporte contextual y no como unica base de diseno.
3. Prioridad interna: documentos del repositorio para coherencia de supuestos y continuidad academica del proyecto.
4. Fecha de consulta web para todas las URLs anteriores: **18 marzo 2026**.

---

**Version:** 1.6  
**Fecha:** Marzo 2026  
**Caso base:** Produccion de proteina aislada de soya a 1 ton/h de grano  
**Notas de modelado:** eficiencia global 90%, evaporacion en 2 efectos, sin ensuciamiento, inclusion de OI preliminar, especificaciones de envasado/entrega y anexo bibliografico web + repositorio.
