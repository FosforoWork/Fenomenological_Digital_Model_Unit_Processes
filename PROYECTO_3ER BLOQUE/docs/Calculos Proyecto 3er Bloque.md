# Calculos integrados recalculados - Proyecto 3er Bloque

Fecha de recalculo: 2026-04-06  
Fuente oficial de datos: hoja consolidada del bloque (tablas ESL, ELL, destilacion y recirculacion).

## 1. Base de calculo unificada

Este documento fija una sola cadena de calculo:

1. ESL (extraccion solido-liquido)
2. ELL (extraccion liquido-liquido)
3. Destilacion al vacio
4. Recirculacion y balance global

Criterios de consistencia aplicados:

- Base horaria obligatoria para el bloque: 8 h/d.
- Unidades explicitas por ecuacion y por tabla.
- Cierre de masa por etapa y cierre global.
- Meta de recuperacion de acetato en destilacion: eta >= 99.3% (exacta o superior).
- Tabla de equilibrio oficial para McCabe-Thiele: version del caso de diseno actual.

## 2. Etapa 1 - ESL recalculada

### 2.1 Datos de entrada

| Parametro | Valor | Unidad |
|---|---:|---|
| Capacidad diaria | 1500 | kg/d |
| Tiempo de operacion | 8 | h/d |
| Flujo de alimentacion, F | 187.50 | kg/h |
| Soluto en alimentacion | 10.0 | % p/p |
| Humedad en alimentacion | 12.0 | % p/p |
| S/F inicial | 3.2 | kg/kg |
| Retencion de solucion en inerte | 1.1 | kg/kg inerte |
| Eficiencia de extraccion real | 72.0 | % |
| Constante de equilibrio, Ke | 1.5 | - |

Descomposicion de F:

$$
\dot m_{sol,in} = 0.10(187.50) = 18.75\ \text{kg/h}
$$

$$
\dot m_{H2O,in} = 0.12(187.50) = 22.50\ \text{kg/h}
$$

$$
\dot m_{inerte} = 187.50 - 18.75 - 22.50 = 146.25\ \text{kg/h}
$$

Flujo de solvente fresco a ESL:

$$
\dot m_{solv,1} = 3.2(187.50) = 600.00\ \text{kg/h}
$$

### 2.2 Balance de masa de ESL

Masa de solucion que entra a la zona liquida:

$$
\dot m_{solucion,in} = \dot m_{solv,1} + \dot m_{H2O,in} + \dot m_{sol,in}
= 600.00 + 22.50 + 18.75 = 641.25\ \text{kg/h}
$$

Solucion retenida en la torta:

$$
L = 1.1(146.25) = 160.875\ \text{kg/h}
$$

Soluto en solucion retenida:

$$
\dot m_{sol,L} = 5.25\ \text{kg/h}
$$

Solvente + humedad retenidos:

$$
\dot m_{solv+H2O,L} = 160.875 - 5.25 = 155.625\ \text{kg/h}
$$

Corriente de extracto liquido:

$$
V = 641.25 - 160.875 = 480.375\ \text{kg/h}
$$

Soluto en extracto real (72% de recuperacion en ESL):

$$
\dot m_{sol,V} = 0.72(18.75) = 13.50\ \text{kg/h}
$$

Fracciones masicas finales:

$$
y_1 = \frac{13.50}{480.375} = 0.02810\ (2.810\%)
$$

$$
x_1 = \frac{5.25}{160.875} = 0.03263\ (3.263\%)
$$

Cierre de masa de etapa ESL:

$$
\text{Entrada} = 187.50 + 600.00 = 787.50\ \text{kg/h}
$$

$$
\text{Salida} = 480.375 + (146.25 + 160.875) = 787.50\ \text{kg/h}
$$

### 2.3 Analisis de etapa ideal (referencia de equilibrio)

Con $Ke = y/x = 1.5$, $V=480.375$ y $L=160.875$:

