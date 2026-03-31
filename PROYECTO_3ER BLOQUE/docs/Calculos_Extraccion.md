# Calculos de Extraccion Liquido-Liquido

## 1. Objetivo

Presentar calculos termodinamicos, fisicos y de dimensionamiento para extraccion liquido-liquido, con ejemplo clasico de acetona desde agua usando tolueno como solvente.

## 2. Base de calculo

| Variable | Valor |
|---|---:|
| Alimentacion acuosa, F | 1000 kg/h |
| Fraccion masica de acetona en F | 0.10 |
| Acetona en alimentacion | 100 kg/h |
| Solvente tolueno total, S | 800 kg/h |
| Coeficiente de distribucion, KD | 2.0 |
| Temperatura | 25 C |

## 3. Modelo termodinamico y de equilibrio

### 3.1 Coeficiente de distribucion

$$
K_D=\frac{C_{A,E}}{C_{A,R}}
$$

Donde:
- $C_{A,E}$ = concentracion de acetona en extracto.
- $C_{A,R}$ = concentracion de acetona en refinado.

### 3.2 Fraccion remanente en una etapa ideal

Para equilibrio lineal y fases inmiscibles:

$$
\frac{x_R}{x_F}=\frac{1}{1+K_D(S/F)}
$$

## 4. Calculos fisicos

### 4.1 Extraccion simple de una etapa

$$
S/F=800/1000=0.8
$$

$$
\frac{x_R}{x_F}=\frac{1}{1+2.0(0.8)}=\frac{1}{2.6}=0.3846
$$

Acetona en refinado:

$$
m_{A,R}=100(0.3846)=38.5\ \text{kg/h}
$$

Acetona extraida:

$$
m_{A,E}=100-38.5=61.5\ \text{kg/h}
$$

Recuperacion:

$$
\eta=\frac{61.5}{100}\times100=61.5\%
$$

### 4.2 Extraccion cruzada en 3 etapas (solvente dividido)

Si $S_i=800/3=266.7$ kg/h por etapa:

$$
\phi=\frac{1}{1+K_D(S_i/F)}=\frac{1}{1+2(0.2667)}=0.6522
$$

Fraccion remanente tras 3 etapas:

$$
\left(\frac{x_R}{x_F}\right)_{3\ etapas}=\phi^3=0.277
$$

Acetona en refinado final:

$$
m_{A,R,3}=100(0.277)=27.7\ \text{kg/h}
$$

Recuperacion total:

$$
\eta_{3\ etapas}=72.3\%
$$

## 5. Dimensionamiento preliminar (mixer-settler)

### 5.1 Caudal volumetrico de mezcla

Con densidad promedio de mezcla $\rho_{mix}\approx950$ kg/m3:

$$
\dot V=\frac{F+S}{\rho_{mix}}=\frac{1800}{950}=1.89\ \text{m}^3/\text{h}
$$

### 5.2 Volumen de mezclador

Tomando $\tau_m=5$ min y factor de seguridad 1.2:

$$
V_m=\dot V\left(\frac{5}{60}\right)(1.2)=0.19\ \text{m}^3
$$

### 5.3 Volumen de decantador

Tomando $\tau_d=20$ min y factor 1.2:

$$
V_d=\dot V\left(\frac{20}{60}\right)(1.2)=0.76\ \text{m}^3
$$

### 5.4 Area de decantacion

Con velocidad superficial de diseno $v_s=1.0$ m/h:

$$
A_d=\frac{\dot V}{v_s}=\frac{1.89}{1.0}=1.89\ \text{m}^2
$$

### 5.5 Potencia de agitacion del mezclador

Criterio rapido:

$$
\frac{P}{V}=1.0\ \text{kW/m}^3\Rightarrow P\approx0.19\ \text{kW}
$$

Motor comercial recomendado: 0.37 kW.

## 6. Propiedades de referencia

| Propiedad | Agua | Acetona | Tolueno |
|---|---:|---:|---:|
| Densidad 25 C, kg/m3 | 997 | 784 | 867 |
| Viscosidad 25 C, mPa*s | 0.89 | 0.32 | 0.56 |
| Punto ebullicion, C | 100.0 | 56.1 | 110.6 |
| Solubilidad en agua | - | Alta | Muy baja |

## 7. Resultado ejecutivo

- Una etapa simple recupera ~61.5% de acetona.
- Tres etapas cruzadas con mismo solvente elevan recuperacion a ~72.3%.
- Equipo preliminar por etapa: mezclador 0.19 m3 y decantador 0.76 m3.
- Dimension de huella de decantacion: ~1.9 m2 por etapa.

## 8. Transferencia interfacial y tiempo de contacto

En sistema liquido-liquido con doble pelicula:

$$
N_A=K_La\,(C_A^*-C_A)
$$

Para mezcladores de baja viscosidad, tiempo de contacto util tipico:

- 3 a 8 min en mezclador.
- 15 a 30 min en decantador para separacion limpia de fases.

Los valores adoptados ($\tau_m=5$ min, $\tau_d=20$ min) quedan en zona recomendada.

## 9. Criterios semiprofesionales de mixer-settler

### 9.1 Intensidad de mezcla

Criterio de potencia volumetrica:

$$
\frac{P}{V}=0.5\text{ a }2.0\ \text{kW/m}^3
$$

Con $V_m=0.19$ m3 y criterio base 1.0:

$$
P\approx0.19\ \text{kW}
$$

Motor comercial 0.37 kW aporta margen para variaciones de viscosidad.

### 9.2 Velocidad superficial en decantador

Rango recomendado para evitar arrastre entre fases:

- 0.3 a 1.5 m/h.

Se adoptó 1.0 m/h, consistente con separacion estable.

## 10. Sensibilidad rapida de recuperacion a S/F

Usando:

$$
\frac{x_R}{x_F}=\frac{1}{1+K_D(S/F)}
$$

con $K_D=2.0$:

| S/F | Recuperacion en 1 etapa |
|---:|---:|
| 0.5 | 50.0% |
| 0.8 | 61.5% |
| 1.2 | 70.6% |

Conclusión: incrementar S/F mejora recuperacion, pero con penalizacion en recuperacion de solvente y OPEX.
