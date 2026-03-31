# Calculos preliminares integrados - Proyecto 3er Bloque

## 1. Base de calculo y criterios de referencia

Este documento integra calculos preliminares de tres etapas:

1. Extraccion solido-liquido (ESL)
2. Extraccion liquido-liquido (ELL)
3. Destilacion al vacio

Se usan como referencia metodologica los criterios del proyecto final consolidado:

- Balance en estado estacionario.
- Factores de seguridad de diseno preliminar ($f_s=1.2$).
- Tiempos de residencia de referencia para mezclado/separacion.
- Verificacion de cierres de masa y cumplimiento de restricciones de recuperacion y energia.

### 1.1 Datos de entrada (3er bloque)

| Etapa | Parametro | Valor |
|---|---|---:|
| ESL | Capacidad de alimentacion | 1500 kg/d |
| ESL | Contenido de soluto en alimentacion | 10% p/p |
| ESL | Humedad de alimentacion | 12% p/p |
| ESL | Relacion solvente/solido, S/F | 3.2 kg/kg |
| ESL | Retencion de solvente en inerte | 1.1 kg/kg inerte |
| ESL | Coeficiente aparente de equilibrio, KE | 1.5 |
| ESL | Eficiencia global de extraccion | 72% |
| ELL | Coeficiente de distribucion, KD | 2.0 |
| ELL | Relacion solvente/alimentacion, S/F | 0.55 kg/kg |
| ELL | Eficiencia de etapa | 80% |
| Destilacion | $x_F$ | 0.42 |
| Destilacion | $x_D$ | 0.90 |
| Destilacion | $x_B$ | 0.04 |
| Destilacion | Eficiencia de platos | 65% |
| Destilacion | Recuperacion minima requerida | 94% |
| Destilacion | Consumo maximo de vapor | 2.2 kg/kg producto |

## 2. Etapa 1 - Extraccion solido-liquido (ESL)

### 2.1 Descomposicion de alimentacion

Base diaria: $F_s=1500$ kg/d.

Soluto en alimentacion:

$$
m_{sol,in}=0.10(1500)=150\ \text{kg/d}
$$

Agua inicial por humedad:

$$
m_{H2O,in}=0.12(1500)=180\ \text{kg/d}
$$

Solido inerte:

$$
m_{inerte}=1500-150-180=1170\ \text{kg/d}
$$

Masa seca total (inerte + soluto):

$$
m_{seca}=1500-180=1320\ \text{kg/d}
$$

### 2.2 Solvente de extraccion y recuperacion de soluto

Con $S/F=3.2$ kg solvente/kg solido:

$$
m_{solv,1}=3.2(1320)=4224\ \text{kg/d}
$$

Soluto extraido (eficiencia 72%):

$$
m_{sol,ext}=0.72(150)=108\ \text{kg/d}
$$

Soluto remanente en torta:

$$
m_{sol,res}=150-108=42\ \text{kg/d}
$$

Retencion de solvente en inerte:

$$
m_{ret}=1.1(1170)=1287\ \text{kg/d}
$$

### 2.3 Balance preliminar de corrientes de salida

Corriente liquida extracto de ESL:

$$
m_{ext,ESL}=(m_{solv,1}+m_{H2O,in})-m_{ret}+m_{sol,ext}
$$

$$
m_{ext,ESL}=(4224+180)-1287+108=3225\ \text{kg/d}
$$

Corriente de torta/solido agotado:

$$
m_{torta}=m_{inerte}+m_{sol,res}+m_{ret}=1170+42+1287=2499\ \text{kg/d}
$$

Verificacion de cierre:

$$
m_{in}=1500+4224=5724\ \text{kg/d}
$$

$$
m_{out}=3225+2499=5724\ \text{kg/d}\ \checkmark
$$

### 2.4 Indicadores y dimensionamiento preliminar ESL

Recuperacion de soluto en ESL:

$$
\eta_{ESL}=\frac{108}{150}=0.72=72\%
$$

Concentracion masica de soluto en extracto ESL:

$$
x_{sol,ext}=\frac{108}{3225}=0.0335\ (3.35\%\ p/p)
$$

Operacion en 8 h/dia (base de diseno del bloque):

$$
\dot m_{in,ESL}=\frac{5724}{8}=715.5\ \text{kg/h}
$$

Tomando $\rho_{mezcla}=1060$ kg/m3, $\tau=0.9$ h y $f_s=1.2$ (criterio de referencia del proyecto final):

$$
\dot V_{ESL}=\frac{715.5}{1060}=0.675\ \text{m}^3/\text{h}
$$

