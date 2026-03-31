# Calculos de Destilacion

## 1. Objetivo

Desarrollar calculos termodinamicos, fisicos y de dimensionamiento para una columna de destilacion binaria, con ejemplo clasico etanol-agua.

## 2. Base de calculo

| Variable | Valor |
|---|---:|
| Mezcla alimentada, F | 100 kmol/h |
| Fraccion molar etanol en alimentacion, xF | 0.50 |
| Producto de tope, xD | 0.90 |
| Producto de fondo, xB | 0.10 |
| Presion | 1 atm |
| Volatilidad relativa promedio, alpha | 2.2 |

## 3. Modelo termodinamico

### 3.1 Equilibrio vapor-liquido simplificado

Para un binario ideal aproximado:

$$
y=\frac{\alpha x}{1+(\alpha-1)x}
$$

### 3.2 Ecuacion de Antoine (referencia)

$$
\log_{10}(P^{sat})=A-\frac{B}{T+C}
$$

Se usa para estimar presiones de vapor y ajustar el equilibrio con temperatura.

## 4. Calculos fisicos de separacion

### 4.1 Numero minimo de etapas teoricas (Fenske)

$$
N_{min}=\frac{\ln\left[\left(\frac{x_D}{1-x_D}\right)\left(\frac{1-x_B}{x_B}\right)\right]}{\ln(\alpha)}
$$

$$
N_{min}=\frac{\ln[(0.9/0.1)(0.9/0.1)]}{\ln(2.2)}=\frac{\ln(81)}{\ln(2.2)}=5.58
$$

Resultado: $N_{min}\approx6$ etapas teoricas.

### 4.2 Reflujo y etapas reales

Tomando un valor practico:

$$
R\approx1.5\,R_{min}
$$

Con una seleccion de diseno intermedia, se adopta:
- Reflujo de operacion: $R=1.65$.
- Etapas teoricas de diseno: $N_t\approx12$ (incluye margen sobre minimo).

### 4.3 Carga termica aproximada

Si el vapor interno en cabeza es $\dot m_V\approx6400$ kg/h y $\lambda\approx850$ kJ/kg:

$$
Q_{cond}\approx\dot m_V\lambda=6400\times850=5.44\times10^6\ \text{kJ/h}
$$

$$
Q_{cond}\approx1510\ \text{kW}
$$

En primera aproximacion:

$$
Q_{reb}\approx Q_{cond}
$$

## 5. Dimensionamiento preliminar de columna

### 5.1 Diametro por criterio Souders-Brown

Velocidad de inundacion:

$$
u_f=C\sqrt{\frac{\rho_L-\rho_V}{\rho_V}}
$$

Supuestos:
- $C=0.11$ m/s
- $\rho_L=780$ kg/m3
- $\rho_V=1.5$ kg/m3

$$
u_f=0.11\sqrt{\frac{780-1.5}{1.5}}\approx2.5\ \text{m/s}
$$

Velocidad de diseno (70% de inundacion):

$$
u_{dis}=0.70\nu_f\approx1.75\ \text{m/s}
$$

Con caudal volumetrico de vapor $Q_V\approx1.19$ m3/s:

$$
A=\frac{Q_V}{\nu_{dis}}=\frac{1.19}{1.75}=0.68\ \text{m}^2
$$

$$
D=\sqrt{\frac{4A}{\pi}}=0.93\ \text{m}
$$

Diametro nominal recomendado: 1.0 m.

### 5.2 Altura de columna

Para 12 etapas y espaciamiento de 0.45 m:

$$
H_{activa}=12\times0.45=5.4\ \text{m}
$$

Con secciones de tope, fondo y holguras:

$$
H_{total}\approx7.0\text{ a }8.0\ \text{m}
$$

## 6. Propiedades termodinamicas y fisicas de referencia

| Propiedad | Etanol | Agua |
|---|---:|---:|
| PM, kg/kmol | 46.07 | 18.02 |
| Punto de ebullicion a 1 atm, C | 78.37 | 100.00 |
| Densidad liquida 25 C, kg/m3 | 789 | 997 |
| Cp liquido, kJ/kg*K | 2.44 | 4.18 |
| Calor latente aprox, kJ/kg | 840 | 2257 |

## 7. Resultado ejecutivo

- Separacion objetivo factible con ~12 etapas teoricas de diseno.
- Diametro preliminar: 1.0 m.
- Altura preliminar: 7-8 m.
- Carga termica de condensador/rehervidor: ~1.5 MW (orden de magnitud).

## 8. Lineas de operacion y McCabe-Thiele (resumen)

En la seccion de enriquecimiento, para condensador total:

$$
y = \frac{R}{R+1}x + \frac{x_D}{R+1}
$$

Con $R=1.65$ y $x_D=0.90$:

$$
y = 0.623x + 0.340
$$

La pendiente intermedia confirma separacion factible sin operar cerca de reflujo minimo.

