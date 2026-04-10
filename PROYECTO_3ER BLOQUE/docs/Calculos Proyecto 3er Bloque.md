# Calculos integrados recalculados - Proyecto 3er Bloque

Fecha de recalculo: 2026-04-10  
Fuente oficial de datos: hoja consolidada del bloque (tablas ESL, ELL, dos destilaciones y recirculacion).

## 1. Base de calculo unificada

Este documento fija una sola cadena de calculo para el caso integrado:

1. ESL (extraccion solido-liquido)
2. ELL (extraccion liquido-liquido)
3. Destilacion 1: Etanol-Agua (desde refinado ELL)
4. Destilacion 2: Acetato-Flor de Jamaica (desde extracto ELL)
5. Recirculacion dual y balance global
6. Analisis economico simplificado

Criterios de consistencia aplicados:

- Base horaria obligatoria para el bloque: 8 h/d.
- Unidades explicitas por ecuacion y por tabla.
- Cierre de masa por etapa y cierre global.
- Trazabilidad explicita de corrientes ELL -> Destilacion 1 y ELL -> Destilacion 2.
- Conservacion de los valores de hoja cuando una misma etapa reporta simultaneamente base composicional y base de masa de soluto.

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

### 3.2 Punto de mezcla y linea de reparto

Coordenadas del punto de mezcla global (base grafica de hoja):

$$
X_M = \frac{S}{M_t} = \frac{264.21}{744.585} = 0.3548\ (35.48\%)
$$

$$
Y_M = \frac{13.50}{744.585} = 0.0181\ (1.81\%)
$$

Valores reportados de la linea de reparto usada en la hoja:

- Punto de mezcla: $M=(35.484,\ 1.813)$
- Extracto grafico: $E=(88.0961,\ 2.1154)$
- Refinado grafico: $R=(1.0577,\ 1.6154)$

Con regla de la palanca reportada:

$$
\dot m_E = 294.50\ \text{kg/h},\qquad \dot m_R = 450.08\ \text{kg/h}
$$

### 3.3 Parametros ELL de etapa real (base de hoja)

| Parametro ELL (etapa real) | Valor | Unidad |
|---|---:|---|
| Punto de mezcla global (X) | 35.48 | % |
| Punto de mezcla global (Y) | 1.81 | % |
| Masa total (Mt) | 744.58 | kg/h |
| Corriente de extracto (E) | 294.50 | kg/h |
| Solvente en extracto real (Xe) | 88.10 | % |
| Soluto en extracto real (Ye) | 2.12 | % |
| Masa soluto en extracto ideal | 6.23 | kg/h |
| Masa soluto en extracto real | 4.98 | kg/h |
| Corriente de refinado (R) | 450.08 | kg/h |
| Solvente en refinado real (Xr) | 1.06 | % |
| Soluto en refinado real (Yr) | 1.62 | % |
| Masa soluto en refinado ideal | 7.27 | kg/h |
| Masa soluto en refinado real | 8.52 | kg/h |

Nota de trazabilidad: se conserva simultaneamente la base composicional (Xe, Ye, Xr, Yr) y la base de masas de soluto (ideal/real) tal como fue entregada en la hoja consolidada.

### 3.4 Corrientes puente a destilacion dual

Desde ELL se definen dos alimentaciones de destilacion:

$$
F_{dest,EA} = \dot m_R = 450.08\ \text{kg/h}
$$

$$
F_{dest,AC} = \dot m_E = 294.50\ \text{kg/h}
$$

Con esta definicion se mantiene una conexion fisica explicita entre etapas.

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

Potencia de agitacion en mezclador:

$$
P_m=\left(\frac{P}{V}\right)V_m=1.0(0.078)=0.078\ \text{kW}
$$

Seleccion recomendada de motor de mezclado:

$$
P_{motor,ELL}=0.18\ \text{kW}
$$

## 4. Etapa 3A - Destilacion etanol-agua (desde refinado ELL)

### 4.1 Datos de diseno

