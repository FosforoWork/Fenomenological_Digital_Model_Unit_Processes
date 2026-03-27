# Calculos de Tamizado (Clasificacion por Tamanio)

## 1. Objetivo

Presentar calculos fisicos y de dimensionamiento para tamizado en criba vibratoria, con ejemplo clasico de harina y caso de clasificacion de proteina de soya a especificacion 100-200 mesh.

## 2. Base de calculo

### 2.1 Caso simplificado (harina de trigo)

| Variable | Valor |
|---|---:|
| Entrada de harina | 1000 kg/h |
| Malla superior (primer cilindro) | 100 mesh (149 μm) |
| Malla inferior (segundo cilindro) | 200 mesh (74 μm) |
| Fraccion pasante en 200 mesh | 0.10 (10%) |
| Fraccion retenida en 100 mesh | 0.05 (5%) |
| Fraccion especificacion (100-200) | 0.85 (85%) |

### 2.2 Caso proyecto (proteina de soya post-molienda)

| Variable | Valor |
|---|---:|
| Polvo de entrada | 364.6 kg/h |
| Malla superior | 100 mesh (149 μm) |
| Malla inferior | 200 mesh (74 μm) |
| Especificacion comercial | Pasa 200 mesh &lt;2%, retiene 100 &gt;5% rechazado |
| Humedad de entrada | &lt;5% (post-secado) |
| Densidad aparente | 0.7-0.8 kg/dm³ |

## 3. Balances de masa en criba de doble malla

### 3.1 Balances globales

$$
\dot m_{entrada}=\dot m_{pasante,200}+\dot m_{retenido,100}+\dot m_{especificacion,100-200}
$$

### 3.2 Fracciones y rendimientos

Fraccion en pasante 100 mesh (finos):

$$
\frac{m_{<100}}{m_{entrada}}=\alpha
$$

Fraccion en especificacion 100-200:

$$
\frac{m_{100-200}}{m_{entrada}}=\beta
$$

Fraccion rechazada (retenida en 100):

$$
\frac{m_{>100}}{m_{entrada}}=\gamma
$$

Balance:

$$
\alpha+\beta+\gamma=1.0
$$

### 3.3 Eficiencia de separacion

Para especificacion objetivo (100-200 mesh):

$$
\eta=\frac{m_{100-200,obtenida}}{m_{100-200,alimentada}}\times100\%
$$

En practica industrial, eficiencia tipica 85-95% en cribas vibratorias bien ajustadas.

## 4. Ejemplo clasico: tamizado de harina

### 4.1 Balances de entrada y salida

Especificacion deseada: &lt;5% sobre 100 mesh y &lt;10% bajo 200 mesh.

| Fraccion | Flujo (kg/h) | % |
|---|---:|---:|
| &lt;200 mesh (finos) | 100 | 10.0 |
| 100-200 mesh (especific) | 850 | 85.0 |
| &gt;100 mesh (rechazado) | 50 | 5.0 |
| **Total entrada** | **1000** | **100** |

### 4.2 Eficiencia de separacion

Si en alimentacion hay 900 kg/h de material que deberia estar en rango 100-200:

$$
\eta_{separacion}=\frac{850}{900}\times100=94.4\%
$$

## 5. Caso proyecto: proteina de soya

### 5.1 Composicion esperada post-molienda

Con distribucion Rosin-Rammler estimada:

| Fraccion | Datos | Flujo (kg/h) |
|---|---|---:|
| &lt;200 mesh | Una estimacion baja (3-5% tipico) | 10.9 - 18.2 |
| 100-200 mesh (especific) | Mayoria (90-92%) | 328-335 |
| &gt;100 mesh (rechazados) | Aglomerados (5-7%) | 18-25 |
| **Total entrada** | - | **364.6** |

### 5.2 Balances por criba doble-malla

Primera malla (100 mesh):

$$
m_{<100}=364.6\times0.05=18.2\ \text{kg/h}
$$

$$
m_{>100}=364.6\times0.95=346.4\ \text{kg/h}
$$

Segunda malla (200 mesh, sobre material &gt;100):

$$
m_{200-100}=346.4\times0.94=325.6\ \text{kg/h}
$$

$$
m_{>200}=346.4\times0.06=20.8\ \text{kg/h}
$$

**Salida final:**

| Stream | kg/h | % |
|---|---:|---:|
| &lt;200 mesh (finos) | 18.2 | 5.0 |
| 100-200 mesh (producto) | 325.6 | 89.3 |
| &gt;100 mesh (gruesos) | 20.8 | 5.7 |

### 5.3 Eficiencia de tamizado

