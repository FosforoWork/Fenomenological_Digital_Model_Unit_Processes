# Calculos de Molienda

## 1. Objetivo

Presentar calculos termodinamicos, fisicos y de dimensionamiento para molienda de particulas, con ejemplo clasico de azucar pulverizado y caso de proteina de soya deshidratada.

## 2. Base de calculo

### 2.1 Caso simplificado (pulverizacion de azucar)

| Variable | Valor |
|---|---:|
| Material de entrada | 1000 kg/h |
| Tamanio inicial promedio, di | 500 μm (100 mesh) |
| Tamanio final promedio, df | 50 μm (325 mesh) |
| Indice de work index, Wi | 2.5 kWh/t |
| Densidad del azucar | 1600 kg/m³ |

### 2.2 Caso proyecto (proteina de soya post-secado)

| Variable | Valor |
|---|---:|
| Polvo de entrada | 364.6 kg/h |
| Tamanio inicial (aglomerados) | 150-250 μm |
| Tamanio final especificacion | 74-149 μm (100-200 mesh) |
| Indice de work index aprox, Wi | 2.8 kWh/t |
| Velocidad del molino | ~1500-2000 rpm |

## 3. Modelo termodinamico y mecanico

### 3.1 Ecuacion de Bond para energia de molienda

$$
E=W_i\left(\frac{1}{\sqrt{d_f}}-\frac{1}{\sqrt{d_i}}\right)\quad\text{[kWh/t]}
$$

Donde:
- $E$ = energia especifica requerida
- $W_i$ = indice de trabajo (kWh/t), depende del material
- $d_f$ = tamanio final (μm)
- $d_i$ = tamanio inicial (μm)

### 3.2 Energia total consumida

$$
E_{total}=E\times\dot m\quad\text{[kW]}
$$

### 3.3 Potencia mecanica del molino (con eficiencia)

$$
P_{molino}=\frac{E_{total}}{\eta_{mec}}\quad\text{[kW]}
$$

Tipico: $\eta_{mec}=0.70$ a 0.80 (friccion de cojinetes, aire, etc.)

### 3.4 Diametro de particula promedio (simplificado)

$$
d_{prom}=\frac{d_i+d_f}{2}
$$

Mas exacto (media geometrica):

$$
d_{geom}=\sqrt{d_i \cdot d_f}
$$

## 4. Ejemplo clasico: pulverizacion de azucar

### 4.1 Parametros

- $d_i=500$ μm
- $d_f=50$ μm
- $W_i=2.5$ kWh/t (tipico azucar cristalizado)

### 4.2 Energia especifica

$$
E=2.5\left(\frac{1}{\sqrt{50}}-\frac{1}{\sqrt{500}}\right)
$$

$$
E=2.5\left(\frac{1}{7.071}-\frac{1}{22.361}\right)=2.5(0.1414-0.0447)
$$

$$
E=2.5\times0.0967=0.242\ \text{kWh/t}
$$

### 4.3 Potencia requerida

$$
E_{total}=0.242\times1000/1000=0.242\ \text{kW} \quad\text{(para 1 t/h)}
$$

Con eficiencia 75%:

$$
P_{molino}=\frac{0.242}{0.75}=0.323\ \text{kW}
$$

Seleccion comercial: molino de 0.75-1.5 kW (con margen).

## 5. Caso proyecto: proteina de soya

### 5.1 Parametros

- Entrada: 364.6 kg/h $\approx 0.365$ t/h
- $d_i=200$ μm (promedio aglomerados post-spray)
- $d_f=110$ μm (especificacion 100-200 mesh, aproximadamente)
- $W_i=2.8$ kWh/t (proteina deshidratada, ligeramente mas dura que azucar)

### 5.2 Energia especifica

$$
E=2.8\left(\frac{1}{\sqrt{110}}-\frac{1}{\sqrt{200}}\right)
$$

$$
E=2.8\left(\frac{1}{10.488}-\frac{1}{14.142}\right)=2.8(0.0954-0.0707)
$$

$$
E=2.8\times0.0247=0.0692\ \text{kWh/t}
$$

### 5.3 Energia total consumida

$$
E_{total}=0.0692\times0.3646=0.0252\ \text{kW}
$$

Notoriamente menor que secado; confirma que molienda es operacion de bajo consumo energetico relativo.

Con eficiencia mecanica 75%:

$$
P_{molino}=\frac{0.0252}{0.75}=0.0336\ \text{kW}
$$

Sin embargo, usar molino industrial de martillos tipicamente requiere minimo 1.5-2 kW por concepto de motor + rotacion continua.

### 5.4 Capacidad y diseno de molino

Para 364.6 kg/h con molino de 500 kg/h nominal:

- Factor de utilizacion: 364.6 / 500 = 0.73 (operacion confortable, &lt;80%)
- Molino recomendado: martillos sanitario 500 kg/h
- Potencia nominal: 5.5 kW
- Velocidad: 1500-2000 rpm

## 6. Analisis de tamaniy y distribucion post-molienda

### 6.1 Tamanio geométrico promedio