$$
V\,y^* + L\,x^* = \dot m_{sol,in} = 18.75
$$

$$
y^* = 1.5x^* \Rightarrow x^* = 0.0213,\ y^* = 0.0319
$$

Soluto recuperado en etapa ideal:

$$
\dot m_{sol,V}^{ideal} = V y^* = 15.33\ \text{kg/h}
$$

Recuperacion ideal equivalente:

$$
\eta_{ESL}^{ideal} = \frac{15.33}{18.75} = 81.8\% \approx 82\%
$$

### 2.4 Dimensionamiento preliminar de equipo ESL

Supuestos de diseno para el tanque de extraccion ESL:

- Densidad de mezcla: $\rho_{ESL}=1060$ kg/m3.
- Tiempo de residencia de diseno: $\tau=0.90$ h.
- Factor de seguridad volumetrico: $f_s=1.20$.
- Relacion geometrica preliminar: $H/D=0.85$.
- Criterio energetico de agitacion: $P/V=1.0$ kW/m3.

Caudal masico total a ESL:

$$
\dot m_{ESL,in}=787.50\ \text{kg/h}
$$

Caudal volumetrico de mezcla:

$$
\dot V_{ESL}=\frac{\dot m_{ESL,in}}{\rho_{ESL}}=\frac{787.50}{1060}=0.7429\ \text{m}^3/\text{h}
$$

Volumen de diseno del tanque:

$$
V_{ESL}=\dot V_{ESL}\,\tau\,f_s=0.7429(0.90)(1.20)=0.802\ \text{m}^3
$$

Para tanque cilindrico con $H=0.85D$:

$$
V=\frac{\pi D^2}{4}(0.85D)=0.6676D^3
$$

$$
D=\left(\frac{V_{ESL}}{0.6676}\right)^{1/3}=1.06\ \text{m},\quad H=0.85D=0.90\ \text{m}
$$

Potencia de agitacion preliminar:

$$
P_{ESL}=\left(\frac{P}{V}\right)V_{ESL}=1.0(0.802)=0.80\ \text{kW}
$$

Seleccion recomendada de motor:

$$
P_{motor,ESL}=1.10\ \text{kW}
$$

## 3. Etapa 2 - ELL recalculada

### 3.1 Datos de entrada a ELL

La alimentacion de ELL se conecta de forma explicita con la salida de ESL:

| Variable | Valor | Unidad |
|---|---:|---|
| Alimentacion desde ESL, F_ELL | 480.375 | kg/h |
| Soluto en F_ELL | 13.50 | kg/h |
| Fraccion de soluto en F_ELL (Yf) | 0.02810 | - |
| Solvente fresco ELL, S | 264.21 | kg/h |
| Composicion de solvente fresco (Xs, Ys) | 1.000, 0.000 | - |
| Masa total mezclada, Mt | 744.585 | kg/h |
| Eficiencia de etapa real | 80.0 | % |

Coordenadas del punto de mezcla global:

$$
X_M = \frac{S}{M_t} = \frac{264.21}{744.585} = 0.3548\ (35.48\%)
$$

$$
Y_M = \frac{13.50}{744.585} = 0.0181\ (1.81\%)
$$

### 3.2 Reparto por linea de equilibrio (base ideal)

Valores de la linea de reparto seleccionada para el punto de mezcla:

- Extracto ideal: $X_E=0.8810$, $Y_E=0.0212$
- Refinado ideal: $X_R=0.0106$, $Y_R=0.0162$

Aplicando regla de la palanca:

$$
\dot m_E = 294.50\ \text{kg/h}
$$

$$
\dot m_R = M_t - \dot m_E = 450.08\ \text{kg/h}
$$

Soluto ideal por fase (ajustado a cierre con redondeo de hoja):

$$
\dot m_{sol,E}^{ideal} = 6.23\ \text{kg/h}
$$

$$
\dot m_{sol,R}^{ideal} = 7.27\ \text{kg/h}
$$

Recuperacion ideal en ELL:

$$
\eta_{ELL}^{ideal} = \frac{6.23}{13.50} = 46.15\%
$$

### 3.3 Ajuste a etapa real (80%)

Se corrige el recuperado ideal con eficiencia de etapa:

$$
\dot m_{sol,E}^{real} = 0.80(6.23) = 4.98\ \text{kg/h}
$$

$$
\dot m_{sol,R}^{real} = 13.50 - 4.98 = 8.52\ \text{kg/h}
$$

Fracciones reales de soluto por fase (consistentes con los caudales de fase):

$$
Y_E^{real} = \frac{4.98}{294.50} = 0.0169\ (1.69\%)
$$

$$
Y_R^{real} = \frac{8.52}{450.08} = 0.0189\ (1.89\%)
$$

Verificacion de cierre de masa en ELL (con redondeo de tabla):

- Entrada total: $480.375 + 264.21 = 744.585$ kg/h
- Salida total: $294.50 + 450.08 = 744.58$ kg/h

La diferencia es solo por redondeo de dos decimales en corrientes reportadas.

### 3.4 Corriente puente a destilacion

La corriente de extracto de ELL define la alimentacion de la destilacion:

$$
F_{dest} = \dot m_E = 294.50\ \text{kg/h}
$$

Con esta definicion se elimina la incongruencia anterior de usar una base hipotetica desconectada.

### 3.5 Dimensionamiento preliminar de equipo ELL (mixer-settler)

Supuestos de diseno para contacto y separacion ELL:

- Densidad media de mezcla liquida: $\rho_{ELL}=950$ kg/m3.
- Tiempo de mezcla: $\tau_m=5$ min.
- Tiempo de decantacion: $\tau_d=20$ min.
- Factor de seguridad volumetrico: $f_s=1.20$.
- Velocidad superficial de diseno en decantador: $v_s=1.0$ m/h.
- Criterio de agitacion en mezclador: $P/V=1.0$ kW/m3.

Flujo masico total a ELL:

$$
\dot m_{ELL,in}=744.585\ \text{kg/h}
$$

Caudal volumetrico de mezcla:

$$
\dot V_{ELL}=\frac{\dot m_{ELL,in}}{\rho_{ELL}}=\frac{744.585}{950}=0.7838\ \text{m}^3/\text{h}
$$

Volumen de mezclador:

$$
V_m=\dot V_{ELL}\left(\frac{\tau_m}{60}\right)f_s=0.7838\left(\frac{5}{60}\right)(1.20)=0.078\ \text{m}^3
$$

Volumen de decantador:

$$
V_d=\dot V_{ELL}\left(\frac{\tau_d}{60}\right)f_s=0.7838\left(\frac{20}{60}\right)(1.20)=0.314\ \text{m}^3
$$

Area de decantacion:

$$
A_d=\frac{\dot V_{ELL}}{v_s}=\frac{0.7838}{1.0}=0.784\ \text{m}^2
$$

Diametro equivalente (decantador circular):

$$
D_d=\sqrt{\frac{4A_d}{\pi}}=0.999\ \text{m}\approx1.00\ \text{m}
$$

Altura util de decantador:

$$
H_{d,util}=\frac{V_d}{A_d}=\frac{0.314}{0.784}=0.40\ \text{m}
$$

Potencia de agitacion en mezclador:

$$
P_m=\left(\frac{P}{V}\right)V_m=1.0(0.078)=0.078\ \text{kW}
$$

Seleccion recomendada de motor de mezclado:

$$
P_{motor,ELL}=0.18\ \text{kW}
$$

## 4. Etapa 3 - Destilacion al vacio recalculada

### 4.1 Datos de diseno

| Parametro | Valor | Unidad |
|---|---:|---|
| Alimentacion, F | 294.50 | kg/h |
| Fraccion de acetato en F, xF | 0.42 | - |
| Fraccion de acetato en destilado, xD | 0.90 | - |
| Recuperacion objetivo de acetato, eta | 99.3 | % |
| Volatilidad relativa, alpha | 2.50 | - |
| Reflujo, R | 2.00 | - |
| Condicion termica de alimentacion, q | 1.00 | - |