| Parametro | Valor | Unidad |
|---|---:|---|
| Alimentacion, F | 450.08 | kg/h |
| Fraccion de etanol en F, xF | 0.42 | - |
| Fraccion de etanol en destilado, xD | 0.90 | - |
| Recuperacion de etanol | 0.9468 | - |
| Fraccion de etanol en fondos, xB | 0.0400 | - |
| Volatilidad relativa, alpha | 3.39 | - |
| Reflujo, R | 0.79 | - |
| Reflujo minimo, Rmin | 0.53 | - |
| Condicion termica de alimentacion, q | 1.00 | - |

Etanol en alimentacion:

$$
\dot m_{EtOH,F} = F x_F = 450.08(0.42) = 189.03\ \text{kg/h}
$$

### 4.2 Balance de masa de columna

Flujos reportados:

$$
D = 198.87\ \text{kg/h},\qquad B = 251.21\ \text{kg/h}
$$

Etanol en destilado:

$$
\dot m_{EtOH,D} = D x_D = 198.87(0.90) = 178.98\ \text{kg/h}
$$

Recuperacion de etanol:

$$
\eta_{EtOH} = \frac{D x_D}{F x_F} = \frac{178.98}{189.03} = 0.9468\ (94.68\%)
$$

Fraccion de etanol en fondos (verificacion):

$$
x_B = \frac{F x_F - D x_D}{B} = 0.0400
$$

### 4.3 Numero de etapas y McCabe-Thiele

Numero minimo de etapas por Fenske (hoja):

$$
N_{min} = 4.402\ \text{platos}
$$

Resultados de diseno por hoja:

- Parametro de flujo: $X=0.1474$
- Aproximacion de Eduljee: $0.4966$
- Numero de etapas por McCabe-Thiele (aprox): $9.73$ platos teoricos
- Sin rehervidor: $8.73$ platos
- Con eficiencia de platos: $13.43$ platos
- Con rehervidor: $15.00$ platos reales totales

Lineas de operacion usadas en grafico:

$$
\text{LOR: } y = 0.44x + 0.50
$$

$$
\text{q-line (q=1): } x = 0.42\ \text{(interseccion en } y=0.688\text{)}
$$

$$
\text{LOA: } y = 1.70x - 0.0282
$$

Tabla de equilibrio usada (etanol-agua):

| x (liquido) | y (vapor) |
|---:|---:|
| 0.000 | 0.000 |
| 0.050 | 0.210 |
| 0.100 | 0.340 |
| 0.200 | 0.510 |
| 0.300 | 0.630 |
| 0.400 | 0.720 |
| 0.500 | 0.790 |
| 0.600 | 0.850 |
| 0.700 | 0.890 |
| 0.800 | 0.920 |
| 0.900 | 0.950 |
| 0.956 | 0.956 |

Tabla de escalonamiento reportada:

| Etapa | y vapor | x liquido | Fase |
|---:|---:|---:|---|
| 1 | 0.900 | 0.733 | Enriquecimiento |
| 2 | 0.826 | 0.560 | Enriquecimiento |
| 3 | 0.750 | 0.443 | Enriquecimiento |
| 4 | 0.698 | 0.375 | Agotamiento |
| 5 | 0.611 | 0.285 | Agotamiento |
| 6 | 0.457 | 0.169 | Agotamiento |
| 7 | 0.259 | 0.069 | Agotamiento |
| 8 | 0.089 | 0.021 | Agotamiento |

### 4.4 Flujos internos, energia y dimensionamiento

Flujos internos reportados:

| Seccion | Liquido (kg/h) | Vapor (kg/h) |
|---|---:|---:|
| Rectificacion | 157.70 | 356.58 |
| Agotamiento | 607.78 | 356.58 |

Dimensionamiento hidraulico (columna etanol-agua):

