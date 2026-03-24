# Calculos de Secado por Atomizacion

## 1. Objetivo

Presentar calculos termodinamicos, fisicos y de dimensionamiento para secado por atomizacion (spray dryer), con ejemplo clasico simplificado y caso aplicado a proteina de soya.

## 2. Base de calculo

### 2.1 Caso simplificado (cafe instantaneo)

| Variable | Valor |
|---|---:|
| Extracto de cafe (entrada) | 500 kg/h |
| Humedad de entrada | 0.95 (95%) |
| Humedad final objetivo | 0.03 (3%) |
| Temperatura aire entrada | 180 C |
| Temperatura aire salida | 85 C |
| Densidad del aire (promedio) | 0.65 kg/m³ |

### 2.2 Caso proyecto (proteina de soya)

| Variable | Valor |
|---|---:|
| Pasta liquida (entrada) | 692.8 kg/h |
| Fraccion humedad entrada | 0.50 |
| Fraccion humedad final objetivo | 0.05 |
| Temperatura aire entrada | 190 C |
| Temperatura aire salida | 85 C |
| Tiempo de residencia en camara | 10-20 s |
| Densidad promedio lodo | 1080 kg/m³ |

## 3. Modelos termodinamicos

### 3.1 Balance de masa de agua

$$
\dot m_{H2O,evap}=\dot m_{entrada}\,x_{H2O,in}-\dot m_{polvo,seco}\,x_{H2O,out}
$$

Forma simplificada para cambio unilateral:

$$
\dot m_{H2O,evap}=\dot m_{entrada}(h_{in}-h_{out})
$$

Donde $h$ es la humedad absoluta (kg agua / kg solido seco).

### 3.2 Energia latente de vaporización

A 100 C (presion atmosferica):

$$
\lambda_{vap}=2257\ \text{kJ/kg}
$$

A 48 C (bajo vacio tipico):

$$
\lambda_{vap}\approx2370\ \text{kJ/kg}
$$

Aproximacion lineal para rango 50-200 C:

$$
\lambda_{vap}=2500-2.4\,T_C
$$

### 3.3 Energia de calentamiento y enfriamiento de aire

$$
Q_{aire}=\dot m_{aire}\,C_{p,aire}(T_{in}-T_{out})
$$

Para aire seco: $C_{p,aire}\approx1.005$ kJ/kg·K

### 3.4 Carga termica total del secador

$$
Q_{sec,total}=\dot m_{H2O}\lambda_{vap}+Q_{sensible,producto}+Q_{perdidas}
$$

Aproximacion practica con eficiencia 90%:

$$
Q_{real}=\frac{Q_{proceso}}{0.90}
$$

## 4. Ejemplo clasico: cafe instantaneo

### 4.1 Agua a evaporar

$$
\dot m_{H2O}=500\times\frac{0.95}{0.05}-500\times\frac{0.03}{0.97}\approx500\times(19-0.031)\approx9485\ \text{kg/h}
$$

Corrigiendo (base seco):

$$
h_{in}=\frac{0.95}{1-0.95}=19\ \text{kg H2O/kg solido}
$$

$$
h_{out}=\frac{0.03}{1-0.03}=0.0309\ \text{kg H2O/kg solido}
$$

$$
m_{solido,seco}=\frac{500}{1+19}=25\ \text{kg/h}
$$

$$
\dot m_{H2O}=25\times(19-0.0309)=473\ \text{kg/h}
$$

### 4.2 Energia de evaporacion

$$
Q_{lat}=473\times2400=1,135,200\ \text{kJ/h}=315\ \text{kW}
$$

### 4.3 Caudal de aire requerido (aproximado)

Con $\Delta T_{aire}=180-85=95$ K:

$$
\dot m_{aire}=\frac{Q_{lat}}{C_{p,aire}\Delta T}=\frac{315}{1.005\times95}=3290\ \text{kg/h}
$$

Caudal volumetrico (a T promedio ~130 C, $\rho\approx0.75$ kg/m³):

$$
\dot V_{aire}=\frac{3290}{0.75}=4387\ \text{m}^3/\text{h}
$$

## 5. Caso proyecto: proteina de soya

### 5.1 Agua a evaporar

$$
h_{in}=\frac{0.50}{1-0.50}=1.0\ \text{kg H2O/kg solido}
$$

$$
h_{out}=\frac{0.05}{1-0.05}=0.0526\ \text{kg H2O/kg solido}
$$

$$
m_{solido}=\frac{692.8}{1+1.0}=346.4\ \text{kg/h}
$$

$$
\dot m_{H2O}=346.4\times(1.0-0.0526)=328.2\ \text{kg/h}
$$

### 5.2 Energia de evaporacion

$$
Q_{lat}=328.2\times2400=787,680\ \text{kJ/h}=219\ \text{kW}
$$

Considerando sensible y perdidas:

$$
Q_{proceso}\approx340\ \text{kW}
$$

Con eficiencia 90%:

$$
Q_{real}=\frac{340}{0.90}=378\ \text{kW}
$$

### 5.3 Caudal de aire

