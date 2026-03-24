# Calculos del Proyecto Final
## Produccion de proteina aislada de soya (base: 1 ton/h de grano)

> Documento consolidado en formato Markdown, con calculos trazables, unidades consistentes y criterios explicitos para evitar ambiguedades.

---

## Indice

1. [Objetivo](#1-objetivo)
2. [Base de calculo y supuestos](#2-base-de-calculo-y-supuestos)
3. [Calculos por etapa](#3-calculos-por-etapa)
4. [Resultados del caso base](#4-resultados-del-caso-base)
5. [Verificaciones globales](#5-verificaciones-globales)
6. [Balance final de rendimiento por etapa](#6-balance-final-de-rendimiento-por-etapa)
7. [Analisis economico preliminar (CAPEX y OPEX)](#7-analisis-economico-preliminar-capex-y-opex)
8. [Resumen ejecutivo de variables](#8-resumen-ejecutivo-de-variables)
9. [Presentacion de ingenieria: Datasheets de equipos](#9-presentacion-de-ingenieria-datasheets-de-equipos)
10. [Presentacion de ingenieria: PFD narrativo y control](#10-presentacion-de-ingenieria-pfd-narrativo-y-control)
11. [Presentacion de ingenieria: Matriz de criticidad](#11-presentacion-de-ingenieria-matriz-de-criticidad)
12. [Presentacion de ingenieria: Riesgos y mitigacion](#12-presentacion-de-ingenieria-riesgos-y-mitigacion)
13. [Especificaciones de envasado y estrategia de entrega](#13-especificaciones-de-envasado-y-estrategia-de-entrega)
14. [Referencias internas](#14-referencias-internas)
15. [Anexo de bibliografia consultada](#15-anexo-de-bibliografia-consultada)

---

## 1. Objetivo

Consolidar una base de calculo unica, coherente y trazable para el proceso de produccion de proteina aislada de soya.

Esta version eleva el realismo del modelo con los siguientes criterios de diseno:

- Eficiencia global fija de equipos: 90%
- Evaporacion en multiple efecto (2 efectos)
- Sin factor de ensuciamiento
- Sin analisis por rangos para el caso base
- Inclusion de analisis economico preliminar (CAPEX/OPEX)

---

## 2. Base de calculo y supuestos

### 2.1 Alimentacion

| Variable | Valor |
|---|---:|
| Grano de soya | 1000 kg/h |
| Proteina en grano | 37.5% p/p |
| Proteina de entrada | 375 kg/h |
| Agua de extraccion (1:12) | 12000 kg/h |

### 2.2 Supuestos promedio de operacion

| Variable | Valor | Justificacion tecnica |
|---|---:|---|
| Eficiencia de extraccion proteica (Etapa 1) | 88% | Literatura para extraccion alcalina sin precalentamiento: rango 85–92% segun tiempo/T. Valor conservador típico industrial |
| Recuperacion proteica en precipitacion (Etapa 4) | 98% | Estándar aislado de soya; pérdida 2% por solubilidad residual a pH isoelectrico |
| Humedad de pasta post-centrifugacion | 50% | Centrifuga decantadora sanitaria típica; <50% requiere otros métodos (filtro-prensa) |
| Humedad final de polvo | 5% | Estándar aislado proteico en polvo; <5% critica para estabilidad microbiologica y agua disponible |
| pH de extraccion | 8.75 | Alcalinidad minima para solubilizacion proteica; pH > 10 riesgo de hidrolisis; pH < 8.5 extraccion incompleta |
| Temperatura de extraccion | 55 C | Equilibrio: T > 65°C riesgo desnaturalizacion; T < 50°C cinetica lenta; 55°C optimo para proceso |
| Pasteurizacion | 80 C por 22 s | HTST standard (High Temperature Short Time); inactivacion bacteriana ~6 log CFU; preserva proteina |
| Evaporacion multiple efecto | 2 efectos | Economia de vapor 1.85 kg/kg; 3+ efectos sin ganancia significativa para caudal 12.4 m3/h |
| Presion de referencia en evaporacion | 0.40 bar abs | Compromiso: T baja (48°C) para producto termolabil vs ΔT suficiente (22 K/efecto) para transferencia |
| Solidos de concentrado a salida de evaporador | 23% p/p | Limite antes de ensuciamiento excesivo; >25% riesgo fouling; <20% incrementa vapor requerido |
| Eficiencia global de equipos/utilidades | 90% | Asume perdidas reales, variabilidad y degradacion de desempeño; no es eficiencia idealizacion teorica |

### 2.3 Criterios de reporte

1. Se reportan dos salidas finales:
  1. Polvo total (kg/h)
  2. Proteina pura recuperada (kg/h)
2. Los reactivos de ajuste de pH (NaOH/HCl) se incluyen en OPEX y se consideran despreciables en el cierre principal de masa.
3. No se aplica factor de ensuciamiento en transferencia de calor.

### 2.4 Criterios generales de diseño y referencias

| Criterio | Valor/Rango | Justificación |
|---|---|---|
| Geometría tanques agitados | H/D = 0.8–1.0 | Evita vorticidad excesiva; barrido uniforme |
| Estimación viscosidad líquido | μ ≈ 0.020 Pa·s | Suspensiones acuosas con sólidos 3–5% |
| Factor G en centrifugas | 1800–2200 g | Rango estándar para sólidos 100–250 μm |
| Factor servicio bomba | 15% sobre caudal nominal | Variabilidad operativa + picos cortos |
| Margen diseño intercambiadores | 10% Área adicional | Cubre fouling futuro leve |
| Velocidad en tuberías | 0.3–1.8 m/s | Rango óptimo para fluidos alimentarios |
| Eficiencia global equipos | 90% | Asume pérdidas reales y variabilidad |
| Altura manométrica bombas | 18–30 m | Supera resistencias línea y elevación |
| Recuperación térmica | 55% en intercambiadores | Estimé empírica placas sanitarias |
| Economía vapor (2 efectos) | 1.85 kg/kg | Correlación estándar doble efecto |
| Coeficiente U placas limpias | 400–600 W/(m²K) | Para agua-agua AISI 316L |
| Coeficiente U evaporador falling film | 750–950 W/(m²K) | Para jugo/concentrado diluido |
| Presión evaporación | 0.40 bar abs | Compromiso T baja vs ΔT suficiente |
| Tiempo de pasteurización | 22 s a 80°C | HTST estándar |
| Factor instalación CAPEX | 30% equipos | Estándar industrial equipos 1–5 MW |
| Factor ingeniería CAPEX | 15% equipos | Especializado alimentos |
| Contingencia CAPEX | 10% subtotal | Cubre cambios menores |

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


## 3.0 Etapa 0: Captacion/almacenamiento de agua de extraccion

Esta etapa define el bloque hidrico previo a la extraccion alcalina: recepcion desde red industrial, almacenamiento intermedio y bombeo de alimentacion.

### 3.0.1 Caudal de diseno de agua

$$
\dot{V}_{agua} = 12000\ \text{L/h} = 12.0\ \text{m}^3/\text{h} = 0.00333\ \text{m}^3/\text{s}
$$

### 3.0.2 Volumen de tanque de agua de extraccion

Con autonomia de 1 h y reserva del 20%:

$$
V_{base} = 12.0\ \text{m}^3
$$

$$
V_{tanque,agua} = V_{base}\cdot1.20 = 14.4\ \text{m}^3
$$

Capacidad nominal recomendada: **15 m3**.

### 3.0.3 Bombeo de alimentacion de agua (estimacion basica)

Supuestos de linea de alimentacion desde tanque de agua a preparacion de extractante:

- Diametro interno de referencia: 0.063 m (DN65)
- Altura dinamica de diseno: 10.7 m
- Eficiencia hidraulica de bomba: 65%
- Eficiencia de motor: 90%

Potencia hidraulica:

$$
P_h = \rho g Q H = 1000\cdot9.81\cdot0.00333\cdot10.7 = 0.35\ \text{kW}
$$

Potencia de motor requerida:

$$
P_{motor} = \frac{P_h}{\eta_b\eta_m} = \frac{0.35}{0.65\cdot0.90} = 0.60\ \text{kW}
$$

Seleccion preliminar: bomba sanitaria de **1.5 kW** para margen operativo.

### 3.0.4 Integracion al caso base

- El caudal de 12.0 m3/h alimenta la relacion 1:12 del bloque de extraccion.
- El tanque de 15 m3 estabiliza variaciones de red y evita interrupciones cortas.
- La potencia de bombeo de 0.60 kW se considera parte de consumos electricos auxiliares.


## 3.1 Etapa 1: Extraccion alcalina

### 3.1.1 Proteina extraida

$$
\dot{m}_{prot,ext} = \dot{m}_{prot,in} \cdot \eta_{ext}
$$

$$
\dot{m}_{prot,ext} = 375 \cdot 0.88 = 330\ \text{kg/h}
$$

Proteina no extraida (queda en okara):

$$
\dot{m}_{prot,okara} = 375 - 330 = 45\ \text{kg/h}
$$

### 3.1.2 Caudal total de lodo

$$
\dot{m}_{lodo} = 1000 + 12000 = 13000\ \text{kg/h}
$$

### 3.1.3 Volumen de tanque (referencia de diseno)

Supuestos:

- **Densidad del lodo:** 1060 kg/m³ *(Suspensión acuosa con ~5% sólidos totales; típico rango 1050–1100 kg/m³)*
- **Tiempo de residencia:** 0.9 h *(Industrial típico 0.7–1.2 h; suficiente para contacto sólido-líquido sin agitación extrema)*
- **Factor de seguridad:** 1.2 *(Cubre variabilidad operativa, espacio espuma/gas y picos cortos de caudal)*

$$
\dot{V}_{in} = \frac{13000}{1060} = 12.26\ \text{m}^3/\text{h}
$$

$$
V_{tanque} = \dot{V}_{in} \cdot \tau \cdot f_s = 12.26 \cdot 0.9 \cdot 1.2 = 13.24\ \text{m}^3
$$

Valor recomendado de diseno: **14 m3**.

### 3.1.4 Diseno operativo del tanque y agitador

**Criterio de geometría:** Se adopta relacion $H/D = 0.85$ *(Rango óptimo 0.8–1.0 para tanques agitados; evita vortex excesivo y garantiza barrido uniforme)*

Para tanque cilindrico vertical:

$$
V = \frac{\pi D^2}{4}H = \frac{\pi D^2}{4}(0.85D)
$$

$$
D = 2.71\ \text{m},\quad H = 2.30\ \text{m}
$$

Para margen operativo y espacio de espuma/gas se adopta altura total de casco:

$$
H_{total} = 3.30\ \text{m}
$$

**Agitador tipo PBT de 6 palas:**

- **Diametro de impulsor:** $D_{ag} = 0.40D = 1.08\ \text{m}$ *(Estándar regla 0.35–0.45 × D_tanque; asegura barrido sin zonas muertas)*
- **Velocidad de operacion:** $N = 80\ \text{rpm}$ *(Re > 10⁴ régimen turbulento; rango industrial típico 30–100 rpm para líquidos viscosos)*
- **Numero de baffles:** 4, ancho $B = D/10 = 0.27\ \text{m}$ *(Suprime vortex; regla estándar B = D/10 evita turbulencia excesiva)*

Verificacion hidrodinamica y potencia:

$$
Re_{ag} = \frac{\rho N D_{ag}^2}{\mu} = \frac{1060\cdot(80/60)\cdot(1.08)^2}{0.020} \approx 8.2\times10^4
$$

$$
P_{ag} = N_p\rho N^3D_{ag}^5 = 1.5\cdot1060\cdot(80/60)^3\cdot(1.08)^5 \approx 5.5\ \text{kW}
$$

Con eficiencia global del 90%:

$$
P_{ag,real} = \frac{5.5}{0.90} = 6.1\ \text{kW}
$$

Seleccion comercial preliminar:

- Tanque AISI 316L, volumen nominal 14 m3
- Motor agitador 7.5 kW, 4 polos, con variador de frecuencia

---

## 3.2 Etapa 1.2: Separacion solido-liquido

Valores promedio adoptados:

- Extracto liquido: 12400 kg/h
- Okara humedo: 600 kg/h

Verificacion:

$$
12400 + 600 = 13000\ \text{kg/h}\ \checkmark
$$

Composicion promedio de okara:

- Humedad: 65%
- Agua en okara: 390 kg/h
- Solidos en okara: 210 kg/h

Se asume que en estos solidos se incluyen 45 kg/h de proteina no extraida; el resto es fibra e insolubles.

### 3.2.1 Diseno operativo de centrifuga post-lixiviacion

**Caudal de diseño con factor de servicio:** 15% *(Cubre variabilidad operativa y picos cortos; práctica industrial estándar)*

$$
\dot{V}_{dis} = 13.0\cdot1.15 = 14.95\ \text{m}^3/\text{h}
$$

Se selecciona arreglo de **2 centrifugas decantadoras en paralelo** para continuidad operativa *(Permite mantenimiento sin parada; redundancia operativa)*:

- **Capacidad unitaria:** 8 m³/h
- **Capacidad total instalada:** 16 m³/h
- **Diametro de tambor:** 0.60 m
- **Longitud de tambor:** 1.60 m
- **Factor G operativo:** 1800 g *(Suficiente para sólidos 100–200 μm; >2000 g no mejora significativamente recuperación)*
- **Potencia por unidad:** 11 kW

Potencia electrica real por unidad (90%):

$$
P_{real,u} = \frac{11}{0.90} = 12.2\ \text{kW}
$$

Potencia real total instalada en esta operacion:

$$
P_{real,total} = 2\cdot12.2 = 24.4\ \text{kW}
$$

---

## 3.3 Etapa 2: Neutralizacion y pasteurizacion

### 3.3.1 Carga termica bruta

Se calienta el extracto de 25 C a 80 C:

$$
Q_{pasteur,bruto} = \dot{m} \cdot C_p \cdot \Delta T
$$

Datos:

- $\dot{m} = 12400\ \text{kg/h}$
- $C_p = 3.8\ \text{kJ/(kg K)}$
- $\Delta T = 55\ \text{K}$

$$
Q_{pasteur,bruto} = 12400 \cdot 3.8 \cdot 55 = 2{,}592{,}400\ \text{kJ/h}
$$

$$
Q_{pasteur,bruto} = \frac{2{,}592{,}400}{3600} = 720\ \text{kW}
$$

### 3.3.2 Carga termica neta (con recuperacion)

Con recuperacion termica del 55% en el intercambiador de placas:

$$
Q_{pasteur,neto} = Q_{bruto} \cdot (1 - 0.55) = 720 \cdot 0.45 = 324\ \text{kW}
$$

### 3.3.3 Diseno operativo del intercambiador de placas

**Parámetros de transferencia de calor:**

- **Coeficiente global $U = 500\ \text{W/(m}^2\text{K)}$** *(Typical water-water placas AISI 316L limpias; sin fouling asumido en caso base; rango típico 400–600 W/(m²K) para equipos sanitarios)*
- **Diferencia logarítmica media $\Delta T_{lm} = 18\ \text{K}$** *(Consecuencia de recuperación térmica 55% y perfiles de entrada/salida especificados en sección 3.3.2)*

**Area requerida:**

$$
A = \frac{Q}{U\Delta T_{lm}} = \frac{324000}{500\cdot18} = 36.0\ \text{m}^2
$$

**Con margen de diseño de 10%** *(Cubre futuros fouling leve y degradación de U con tiempo; estándar industrial para equipos nuevos)*:

$$
A_{dis} = 39.6\ \text{m}^2
$$

Si el area efectiva por placa es 0.55 m2:

$$
N_{placas} \approx \frac{39.6}{0.55} + 1 \approx 73
$$

Seleccion comercial preliminar: intercambiador de placas sanitarias de 72-76 placas.

Bombas asociadas al lazo termico/producto (caudal de diseno 14.3 m3/h, H = 22 m):

$$
P_{bomba} = \frac{\rho g\dot{V}H}{\eta} = \frac{1050\cdot9.81\cdot(14.3/3600)\cdot22}{0.90} \approx 1.0\ \text{kW}
$$

Seleccion comercial preliminar: bomba centrifuga sanitaria de 2.2 kW.

---

## 3.4 Etapa 3: Concentracion por evaporacion al vacio (multiple efecto)

Para mantener coherencia fisica con la masa de solidos extraidos:

- Solidos disueltos/finos hacia evaporador: 566 kg/h
- Flujo al evaporador: 12400 kg/h

### 3.4.1 Flujo de concentrado (23% solidos)

$$
\dot{m}_{conc} = \frac{\dot{m}_{solidos}}{x_{solidos,salida}} = \frac{566}{0.23} = 2461\ \text{kg/h}
$$

### 3.4.2 Agua evaporada

$$
\dot{m}_{evap} = \dot{m}_{in} - \dot{m}_{conc} = 12400 - 2461 = 9939\ \text{kg/h}
$$

### 3.4.3 Carga termica de evaporacion (proceso)

Con calor latente promedio a 55 C: $\lambda = 2355\ \text{kJ/kg}$

$$
Q_{evap,proceso} = \dot{m}_{evap} \cdot \lambda = 9939 \cdot 2355 = 23{,}406{,}345\ \text{kJ/h}
$$

$$
Q_{evap,proceso} = \frac{23{,}406{,}345}{3600} = 6502\ \text{kW}
$$

### 3.4.4 Requerimiento termico con 2 efectos

**Economía de vapor para doble efecto:** *(Correlación empírica estándar; literatura rango 1.7–2.0 kg/kg según ΔT y presión)*

$$
E_{v} = 1.85\ \frac{\text{kg agua evaporada}}{\text{kg vapor vivo}}
$$

Carga termica equivalente con vapor vivo:

$$
Q_{evap,vapor} = \frac{Q_{evap,proceso}}{E_v} = \frac{6502}{1.85} = 3515\ \text{kW}
$$

Ajuste por eficiencia global del 90% en utilidades/equipo:

$$
Q_{evap,utilidad} = \frac{Q_{evap,vapor}}{0.90} = \frac{3515}{0.90} = 3906\ \text{kW}
$$

### 3.4.5 Diseno operativo del evaporador de doble efecto

Se distribuye la carga termica de proceso en dos cuerpos:

$$
Q_{ef1} = Q_{ef2} = \frac{6502}{2} = 3251\ \text{kW}
$$

**Parámetros de transferencia en evaporador:**

- **$U_{ef} = 850\ \text{W/(m}^2\text{K)}$** *(Estándar falling film sanitario sin fouling; rango 750–950 W/(m²K) típico para jugo/concentrados)*
- **$\Delta T_{ef} = 22\ \text{K}$ por efecto** *(Consecuencia presión absoluta 0.40 bar y distribución de carga balanceada)*

Area por efecto:

$$
A_{ef} = \frac{3{,}251{,}000}{850\cdot22} = 173.8\ \text{m}^2
$$

Area total instalada:

$$
A_{tot,evap} = 2\cdot173.8 = 347.6\ \text{m}^2
$$

Traduccion a geometria tubular (por efecto):

- Diametro interno de tubo: 25 mm
- Longitud util por tubo: 3.0 m
- Area por tubo: $A_t = \pi DL = 0.236\ \text{m}^2$

$$
N_{tubos,ef} = \frac{173.8}{0.236} \approx 736\ \text{tubos/efecto}
$$

Sistema de vacio y condensacion preliminar:

- Bomba de vacio: 5 m3/min por tren
- Potencia de motor: 2.2 kW
- Condensador de vapores: 45 m2 (total para ambos efectos)

---

## 3.5 Etapa 4: Precipitacion isoelectrica

### 3.5.1 Proteina precipitada

$$
\dot{m}_{prot,prec} = \dot{m}_{prot,ext} \cdot 0.98 = 330 \cdot 0.98 = 323.4\ \text{kg/h}
$$

Se considera coprecipitacion promedio de otros solidos: 23 kg/h.

Entonces, solidos secos de pasta precipitada:

$$
\dot{m}_{solidos,pasta} = 323.4 + 23 = 346.4\ \text{kg/h}
$$

---

## 3.6 Etapa 4.2: Centrifugacion post-precipitacion

Con humedad de pasta al 50%:

$$
\dot{m}_{pasta} = \frac{\dot{m}_{solidos,pasta}}{1 - H} = \frac{346.4}{0.50} = 692.8\ \text{kg/h}
$$

- Pasta hacia secado: 692.8 kg/h
- Agua en pasta: 346.4 kg/h

### 3.6.1 Diseno operativo de centrifuga post-precipitacion

Caudal volumetrico aproximado de pasta/suero a la entrada:

$$
\dot{V}_{4.2} \approx \frac{692.8}{1080} = 0.64\ \text{m}^3/\text{h}
$$

Se selecciona centrifuga decantadora sanitaria para operacion estable con margen:

- Capacidad nominal: 3 m3/h
- Factor G: 2200 g
- Diametro de tambor: 0.40 m
- Longitud de tambor: 1.20 m
- Potencia de motor: 7.5 kW

Potencia real con eficiencia global:

$$
P_{real,4.2} = \frac{7.5}{0.90} = 8.3\ \text{kW}
$$

---

## 3.7 Etapa 5: Secado por atomizacion

Objetivo de humedad final de polvo: 5%.

### 3.7.1 Flujo de polvo final

$$
\dot{m}_{polvo} = \frac{\dot{m}_{solidos,pasta}}{1 - 0.05} = \frac{346.4}{0.95} = 364.6\ \text{kg/h}
$$

### 3.7.2 Agua evaporada en secador

$$
\dot{m}_{H2O,secado} = \dot{m}_{pasta} - \dot{m}_{polvo} = 692.8 - 364.6 = 328.2\ \text{kg/h}
$$

### 3.7.3 Energia de secado (proceso)

Termino latente aproximado:

$$
Q_{lat,sec} = 328.2 \cdot 2400 = 787{,}680\ \text{kJ/h} = 219\ \text{kW}
$$

Considerando sensible del aire y perdidas internas del secador:

$$
Q_{secado,proceso} \approx 340\ \text{kW}
$$

### 3.7.4 Diseno operativo del spray dryer

Con base en el deber termico y residencia de particula, se adopta camara cilindrica-conica.

Dimensiones de camara:

- Diametro interno: 3.0 m
- Altura cilindrica: 4.5 m
- Altura de cono: 2.0 m

Volumen geometrico:

$$
V_{cil} = \frac{\pi D^2}{4}H = \frac{\pi(3.0)^2}{4}(4.5)=31.8\ \text{m}^3
$$

$$
V_{cono}=\frac{1}{3}\frac{\pi D^2}{4}H_c=\frac{1}{3}\frac{\pi(3.0)^2}{4}(2.0)=4.7\ \text{m}^3
$$

$$
V_{total}=31.8+4.7=36.5\ \text{m}^3
$$

**Selección de atomización y aire:**

- **Disco atomizador:** 100 mm *(Tamaño típico; DVB resultante ~80 μm; equilibrio entre fineza y consumo energético)*
- **Velocidad de disco:** 18000 rpm *(Estándar spray dryer; velocidad periférica ~9400 m/s; regímenes 12000–25000 rpm según aplicación)*
- **Flujo de aire de proceso:** 9000 m³/h *(Ratio aire/producto ~5.5 m³/kg/h; suficiente para deshidratación rápida en camara)*
- **Ventilador principal:** 7.5 kW
- **Generador de calor nominal:** 400 kW *(Potencia nominal; cubre proceso + pérdidas convectivas)*

Consumo real de utilidades del bloque (90%):

$$
P_{vent,real}=\frac{7.5}{0.90}=8.3\ \text{kW}
$$

$$
Q_{calor,real}=\frac{340}{0.90}=378\ \text{kW}
$$

### 3.7.5 Diseno operativo de molienda y tamizado final

Para una produccion de 364.6 kg/h de polvo:

- Molino de martillos sanitario: 500 kg/h
- Potencia de molino: 5.5 kW
- Criba vibratoria: 500 kg/h, doble malla 100/200 mesh
- Potencia de criba: 1.5 kW

Potencia real conjunta:

$$
P_{mol+crib,real}=\frac{5.5+1.5}{0.90}=7.8\ \text{kW}
$$

---

## 3.8 Consumo real de utilidades con eficiencia global del 90%

Para cada bloque energetico:

$$
Q_{utilidad} = \frac{Q_{proceso}}{\eta_{global}},\quad \eta_{global}=0.90
$$

| Equipo/servicio | Carga de proceso (kW) | Eficiencia global | Consumo real de utilidad (kW) |
|---|---:|---:|---:|
| Pasteurizacion (neta) | 324 | 0.90 | 360 |
| Evaporacion 2 efectos (vapor vivo equivalente) | 3515 | 0.90 | 3906 |
| Secado por atomizacion | 340 | 0.90 | 378 |
| Bombas + agitadores + equipos mecanicos | 54 | 0.90 | 60 |
| **Total utilidades del caso base** | - | - | **4704 kW** |

Nota hidrica de cierre: la bomba de alimentacion de agua calculada en 3.0.3 (0.60 kW) queda absorbida en el bloque de consumos auxiliares y no modifica el total redondeado del caso base.

## 3.9 Diseno operativo de tuberias y bombas por etapa

### 3.9.1 Tuberias principales de proceso

| Tramo | Caudal (m3/h) | Diametro nominal | Diametro interno aprox. (m) | Velocidad (m/s) |
|---|---:|---|---:|---:|
| Alimentacion a extraccion | 13.0 | DN80 (3") | 0.078 | 0.76 |
| Extracto a pasteurizacion | 12.4 | DN65 (2.5") | 0.063 | 1.11 |
| Pasteurizado a evaporador | 12.4 | DN65 (2.5") | 0.063 | 1.11 |
| Concentrado a precipitacion | 2.46 | DN40 (1.5") | 0.041 | 0.52 |
| Pasta a secado | 0.64 | DN32 (1.25") | 0.035 | 0.18 |

Las velocidades quedan en el rango operativo para fluidos alimentarios viscosos (aprox. 0.3 a 1.8 m/s).

### 3.9.2 Bombas de transferencia por etapa

| Servicio | Caudal diseno (m3/h) | Altura manometrica (m) | Potencia hidraulica estimada (kW) | Potencia real (kW, 90%) | Seleccion preliminar |
|---|---:|---:|---:|---:|---|
| Agua/lodo a tanque de extraccion | 13.0 | 18 | 0.68 | 0.75 | 1.5 kW sanitaria |
| Extracto a intercambiador | 14.3 | 22 | 0.90 | 1.00 | 2.2 kW sanitaria |
| Extracto a evaporador | 14.3 | 28 | 1.15 | 1.28 | 3.0 kW sanitaria |
| Concentrado a precipitacion | 2.8 | 24 | 0.19 | 0.21 | 1.1 kW sanitaria |
| Pasta a atomizacion (cavidad progresiva) | 0.8 | 30 | 0.07 | 0.08 | 1.5 kW desplazamiento positivo |

Nota: la potencia real instalada seleccionada comercialmente se redondea hacia arriba respecto a la potencia calculada.

### 3.9.3 Cierre hidraulico implementado

La implementacion completa de las fases hidraulicas (validacion de entradas, memoria de calculo detallada, seleccion tecnica y paquete integrado con MTO preliminar) se consolida en:

- Implementacion_Hidraulica.md

Este documento complementa esta seccion con:

1. Perdidas por friccion y menores por tramo con trazabilidad de supuestos.
2. TDH y potencia de bombeo por servicio.
3. Criterio de NPSH preliminar y capacidad de tanque de agua.
4. Lista preliminar de materiales y equipos hidraulicos.

## 3.10 Cuadro maestro de seleccion comercial de equipos

| Equipo | Servicio | Capacidad de diseno | Dimensiones principales | Potencia seleccionada |
|---|---|---|---|---:|
| Tanque agitado + PBT | Extraccion alcalina | 13.0 m3/h de lodo | Tanque D = 2.71 m, H util = 2.30 m, H total = 3.30 m, V = 14 m3 | 7.5 kW |
| Centrifuga decantadora (x2) | Separacion post-lixiviacion | 2 x 8 m3/h | Tambor 0.60 m x 1.60 m; envolvente por unidad aprox. 2.40 x 0.95 x 1.20 m | 2 x 11 kW |
| Intercambiador de placas | Neutralizacion/pasteurizacion | 324 kW netos | Area = 39.6 m2, 72-76 placas; bastidor aprox. 2.20 x 0.90 x 1.20 m | - |
| Bomba sanitaria de lazo | Transferencia a intercambiador | 14.3 m3/h @ 22 m | Conexion 2.5 in tri-clamp; huella aprox. 0.80 x 0.35 m, altura 0.45 m | 2.2 kW |
| Evaporador falling film (2 efectos) | Concentracion al vacio | 9939 kg/h agua evaporada | 173.8 m2/efecto, 736 tubos/efecto; cuerpo por efecto aprox. D = 1.20 m, H = 5.50 m | - |
| Bomba de vacio | Sistema de vacio evaporador | 5 m3/min | Skid de vacio aprox. 1.20 x 0.80 x 1.50 m + condensador horizontal L = 2.00 m, D = 0.60 m | 2.2 kW |
| Centrifuga decantadora | Post-precipitacion | 3 m3/h nominal | Tambor 0.40 m x 1.20 m; envolvente aprox. 1.80 x 0.75 x 1.10 m | 7.5 kW |
| Spray dryer | Secado por atomizacion | 364.6 kg/h polvo | Camara D = 3.0 m, H total = 6.5 m, V = 36.5 m3; cono H = 2.0 m | Vent. 7.5 kW + calor 400 kW |
| Molino de martillos | Ajuste granulometrico | 500 kg/h | Equipo aprox. 1.40 x 0.90 x 1.60 m; malla de salida 100-200 mesh | 5.5 kW |
| Criba vibratoria | Clasificacion final | 500 kg/h | Equipo aprox. 1.80 x 0.90 x 1.20 m; doble malla 100/200 mesh | 1.5 kW |

## 3.11 Instrumentacion minima por equipo

| Equipo | Variable critica | Instrumento | Rango recomendado | Accion de control |
|---|---|---|---|---|
| Tanque de extraccion | pH | Sonda pH en linea | 6-10 | Dosificar NaOH/HCl |
| Tanque de extraccion | Temperatura | PT100 clase A | 0-100 C | Control chaqueta/calefaccion |
| Tanque de extraccion | Nivel | Transmisor de nivel | 0-100% | Evitar sobrellenado |
| Centrifugas | Velocidad tambor | Tacometro/encoder | 0-4000 rpm | Ajuste de G |
| Centrifugas | Torque tornillo | Sensor de torque | 0-100% | Evitar atascamiento |
| Intercambiador | T entrada/salida | PT100 en ambas lineas | 0-120 C | Control termico |
| Intercambiador | Presion diferencial | Transmisor DP | 0-2 bar | Detectar ensuciamiento hidraulico |
| Evaporador doble efecto | Vacio | Vacuometro digital | 0-1 bar abs | Control de bomba de vacio |
| Evaporador doble efecto | Solidos salida | Refractometro en linea | 0-30 Brix | Ajustar recirculacion/vapor |
| Spray dryer | T inlet/outlet aire | Termocupla tipo K | 0-250 C | Control de quemador/aire |
| Spray dryer | Flujo de aire | Caudalimetro de aire | 0-15000 m3/h | Control de ventilador |
| Spray dryer | Humedad de polvo | Analizador NIR o laboratorio | 0-10% | Ajuste de temperatura y caudal |
| Bombas de transferencia | Presion descarga | Manometro/transmisor | 0-6 bar | Confirmar punto de operacion |
| Molino/criba | Corriente de motor | Medidor de corriente | 0-150% | Proteger por sobrecarga |

## 3.12 Operacion innovadora: preconcentracion por osmosis inversa (OI)

Objetivo tecnico de la OI en este caso base:

- Reducir la carga termica de evaporacion al vacio removiendo agua por via de membrana antes del EV-301A/B.
- Mantener temperatura de operacion baja para proteger funcionalidad proteica.
- Desplazar parte del consumo energetico desde calor (vapor) hacia electricidad de bombeo de alta presion.

### 3.12.1 Integracion de proceso propuesta

Ubicacion recomendada:

- Corriente de extracto clarificado, luego de separacion post-lixiviacion y previo al tren de evaporacion.

Esquema de integracion:

1. Alimentacion OI desde extracto clarificado.
2. Permeado a tanque de agua de servicio/CIP no critico.
3. Retentado concentrado a EV-301A/B para concentracion final y control de solidos.

### 3.12.2 Base de diseno preliminar de OI

Supuestos de diseno para preconcentracion:

- Flujo de entrada a OI: 12400 kg/h (aprox. 12.4 m3/h)
- Recuperacion volumetrica de permeado: 25%
- Densidad aproximada de corriente: 1000 kg/m3
- Rechazo de proteina por membrana: >99% (supuesto de membrana adecuada para proteina disuelta)

Resultados de caudales:

$$
\dot{m}_{perm} = 12400 \cdot 0.25 = 3100\ \text{kg/h}
$$

$$
\dot{m}_{ret} = 12400 - 3100 = 9300\ \text{kg/h}
$$

### 3.12.3 Impacto termico en evaporacion (estimacion de primer orden)

Si la OI retira 3100 kg/h de agua antes del evaporador, la remocion termica potencial en EV disminuye en la misma magnitud:

$$
\dot{m}_{evap,nuevo} = 9939 - 3100 = 6839\ \text{kg/h}
$$

Con calor latente medio $\lambda = 2355\ \text{kJ/kg}$:

$$
Q_{evap,proceso,nuevo} = 6839\cdot2355 = 16{,}105{,}845\ \text{kJ/h}
$$

$$
Q_{evap,proceso,nuevo} = \frac{16{,}105{,}845}{3600} = 4474\ \text{kW}
$$

Comparado con caso base (6502 kW), la reduccion potencial de carga de proceso en evaporacion es:

$$
\Delta Q_{evap} = 6502 - 4474 = 2028\ \text{kW}
$$

### 3.12.4 Variables criticas de operacion OI

| Variable | Rango operativo recomendado | Riesgo fuera de rango |
|---|---|---|
| Presion transmembrana | 18-30 bar | Menor flujo de permeado o compactacion de membrana |
| Flujo cruzado | 1.0-2.0 m/s | Polarizacion de concentracion y fouling acelerado |
| Temperatura de alimentacion | 20-35 C | Baja T reduce flujo; alta T acelera ensuciamiento |
| pH de alimentacion | 6.5-8.5 | pH extremo reduce vida util de membrana |
| SDI (indice ensuciamiento) | < 4 | Ensuciamiento rapido y caida de recuperacion |

### 3.12.5 Limitaciones y criterio de implementacion

1. La OI se plantea como modulo innovador de preconcentracion, no como reemplazo total de evaporacion.
2. Requiere prefiltracion fina y protocolo CIP de membranas para sostener recuperacion.
3. La factibilidad final debe cerrarse con piloto corto para confirmar rechazo proteico, flujo de permeado y frecuencia de limpieza.

---

## 4. Resultados del caso base

## 4.1 Indicadores de produccion

- **Polvo final total:** 364.6 kg/h
- **Proteina pura recuperada:** 323.4 kg/h

Pureza proteica del polvo:

$$
\%P = \frac{323.4}{364.6} \cdot 100 = 88.7\%
$$

## 4.2 Rendimientos

Rendimiento de recuperacion de proteina (base proteina de entrada):

$$
\eta_{prot,global} = \frac{323.4}{375} \cdot 100 = 86.2\%
$$

Rendimiento masico de polvo (base grano):

$$
\eta_{polvo/grano} = \frac{364.6}{1000} \cdot 100 = 36.5\%
$$

---

## 5. Verificaciones globales

## 5.1 Balance global de masa

Entrada total:

- 13000 kg/h

Salidas principales:

- Okara humedo: 600 kg/h
- Condensado de evaporador: 9939 kg/h
- Suero residual: 1769 kg/h
- Polvo final: 364.6 kg/h
- Vapor removido en spray dryer: 328.2 kg/h

Suma de salidas:

$$
600 + 9939 + 1769 + 364.6 + 328.2 = 13000.8\ \text{kg/h}
$$

Error por redondeo:

$$
\frac{13000.8 - 13000}{13000} \cdot 100 = 0.006\%\ \checkmark
$$

## 5.2 Balance energetico del caso base (realista)

- Pasteurizacion (utilidad real): 360 kW
- Evaporacion 2 efectos (utilidad real): 3906 kW
- Secado por atomizacion (utilidad real): 378 kW
- Bombas + agitadores + equipos mecanicos (electricidad real): 60 kW

$$
\dot{E}_{total,real} \approx 360 + 3906 + 378 + 60 = 4704\ \text{kW}
$$

Consumo especifico por kg de proteina recuperada:

$$
e_{esp,prot} = \frac{4704}{323.4} = 14.5\ \text{kWh/kg proteina}
$$

Consumo especifico por kg de polvo:

$$
e_{esp,polvo} = \frac{4704}{364.6} = 12.9\ \text{kWh/kg polvo}
$$

Equivalencia en MJ/kg (requisito de reporte energetico):

$$
e_{esp,prot} = 14.5\cdot3.6 = 52.2\ \text{MJ/kg proteina}
$$

$$
e_{esp,polvo} = 12.9\cdot3.6 = 46.4\ \text{MJ/kg polvo}
$$

## 5.3 Validacion de consistencia de balances y unidades

Checklist de validacion del caso base:

1. Cierre masico global: error de 0.006% (aceptable, menor a 0.5%).
2. Coherencia de potencia total: 4704 kW = suma de bloques de utilidad y equipos mecanicos.
3. Coherencia de OPEX electrico: 60 kW instalados -> 48,000 USD/ano a 8000 h/ano y 0.10 USD/kWh.
4. Coherencia de conversion energetica: 1 kWh = 3.6 MJ aplicada en indicadores especificos.
5. Coherencia de base de materia prima: todo el caso base mantiene soya como unica alimentacion.

Tabla de verificacion rapida:

| Verificacion | Resultado | Criterio |
|---|---:|---|
| Cierre de masa global | 99.994% | >= 99.5% |
| Balance energetico total | 4704 kW | Suma de bloques consistente |
| Consumo especifico proteina | 14.5 kWh/kg = 52.2 MJ/kg | Conversion correcta |
| Consumo especifico polvo | 12.9 kWh/kg = 46.4 MJ/kg | Conversion correcta |
| Trazabilidad de unidades | Cumple | kg/h, kW, kWh/kg y MJ/kg |

---

## 6. Balance final de rendimiento por etapa

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

## 7. Analisis economico preliminar (CAPEX y OPEX)

### 7.1 Criterios economicos del caso base

- Moneda base de reporte: USD y Bs en paralelo.
- Tipo de cambio de referencia: 1 USD = 6.96 Bs.
- Horas de operacion anual: 8000 h/ano.
- Alcance OPEX: energia termica/electrica, agua/efluentes, reactivos de pH y materia prima.
- Alcance CAPEX: estimacion preliminar de equipos y factores de instalacion.

### 7.2 CAPEX preliminar

| Concepto | Costo (USD) | Costo (Bs) | Justificación técnica |
|---|---:|---:|---|
| Equipos directos de proceso | 1,960,000 | 13,641,600 | Suma de datasheets comerciales; equipos sanitarios AISI 316L |
| Instalación y montaje (30%) | 588,000 | 4,092,480 | Regla industrial estándar para equipos medianos 1–5 MW; incluye tuberías, soportes, conexiones |
| Ingeniería e indirectos (15%) | 294,000 | 2,046,240 | Porcentaje típico especializado en procesos alimentarios; incluye diseño ejecutivo, dibujos, coordinación |
| Contingencia preliminar (10%) | 284,200 | 1,978,032 | Cubre cambios menores, variabilidad de mercado y actividades no previstas en estimación |
| **CAPEX total estimado** | **3,126,200** | **21,758,352** | - |

### 7.3 OPEX anual preliminar

#### 7.3.1 Energia

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

#### 7.3.2 Agua y efluentes

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

#### 7.3.4 Materia prima

**Supuesto:**

- **Soya:** 1 ton/h *(Base de cálculo; grano limpio con humedad ~12%, proteina 37.5% p/p)*
- **Precio medio:** 430 USD/ton *(Promedio mundial enero 2026; rango 380–480 USD/ton según origen/contrato)*

$$
M_{soya,anual} = 1 \cdot 8000 = 8000\ \text{ton/ano}
$$

$$
C_{soya} = 8000 \cdot 430 = 3{,}440{,}000\ \text{USD/ano}
$$

### 7.4 Resumen OPEX y costo unitario

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

### 7.5 Verificacion cruzada de potencia instalada vs OPEX

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

## 8. Resumen ejecutivo de variables

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

## 9. Presentacion de ingenieria: Datasheets de equipos

### 9.1 DS-101 Tanque de extraccion + agitador

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

### 9.2 DS-102 Centrifugas post-lixiviacion

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

### 9.3 DS-201 Intercambiador de placas

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

### 9.4 DS-301 Evaporador doble efecto

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

### 9.5 DS-401 Centrifuga post-precipitacion

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

### 9.6 DS-501 Spray dryer

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

### 9.7 DS-601 Molino y criba

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

## 10. Presentacion de ingenieria: PFD narrativo y control

### 10.1 Secuencia operacional del proceso

1. **Recepcion y preparacion de alimentacion:** grano + agua de extraccion (1:12) se acondicionan para formar lodo de extraccion.
2. **Extraccion alcalina (TK-101/AG-101):** se controla pH 8.75 y 55 C para maximizar proteina disuelta.
3. **Separacion post-lixiviacion (CF-102A/B):** se separa okara humedo y extracto proteico.
4. **Neutralizacion y pasteurizacion (HX-201):** el extracto se ajusta y se lleva a 80 C por 22 s con recuperacion termica.
5. **Concentracion (EV-301A/B):** evaporacion en doble efecto para alcanzar 23% de solidos.
6. **Precipitacion isoelectrica:** ajuste de pH a zona de precipitacion para recuperar proteina.
7. **Centrifugacion final (CF-401):** separacion de pasta proteica con 50% de humedad.
8. **Secado por atomizacion (SD-501):** reduccion de humedad final a 5%.
9. **Molienda y clasificacion (ML-601/CR-601):** ajuste granulometrico final de producto.

### 10.2 Lazos de control recomendados

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

### 10.3 Alarmas e interlocks minimos

1. Alta temperatura en tanque de extraccion (interlock de corte de calefaccion).
2. Alta presion diferencial en intercambiador (alarma de posible ensuciamiento hidraulico).
3. Perdida de vacio en evaporador (interlock de reduccion de carga termica).
4. Alta temperatura de salida en spray dryer (interlock de seguridad de producto/equipo).
5. Vibracion alta en centrifugas o criba (interlock de parada controlada).

### 10.4 PFD visual integrado del proceso

Para la representacion visual integrada del proceso completo (equipos, corrientes principales y nodo de operacion innovadora), ver:

- [PFD_Integrado.md](PFD_Integrado.md)

Resumen de integracion del PFD visual:

1. La operacion innovadora de OI se ubica entre separacion post-lixiviacion y evaporacion.
2. El permeado de OI se deriva a tanque de agua de servicio/CIP no critico.
3. El retentado de OI alimenta EV-301A/B para completar concentracion termica.
4. El resto del tren (precipitacion, centrifugacion final, secado, molienda y envasado) mantiene la secuencia del caso base.

---

## 11. Presentacion de ingenieria: Matriz de criticidad

### 11.1 Criticidad de variables operativas

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

### 11.2 Priorizacion de seguimiento operativo

1. **Prioridad 1 (criticas):** pH extraccion, vacio evaporador, % solidos evaporador, T spray dryer, humedad final.
2. **Prioridad 2 (importantes):** DeltaP intercambiador, G de centrifugas, pH de precipitacion.
3. **Prioridad 3 (soporte):** variables de molienda y clasificacion final.

### 11.3 Analisis de ventas

Base economica tomada del caso actual:

- Produccion anual de polvo: 2,916,800 kg/ano
- OPEX total anual: 4,959,920 USD/ano
- Tipo de cambio: 1 USD = 6.96 Bs

Precio minimo de equilibrio (sin utilidad):

$$
P_{eq} = \frac{OPEX_{anual}}{M_{polvo,anual}} = \frac{4{,}959{,}920}{2{,}916{,}800} = 1.70\ \text{USD/kg}
$$

$$
P_{eq,Bs} = 1.70\cdot6.96 = 11.83\ \text{Bs/kg}
$$

Para evaluar viabilidad comercial se proponen tres escenarios de precio de venta:

| Escenario | Precio de venta (USD/kg) | Precio de venta (Bs/kg) | Ingreso anual (USD) | Utilidad operativa anual (USD) | Margen operativo (%) |
|---|---:|---:|---:|---:|---:|
| Conservador | 2.20 | 15.31 | 6,416,960 | 1,457,040 | 22.7 |
| Base | 2.60 | 18.10 | 7,583,680 | 2,623,760 | 34.6 |
| Alto | 3.00 | 20.88 | 8,750,400 | 3,790,480 | 43.3 |

Donde:

$$
Ingreso = P_{venta}\cdot M_{polvo,anual}
$$

$$
Utilidad\ operativa = Ingreso - OPEX_{anual}
$$

$$
Margen\ operativo = \frac{Utilidad\ operativa}{Ingreso}\cdot100
$$

Conclusiones de viabilidad preliminar:

1. El proyecto es viable siempre que el precio de venta promedio sea mayor a 1.70 USD/kg de polvo.
2. Un precio de 2.60 USD/kg genera margen operativo de 34.6%, suficiente para absorber gastos no incluidos en este modelo preliminar (depreciacion, impuestos, financieros).
3. La rentabilidad es altamente sensible al precio de mercado de la soya y al precio final del aislado.

---

## 12. Presentacion de ingenieria: Riesgos y mitigacion

### 12.1 Criterio de evaluacion

Se adopta una matriz cualitativa 3x3:

- Probabilidad: Baja (B), Media (M), Alta (A)
- Impacto: Bajo (B), Medio (M), Alto (A)
- Nivel de riesgo inicial: Bajo, Medio, Alto

### 12.2 Matriz de riesgos y mitigacion

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

### 12.3 Plan de accion priorizado

1. **Corto plazo (0-3 meses):** formalizar limites operativos, responsables por indicador y frecuencia de seguimiento diaria/turno.
2. **Mediano plazo (3-6 meses):** fortalecer mantenimiento preventivo de centrifugas, vacio y secador; estandarizar rutinas CIP.
3. **Largo plazo (6-12 meses):** consolidar estrategia comercial de precio minimo, contratos de soya y tablero integral de riesgos.

### 12.4 Riesgos economicos clave vinculados a ventas

1. Si el precio de venta cae por debajo de USD 1.70/kg, el proyecto entra en zona de no equilibrio operativo.
2. Si el costo de soya sube sin ajuste de precio de venta, el margen operativo se reduce de forma directa.
3. La mitigacion economica principal es gestionar simultaneamente precio de compra (soya) y precio neto de venta del aislado.

---

## 13. Especificaciones de envasado y estrategia de entrega

### 13.1 Especificaciones de envasado final

| Parametro | Especificacion de diseno | Criterio tecnico |
|---|---|---|
| Tipo de empaque primario | Bolsa laminada tricapa (PE/Al/PEBD) | Alta barrera a humedad, oxigeno y luz |
| Peso neto por unidad | 20 kg (formato industrial) | Manejo logistico y trazabilidad por lote |
| Sistema de cierre | Termosellado continuo, sello >= 4 mm | Integridad mecanica en transporte |
| Empaque secundario | Saco externo kraft multicapa | Proteccion mecanica adicional |
| Inertizacion | Purga opcional con N2 en linea de llenado | Reduce oxidacion y mantiene calidad |

### 13.2 Criterios de calidad y trazabilidad de lote

Campos minimos en etiqueta:

- Codigo de lote (fecha-turno-secuencia)
- Fecha de produccion y vencimiento
- % proteina y % humedad
- Peso neto y condiciones de almacenamiento

Criterio operativo de liberacion:

1. Humedad final <= 5.0%.
2. Integridad de sello conforme a inspeccion de linea.
3. Registro de lote completo (materia prima -> producto final).

### 13.3 Almacenamiento en planta y despacho

| Variable | Especificacion | Motivo |
|---|---|---|
| Temperatura de almacen | 15-25 C | Estabilidad fisicoquimica |
| Humedad relativa | <= 60% | Evitar aglomeracion del polvo |
| Rotacion | FIFO | Minimizar envejecimiento de inventario |
| Estiba | Pallets con separacion de piso y pared | Control sanitario y ventilacion |

### 13.4 Estrategia de entrega del producto final

1. Consolidar despacho por lotes trazables con COA (certificado de analisis).
2. Priorizar transporte cubierto y seco para preservar humedad objetivo.
3. Aplicar inspeccion de recepcion en cliente para validar integridad de empaque y etiqueta.
4. Mantener canal de retroalimentacion lote-cliente para gestion rapida de no conformidades.

---

## 14. Referencias internas

- Formulario.md
- Planteamiento.md
- Variables de operacion.md
- Sintesis.md
- PFD_Integrado.md
- Implementacion_Hidraulica.md

---

## 15. Anexo de bibliografia consultada

Este anexo consolida las fuentes tecnicas consultadas para sustentar criterios de proceso, propiedades de materia prima, supuestos operativos y contexto economico preliminar.

### 15.1 Fuentes internas del repositorio

1. `PROYECTO_FINAL_UNITARIOS/docs/Variables de operacion.md`  
  Base de variables operativas por etapa, rangos de pH, temperatura y caudales de referencia.
2. `PROYECTO_FINAL_UNITARIOS/docs/Formulario.md`  
  Apoyo de ecuaciones y relacion de calculos usados en balances y diseno preliminar.
3. `PROYECTO_FINAL_UNITARIOS/docs/Planteamiento.md`  
  Alcance del proyecto, criterios de entrega y estructura de objetivos.
4. `PROYECTO_FINAL_UNITARIOS/docs/Sintesis.md`  
  Consolidacion narrativa para coherencia tecnica del caso base.
5. `PROYECTO_FINAL_UNITARIOS/docs/PFD_Integrado.md`  
  Representacion visual del tren de proceso y nodo de innovacion OI.

### 15.2 Fuentes tecnicas web consultadas

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

### 15.3 Criterio de calidad de fuentes y trazabilidad

1. Prioridad alta: organismos tecnicos/institucionales (FAO, NIST, World Bank).
2. Prioridad media: entradas de referencia enciclopedica usadas solo como soporte contextual y no como unica base de diseno.
3. Prioridad interna: documentos del repositorio para coherencia de supuestos y continuidad academica del proyecto.
4. Fecha de consulta web para todas las URLs anteriores: **18 marzo 2026**.

---

**Version:** 1.6  
**Fecha:** Marzo 2026  
**Caso base:** Produccion de proteina aislada de soya a 1 ton/h de grano  
**Notas de modelado:** eficiencia global 90%, evaporacion en 2 efectos, sin ensuciamiento, inclusion de OI preliminar, especificaciones de envasado/entrega y anexo bibliografico web + repositorio.