| Parametro | Valor | Unidad |
|---|---:|---|
| Temperatura de ebullicion agua-etanol | 351.35 | K |
| Temperatura de operacion (1 atm) | 78.20 | C |
| Presion | 1.00 | atm |
| Densidad de vapor | 1.50 | kg/m3 |
| Densidad de liquido a T operativa | 743.00 | kg/m3 |
| Flujo volumetrico de vapor | 237.62 | m3/h |
| Flujo volumetrico de vapor | 0.0660 | m3/s |
| K de inundacion | 0.09 | m/s |
| Velocidad de inundacion | 2.00 | m/s |
| Velocidad operativa | 1.60 | m/s |
| Area de columna | 0.0412 | m2 |
| Diametro de columna | 0.2291 | m |
| Platos reales adoptados | 15.00 | platos |
| Espaciamiento entre platos | 0.50 | m |
| Holgura adicional | 2.50 | m |
| Altura total de columna | 9.50 | m |

Resumen termico (hoja):

| Parametro | Valor | Unidad |
|---|---:|---|
| Calor en condensador | 89.10 | kW |
| Calor en rehervidor | 222.86 | kW |
| Masa de vapor de caldera | 364.68 | kg/h |
| Consumo especifico de vapor | 1.83 | kg/kg |

## 5. Etapa 3B - Destilacion acetato-flor de jamaica (desde extracto ELL)

### 5.1 Datos de diseno

| Parametro | Valor | Unidad |
|---|---:|---|
| Alimentacion, F | 294.50 | kg/h |
| Masa de acetato en F | 259.45 | kg/h |
| Masa de soluto en F | 6.23 | kg/h |
| xF reportado | 0.9766 | - |
| xD reportado | 0.9990 | - |
| Recuperacion objetivo | 0.993 | - |
| xB reportado | 0.0426 | - |
| Volatilidad relativa, alpha | 2.50 | - |
| Reflujo, R | 2.00 | - |

Constantes de Antoine para acetato de etilo (hoja):

| Constante | Valor |
|---|---:|
| A | 7.10179 |
| B | 1244.951 |
| C | 217.881 |

### 5.2 Balance de masa de columna

Flujos reportados:

$$
D = 257.89\ \text{kg/h},\qquad B = 36.62\ \text{kg/h}
$$

Recuperacion de acetato reportada:

$$
\eta_{Ac} = 99.3\%
$$

Se conserva la base composicional reportada de la hoja ($x_F$, $x_D$, $x_B$) para trazabilidad con la memoria original de calculo.

### 5.3 Numero de etapas y desempeno

Resultados de hoja para diseno de columna:

- Numero minimo de etapas (Fenske): $N_{min}=10.94$
- Reflujo minimo: $R_{min}=0.61$
- Parametro de flujo: $0.46$
- Aproximacion de Eduljee: $0.27$
- Numero de etapas teoricas: $15.24$
- Sin rehervidor: $14.24$ platos
- Con eficiencia de platos: $21.91$ platos
- Con rehervidor: $23.00$ etapas reales

### 5.4 Flujos internos, energia y dimensionamiento

Flujos internos reportados:

| Seccion | Liquido (kg/h) | Vapor (kg/h) |
|---|---:|---:|
| Rectificacion | 515.78 | 773.66 |
| Agotamiento | 810.28 | 773.66 |

Dimensionamiento hidraulico (columna acetato):

| Parametro | Valor | Unidad |
|---|---:|---|
| Temperatura de ebullicion acetato | 324.4669 | K |
| Temperatura de operacion (300 mmHg) | 51.32 | C |
| Presion reportada | 0.394736842 | mmHg |
| Densidad de vapor | 1.31 | kg/m3 |
| Densidad de liquido a T operativa | 861.34 | kg/m3 |
| Flujo volumetrico de vapor | 592.27 | m3/h |
| Flujo volumetrico de vapor | 0.1645 | m3/s |
| K de inundacion | 0.09 | m/s |
| Velocidad de inundacion | 2.31 | m/s |
| Velocidad operativa | 1.85 | m/s |
| Area de columna | 0.0891 | m2 |
| Diametro de columna | 0.3367 | m |
| Platos reales adoptados | 22.00 | platos |
| Espaciamiento entre platos | 0.50 | m |
| Holgura adicional | 2.50 | m |
| Altura total de columna | 13.00 | m |