$$
\dot m_{aire}=\frac{Q_{proceso}}{C_{p,aire}\Delta T}=\frac{340}{1.005\times(190-85)}=3350\ \text{kg/h}
$$

Volumetrico a T promedio ~137 C, $\rho\approx0.72$ kg/m³:

$$
\dot V_{aire}=\frac{3350}{0.72}=4653\ \text{m}^3/\text{h}
$$

Valor recomendado operativo: 4500-5000 m³/h (9000 m³/h es flujo nominal para margen).

## 6. Dimensionamiento de camara (spray dryer)

### 6.1 Volumen de camara cilindrica-conica

Para tiempo de residencia objetivo de 10-20 s y caudal de aire de proceso de 9000 m3/h:

Velocidad periferica del aire:  ~1.5 m/s hacia abajo; considerando expansión:

$$
\dot V_{aire,proceso}=9000\ \text{m}^3/\text{h}=2.5\ \text{m}^3/\text{s}
$$

Tiempo de caida de particula en camara (t = 10-20 s) con velocidad terminal promedio ~0.5 m/s:

$$
H_{caida}\approx 0.5\ \text{m/s}\times15\ \text{s}=7.5\ \text{m}
$$

Con geometria cilindrica-conica: $D=3.0$ m, $H_{cil}=4.5$ m, $H_{cono}=2.0$ m:

$$
V_{cil}=\frac{\pi D^2}{4}H=\frac{\pi(3.0)^2}{4}(4.5)=31.8\ \text{m}^3
$$

$$
V_{cono}=\frac{1}{3}\frac{\pi D^2}{4}H_c=\frac{1}{3}\frac{\pi(3.0)^2}{4}(2.0)=4.7\ \text{m}^3
$$

$$
V_{total}=31.8+4.7=36.5\ \text{m}^3
$$

### 6.2 Disco atomizador

- Diametro del disco: 100 mm
- Velocidad de rotacion: 18000 rpm
- Velocidad periferica: $v=\pi D N = \pi(0.1)(300)=94.2$ m/s (tipicamente 80-120 m/s)
- Tamanio de gota (DVB): ~ 80 μm

### 6.3 Potencia del ventilador

Calda de presion estimada en camara: ~500 Pa

$$
P_{vent}=\frac{\dot V \Delta P}{\eta}=\frac{2.5\times500}{0.75}=1667\ \text{W}\approx1.7\ \text{kW}
$$

Seleccion comercial: 7.5 kW (incluye margen y ductos).

## 7. Tabla de propiedades termodinamicas

| Propiedad | Agua 100 C | Aire seco 25 C | Aire seco 150 C |
|---|---:|---:|---:|
| Densidad, kg/m³ | 958 | 1.18 | 0.835 |
| Cp, kJ/kg·K | 4.22 | 1.005 | 1.026 |
| Viscosidad dinamica, Pa·s | 0.000280 | 0.0000184 | 0.0000205 |
| Conductividad termica, W/m·K | 0.680 | 0.026 | 0.030 |
| Calor latente, kJ/kg | 2257 | - | - |

## 8. Resultado ejecutivo

- Caso cafe: 473 kg/h agua, ~315 kW energia latente, 4400 m³/h aire.
- Caso soya: 328 kg/h agua, ~219 kW energia latente, 4650 m³/h aire.
- Camara recomendada: D=3.0 m cilindrica + cono, V total=36.5 m³.
- Ventilador: 7.5 kW; generador de calor: 378 kW real.
- Polvo final: ~365 kg/h proteina a &lt;5% humedad, tamanio ~80 μm.

## 9. Eficiencia termica y perdidas

Se define eficiencia termica global del secador:

$$
\eta_{th}=\frac{Q_{evap\ util}}{Q_{input}}
$$

Para el caso base:

$$
\eta_{th}=\frac{219}{378}=0.58\ (58\%)
$$

Valor coherente para spray dryer con perdidas por paredes, gases de escape y finos arrastrados.

## 10. Recuperacion de finos en ciclón (preliminar)

Se adopta eficiencia global de ciclón simple para polvo fino alimentario:

- 85 a 95% para particulas > 10-20 μm.

Balance de finos si arrastre bruto = 3% del polvo:

$$
m_{arrastre}=0.03\times364.6=10.9\ \text{kg/h}
$$

Con ciclón al 90%:

$$
m_{recuperado}=0.90\times10.9=9.8\ \text{kg/h}
$$

Finos perdidos al stack:

$$
m_{perdido}=1.1\ \text{kg/h}
$$

## 11. Sensibilidad operativa rapida

| Variable | Cambio | Efecto esperado |
|---|---|---|
| Aire entrada 190 -> 200 C | +10 C | Menor humedad final, mayor riesgo termico |
| Aire salida 85 -> 95 C | +10 C | Menor secado neto, posible incremento de humedad |
| Humedad entrada 50 -> 55% | +5% abs | Aumenta carga termica y caudal de aire requerido |

Conclusión: controlar humedad de alimentacion y temperatura de salida del aire es critico para estabilidad del polvo final.