Si de esto se recicla el material &gt;100 mesh nuevamente:

$$
\eta_{ciclo}=\frac{325.6}{364.6}\times100=89.3\%\ \text{en una pasada}
$$

Con reciclaje a molino de gruesos:

$$
\eta_{global}\approx95-98\%\ \text{(multipasadas)}
$$

## 6. Dimensionamiento de criba vibratoria

### 6.1 Area superficial de malla requerida

Criterio empirico de carga superficial para polvos secos:

$$
q_{sup}=5\text{ a }10\ \text{t/(m}^2\cdot\text{h)}
$$

Para 364.6 kg/h = 0.3646 t/h:

$$
A_{malla}=\frac{0.3646}{7.5}=0.049\ \text{m}^2
$$

Con margen de seguridad (factor 1.5):

$$
A_{diseno}=0.049\times1.5=0.073\ \text{m}^2
$$

Criba rectangular tipica: 0.9 m × 0.1 m = 0.09 m² (suficiente).

### 6.2 Frecuencia y amplitud de vibracion

Tipico para criba lineal:

- Frecuencia: 50-100 Hz
- Amplitud: 3-8 mm
- Selecta para polvos secos: ~70 Hz, 5 mm

### 6.3 Potencia de motor vibrador

Para criba de 0.09 m² con material seco:

$$
P_{motor}=1.0\text{ a }1.5\ \text{kW}
$$

Seleccion: motor vibratorio 1.5 kW incluido en bloque "criba vibratoria".

## 7. Propiedades de materiales y mallas

### 7.1 Especificaciones de mesh

| Mesh | Apertura (μm) | Uso tipico |
|---|---:|---|
| 50 | 297 | Gruesos, arena |
| 100 | 149 | Limite grueso general |
| 150 | 105 | Granulometria media |
| 200 | 74 | Limite fino general |
| 325 | 44 | Polvos finos |
| 400 | 37 | Pigmentos, talcos |

### 7.2 Densidades aparentes (bulk)

| Material | ρ_aparente (kg/m³) | Notas |
|---|---:|---|
| Harina trigo | 750 | Aireada |
| Proteina polvo | 700-800 | Aglomerada, baja densidad |
| Azucar granulada | 900 | Cristales densos |
| Sal fina | 1100 | Higroscopica |

### 7.3 Mallas de acero inoxidable

- Diametro de alambre: 0.08-0.15 mm (depende de apertura)
- Material: acero inoxidable 304 o 316 (alimentos)
- Durabilidad: 500-1000 h de operacion continua
- Costo de reemplazo: bajo (10-15 USD por malla)

## 8. Resultado ejecutivo

- Caso harina: 85% en especificacion, eficiencia ~94% en una pasada.
- Caso soya: entrada 364.6 kg/h, salida especificacion (100-200 mesh) ~326 kg/h (89.3% en una pasada).
- Criba recomendada: vibratoria doble malla, 0.9 m × 0.1 m, 70 Hz, 5 mm amplitud.
- Potencia: 1.5 kW (motor vibrador); bajo consumo relativo.
- Con reciclaje de gruesos a molino: recuperacion global 95-98%.

## 9. Probabilidad de paso y humedad critica

Una expresion simplificada para probabilidad de paso por malla es:

$$
P_{paso}=1-e^{-k\,t\,\phi}
$$

donde $k$ depende de vibracion y geometria, $t$ es tiempo de residencia sobre malla, y $\phi$ representa cercania de particula al tamano de abertura.

En polvos proteicos finos, humedad critica orientativa:

- 6 a 8%: inicia aumento fuerte de aglomeracion.

Por eso se recomienda alimentar la criba con humedad <= 5%.

## 10. Colmatacion y perdida de capacidad

Se modela capacidad efectiva con factor de ensuciamiento de malla $f_c$:

$$
Q_{ef}=Q_{nom}(1-f_c)
$$

Si $f_c=0.15$ por acumulacion de finos:

$$
Q_{ef}=500(1-0.15)=425\ \text{kg/h}
$$

Sigue por encima de la carga del proceso (364.6 kg/h), pero con menor holgura operacional.

## 11. Recomendaciones de operacion semipro

| Item | Recomendacion |
|---|---|
| Limpieza de malla | Cada 4-8 h de operacion continua |
| Verificacion de tension de malla | Diario |
| Cambio preventivo de malla | 500-1000 h, segun abrasividad |
| Monitoreo de finos fuera de especificacion | Por lote o cada turno |

Conclusión: la estabilidad granulometrica depende tanto del molino como del estado de malla y la humedad del polvo.