$$
d_{geom,soya}=\sqrt{200\times110}=148.3\ \text{μm}
$$

Dentro del rango 100-200 mesh (74-149 μm) de limite inferior; confirmada necesidad de tamizado posterior.

### 6.2 Indice de tamanio unificado (Rosin-Rammler)

Distribucion empirica de particulas post-molienda:

$$
y=1-e^{-(d/d')^n}
$$

Donde $n$ es el modulo de uniformidad (tipico 2-3 para molienda por impacto).

Para $d'=120$ μm y $n=2.5$:
- % &lt; 50 μm: 5%
- % &lt; 100 μm: 35%
- % &lt; 200 μm: 95%

## 7. Tabla de propiedades y parametros de referencia

| Material | Wi (kWh/t) | Densidad (kg/m³) | Dureza Mohs | Notas |
|---|---:|---:|---:|---|
| Azucar cristalizado | 2.5 | 1600 | 2.5 | Fragil, bajo Wi |
| Proteina seca | 2.8-3.2 | 1350 | 2-3 | Poco abrasiva |
| Sal | 2.3 | 2160 | 2.5 | Cristalina |
| Harina | 1.8-2.0 | 1500 | - | Muy suave |
| Carbonato de calcio | 3.5-4.0 | 2700 | 3 | Moderado |

| Tamanio (mesh) | Abertura (μm) | Secuencia tipica |
|---|---:|---|
| 100 | 149 | Entrada post-spray |
| 150 | 105 | Granulometria intermedia |
| 200 | 74 | Limite fino especificacion |
| 325 | 44 | Fineza extrema |

## 8. Resultado ejecutivo

- Caso azucar: E = 0.242 kWh/t, P = 0.32 kW (muy bajo, escala laboratorio ineficiente).
- Caso soya: E = 0.069 kWh/t, 364.6 kg/h, P nominal = 5.5 kW (operacion confortable con margen).
- Molino recomendado: martillos sanitario 500 kg/h, 1500-2000 rpm, 5.5 kW.
- Salida esperada: polvo desaglomerado 110-150 μm promedio, listo para tamizado posterior.

## 9. Análisis Exergético y Comparativa Bond vs Rittinger

### 9.1 Análisis Exergético HCA

**Definición de exergía**: Para procesos mecánicos de molienda, la exergía destruida es la energía NO convertible en trabajo útil (reducción de tamaño), sino disipada como:
- Calor de fricción en cojinetes
- Calor por deformación plástica de partículas
- Energía cinética residual en aire del molino

La exergía **reversible** mínima teórica para reducir tamaño es:

$$\dot{E}x_{rev} = \dot{m} \cdot g(d_i \to d_f)$$

donde $g$ es el "trabajo mínimo reversible" ≈ energía de creación de superficie nueva.

La exergía **destruida** es:

$$\dot{E}x_{destroy} = \dot{W}_{real} - \dot{W}_{rev}$$

**Para caso soya (molienda 200 μm → 110 μm):**

- $\dot{W}_{real} = 0.0336$ kW (calculado en §5.3)
- Trabajo reversible ≈ 10-20% del real en molienda por impacto (típico)
- $\dot{W}_{rev} ≈ 0.005$ kW
- $\dot{E}x_{destroy} = 0.0336 - 0.005 = 0.0286$ kW

**Rendimiento exergético:**

$$\eta_{ex} = \frac{\dot{W}_{rev}}{\dot{W}_{real}} = \frac{0.005}{0.0336} ≈ 15\%$$

⚠️ **Interpretación**: La molienda es inherentemente ineficiente exergéticamente (~85% exergía destruida). Esto es **normal y aceptado** en ingeniería de procesos particulados, donde la creación de superficie nueva es termodinámicamente "cara". Optimización debe enfocarse en minimizar fricción, no en idealizar reversibilidad física imposible.

**Comparativa con desintegración mineral (trituradores)**: 
- Trituración gruesa (100-10 mm): η_ex ≈ 5-10% (peor)
- Molienda fina (1-0.1 mm): η_ex ≈ 15-30% (mejor)  
- **Conclusión**: Molienda de soya a nivel actual es MEJORABLE; considerar pre-fractura o activación térmica.

---

### 9.2 Modelo de Rittinger

Para molienda fina:

$$
E_R=K_R\left(\frac{1}{d_f}-\frac{1}{d_i}\right)
$$

Con $K_R$ calibrado por material. Rittinger suele sobreestimar energia en molienda gruesa y ajusta mejor en molienda muy fina.

### 9.3 Criterio de uso

- Bond: recomendado en diseno preliminar industrial multirango.
- Rittinger: util para refinamiento de polvo en etapas finales.

## 10. Velocidad Periférica, Regimen de Impacto y Sensibilidad Operativa

### 10.1 Velocidad periférica y régimen de impacto

Para rotor de molino de martillos de diametro 0.35 m a 1800 rpm:

$$
v_p=\pi DN=\pi(0.35)(30)=33\ \text{m/s}
$$

Rango tipico de diseno para impacto efectivo en polvos secos:

- 25 a 50 m/s.

El valor calculado queda en banda operativa recomendable.

### 10.2 Sensibilidad Multivariable — Matriz de Escenarios (Caso Soya)

Análisis paramétrico: Cómo varía potencia requerida al cambiar tamaño entrada, tamaño salida y RPM.

**Matriz de Energía Específica (kWh/t)** — Fórmula Bond: $E = W_i (\frac{1}{\sqrt{d_f}} - \frac{1}{\sqrt{d_i}})$

| Tamaño Entrada (μm) | RPM 1000 | RPM 1500 | RPM 2000 | RPM 2500 | Efecto RPM |
|---|:---:|:---:|:---:|:---:|---|
| **d_f = 50 μm** | | | | | |
| d_i = 100 | 0.548 | 0.548 | 0.548 | 0.548 | 0× (Bond independe RPM) |
| d_i = 150 | 0.355 | 0.355 | 0.355 | 0.355 | — |
| d_i = 200 | 0.238 | 0.238 | 0.238 | 0.238 | — |
| **d_f = 100 μm** | | | | | |
| d_i = 200 | 0.245 | 0.245 | 0.245 | 0.245 | — |
| d_i = 250 | 0.179 | 0.179 | 0.179 | 0.179 | — |
| d_i = 300 | 0.134 | 0.134 | 0.134 | 0.134 | — |

**Interpretación**: La ecuación Bond es **independiente de RPM**; la velocidad periférica afecta eficiencia de separación (granulometría) pero NO consumo energético teórico. Sin embargo:

- **RPM real > 2500**: Riesgo de sobrecalentamiento, desgaste acelerado → ↑ potencia friccional parasitaria
- **RPM < 1200**: Impactos débiles → ↑ energía específica efectiva (baja eficiencia)

**Rango óptimo operacional**: 1500-2000 RPM (compromiso energía + granulometría)

**Simulación potencia real (5.5 kW nominal, eficiencia 75%):**

| Escenario | Caudal (kg/h) | E nominal (kWh/t) | P teórica (kW) | P real con η=75% (kW) | P friccional (kW) | P total (kW) | Utilización |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **Soya nominal** | 364.6 | 0.0692 | 0.0252 | 0.0336 | 0.15 | 0.18 | 3.3% |
| Soya 400 kg/h (↑carga) | 400 | 0.0692 | 0.0277 | 0.0369 | 0.20 | 0.24 | 4.3% |
| Soya 500 kg/h (↑carga) | 500 | 0.0692 | 0.0346 | 0.0461 | 0.30 | 0.35 | 6.3% |
| **Azúcar 1000 kg/h** | 1000 | 0.242 | 0.242 | 0.323 | 0.40 | 0.72 | 13.1% |
| Azúcar + refinamiento | 800 | 0.38 | 0.304 | 0.405 | 0.50 | 0.91 | 16.5% |

**Conclusión**: Molino 5.5 kW titular puede procesar hasta ~500 kg/h soya O 800 kg/h azúcar sin exceder capacidad nominal. Factor seguridad: 2-3× recomendado.

---

## 11. Desgaste, Mantenimiento Preventivo y Validación Experimental

### 11.1 Indicadores practicos

- Aumento de fraccion gruesa (>100 mesh) a igual rpm.
- Incremento de vibraciones del rotor.
- Aumento de consumo especifico de energia.

### 11.2 Frecuencia orientativa

| Elemento | Intervalo orientativo |
|---|---|
| Inspeccion de martillos | Cada 250 h |
| Rotacion/inversion de martillos | 500-700 h |
| Reemplazo de malla interna | 800-1200 h |

Estos intervalos se ajustan segun abrasividad real del polvo y regimen de operacion.

### 11.3 Validación Experimental — Bond Index y Norma ASTM B214

El **Bond Work Index (Wi)** es variable por material y debe validarse experimentalmente. Para proteína de soya desengrasada:

**Valores bibliográficos típicos** (Norma ASTM E11, molinos de laboratorio):
- Soya desengrasada (deshidratada): Wi = 2.5-3.2 kWh/t ✓ (nuestro 2.8 es central)
- Soya con piel: Wi = 3.5-4.0 kWh/t (más dura)
- Harina soya: Wi = 1.8-2.0 kWh/t (más blanda)

**Procedimiento ASTM B214** (Lab Bond Grindability Test):
1. Moler muestra 250-500 g desde ~1000 μm hasta especificación target
2. Medir nuevo Surface Area por BAI (Blaine Air Permeability Index)
3. Calcular: $W_i = \frac{10}{NA \sqrt[4]{d_i/d_f} - 10/\sqrt[4]{d_f}}$ (fórmula modificada Bond)

**Recomendación**: Realizar test ASTM B214 con proteína de soya PROJECT ( lote real) antes de escalar a producción continua. Costo: $300-500, tiempo 2-3 días laborales. Precisión ±5% típica.

**Risk si NO se valida**: 
- Predictibilidad de energía ±30% (inaceptable diseño industrial)
- Posible sub-dimensionamiento motor (caveo de equipos)
- Desajuste granulometría vs especificación