Resumen termico (hoja):

| Parametro | Valor | Unidad |
|---|---:|---|
| Lambda de diseno | 366 | kJ/kg |
| Calor en condensador | 78.66 | kW |
| Calor en rehervidor | 78.66 | kW |

## 6. Recirculacion de solventes y balance global

### 6.1 Recuperacion de solventes

| Recuperacion Etanol-Agua | Valor | Unidad |
|---|---:|---|
| Solvente requerido | 600.00 | kg/h |
| Solvente recuperado | 198.87 | kg/h |
| Reposicion para ELL | 401.1283 | kg/h |

| Recuperacion Acetato | Valor | Unidad |
|---|---:|---|
| Solvente requerido | 264.21 | kg/h |
| Solvente recuperado | 257.89 | kg/h |
| Reposicion para ELL | 6.32 | kg/h |

Verificacion de reposicion:

$$
\dot m_{makeup,EA}=600.00-198.87=401.13\ \text{kg/h}
$$

$$
\dot m_{makeup,AC}=264.21-257.89=6.32\ \text{kg/h}
$$

### 6.2 Balance global del bloque

Balance global sin recirculacion interna (base de requerimientos de solvente):

| Indicador | Valor | Unidad |
|---|---:|---|
| Entradas globales | 1051.71 | kg/h |
| Salidas globales | 1051.71 | kg/h |
| Cierre | 100.00 | % |

Balance global con recirculacion cerrada (base de reposicion):

| Indicador | Valor | Unidad |
|---|---:|---|
| Entradas netas | 594.95 | kg/h |
| Salidas netas | 594.95 | kg/h |
| Cierre | 100.00 | % |

### 6.3 Indicador global de consumo de solvente

Consumo global de solvente (hoja):

$$
CGS=2.17\ \text{kg/kg}
$$

Una forma operativa coherente con la base del bloque es:

$$
CGS = \frac{\dot m_{makeup,EA}+\dot m_{makeup,AC}}{F_{ESL}}
=\frac{401.1283+6.32}{187.50}=2.17\ \text{kg/kg}
$$

## 7. Analisis economico simplificado (materiales y utilidades)

Base economica de esta iteracion:

- Moneda de reporte: USD.
- Horas de operacion anual: 2920 h/ano.
- Verificacion de anualizacion: $H_{anual}=8\ \text{h/dia}\times365\ \text{d/ano}=2920\ \text{h/ano}$.
- Tarifa termica equivalente: 0.035 USD/kWh.
- Tarifa electrica: 0.10 USD/kWh.
- Precio de materia prima (flor de Jamaica): 0.80 USD/kg.
- Precio de reposicion de solvente: 1.25 USD/kg.

### 7.1 Consumos fisicos base

| Concepto | Simbolo | Valor | Unidad |
|---|---|---:|---|
| Carga termica total en rehervidores | $Q_{reb,tot}$ | 301.52 | kW |
| Electricidad auxiliar ESL | $P_{ESL}$ | 1.10 | kW |
| Electricidad auxiliar ELL | $P_{ELL}$ | 0.18 | kW |
| Potencia auxiliar total | $P_{aux}$ | 1.28 | kW |
| Reposicion total de solvente | $\dot m_{solv}$ | 407.45 | kg/h |
| Materia prima (alimentacion ESL) | $\dot m_{MP}$ | 187.50 | kg/h |
| Destilado etanol-agua | $\dot m_{D,EA}$ | 198.87 | kg/h |
| Destilado acetato | $\dot m_{D,AC}$ | 257.89 | kg/h |
| Destilado total de referencia | $\dot m_{D,tot}$ | 456.76 | kg/h |

### 7.2 Costos de operacion por utilidad/material