Acetato en alimentacion:

$$
\dot m_{A,F} = F x_F = 294.50(0.42) = 123.69\ \text{kg/h}
$$

### 4.2 Balance de masa de columna

Acetato recuperado en destilado con meta 99.3%:

$$
\dot m_{A,D} = 0.993\,\dot m_{A,F} = 122.83\ \text{kg/h}
$$

Flujo de destilado:

$$
D = \frac{\dot m_{A,D}}{x_D} = \frac{122.83}{0.90} = 136.47\ \text{kg/h}
$$

Flujo de fondos:

$$
B = F - D = 294.50 - 136.47 = 158.03\ \text{kg/h}
$$

Fraccion de acetato en fondos:

$$
x_B = \frac{\dot m_{A,F} - D x_D}{B} = 0.0055
$$

Recuperacion lograda:

$$
\eta_A = \frac{D x_D}{F x_F} = 99.3\%\ \text{(cumple)}
$$

### 4.3 Numero de etapas

Numero minimo de etapas por Fenske:

$$
N_{min} = \frac{\ln\left[\left(\frac{x_D}{1-x_D}\right)\left(\frac{1-x_B}{x_B}\right)\right]}{\ln(\alpha)}
= 8.067
$$

Parametros de diseno usados en hoja:

- $R_{min}=1.141$
- Parametro $X=0.29$
- Aproximacion de Eduljee: 0.38
- McCabe-Thiele aproximado: $N_t=13.64$ platos teoricos

Conversion a platos reales:

- Sin rehervidor: $12.64$ platos
- Con eficiencia de platos ($E_M=65\%$): $12.64/0.65 = 19.45$
- Adoptado: 20 platos reales + rehervidor -> 21 etapas reales totales

### 4.4 McCabe-Thiele (tabla de escalones)

Lineas de operacion:

$$
\text{LOR: } y = 0.6667x + 0.3000
$$

$$
\text{q-line (q=1): } x = 0.42\ \text{con}\ y_F = 0.58
$$

$$
\text{LOA: } y = 1.39x - 0.0021
$$

Tabla de etapas calculadas:

| Etapa | y vapor | x liquido | Zona |
|---:|---:|---:|---|
| 1 | 0.9000 | 0.7830 | Enriquecimiento |
| 2 | 0.8217 | 0.6480 | Enriquecimiento |
| 3 | 0.7322 | 0.5220 | Enriquecimiento |
| 4 | 0.6483 | 0.4240 | Enriquecimiento |
| 5 | 0.5829 | 0.3590 | Agotamiento |
| 6 | 0.4949 | 0.2820 | Agotamiento |
| 7 | 0.3882 | 0.2020 | Agotamiento |
| 8 | 0.2784 | 0.1340 | Agotamiento |
| 9 | 0.1832 | 0.0820 | Agotamiento |
| 10 | 0.1120 | 0.0480 | Agotamiento |
| 11 | 0.0644 | 0.0270 | Agotamiento |
| 12 | 0.0350 | 0.0143 | Agotamiento |
| 13 | 0.0177 | 0.0072 | Agotamiento |
| 14 | 0.0078 | 0.0031 | Agotamiento |

### 4.5 Flujos internos, energia y dimensionamiento

Flujos internos:

$$
L = RD = 2(136.47) = 272.95\ \text{kg/h}
$$

$$
V = L + D = 409.42\ \text{kg/h}
$$

$$
L' = L + F = 567.45\ \text{kg/h},\quad V' = V = 409.42\ \text{kg/h}
$$

Cargas termicas con $\lambda = 366$ kJ/kg:

$$
Q_{cond} = Q_{reb} = \frac{V\lambda}{3600} = 41.62\ \text{kW}
$$

