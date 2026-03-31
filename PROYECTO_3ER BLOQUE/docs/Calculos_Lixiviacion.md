# Calculos de Lixiviacion

## 1. Objetivo

Presentar calculos termodinamicos, fisicos y de dimensionamiento para una operacion de lixiviacion (extraccion solido-liquido), usando:
- Ejemplo clasico simplificado (sal en agua).
- Caso aplicado del proyecto (proteina de soya).

## 2. Base y propiedades de referencia

### 2.1 Datos del caso simplificado (sal en agua)

| Variable | Valor |
|---|---:|
| Masa de solido inerte (arena) | 100 kg |
| Masa de NaCl inicial en solido | 20 kg |
| Agua de lixiviacion | 200 kg |
| Temperatura | 25 C |

### 2.2 Datos del caso proyecto (soya)

| Variable | Valor |
|---|---:|
| Harina de soya | 1000 kg/h |
| Fraccion de proteina en soya | 0.375 |
| Proteina de entrada | 375 kg/h |
| Agua de extraccion (1:12) | 12000 kg/h |
| pH de operacion | 8.5-9.0 |
| Temperatura | 55 C |
| Tiempo de residencia objetivo | 0.9 h |
| Densidad lodo proteico (aprox.) | 1060 kg/m3 |
| Viscosidad dinamica (aprox.) | 0.020 Pa*s |

## 3. Modelo termodinamico y fisico

### 3.1 Balance de masa de soluto

$$
\dot m_{s,in} = \dot m_{s,out} + \dot m_{s,acum}
$$

En estado estacionario:

$$
\dot m_{s,in} = \dot m_{s,out}
$$

### 3.2 Rendimiento de lixiviacion

$$
\eta_{ext} = \frac{m_{soluto,extraido}}{m_{soluto,inicial}}\times 100\%
$$

### 3.3 Modelo cinetico simplificado (aproximacion de primer orden)

$$
\frac{dC}{dt}=k_La(C^*-C)
$$

Solucion integrada:

$$
\frac{C^*-C_t}{C^*-C_0}=e^{-k_La t}
$$

## 4. Ejemplo clasico: extraccion de NaCl en agua

Si tras 30 min se extraen 18 kg de los 20 kg iniciales de NaCl:

$$
\eta_{ext}=\frac{18}{20}\times100=90\%
$$

Si se toma $C_0=0$, $C_t=0.90C^*$ en $t=30$ min:

$$
\frac{C^*-0.90C^*}{C^*}=0.10=e^{-k_La t}
$$

$$
k_La=\frac{-\ln(0.10)}{30}=0.0768\ \text{min}^{-1}
$$

## 5. Caso proyecto: proteina de soya

### 5.1 Proteina extraida

$$
\dot m_{prot,extraida}=\dot m_{prot,in}\,\eta_{ext}
$$

Con $\eta_{ext}=0.88$:

$$
\dot m_{prot,extraida}=375\times0.88=330\ \text{kg/h}
$$

Perdida con solidos (okara):

$$
\dot m_{prot,no\ extraida}=375-330=45\ \text{kg/h}
$$

### 5.2 Caudal total de lodo

$$
\dot m_{lodo}=1000+12000=13000\ \text{kg/h}
$$

$$
\dot V_{in}=\frac{\dot m_{lodo}}{\rho}=\frac{13000}{1060}=12.26\ \text{m}^3/\text{h}
$$

## 6. Dimensionamiento preliminar del extractor (tanque agitado)

### 6.1 Volumen util de tanque

$$
V=\dot V_{in}\,\tau\,f_s
$$

Con $\tau=0.9$ h y $f_s=1.2$:

$$
V=12.26\times0.9\times1.2=13.24\ \text{m}^3
$$

Seleccion: tanque nominal de 14 m3.

### 6.2 Geometria con relacion H/D = 0.85

$$
V=\frac{\pi D^2}{4}H=\frac{\pi D^2}{4}(0.85D)
$$

Para $V\approx14$ m3:

$$
D\approx2.76\ \text{m},\quad H\approx2.35\ \text{m}
$$