$$
V_{tanque,ESL}=\dot V_{ESL}\tau f_s=0.675(0.9)(1.2)=0.729\ \text{m}^3
$$

Con geometria preliminar $H/D=0.85$:

$$
V=\frac{\pi D^2}{4}(0.85D)\Rightarrow D\approx1.03\ \text{m},\ H\approx0.88\ \text{m}
$$

Estimacion rapida de agitacion ($P/V\approx1$ kW/m3):

$$
P_{ESL}\approx0.73\ \text{kW}\ \Rightarrow\ \text{seleccion preliminar: }1.1\ \text{kW}
$$

## 3. Etapa 2 - Extraccion liquido-liquido (ELL)

Se toma como alimentacion a ELL la corriente liquida de ESL.

### 3.1 Datos de entrada a ELL

| Variable | Valor |
|---|---:|
| Alimentacion a ELL, $F_{ELL}$ | 3225 kg/d |
| Soluto de entrada a ELL | 108 kg/d |
| KD | 2.0 |
| S/F | 0.55 |
| Eficiencia de etapa | 80% |

Solvente fresco de ELL:

$$
m_{solv,2}=0.55(3225)=1773.75\ \text{kg/d}
$$

### 3.2 Recuperacion ideal y recuperacion real

Fraccion remanente ideal en refinado para una etapa:

$$
\phi=\frac{x_R}{x_F}=\frac{1}{1+K_D(S/F)}=\frac{1}{1+2(0.55)}=0.47619
$$

Soluto en refinado ideal:

$$
m_{sol,R}^{ideal}=108(0.47619)=51.43\ \text{kg/d}
$$

Soluto extraido ideal:

$$
m_{sol,E}^{ideal}=108-51.43=56.57\ \text{kg/d}
$$

Aplicando eficiencia de etapa (80%) sobre la extraccion ideal:

$$
m_{sol,E}^{real}=0.80(56.57)=45.26\ \text{kg/d}
$$

$$
m_{sol,R}^{real}=108-45.26=62.74\ \text{kg/d}
$$

Recuperacion real en ELL:

$$
\eta_{ELL}=\frac{45.26}{108}=41.9\%
$$

Recuperacion acumulada frente al soluto inicial del solido:

$$
\eta_{acum,ESL+ELL}=\frac{45.26}{150}=30.2\%
$$

### 3.3 Balance preliminar de fases en ELL

Masa de extracto organico (aprox. sin solubilidad cruzada):

$$
m_{E,ELL}=m_{solv,2}+m_{sol,E}^{real}=1773.75+45.26=1819.01\ \text{kg/d}
$$

Masa de refinado:

$$
m_{R,ELL}=3225-45.26=3179.74\ \text{kg/d}
$$

Verificacion de cierre:

$$
m_{in}=3225+1773.75=4998.75\ \text{kg/d}
$$

$$
m_{out}=1819.01+3179.74=4998.75\ \text{kg/d}\ \checkmark
$$

### 3.4 Dimensionamiento preliminar de mixer-settler

Operacion en 8 h/dia:

$$
\dot m_{in,ELL}=\frac{4998.75}{8}=624.84\ \text{kg/h}
$$

Con $\rho_{mix}=950$ kg/m3:

$$
\dot V_{ELL}=\frac{624.84}{950}=0.658\ \text{m}^3/\text{h}
$$

Tomando criterios de referencia del bloque de extraccion:

- Tiempo de mezcla: $\tau_m=5$ min.
- Tiempo de decantacion: $\tau_d=20$ min.
- Factor de seguridad: $f_s=1.2$.

Volumen de mezclador:

$$
V_m=\dot V_{ELL}\left(\frac{5}{60}\right)f_s=0.658\left(\frac{5}{60}\right)(1.2)=0.0658\ \text{m}^3
$$

Volumen de decantador:

$$
V_d=\dot V_{ELL}\left(\frac{20}{60}\right)f_s=0.263\ \text{m}^3
$$

Area de decantacion para $v_s=1.0$ m/h:

$$
A_d=\frac{\dot V_{ELL}}{v_s}=0.658\ \text{m}^2
$$

Potencia de mezcla preliminar con $P/V\approx1$ kW/m3:

$$
P_{ELL}\approx0.066\ \text{kW}\ \Rightarrow\ \text{seleccion preliminar: }0.18\ \text{kW}
$$

## 4. Etapa 3 - Destilacion al vacio (guiada por tablas)

### 4.1 Base y especificaciones de diseno

Para la etapa de destilacion se adopta base molar estandar:

$$
F=100\ \text{kmol/h},\ x_F=0.42,\ x_D=0.90,\ x_B=0.04
$$

Condiciones operativas de vacio y diseno:

$$
P\approx300\ \text{mmHg},\ \alpha=2.5,\ R=2,\ q=1
$$

### 4.2 Balance de masa y recuperacion

Producto de tope:

$$
D=\frac{F(x_F-x_B)}{x_D-x_B}=\frac{100(0.42-0.04)}{0.90-0.04}=44.186\ \text{kmol/h}
$$

Producto de fondo:

$$
B=F-D=55.814\ \text{kmol/h}
$$

Recuperacion del componente ligero en destilado:

$$
Rec=\frac{Dx_D}{Fx_F}=\frac{44.186(0.90)}{100(0.42)}=94.68\%
$$

Cumple recuperacion minima requerida (94%).

### 4.3 Numero minimo de etapas (Fenske)

$$
N_{min}=\frac{\ln\left[\left(\frac{x_D}{1-x_D}\right)\left(\frac{1-x_B}{x_B}\right)\right]}{\ln(\alpha)}
$$

$$
N_{min}=\frac{\ln[(0.90/0.10)(0.96/0.04)]}{\ln(2.5)}=\frac{\ln(216)}{\ln(2.5)}=5.87
$$

### 4.4 Tabla de equilibrio de referencia para McCabe-Thiele

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

Linea de enriquecimiento para $R=2$:

$$
y_R=\frac{R}{R+1}x+\frac{x_D}{R+1}=0.667x+0.300
$$

Con $q=1$, la interseccion de ambas lineas de operacion se fija en $x_F=0.42$:

$$
y_F=0.667(0.42)+0.300=0.580
$$

La linea de agotamiento se obtiene con los puntos $(x_B,x_B)$ y $(x_F,y_F)$:

$$
y_S=\frac{0.580-0.040}{0.420-0.040}(x-0.040)+0.040
$$

$$
y_S=1.421x-0.0169
$$

### 4.5 McCabe-Thiele aproximado (escalonamiento punto a punto)

Se usa interpolacion lineal en la tabla de equilibrio para hallar $x_n$ desde cada $y_n$.

| Etapa $n$ | $y_n$ (linea op.) | $x_n$ (equilibrio) | Seccion |
|---:|---:|---:|---|
| 1 | 0.9000 | 0.7333 | Enriquecimiento |
| 2 | 0.7889 | 0.4984 | Enriquecimiento |
| 3 | 0.6323 | 0.3026 | Enriquecimiento -> cruce de alimentacion |
| 4 | 0.4133 | 0.1431 | Agotamiento |
| 5 | 0.1865 | 0.0444 | Agotamiento |
| 6 | 0.0462 | 0.0110 | Agotamiento |

Comentarios de escalonamiento:

- El cruce de alimentacion ocurre entre las etapas 2 y 3 (desde el tope).
- El valor objetivo de fondo $x_B=0.04$ cae entre $x_5=0.0444$ y $x_6=0.0110$.

Fraccion de ultima etapa:

$$
f_{ult}=\frac{x_5-x_B}{x_5-x_6}=\frac{0.0444-0.0400}{0.0444-0.0110}=0.132
$$

Numero de etapas teoricas por escalonamiento:

$$
N_t\approx5+0.132=5.13\ \text{(sin rehervidor)}
$$

Incluyendo rehervidor como etapa de equilibrio adicional:

$$
N_{t,total}\approx6.13\ \Rightarrow\ \text{adoptar }7\ \text{etapas teoricas}
$$

Etapas reales con eficiencia de platos $E_M=65\%$:

$$
N_{real}=\frac{7}{0.65}=10.77\ \Rightarrow\ \text{adoptar }11\ \text{platos reales}
$$

### 4.6 Flujos internos y cargas termicas preliminares

Flujos internos en seccion de enriquecimiento:

$$
L=RD=2(44.186)=88.37\ \text{kmol/h}

## 5. Visualizacion de curvas de destilacion por terminal (CLI)

Script implementado en:

- `PROYECTO_3ER BLOQUE/python/curvas_destilacion_cli.py`

Ejemplo de ejecucion (muestra tabla de etapas y abre grafica interactiva):

```bash
python "PROYECTO_3ER BLOQUE/python/curvas_destilacion_cli.py"
```

Ejecucion sin abrir ventana y exportando HTML:

```bash
python "PROYECTO_3ER BLOQUE/python/curvas_destilacion_cli.py" --no-show --html "PROYECTO_3ER BLOQUE/media/images/curvas_destilacion_test.html"
```

Ajuste de parametros de operacion desde terminal:

```bash
python "PROYECTO_3ER BLOQUE/python/curvas_destilacion_cli.py" --R 2.5 --xF 0.42 --xD 0.92 --xB 0.05 --q 1
```