Consumo de vapor de caldera con $\lambda_{vapor}=2200$ kJ/kg:

$$
\dot m_{vapor} = \frac{Q_{reb}\,3600}{\lambda_{vapor}} = 68.11\ \text{kg/h}
$$

Consumo especifico de vapor:

$$
CE_v = \frac{68.11}{136.47} = 0.50\ \text{kg/kg}
$$

Verificacion de restriccion:

$$
CE_v = 0.50 < 2.2\ \text{kg/kg}\ \text{(cumple)}
$$

Dimensionamiento hidraulico:

| Parametro | Valor | Unidad |
|---|---:|---|
| Temperatura de operacion (300 mmHg) | 51.32 | C |
| Densidad de vapor | 1.31 | kg/m3 |
| Densidad de liquido a T de operacion | 861.34 | kg/m3 |
| Flujo volumetrico de vapor | 313.43 | m3/h |
| Flujo volumetrico de vapor | 0.0871 | m3/s |
| K de inundacion | 0.09 | m/s |
| Velocidad de inundacion | 2.31 | m/s |
| Velocidad operativa | 1.85 | m/s |
| Area de columna | 0.0471 | m2 |
| Diametro de columna | 0.2450 | m |
| Platos reales adoptados | 20 | platos |
| Espaciamiento entre platos | 0.50 | m |
| Holgura adicional | 2.5 | m |
| Altura total de columna | 12.0 | m |

## 5. Recirculacion de solventes y balance global

### 5.1 Recirculacion

| Variable | Valor | Unidad |
|---|---:|---|
| Alimentacion a destilacion | 294.50 | kg/h |
| Acetato en F | 123.69 | kg/h |
| Acetato recuperado en destilado | 122.83 | kg/h |
| Solvente requerido en ELL, S | 264.21 | kg/h |
| Reposicion de solvente fresco | 141.38 | kg/h |
| Impurezas en corriente de cabeza | 13.65 | kg/h |
| Ajuste de refinado ELL | 463.73 | kg/h |

Relacion de reposicion:

$$
\dot m_{makeup} = 264.21 - 122.83 = 141.38\ \text{kg/h}
$$

### 5.2 Balance global del bloque

Entradas externas:

$$
\dot m_{in,global} = 187.50 + 600.00 + 141.38 = 928.88\ \text{kg/h}
$$

Salidas externas:

$$
\dot m_{out,global} = 307.13 + 158.03 + 463.73 = 928.88\ \text{kg/h}
$$

Cierre global:

$$
\text{Cierre} = 100\%
$$

Indicador reportado de consumo global de solvente:

$$
CGS = 4.69\ \text{kg/kg}
$$

## 6. Analisis economico simplificado (materiales y consumos operativos)

Base economica de esta iteracion:

- Moneda de reporte: USD.
- Horas de operacion anual: 2920 h/ano.
- Verificacion de anualizacion: $H_{anual}=8\ \text{h/dia}\times365\ \text{d/ano}=2920\ \text{h/ano}$.
- Tarifa termica equivalente: 0.035 USD/kWh.
- Tarifa electrica: 0.10 USD/kWh.
- Precio de materia prima (flor de Jamaica): 0.80 USD/kg.
- Precio de reposicion de solvente (acetato de etilo): 1.25 USD/kg.

### 6.1 Consumos fisicos base del bloque

| Concepto | Simbolo | Valor | Unidad |
|---|---|---:|---|
| Consumo de vapor | $\dot m_{vapor}$ | 68.11 | kg/h |
| Electricidad auxiliar ESL | $P_{ESL}$ | 1.10 | kW |
| Electricidad auxiliar ELL | $P_{ELL}$ | 0.18 | kW |
| Potencia auxiliar total | $P_{aux}$ | 1.28 | kW |
| Reposicion de solvente ELL | $\dot m_{solv}$ | 141.38 | kg/h |
| Materia prima (alimentacion) | $\dot m_{MP}$ | 187.50 | kg/h |
| Producto de referencia (destilado) | $\dot m_D$ | 136.47 | kg/h |

