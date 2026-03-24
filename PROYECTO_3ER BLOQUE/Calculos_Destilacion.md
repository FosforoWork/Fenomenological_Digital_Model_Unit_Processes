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