Exportacion PNG (requiere `kaleido`):

```bash
python "PROYECTO_3ER BLOQUE/python/curvas_destilacion_cli.py" --no-show --png "PROYECTO_3ER BLOQUE/media/images/curvas_destilacion.png"
```
$$

$$
V=(R+1)D=3(44.186)=132.56\ \text{kmol/h}
$$

Para $q=1$:

$$
L'=L+F=188.37\ \text{kmol/h},\quad V'=V=132.56\ \text{kmol/h}
$$

Estimacion energetica preliminar (base de mezcla ligera tipo etanol-agua):

- $\overline M_V\approx43.27$ kg/kmol
- $\lambda_{mix}\approx850$ kJ/kg
- $\lambda_{vapor}\approx2200$ kJ/kg

$$
\dot m_V=132.56(43.27)=5736\ \text{kg/h}
$$

$$
Q_{cond}\approx\dot m_V\lambda_{mix}=5736(850)=4.88\times10^6\ \text{kJ/h}=1354\ \text{kW}
$$

$$
Q_{reb}\approx Q_{cond}
$$

Consumo de vapor vivo:

$$
\dot m_{vapor}=\frac{Q_{reb}}{\lambda_{vapor}}=\frac{4.88\times10^6}{2200}=2216\ \text{kg/h}
$$

Flujo de producto de tope en masa:

$$
\dot m_D=D\overline M_D=44.186(43.27)=1912\ \text{kg/h}
$$

Consumo especifico de vapor:

$$
CE_v=\frac{\dot m_{vapor}}{\dot m_D}=\frac{2216}{1912}=1.16\ \text{kg/kg producto}
$$

Cumple restriccion de consumo maximo ($1.16 < 2.2$ kg/kg).

### 4.7 Diametro y altura preliminar de columna

Estimacion de caudal volumetrico de vapor en cabeza (gas ideal, $T\approx333$ K, $P\approx0.395$ atm):

$$
Q_V\approx\frac{\dot nRT}{P}=2.56\ \text{m}^3/\text{s}
$$

Densidad de vapor:

$$
\rho_V\approx0.63\ \text{kg/m}^3
$$

Con $\rho_L\approx850$ kg/m3 y $C=0.11$ m/s (Souders-Brown):

$$
u_f=C\sqrt{\frac{\rho_L-\rho_V}{\rho_V}}=4.06\ \text{m/s}
$$

$$
u_{dis}=0.70u_f=2.84\ \text{m/s}
$$

$$
A=\frac{Q_V}{u_{dis}}=\frac{2.56}{2.84}=0.901\ \text{m}^2
$$

$$
D_{col}=\sqrt{\frac{4A}{\pi}}=1.07\ \text{m}\ \Rightarrow\ \text{diametro nominal: }1.1\ \text{m}
$$

Altura preliminar (platos reales + holguras):

$$
H_{activa}=11(0.45)=4.95\ \text{m}
$$

$$
H_{total}\approx6.5\text{ a }7.5\ \text{m}
$$

## 5. Resumen integrado de resultados preliminares

| Etapa | Resultado clave 1 | Resultado clave 2 | Resultado clave 3 |
|---|---|---|---|
| ESL | Soluto extraido: 108 kg/d | Recuperacion: 72% | Tanque preliminar: 0.73 m3 (motor 1.1 kW) |
| ELL | Soluto recuperado real: 45.26 kg/d | Recuperacion etapa: 41.9% | Mixer-settler: $V_m=0.066$ m3, $V_d=0.263$ m3 |
| Destilacion vacio | Recuperacion de ligero: 94.68% | $N_{real}\approx11$ platos | $D_{col}\approx1.1$ m, $CE_v\approx1.16$ kg/kg |

## 6. Verificaciones de cumplimiento

1. Cierre de masa ESL: conforme.
2. Cierre de masa ELL: conforme.
3. Recuperacion minima en destilacion: cumple (94.68% >= 94%).
4. Consumo maximo de vapor: cumple (1.16 < 2.2 kg/kg producto).
5. Operacion de destilacion al vacio: consistente con criterio de tablas y diseno preliminar.

## 7. Observaciones para siguiente iteracion

1. Refinar ESL/ELL con datos experimentales de particion real y arrastre de fases para reducir incertidumbre en recuperacion global.
2. En destilacion, realizar sensibilidad de diseno variando $R$ (por ejemplo 1.6, 2.0 y 2.4) para optimizar compromiso entre numero de platos y consumo de vapor.
3. En el cierre global del bloque, conectar explicitamente la composicion de la corriente de ELL con la alimentacion real a destilacion cuando se defina el diagrama de proceso final.