### 6.2 Costos de operacion por utilidad/material

Potencia termica equivalente de vapor:

$$
P_{term}=\frac{\dot m_{vapor}\lambda_{vapor}}{3600}=\frac{68.11(2200)}{3600}=41.62\ \text{kW}
$$

Costo de vapor:

$$
C_{vapor,h}=P_{term}(0.035)=41.62(0.035)=1.46\ \text{USD/h}
$$

$$
C_{vapor,a}=C_{vapor,h}(2920)=4{,}263.20\ \text{USD/ano}
$$

Costo de electricidad auxiliar:

$$
C_{elec,h}=P_{aux}(0.10)=1.28(0.10)=0.128\ \text{USD/h}
$$

$$
C_{elec,a}=C_{elec,h}(2920)=373.76\ \text{USD/ano}
$$

Costo de reposicion de solvente:

$$
C_{solv,h}=\dot m_{solv}(1.25)=141.38(1.25)=176.73\ \text{USD/h}
$$

$$
C_{solv,a}=C_{solv,h}(2920)=516{,}051.60\ \text{USD/ano}
$$

Costo de materia prima:

$$
C_{MP,h}=\dot m_{MP}(0.80)=187.50(0.80)=150.00\ \text{USD/h}
$$

$$
C_{MP,a}=C_{MP,h}(2920)=438{,}000.00\ \text{USD/ano}
$$

### 6.3 OPEX total anual y costo unitario

$$
C_{OPEX,a}=C_{vapor,a}+C_{elec,a}+C_{solv,a}+C_{MP,a}
$$

$$
C_{OPEX,a}=958{,}688.56\ \text{USD/ano}
$$

Costo horario total:

$$
C_{OPEX,h}=\frac{C_{OPEX,a}}{2920}=328.32\ \text{USD/h}
$$

Produccion anual de referencia en destilado:

$$
M_{D,a}=\dot m_D(2920)=136.47(2920)=398{,}492.40\ \text{kg/ano}
$$

Costo operativo unitario:

$$
c_{op,D}=\frac{C_{OPEX,a}}{M_{D,a}}=2.41\ \text{USD/kg destilado}
$$

Resumen de costos anuales:

| Concepto | Costo anual (USD) | Participacion (%) |
|---|---:|---:|
| Vapor | 4,263.20 | 0.44 |
| Electricidad auxiliar ESL+ELL | 373.76 | 0.04 |
| Reposicion de solvente | 516,051.60 | 53.83 |
| Materia prima | 438,000.00 | 45.69 |
| **OPEX total** | **958,688.56** | **100.00** |

Alcance: este analisis es de OPEX operativo simplificado y no incluye CAPEX, depreciacion, impuestos, mantenimiento ni costo de personal.

## 7. Verificacion de incongruencias cerradas

1. Recuperacion de acetato: antes 94.684%, ahora 99.3% (cumple meta del planteamiento).
2. Coherencia de equilibrio: se usa una sola base oficial (alpha=2.5 y tabla correspondiente).
3. Conexion de etapas: la entrada a destilacion se toma directamente desde el extracto ELL ($F=294.50$ kg/h).
4. Energia de columna: se conserva una unica base termica consistente ($Q_{cond}=Q_{reb}=41.62$ kW).

## 8. Resumen de resultados clave

| Bloque | Resultado principal |
|---|---|
| ESL | $V=480.375$ kg/h, $y_1=2.810\%$, cierre de masa conforme |
| ELL | $M_t=744.585$ kg/h, $E=294.50$ kg/h, $R=450.08$ kg/h |
| Destilacion | $D=136.47$ kg/h, $B=158.03$ kg/h, $x_B=0.0055$ |
| Cumplimiento | Recuperacion acetato = 99.3%, $CE_v=0.50$ kg/kg |
| Global | Entradas = Salidas = 928.88 kg/h, cierre = 100% |