Altura de casco recomendada con margen operativo: 3.2 a 3.4 m.

### 6.3 Agitacion: Reynolds y potencia

Supuestos:
- $D_{ag}=0.40D=1.10$ m
- $N=80$ rpm $=1.333$ s-1
- $N_p=1.5$ (PBT)

Numero de Reynolds del agitador:

$$
Re_{ag}=\frac{\rho N D_{ag}^2}{\mu}=\frac{1060\times1.333\times1.10^2}{0.020}=8.5\times10^4
$$

Regimen: turbulento.

Potencia:

$$
P=N_p\rho N^3 D_{ag}^5
$$

$$
P\approx1.5\times1060\times1.333^3\times1.10^5\approx6.1\ \text{kW}
$$

Motor recomendado: 7.5 kW con variador.

## 7. Tabla de propiedades fisicas de referencia

| Propiedad | Agua 25 C | Lodo proteico (55 C, aprox.) |
|---|---:|---:|
| Densidad, kg/m3 | 997 | 1040-1080 |
| Viscosidad, Pa*s | 0.00089 | 0.010-0.030 |
| Cp, kJ/kg*K | 4.18 | 3.6-4.0 |
| Conductividad, W/m*K | 0.60 | 0.45-0.58 |

## 8. Resultado ejecutivo

- Caso simplificado: $\eta_{ext}=90\%$, $k_La=0.0768$ min-1.
- Caso soya: proteina extraida de 330 kg/h.
- Tanque recomendado: 14 m3 con agitador de 7.5 kW.
- Ventana operativa robusta: pH 8.5-9.0 y 50-60 C.

## 9. Criterios de diseno semiprofesional

### 9.1 Deflectores (baffles)

Para tanques agitados con flujo turbulento:

- Numero recomendado: 4 baffles.
- Ancho recomendado: $B\approx D/10$.
- Separacion a pared: 1-2% de $D$ para evitar zonas muertas.

Con $D=2.76$ m:

$$
B=2.76/10=0.276\ \text{m}
$$

### 9.2 Potencia corregida por accesorios internos

Se considera correccion por baffles y viscosidad aparente:

$$
P_{corr}=P\,f_b\,f_\mu
$$

Con $f_b=1.15$ y $f_\mu=1.05$:

$$
P_{corr}=6.1\times1.15\times1.05=7.36\ \text{kW}
$$

Seleccion 7.5 kW mantiene margen operativo.

## 10. Hidraulica de linea de alimentacion

Se integra criterio de Darcy-Weisbach para la linea de alimentacion de lixiviante.

Datos de referencia:

- $Q=12\ \text{m}^3/\text{h}=0.00333\ \text{m}^3/s$
- $D_i=0.063$ m (DN65)
- $L=50$ m
- $f=0.018$
- $\Sigma K=8.0$

Velocidad:

$$
v=\frac{Q}{A}=1.07\ \text{m/s}
$$

Perdida por friccion:

$$
h_f=f\frac{L}{D}\frac{v^2}{2g}=0.84\ \text{m}
$$

Perdidas menores:

$$
h_m=\Sigma K\frac{v^2}{2g}=0.47\ \text{m}
$$

Con elevacion estatica de 8.0 m y margen 15%:

$$
H_{TDH}\approx10.7\ \text{m}
$$

## 11. Sensibilidad operativa rapida

### 11.1 Efecto de temperatura sobre rendimiento

| Temperatura | Impacto esperado en $\eta_{ext}$ |
|---|---|
| 45-50 C | Menor cinetica, aumento de tiempo requerido |
| 50-60 C | Zona recomendada de operacion |
| >65 C | Riesgo de desnaturalizacion proteica |

### 11.2 Efecto de tiempo de residencia

| $\tau$ (h) | Volumen requerido para 12.26 m3/h (fs = 1.2) |
|---:|---:|
| 0.75 | 11.0 m3 |
| 0.90 | 13.2 m3 |
| 1.00 | 14.7 m3 |

Conclusión: diseno de 14 m3 conserva robustez ante variaciones de carga.
