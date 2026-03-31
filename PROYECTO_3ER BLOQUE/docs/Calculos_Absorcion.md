# Calculos de Absorcion Gas-Liquido

## 1. Objetivo

Desarrollar calculos termodinamicos, fisicos y de dimensionamiento de una torre de absorcion, con ejemplo clasico de absorcion de NH3 desde aire usando agua.

## 2. Base de calculo

| Variable | Valor |
|---|---:|
| Gas inerte (base libre de soluto), G | 100 kmol/h |
| Fraccion molar NH3 en gas de entrada, y_in | 0.050 |
| Fraccion molar NH3 en gas de salida, y_out | 0.005 |
| Solvente (agua), L | 120 kmol/h |
| Fraccion NH3 en liquido de entrada, x_in | 0.000 |
| Parametro de equilibrio lineal, y*=m*x | m = 0.9 |
| Temperatura | 25 C |
| Presion | 1 atm |

## 3. Modelo termodinamico

### 3.1 Equilibrio gas-liquido

A bajas concentraciones:

$$
y^*=m x
$$

Donde $m$ depende de temperatura y sistema quimico.

### 3.2 Ley de Henry (forma general)

$$
p_A=H x_A
$$

En forma adimensional se puede usar $m=H/P$.

## 4. Calculos fisicos

### 4.1 Balance de soluto (NH3)

$$
L(x_{out}-x_{in})=G(y_{in}-y_{out})
$$

$$
120(x_{out}-0)=100(0.050-0.005)=4.5
$$

$$
x_{out}=0.0375
$$

### 4.2 Verificacion de fuerza impulsora en fondo

$$
y^*_{fondo}=m x_{out}=0.9(0.0375)=0.0338
$$

Como $y_{in}=0.050 > y^*_{fondo}=0.0338$, hay fuerza impulsora positiva.

### 4.3 Numero de unidades de transferencia global (aprox. log-media)

Fuerza impulsora en tope:

$$
\Delta y_{top}=y_{out}-m x_{in}=0.005
$$

Fuerza impulsora en fondo:

$$
\Delta y_{bot}=y_{in}-m x_{out}=0.0162
$$

Media logaritmica:

$$
\Delta y_{lm}=\frac{\Delta y_{bot}-\Delta y_{top}}{\ln(\Delta y_{bot}/\Delta y_{top})}=0.0092
$$

Numero de unidades de transferencia:

$$
NTU_{OG}\approx\frac{y_{in}-y_{out}}{\Delta y_{lm}}=\frac{0.045}{0.0092}=4.89
$$

## 5. Dimensionamiento preliminar de torre empacada

### 5.1 Altura por metodo HTU-NTU

$$
Z=HTU_{OG}\times NTU_{OG}
$$

Con $HTU_{OG}=0.8$ m (valor tipico preliminar):

$$
Z=0.8\times4.89=3.91\ \text{m}
$$

Altura recomendada de lecho: 4.0 m.

### 5.2 Diametro de torre por velocidad superficial de gas

Caudal total de gas aproximado:

$$
\dot n_G\approx105\ \text{kmol/h}
$$

A 25 C y 1 atm ($24.47$ m3/kmol):

$$
Q_G=105\times24.47=2569\ \text{m}^3/\text{h}=0.714\ \text{m}^3/s
$$

Con velocidad superficial de diseno $u_G=1.5$ m/s:

$$
A=\frac{Q_G}{u_G}=\frac{0.714}{1.5}=0.476\ \text{m}^2
$$

$$
D=\sqrt{\frac{4A}{\pi}}=0.78\ \text{m}
$$

Diametro nominal recomendado: 0.80 m.

### 5.3 Caida de presion (criterio preliminar)

Para empaque aleatorio plastico/metalico en operacion moderada:
- 200 a 500 Pa/m de lecho.
- Para 4 m: 0.8 a 2.0 kPa.

## 6. Propiedades fisicas y termodinamicas de referencia

| Propiedad | Aire | NH3 | Agua |
|---|---:|---:|---:|
| PM, kg/kmol | 28.97 | 17.03 | 18.02 |
| Densidad 25 C, kg/m3 | 1.18 | 0.73 (gas) | 997 |
| Solubilidad en agua 25 C | Baja (aire) | Alta | - |
| Cp aprox, kJ/kg*K | 1.0 | 2.1 (gas) | 4.18 |

## 7. Resultado ejecutivo

- Remocion objetivo de NH3: 90% (de 5% a 0.5% molar).
- Torre preliminar: D = 0.80 m, lecho empacado Z = 4.0 m.
- NTU global estimado: 4.89.
- El proceso es sensible a temperatura: al subir T, suele disminuir absorcion fisica.

## 8. Correlaciones de transferencia de masa

Para estimacion de coeficiente de pelicula en gas (base particula/empaque):

$$
Sh = 2 + 0.6\,Re^{1/2}Sc^{1/3}
$$

donde:

$$
Sh=\frac{k_G d_p}{D_{AB}}
$$

Esta correlacion permite afinar $K_Ga$ cuando se dispone de datos de empaque y difusividad.

## 9. Flujos limites y operacion segura

### 9.1 Criterio de flujo minimo de solvente

Un limite inferior razonable para mantener fuerza impulsora positiva es operar con 20-40% por encima de $L_{min}$.

Con $L=120$ kmol/h, el caso base evita pinch en la parte superior.

### 9.2 Criterio de inundacion

Para torres empacadas se recomienda operar en:

$$
u_G=0.60\text{ a }0.80\,u_{flood}
$$

El valor usado ($u_G=1.5$ m/s) se interpreta como zona moderada para empaques comerciales de baja perdida.

## 10. Especificacion preliminar de ventilador

Con caudal de gas:

$$
Q_G=0.714\ \text{m}^3/s
$$

y caida de presion del lecho de 1.5 kPa (valor medio), eficiencia 70%:

$$
P_{vent}=\frac{Q_G\Delta P}{\eta}=\frac{0.714\times1500}{0.70}=1.53\ \text{kW}
$$

Seleccion semiprofesional: ventilador de 2.2 kW con control de velocidad.