Costo termico horario:

$$
C_{vapor,h}=Q_{reb,tot}(0.035)=301.52(0.035)=10.55\ \text{USD/h}
$$

$$
C_{vapor,a}=C_{vapor,h}(2920)=30{,}815.34\ \text{USD/ano}
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
C_{solv,h}=\dot m_{solv}(1.25)=407.45(1.25)=509.31\ \text{USD/h}
$$

$$
C_{solv,a}=C_{solv,h}(2920)=1{,}487{,}186.30\ \text{USD/ano}
$$

Costo de materia prima:

$$
C_{MP,h}=\dot m_{MP}(0.80)=187.50(0.80)=150.00\ \text{USD/h}
$$

$$
C_{MP,a}=C_{MP,h}(2920)=438{,}000.00\ \text{USD/ano}
$$

### 7.3 OPEX total anual y costo unitario

$$
C_{OPEX,a}=C_{vapor,a}+C_{elec,a}+C_{solv,a}+C_{MP,a}
$$

$$
C_{OPEX,a}=1{,}956{,}375.40\ \text{USD/ano}
$$

Costo horario total:

$$
C_{OPEX,h}=\frac{C_{OPEX,a}}{2920}=670.00\ \text{USD/h}
$$

Produccion anual de referencia en destilados combinados:

$$
M_{D,a}=\dot m_{D,tot}(2920)=456.76(2920)=1{,}333{,}739.20\ \text{kg/ano}
$$

Costo operativo unitario combinado:

$$
c_{op,D} = \frac{C_{OPEX,a}}{M_{D,a}}=1.47\ \text{USD/kg destilado}
$$

Resumen de costos anuales:

| Concepto | Costo anual (USD) | Participacion (%) |
|---|---:|---:|
| Vapor (dos columnas) | 30,815.34 | 1.58 |
| Electricidad auxiliar ESL+ELL | 373.76 | 0.02 |
| Reposicion total de solvente | 1,487,186.30 | 76.02 |
| Materia prima | 438,000.00 | 22.39 |
| **OPEX total** | **1,956,375.40** | **100.00** |

Alcance: este analisis es de OPEX operativo simplificado y no incluye CAPEX, depreciacion, impuestos, mantenimiento ni costo de personal.

## 8. Verificacion de coherencia cerrada

1. Conexion de etapas: la rama de refinado ELL alimenta la destilacion etanol-agua y la rama de extracto ELL alimenta la destilacion acetato.
2. Distilacion dual: se elimina la base de columna unica y se reportan dos trenes con sus propias etapas, energia y dimensionamiento.
3. Recirculacion dual: se separa reposicion de etanol y reposicion de acetato; los balances globales cierran al 100% en ambas bases reportadas.
4. ELL etapa real: se preservan los valores de hoja tanto en base composicional como en base de masa de soluto para asegurar trazabilidad academica.
5. Economia: se mantiene la estructura de precios unitarios del informe previo y se recalcula con los nuevos caudales y cargas de dos columnas.

## 9. Resumen de resultados clave

| Bloque | Resultado principal |
|---|---|
| ESL | $V=480.375$ kg/h, $y_1=2.810\%$, cierre de masa conforme |
| ELL | $M_t=744.585$ kg/h, $E=294.50$ kg/h, $R=450.08$ kg/h |
| Destilacion Etanol-Agua | $D=198.87$ kg/h, $B=251.21$ kg/h, $\eta_{EtOH}=94.68\%$, 15 etapas reales |
| Destilacion Acetato | $D=257.89$ kg/h, $B=36.62$ kg/h, $\eta_{Ac}=99.3\%$, 23 etapas reales |
| Recirculacion | Makeup etanol $=401.13$ kg/h, makeup acetato $=6.32$ kg/h |
| Global | Entradas = Salidas = 1051.71 kg/h, cierre = 100% |
| Economia | OPEX = 1,956,375.40 USD/ano, costo unitario = 1.47 USD/kg |
