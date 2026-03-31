# Informe Final Consolidado
## Produccion de proteina aislada de soya (caso base integrado con OI)

Fecha: Marzo 2026

---

## Indice

1. [Objetivo y alcance](#1-objetivo-y-alcance)
2. [Fuentes y criterio de consistencia](#2-fuentes-y-criterio-de-consistencia)
3. [Base de calculo y supuestos](#3-base-de-calculo-y-supuestos)
4. [Calculos del proceso por etapas](#4-calculos-del-proceso-por-etapas)
5. [Resultados del caso base integrado con OI](#5-resultados-del-caso-base-integrado-con-oi)
6. [Verificaciones globales](#6-verificaciones-globales)
7. [Analisis economico preliminar](#7-analisis-economico-preliminar)
8. [Control, criticidad y riesgos](#8-control-criticidad-y-riesgos)
9. [Especificaciones de producto, envasado y entrega](#9-especificaciones-de-producto-envasado-y-entrega)
10. [Recomendaciones implementables](#10-recomendaciones-implementables)
11. [Conclusiones](#11-conclusiones)
12. [Bibliografia consultada](#12-bibliografia-consultada)
13. [Anexos visuales de planta y equipos](#13-anexos-visuales-de-planta-y-equipos)

---

## 1. Objetivo y alcance

Consolidar en un solo documento tecnico todos los calculos del proyecto final de produccion de proteina aislada de soya, con trazabilidad de supuestos, balances, energia, economia y criterios de control.

Alcance de esta version:

- Caso base de 1 ton/h de grano de soya.
- Integracion de preconcentracion por osmosis inversa (OI) en el tren principal.
- Inclusion de calculos de etapas 0, 1, 1.2, 2, 2C (OI), 3, 4, 4.2, 5, 5.2 y 6.
- Integracion de analisis preliminar CAPEX/OPEX.
- Inclusion de indice y referencias bibliograficas.

Fuera de alcance:

- Corridas de simulacion adicionales.
- Pruebas experimentales nuevas.
- Fuentes externas no listadas en la documentacion del proyecto final.

---

## 2. Fuentes y criterio de consistencia

Criterio de precedencia para valores numericos:

1. Documento maestro de calculos del proyecto final (fuente maestra).
2. Formulario consolidado de ecuaciones de diseno.
3. Implementacion hidraulica consolidada del proceso.
4. Especificaciones de variables de operacion.
5. Diagrama de flujo integrado del proceso.
6. Informe tecnico simplificado de referencia.

Regla de consolidacion aplicada:

- Si existe discrepancia, se conserva el valor de la fuente maestra.
- Cuando OI altera energia/costos, se recalcula con ecuaciones ya presentes en el proyecto.

---

## 3. Base de calculo y supuestos

### 3.1 Alimentacion

| Variable | Valor |
|---|---:|
| Grano de soya | 1000 kg/h |
| Proteina en grano | 37.5% p/p |
| Proteina de entrada | 375 kg/h |
| Agua de extraccion (1:12) | 12000 kg/h |

### 3.2 Supuestos operativos clave

| Variable | Valor |
|---|---:|
| Eficiencia de extraccion (Etapa 1) | 88% |
| Recuperacion proteica en precipitacion (Etapa 4) | 98% |
| Humedad de pasta post-centrifuga | 50% |
| Humedad final de polvo | 5% |
| pH de extraccion | 8.75 |
| Temperatura de extraccion | 55 C |
| Pasteurizacion | 80 C por 22 s |
| Evaporacion | Doble efecto |
| Economia de vapor | 1.85 kg/kg |
| Eficiencia global de utilidades/equipos | 90% |

### 3.3 Integracion OI adoptada en este informe

| Parametro | Valor |
|---|---:|
| Flujo a OI | 12400 kg/h |
| Recuperacion de permeado | 25% |
| Permeado | 3100 kg/h |
| Retentado a evaporacion | 9300 kg/h |
| Potencia electrica OI (referencia) | 15-20 kW |
| Potencia usada para calculo economico | 18 kW |

---

## 4. Calculos del proceso por etapas

### 4.0 Fluidograma integrado completo

El fluidograma integral del proceso, incluyendo la integracion de OI y las corrientes laterales, se incorpora como figura embebida para lectura directa dentro del informe.

![Fluidograma integrado del proceso de proteina aislada de soya](../media/images/Planta%20industrial%20soja.png)

Lectura operativa de la figura:


### 4.1 Etapa 0: captacion, tanque de agua y bombeo

Valores empleados:

- rho_agua = 1000 kg/m3
- g = 9.81 m/s2
- Q = 0.00333 m3/s
- H = 10.7 m
- eta_bomba = 0.65
- eta_motor = 0.90

Caudal de agua:

$$
\dot{V}_{agua} = 12000\ \text{L/h} = 12.0\ \text{m}^3/\text{h} = 0.00333\ \text{m}^3/\text{s}
$$

Volumen de tanque con reserva 20%:

$$
V_{tanque} = 12.0\cdot1.20 = 14.4\ \text{m}^3
$$

Capacidad nominal: 15 m3.

Potencia hidraulica de referencia:

$$
P_h = \rho gQH = 1000\cdot9.81\cdot0.00333\cdot10.7 = 0.35\ \text{kW}
$$

Potencia de motor:

$$
P_{motor} = \frac{0.35}{0.65\cdot0.90} = 0.60\ \text{kW}
$$

Seleccion comercial: bomba sanitaria de 1.5 kW.

### 4.2 Etapa 1: extraccion alcalina

Valores empleados:

- m_prot_entrada = 375 kg/h
- eficiencia_extraccion = 0.88
- m_lodo_total = 13000 kg/h

Proteina extraida:

$$
\dot{m}_{prot,ext} = 375\cdot0.88 = 330\ \text{kg/h}
$$

Proteina no extraida (okara):

$$
\dot{m}_{prot,okara} = 375 - 330 = 45\ \text{kg/h}
$$

Flujo total de lodo:

$$
\dot{m}_{lodo} = 1000 + 12000 = 13000\ \text{kg/h}
$$

### 4.3 Etapa 1.2: separacion solido-liquido

Valores empleados:

- m_entrada_separacion = 13000 kg/h
- m_extracto = 12400 kg/h
- m_okara_humedo = 600 kg/h

Balances adoptados:

- Extracto liquido: 12400 kg/h
- Okara humedo: 600 kg/h

Verificacion:

$$
12400 + 600 = 13000\ \text{kg/h}
$$

Configuracion de equipo:

- 2 centrifugas en paralelo, 8 m3/h por unidad.
- Capacidad instalada total: 16 m3/h.

### 4.4 Etapa 2: neutralizacion y pasteurizacion

Valores empleados:

- m_flujo = 12400 kg/h
- Cp_mezcla = 3.8 kJ/(kg.K)
- DeltaT = 55 K
- recuperacion_termica = 0.55
- eficiencia_utilidades = 0.90
- U_global = 500 W/(m2.K)
- LMTD = 18 K

Carga termica bruta:

$$
Q_{bruto} = \dot{m}C_p\Delta T = 12400\cdot3.8\cdot55 = 2{,}592{,}400\ \text{kJ/h} = 720\ \text{kW}
$$

Con recuperacion de 55%:

$$
Q_{neto} = 720\cdot(1-0.55) = 324\ \text{kW}
$$

Consumo real (90%):

$$
Q_{util,et2} = \frac{324}{0.90} = 360\ \text{kW}
$$

Area de intercambiador (U=500 W/m2K, LMTD=18 K):

$$
A = \frac{324000}{500\cdot18} = 36.0\ \text{m}^2
$$

Con margen de 10%:

$$
A_{dis} = 39.6\ \text{m}^2
$$

### 4.5 Etapa 2C: preconcentracion por osmosis inversa (OI)

Valores empleados:

- m_alimentacion_OI = 12400 kg/h
- recuperacion_OI = 0.25

Permeado y retentado:

$$
\dot{m}_{perm} = 12400\cdot0.25 = 3100\ \text{kg/h}
$$

$$
\dot{m}_{ret} = 12400 - 3100 = 9300\ \text{kg/h}
$$

La OI reduce carga termica posterior al remover agua por via de membrana antes del evaporador.

### 4.6 Etapa 3: evaporacion al vacio en doble efecto (con OI)

Valores empleados:

- m_evap_base_sin_OI = 9939 kg/h
- m_removida_OI = 3100 kg/h
- lambda_agua = 2355 kJ/kg
- economia_vapor = 1.85 kg/kg
- eficiencia_utilidades = 0.90

Del caso base documental sin OI:

- Agua evaporada: 9939 kg/h
- Carga de proceso: 6502 kW

Con OI integrada (segun calculo preliminar del proyecto):

$$
\dot{m}_{evap,nuevo} = 9939 - 3100 = 6839\ \text{kg/h}
$$

Con $\lambda = 2355\ \text{kJ/kg}$:

$$
Q_{evap,proceso,nuevo} = \frac{6839\cdot2355}{3600} = 4474\ \text{kW}
$$

Vapor vivo equivalente con economia 1.85:

$$
Q_{evap,vapor,nuevo} = \frac{4474}{1.85} = 2418\ \text{kW}
$$

Consumo de utilidad real (90%):

$$
Q_{evap,util,nuevo} = \frac{2418}{0.90} = 2687\ \text{kW}
$$

### 4.7 Etapa 4: precipitacion isoelectrica

Valores empleados:

- m_proteina_extraida = 330 kg/h
- eficiencia_precipitacion = 0.98
- solidos_coprecipitados = 23 kg/h

Proteina precipitada:

$$
\dot{m}_{prot,prec} = 330\cdot0.98 = 323.4\ \text{kg/h}
$$

Coprecipitacion de otros solidos:

$$
\dot{m}_{solidos,pasta} = 323.4 + 23 = 346.4\ \text{kg/h}
$$

### 4.8 Etapa 4.2: centrifugacion post-precipitacion

Valores empleados:

- m_solidos_pasta = 346.4 kg/h
- humedad_pasta = 0.50

Con humedad de pasta de 50%:

$$
\dot{m}_{pasta} = \frac{346.4}{1-0.50} = 692.8\ \text{kg/h}
$$

### 4.9 Etapa 5: secado por atomizacion

Valores empleados:

- m_solidos_secos = 346.4 kg/h
- humedad_final_objetivo = 0.05
- Q_secado_proceso = 340 kW
- eficiencia_utilidades = 0.90

Flujo de polvo final con 5% humedad:

$$
\dot{m}_{polvo} = \frac{346.4}{1-0.05} = 364.6\ \text{kg/h}
$$

Agua evaporada en secador:

$$
\dot{m}_{H2O,sec} = 692.8 - 364.6 = 328.2\ \text{kg/h}
$$

Carga de proceso de secado: 340 kW.

Consumo real (90%):

$$
Q_{sec,util} = \frac{340}{0.90} = 378\ \text{kW}
$$

### 4.10 Etapa 5.2 y 6: molienda/tamizado y envasado

Valores empleados:

- caudal_polvo = 364.6 kg/h
- rango_granulometria = 100-200 mesh
- potencia_molienda_tamizado = 7.8 kW

- Molienda + tamizado: 364.6 kg/h de polvo final a 100-200 mesh.
- Envasado: formato 20-25 kg, con trazabilidad por lote.

Potencia real conjunta molienda+tamizado (referencia): 7.8 kW.

### 4.11 Balance final de rendimiento por etapa

Base de calculo: 375 kg/h de proteina de entrada.

| Etapa | Proteina entrada (kg/h) | Proteina salida (kg/h) | Rendimiento de etapa (%) | Rendimiento acumulado (%) |
|---|---:|---:|---:|---:|
| 1. Extraccion alcalina | 375.0 | 330.0 | 88.0 | 88.0 |
| 1.2 Separacion solido-liquido | 330.0 | 330.0 | 100.0 | 88.0 |
| 2. Neutralizacion/pasteurizacion | 330.0 | 330.0 | 100.0 | 88.0 |
| 2C. Preconcentracion OI | 330.0 | 330.0 | 100.0 | 88.0 |
| 3. Evaporacion | 330.0 | 330.0 | 100.0 | 88.0 |
| 4. Precipitacion isoelectrica | 330.0 | 323.4 | 98.0 | 86.2 |
| 4.2 Centrifugacion | 323.4 | 323.4 | 100.0 | 86.2 |
| 5. Secado por atomizacion | 323.4 | 323.4 | 100.0 | 86.2 |

### 4.12 Dimensionamiento clave de equipos

| Equipo | Servicio | Capacidad de diseno | Parametro principal |
|---|---|---|---|
| TK-101 + AG-101 | Extraccion alcalina | 13.0 m3/h | V = 14 m3, agitador 7.5 kW |
| CF-102A/B | Separacion post-lixiviacion | 2 x 8 m3/h | Factor G = 1800 |
| HX-201 | Neutralizacion/pasteurizacion | 324 kW netos | A = 39.6 m2 |
| EV-301A/B | Evaporacion doble efecto | 6839 kg/h de agua evaporada (con OI) | A total base instalada = 347.6 m2 |
| CF-401 | Post-precipitacion | 3 m3/h nominal | Factor G = 2200 |
| SD-501 | Secado por atomizacion | 364.6 kg/h de polvo | Volumen camara = 36.5 m3 |
| ML-601 + CR-601 | Molienda y tamizado | 500 kg/h | Potencia conjunta real = 7.8 kW |

### 4.13 Resumen hidraulico por tramos

Valores integrados desde la implementacion hidraulica y el calculo maestro.

| Tramo | Caudal (m3/h) | Diametro nominal | Velocidad (m/s) | TDH de referencia |
|---|---:|---|---:|---:|
| Alimentacion a extraccion | 13.0 | DN80 (3") | 0.76 | 18 m |
| Extracto a pasteurizacion | 12.4 | DN65 (2.5") | 1.11 | 22 m |
| Pasteurizado a evaporador | 12.4 | DN65 (2.5") | 1.11 | 28 m |
| Concentrado a precipitacion | 2.46 | DN40 (1.5") | 0.52 | 24 m |
| Pasta a secado | 0.64 | DN32 (1.25") | 0.18 | 30 m |

Criterio de rango de velocidad usado en diseno: 0.3 a 1.8 m/s para lineas de proceso alimentario.

---

## 5. Resultados del caso base integrado con OI

### 5.1 Produccion y calidad

| Indicador | Valor |
|---|---:|
| Polvo final | 364.6 kg/h |
| Proteina pura recuperada | 323.4 kg/h |
| Pureza de polvo | 88.7% |
| Humedad final | 5.0% |
| Rendimiento proteico global | 86.2% |

### 5.2 Energia total integrada con OI

Bloques energeticos consolidados:

| Bloque | Potencia (kW) |
|---|---:|
| Pasteurizacion (utilidad real) | 360 |
| Evaporacion con OI (utilidad real) | 2687 |
| Secado por atomizacion (utilidad real) | 378 |
| Equipos mecanicos base | 60 |
| Bomba OI (electrica) | 18 |
| **Total caso integrado OI** | **3503** |

Comparacion contra caso base sin OI (4704 kW):

$$
\Delta E = 4704 - 3503 = 1201\ \text{kW}
$$

Reduccion relativa:

$$
\%\,reduccion = \frac{1201}{4704}\cdot100 = 25.5\%
$$

---

## 6. Verificaciones globales

### 6.1 Balance global de masa

Suma de salidas principales (con OI integrada):

- Permeado OI: 3100 kg/h
- Condensado de evaporador: 6839 kg/h
- Okara humedo: 600 kg/h
- Suero residual: 1769 kg/h
- Polvo final: 364.6 kg/h
- Vapor removido en secado: 328.2 kg/h

Suma:

$$
3100 + 6839 + 600 + 1769 + 364.6 + 328.2 = 13000.8\ \text{kg/h}
$$

Error de cierre:

$$
\frac{13000.8 - 13000}{13000}\cdot100 = 0.006\%
$$

Criterio: cierre aceptable (error &lt;= 0.5%).

### 6.2 Indicadores especificos de energia

Con 3503 kW:

$$
e_{esp,prot} = \frac{3503}{323.4} = 10.8\ \text{kWh/kg proteina}
$$

$$
e_{esp,polvo} = \frac{3503}{364.6} = 9.6\ \text{kWh/kg polvo}
$$

En MJ/kg:

$$
e_{esp,prot} = 10.8\cdot3.6 = 38.9\ \text{MJ/kg proteina}
$$

$$
e_{esp,polvo} = 9.6\cdot3.6 = 34.6\ \text{MJ/kg polvo}
$$

---

## 7. Analisis economico preliminar

### 7.1 CAPEX (fuente maestra)

| Concepto | Costo (USD) |
|---|---:|
| Equipos directos de proceso | 1,960,000 |
| Instalacion y montaje (30%) | 588,000 |
| Ingenieria e indirectos (15%) | 294,000 |
| Contingencia preliminar (10%) | 284,200 |
| **CAPEX total estimado** | **3,126,200** |

### 7.2 OPEX anual base documental (sin ajuste OI)

| Concepto | Costo anual (USD) |
|---|---:|
| Energia (termica + electrica) | 1,348,320 |
| Agua y efluentes | 75,600 |
| Reactivos (NaOH + HCl) | 96,000 |
| Materia prima (soya) | 3,440,000 |
| **OPEX total** | **4,959,920** |

### 7.3 Ajuste energetico preliminar con OI integrada

Tarifas del proyecto:

- Tarifa termica equivalente: 0.035 USD/kWh
- Tarifa electrica industrial: 0.10 USD/kWh
- Horas anuales: 8000 h/ano

Costo termico anual con OI (3425 kW termicos):

$$
C_{term,OI} = 3425\cdot8000\cdot0.035 = 959{,}000\ \text{USD/ano}
$$

Costo electrico anual con OI (60 + 18 = 78 kW):

$$
C_{elec,OI} = 78\cdot8000\cdot0.10 = 62{,}400\ \text{USD/ano}
$$

Nuevo costo de energia:

$$
C_{energia,OI} = 959{,}000 + 62{,}400 = 1{,}021{,}400\ \text{USD/ano}
$$

Ahorro energetico anual frente al caso base:

$$
\Delta C_{energia} = 1{,}348{,}320 - 1{,}021{,}400 = 326{,}920\ \text{USD/ano}
$$

OPEX anual ajustado preliminar:

$$
OPEX_{OI} = 4{,}959{,}920 - 326{,}920 = 4{,}633{,}000\ \text{USD/ano}
$$

Costo operativo unitario ajustado:

$$
c_{op,polvo,OI} = \frac{4{,}633{,}000}{2{,}916{,}800} = 1.59\ \text{USD/kg polvo}
$$

$$
c_{op,prot,OI} = \frac{4{,}633{,}000}{2{,}587{,}200} = 1.79\ \text{USD/kg proteina}
$$

Nota: este ajuste OI conserva la base de materia prima y reactivos del caso original; solo modifica el bloque energetico con datos ya documentados.

### 7.4 Escenarios de precio de venta

Produccion anual de polvo:

$$
M_{polvo,anual} = 364.6\cdot8000 = 2{,}916{,}800\ \text{kg/ano}
$$

Precio de equilibrio del caso base documental:

$$
P_{eq} = \frac{4{,}959{,}920}{2{,}916{,}800} = 1.70\ \text{USD/kg}
$$

Escenarios de ventas (con OPEX base documental):

| Escenario | Precio venta (USD/kg) | Ingreso anual (USD) | Utilidad operativa (USD) | Margen operativo (%) |
|---|---:|---:|---:|---:|
| Conservador | 2.20 | 6,416,960 | 1,457,040 | 22.7 |
| Base | 2.60 | 7,583,680 | 2,623,760 | 34.6 |
| Alto | 3.00 | 8,750,400 | 3,790,480 | 43.3 |

Para referencia complementaria, con OPEX ajustado OI (4,633,000 USD/ano), el precio de equilibrio preliminar es:

$$
P_{eq,OI} = \frac{4{,}633{,}000}{2{,}916{,}800} = 1.59\ \text{USD/kg}
$$

---

## 8. Control, criticidad y riesgos

### 8.1 Variables de control prioritarias

| Variable | Etapa | Criticidad |
|---|---|---|
| pH de extraccion | 1 | Alta |
| Temperatura de extraccion | 1 | Alta |
| Presion transmembrana OI | 2C | Alta |
| SDI y flujo de membrana | 2C | Alta |
| Vacio en evaporador | 3 | Alta |
| Solidos salida evaporador | 3 | Alta |
| pH de precipitacion | 4 | Alta |
| Humedad final de polvo | 5 | Alta |

### 8.2 Riesgos operativos principales

1. Desvio de pH en extraccion: reduce rendimiento proteico.
2. Ensuciamiento de membranas OI: reduce permeado y aumenta consumo.
3. Perdida de vacio en evaporador: incrementa demanda termica.
4. Humedad final &gt; 5%: riesgo de calidad y rechazo de lote.
5. Variacion de precio de soya o venta: impacto directo en margen operativo.

---

## 9. Especificaciones de producto, envasado y entrega

### 9.1 Especificacion de producto final

| Parametro | Especificacion |
|---|---|
| Producto | Proteina aislada en polvo |
| Caudal final | 364.6 kg/h |
| Pureza | 88.7% |
| Humedad final | &lt;= 5.0% |
| Granulometria | 100-200 mesh |

### 9.2 Envasado

| Parametro | Especificacion |
|---|---|
| Empaque primario | Bolsa laminada tricapa (PE/Al/PEBD) |
| Formato | 20 kg por bolsa |
| Cierre | Termosellado continuo |
| Identificacion | Codigo de lote, fecha, humedad y % proteina |

### 9.3 Entrega y almacenamiento

- Temperatura de almacen: 15-25 C.
- Humedad relativa: &lt;= 60%.
- Rotacion: FIFO.
- Despacho por lote con trazabilidad y certificado de analisis.

---

## 10. Recomendaciones implementables

### 10.1 Horizonte 0-3 meses

| ID | Categoria | Objetivo | Accion recomendada | Indicador de seguimiento | Responsable sugerido |
|---|---|---|---|---|---|
| R-01 | Operativa | Mantener rendimiento de extraccion | Calibrar control de pH de extraccion en inicio de turno y registrar desviaciones | pH 8.7-8.9 en 95% de lotes | Operaciones |
| R-02 | Operativa | Evitar inestabilidad termica | Implementar checklist diario de vacio y temperatura en evaporador | Vacio en rango operativo >= 98% del tiempo | Operaciones / Mantenimiento |
| R-03 | Energetica | Verificar ahorro esperado por OI | Instalar submedicion separada en OI y evaporador | kWh por bloque y reduccion real vs base | Ingenieria de procesos |
| R-04 | Calidad e inocuidad | Reducir riesgo microbiologico | Formalizar plan HACCP para zonas humedas y punto de secado | Cero no conformidades criticas en auditoria interna | Calidad |

### 10.2 Horizonte 3-6 meses

| ID | Categoria | Objetivo | Accion recomendada | Indicador de seguimiento | Responsable sugerido |
|---|---|---|---|---|---|
| R-05 | Escalamiento y piloto | Confirmar desempeno real de OI | Ejecutar piloto corto con seguimiento de flujo, rechazo proteico y fouling | Recuperacion OI 25-30% y retencion proteica >= objetivo | Ingenieria de procesos |
| R-06 | Operativa | Reducir paros por ensuciamiento | Establecer protocolo CIP por condicion (no solo por calendario) | Frecuencia de CIP optimizada sin perdida de calidad | Mantenimiento |
| R-07 | Economica | Mejorar margen operativo | Definir bandas de compra de soya y ventana de cobertura de precio | Variacion de costo de materia prima controlada | Finanzas / Compras |
| R-08 | Calidad e inocuidad | Robustecer especificacion comercial | Ejecutar pruebas funcionales (hidratacion, emulsificacion, gelificacion) del polvo | Cumplimiento de especificacion funcional por lote | Calidad / I+D |

### 10.3 Horizonte 6-12 meses

| ID | Categoria | Objetivo | Accion recomendada | Indicador de seguimiento | Responsable sugerido |
|---|---|---|---|---|---|
| R-09 | Energetica | Reconfigurar uso de vapor | Evaluar migracion de evaporador a esquema de menor demanda termica post-OI | Reduccion adicional de kW termicos por kg de polvo | Ingenieria de procesos |
| R-10 | Economica | Consolidar estrategia de precio de venta | Actualizar trimestralmente punto de equilibrio y margen por escenario | Margen operativo sostenido sobre objetivo | Finanzas / Comercial |
| R-11 | Calidad e inocuidad | Extender vida util comercial | Validar envasado con atmosfera modificada y pruebas aceleradas de estabilidad | Vida util validada 12-24 meses | Calidad / Comercial |
| R-12 | Escalamiento y piloto | Asegurar continuidad de implementacion | Implementar tablero de seguimiento mensual de KPIs tecnicos y economicos | Cumplimiento >= 90% de hitos de mejora anual | Gerencia de planta |

## 11. Conclusiones

1. El tren completo del proyecto final queda consolidado con todos los calculos principales y cierre de masa aceptable (0.006%).
2. La integracion OI mantiene el rendimiento de producto y reduce de forma preliminar la carga energetica total de 4704 kW a 3503 kW (reduccion aproximada de 25.5%).
3. El CAPEX base se mantiene en 3,126,200 USD y el OPEX ajustado preliminar con OI se estima en 4,633,000 USD/ano.
4. El proceso es tecnicamente consistente para presentacion final, con trazabilidad documental y criterios de control/riesgo definidos.

---

## 12. Bibliografia consultada

Fuentes web ya incluidas en el anexo bibliografico del proyecto final:

1. FAO. Technology of Production of Edible Flours and Protein Products from Soybeans. URL: https://www.fao.org/3/t0532e/t0532e05.htm
2. Wikipedia. Soy protein. URL: https://en.wikipedia.org/wiki/Soy_protein
3. Wikipedia. Soybean. URL: https://en.wikipedia.org/wiki/Soybean
4. Wikipedia. Reverse osmosis. URL: https://en.wikipedia.org/wiki/Reverse_osmosis
5. Wikipedia. Multiple-effect evaporator. URL: https://en.wikipedia.org/wiki/Multiple-effect_evaporator
6. NIST. Unit Conversion. URL: https://www.nist.gov/pml/owm/metric-si/unit-conversion
7. World Bank Group. Commodity Markets. URL: https://www.worldbank.org/en/research/commodity-markets

Fecha de consulta reportada en el proyecto: 18 marzo 2026.

---

## 13. Anexos visuales de planta y equipos

### 13.1 Vista general de planta

Figura A-1. Planta industrial de soya y tren completo integrado.

![Figura A-1 Planta industrial de soya](../media/images/Planta%20industrial%20soja.png)

### 13.2 Equipos del tren principal de proceso

Figura A-2. Silaje y manejo de materia prima.

![Figura A-2 Silaje de soya](../media/images/Silaje%20Soja.png)

Figura A-3. Tanque agitado para extraccion alcalina.

![Figura A-3 Tanque agitado](../media/images/Tanque%20agitado.png)

Figura A-4. Decantador centrifugo para separacion solido-liquido.

![Figura A-4 Decantador centrifugo](../media/images/Decantador%20centrifugo%20(separador).png)

Figura A-5. Intercambiador de calor del bloque de neutralizacion/pasteurizacion.

![Figura A-5 Intercambiador de calor](../media/images/Intercambiador%20de%20Calor.png)

Figura A-6. Modulo de osmosis inversa para preconcentracion.

![Figura A-6 Osmosis inversa](../media/images/Osmosis%20Inversa.png)

Figura A-7. Evaporador de doble efecto.

![Figura A-7 Evaporador doble efecto](../media/images/Evaporador%20de%20doble%20efecto.png)

Figura A-8. Precipitador isoelectrico.

![Figura A-8 Precipitador isoelectrico](../media/images/Precipitador%20isoelectrico.png)

Figura A-9. Secador por atomizacion (spray dryer).

![Figura A-9 Spray dryer](../media/images/spray%20dryer.png)

Figura A-10. Secado y palletizado.

![Figura A-10 Secado y palletizado](../media/images/Secado%20y%20palletizado.png)

Figura A-11. Molienda y tamizado final.

![Figura A-11 Tamizado y molienda](../media/images/Tamizado%20y%20Molienda.png)

Figura A-12. Formato comercial de venta.

![Figura A-12 Formato de venta](../media/images/Formato%20de%20venta.png)

### 13.3 Mapeo etapa-equipo del proceso

| Etapa | Equipo principal | Figura anexa |
|---|---|---|
| Recepcion y preparacion | Silaje de soya | A-2 |
| Extraccion alcalina | Tanque agitado | A-3 |
| Separacion primaria | Decantador centrifugo | A-4 |
| Tratamiento termico | Intercambiador de calor | A-5 / A-13 a A-15 |
| Preconcentracion | Osmosis inversa | A-6 |
| Concentracion termica | Evaporador doble efecto | A-7 |
| Purificacion | Precipitador isoelectrico | A-8 |
| Secado | Spray dryer | A-9 |
| Acabado y despacho | Secado/palletizado, molienda/tamizado y formato comercial | A-10, A-11, A-12 |

---

Version: 1.0 consolidada
Estado: Lista para entrega academica