## 9. Diseno termico de condensador y rehervidor

Para verificacion preliminar por LMTD:

$$
Q=U\,A\,\Delta T_{lm}
$$

Tomando $Q=1.51$ MW, $U=500$ W/m2K y $\Delta T_{lm}=20$ K:

$$
A=\frac{1.51\times10^6}{500\times20}=151\ \text{m}^2
$$

Area de orden industrial coherente para columna de 1 m de diametro.

## 10. Verificacion hidraulica de columna

### 10.1 Operacion respecto a inundacion

Se adopto:

$$
u_{dis}=0.70\,u_f
$$

Rango semiprofesional recomendado: 60-80% de inundacion.

### 10.2 Caida de presion orientativa en empaque

Para empaque aleatorio (anillos Pall) en operacion moderada:

- 200 a 600 Pa/m de lecho.
- Para 6 m de zona activa empacada: 1.2 a 3.6 kPa.

Este rango es compatible con operacion atmosferica para etanol-agua.

## 11. Calculos de destilacion al vacio (guiados por tablas)

Para mantener la misma meta de separacion ($x_D=0.90$, $x_B=0.10$), se evalua la operacion a vacio.

### 11.1 Base de operacion al vacio

| Variable | Valor |
|---|---:|
| Presion absoluta de columna | 0.40 atm |
| Presion equivalente | 304 mmHg |
| Alimentacion total, $F$ | 100 kmol/h |
| Fraccion molar de etanol en alimentacion, $z_F$ | 0.50 |
| Destilado objetivo, $x_D$ | 0.90 |
| Fondo objetivo, $x_B$ | 0.10 |

Balance global y de componente ligero:

$$
D=\frac{F(z_F-x_B)}{x_D-x_B}=\frac{100(0.50-0.10)}{0.90-0.10}=50\ \text{kmol/h}
$$

$$
B=F-D=50\ \text{kmol/h}
$$

### 11.2 Tabla 1 obligatoria: coeficientes Antoine y temperaturas de saturacion a 304 mmHg

Ecuacion usada:

$$
\log_{10}(P^{sat}_{mmHg})=A-\frac{B}{T(^\circ C)+C}
$$

Despeje de temperatura para presion fija:

$$
T=\frac{B}{A-\log_{10}(P)}-C
$$

| Componente | A | B | C | $T_{sat}$ a 304 mmHg |
|---|---:|---:|---:|---:|
| Etanol | 8.20417 | 1642.89 | 230.300 | 56.85 C |
| Agua | 8.07131 | 1730.63 | 233.426 | 76.25 C |

Interpretacion: al operar a 0.40 atm se reduce la temperatura de ebullicion de ambos componentes, lo que disminuye degradacion termica y riesgo de ensuciamiento termico.

### 11.3 Tabla 2 obligatoria: tabla de burbuja y volatilidad relativa a vacio

Se resuelve, por composicion liquida, la ecuacion de punto de burbuja ideal:

$$
P= x_E P_E^{sat}(T) + (1-x_E)P_W^{sat}(T)
$$

con $P=304$ mmHg.

| $x_E$ (liquido) | $T_{burbuja}$ (C) | $P_E^{sat}$ (mmHg) | $P_W^{sat}$ (mmHg) | $\alpha=P_E^{sat}/P_W^{sat}$ |
|---:|---:|---:|---:|---:|
| 0.90 | 58.17 | 322.5 | 136.6 | 2.36 |
| 0.50 | 64.40 | 425.9 | 181.9 | 2.34 |
| 0.10 | 73.35 | 621.8 | 268.8 | 2.31 |

Promedio de diseno para McCabe-Thiele:

$$
\alpha_{vac,med}\approx 2.33
$$

### 11.4 Tabla 3 obligatoria: equilibrio vapor-liquido $x-y$ a 0.40 atm

Con volatilidad relativa constante aproximada:

$$
y=\frac{\alpha x}{1+(\alpha-1)x},\quad \alpha=2.33
$$

| $x$ | $y_{eq}$ |
|---:|---:|
| 0.00 | 0.000 |
| 0.10 | 0.206 |
| 0.20 | 0.368 |
| 0.30 | 0.500 |
| 0.40 | 0.608 |
| 0.50 | 0.700 |
| 0.60 | 0.778 |
| 0.70 | 0.845 |
| 0.80 | 0.903 |
| 0.90 | 0.955 |
| 1.00 | 1.000 |

Esta tabla es la referencia obligatoria para trazar curva de equilibrio y para escalonamiento de etapas.

### 11.5 Reflujo minimo y reflujo de operacion por metodo grafico-tabular

Para alimentacion saturada liquida ($q=1$), el pinzamiento minimo se estima en $x_F=0.50$ con:

$$
y^*(x_F=0.50)=0.700
$$

Pendiente de la recta de enriquecimiento a reflujo minimo:

$$
m_{min}=\frac{y^*-x_D}{x_F-x_D}=\frac{0.700-0.900}{0.500-0.900}=0.500
$$

$$
R_{min}=\frac{m_{min}}{1-m_{min}}=\frac{0.500}{0.500}=1.00
$$

Seleccion de diseno (50-60% por encima del minimo):

$$
R=1.55\approx1.55\,R_{min}
$$

Linea de enriquecimiento:

$$
y_R=\frac{R}{R+1}x+\frac{x_D}{R+1}=0.608x+0.353
$$

Interseccion con $q$-linea ($x=0.50$):

$$
y_F=0.608(0.50)+0.353=0.657
$$

Linea de agotamiento (por puntos $(x_B,x_B)$ e interseccion de alimentacion):

$$
y_S=1.392x-0.039
$$

### 11.6 Tabla 4 obligatoria: escalonamiento de McCabe-Thiele por etapas

Se usa en cada etapa:

$$
x_n=\frac{y_n}{\alpha-(\alpha-1)y_n},\quad \alpha=2.33
$$

y luego se pasa a linea de operacion para calcular $y_{n+1}$.

| Etapa $n$ | $y_n$ | $x_n$ por equilibrio | Seccion |
|---:|---:|---:|---|
| 1 | 0.900 | 0.794 | Enriquecimiento |
| 2 | 0.835 | 0.685 | Enriquecimiento |
| 3 | 0.769 | 0.589 | Enriquecimiento |
| 4 | 0.711 | 0.514 | Enriquecimiento |
| 5 | 0.665 | 0.460 | Cambio en alimentacion |
| 6 | 0.601 | 0.393 | Agotamiento |
| 7 | 0.508 | 0.307 | Agotamiento |
| 8 | 0.388 | 0.214 | Agotamiento |
| 9 | 0.259 | 0.130 | Agotamiento |
| 10 | 0.142 | 0.066 | Agotamiento |

Como $x_B=0.10$ cae entre las etapas 9 y 10, la fraccion de la ultima etapa es:

$$
f=\frac{0.130-0.100}{0.130-0.066}=0.469
$$

Etapas teoricas requeridas:

$$
N_t\approx9+0.469+1\ (rehervidor)=10.47\ \Rightarrow\ \text{adoptar }11\ \text{etapas teoricas}
$$

Ubicacion recomendada de alimentacion: alrededor de la etapa 5 (desde el tope).

### 11.7 Cargas termicas al vacio

Flujo molar de vapor en cabeza:

$$
V=(R+1)D=(1.55+1)50=127.5\ \text{kmol/h}
$$

Masa molar media del vapor de cabeza (aprox. 90% mol etanol, 10% agua):

$$
\overline{M}_V=0.90(46.07)+0.10(18.02)=43.27\ \text{kg/kmol}
$$

$$
\dot m_V=127.5\times43.27=5517\ \text{kg/h}
$$

Con calor latente medio de mezcla $\lambda_{mix}\approx898$ kJ/kg:

$$
Q_{cond}=\dot m_V\lambda_{mix}=5517\times898=4.95\times10^6\ \text{kJ/h}
$$

$$
Q_{cond}=1374\ \text{kW},\quad Q_{reb}\approx Q_{cond}
$$

### 11.8 Verificacion hidraulica preliminar al vacio

Con gas ideal en cabeza ($T\approx331$ K, $P=0.40$ atm):

$$
Q_V=\frac{\dot nRT}{P}=2.40\ \text{m}^3/\text{s}
$$

$$
\rho_V=\frac{PM}{RT}=0.64\ \text{kg/m}^3
$$

Tomando $\rho_L=840$ kg/m3 y $C=0.11$ m/s:

$$
u_f=0.11\sqrt{\frac{840-0.64}{0.64}}=3.98\ \text{m/s}
$$

$$
u_{dis}=0.70u_f=2.79\ \text{m/s}
$$

$$
A=\frac{Q_V}{u_{dis}}=\frac{2.40}{2.79}=0.860\ \text{m}^2
$$

$$
D=\sqrt{\frac{4A}{\pi}}=1.05\ \text{m}
$$

Diametro nominal recomendado para vacio: 1.1 m.

### 11.9 Resultado ejecutivo para operacion al vacio

| Parametro | Atmosferico | Vacio (0.40 atm) |
|---|---:|---:|
| Etapas teoricas de diseno | 12 | 11 |
| Reflujo de operacion | 1.65 | 1.55 |
| Carga termica condensador | 1.51 MW | 1.37 MW |
| Diametro preliminar | 1.0 m | 1.1 m |
| Temperatura de tope (orden) | ~78 C | ~58 C |

Conclusion: la destilacion al vacio mantiene la separacion objetivo con menor temperatura de operacion y leve aumento de diametro por mayor caudal volumetrico de vapor.
