# Operaciones Unitarias del 4to Bloque: Secado, Molienda y Tamizado

## 1. Contexto general

El 4to bloque cubre las etapas finales de un proceso integrado de separacion y concentracion: transformar una pasta humeda en polvo seco uniforme, listo para envasado. Estas tres operaciones se complementan:

- **Secado:** Evaporar agua con minimo dano termico al producto
- **Molienda:** Desagregar el polvo inicial en particulas finas
- **Tamizado:** Clasificar por tamano de particula a especificacion comercial

## 2. Secado por Atomizacion (Spray Dryer)

### 2.1 Definicion
El secado por atomizacion transforma un liquido o pasta viscosa en polvo fino mediante:
1. Atomizacion en gotas muy pequenas
2. Contacto contracorriente con aire caliente
3. Evaporacion instantanea en caida a traves de la camara

### 2.2 Fenomeno dominante
- Transferencia simultanea de calor y masa.
- Evaporacion rapida (10-20 s) de particula pequena en ambiente caliente.
- Control cinetico por deshidratacion de frontera, no por difusion interna.

### 2.3 Variables criticas
- Temperatura de aire de entrada (180-200 C en aplicaciones proteicas).
- Temperatura de aire de salida (80-90 C, controlada por producto termolabil).
- Velocidad del disco atomizador (12000-25000 rpm).
- Caudal de aire de proceso (5-6 m³/kg de agua a evaporar).
- Humedad final objetivo (tipico &lt;5% para alimentos).

### 2.4 Ecuaciones guia
Balance de agua evaporada:

$$
\dot m_{H2O,evap}=\dot m_{entrada}-\dot m_{polvo,seco}
$$

Energia de evaporacion (latente + sensible):

$$
Q_{sec}=\dot m_{H2O}\lambda_{vap}+\dot m_{aire}(C_{p,aire})\Delta T_{aire}
$$

Donde $\lambda_{vap}\approx2400$ kJ/kg para evaporacion a presion atmosferica.

### 2.5 Equipos y materiales tipicos
- Camara cilindrica-conica (acero inoxidable 304, recubrimiento termico).
- Disco atomizador (tamanio 50-150 mm, velocidad 10000-25000 rpm).
- Ventilador centrifugo de aire caliente.
- Generador de calor (quemador o intercambiador).

## 3. Molienda (Reduccion de tamanio)

### 3.1 Definicion
La molienda reduce el tamanio de particulas solidas mediante impacto mecanico, friccion o cizalladura.

### 3.2 Fenomeno dominante
- Fractura de particula por concentracion de esfuerzo.
- Energia especifica de molienda (kWh/t de material procesado).

### 3.3 Variables criticas
- Tamanio de entrada (post-atomizacion: ~100-200 μm aglomerados).
- Tamanio de salida (especificacion: 100-200 mesh).
- Velocidad de molino (rpm, afecta energia de impacto).
- Capacidad procesada (kg/h).
- Dureza del material (impacta costo energetico).

### 3.4 Ecuaciones guia
Ecuacion de Bond para energia de molienda:

$$
E = W_i\left(\frac{1}{\sqrt{d_f}}-\frac{1}{\sqrt{d_i}}\right)
$$

Donde:
- $W_i$ = indice de work index (kWh/t, tipico 2-5 para polvos secos)
- $d_f$ = tamanio final (μm)
- $d_i$ = tamanio inicial (μm)

### 3.5 Equipos y materiales tipicos
- Molino de martillos (rotacion rapida, ideal para polvos).
- Molino de bolas (abrasion lenta, para molendas finas).
- Materiales: acero inoxidable o acero endurecido segun contacto.

## 4. Tamizado (Clasificacion por tamanio)

### 4.1 Definicion
El tamizado separa un polvo en fracciones de tamanio mediante una o mas mallas metalicas.

### 4.2 Fenomeno dominante
- Movimiento de particula sobre malla vibrante.
- Probabilidad de paso dependiente de tamanio y peso de particula.

### 4.3 Variables criticas
- Tamanios de malla (abertura nominal en μm o mesh).
- Frecuencia de vibracion (Hz, tipico 50-100).
- Amplitud de movimiento.
- Humedad del polvo (afecta aglomeracion y paso).
- Especificacion de producto (rango de tamanio aceptado).

### 4.4 Ecuaciones guia
Eficiencia global de separacion:

$$
\eta = \frac{m_{pasante,deseado}}{m_{entrada,deseada}}\times100\%
$$

Para especificacion 100-200 mesh:
- Pasa 200 mesh: &lt;2% en peso
- Retencion en 100 mesh: &lt;5%

### 4.5 Equipos y materiales tipicos
- Criba vibratoria (1-3 mallas, para capacidades medianas).
- Clasificador de aire (para finezas &lt;20 μm).
- Mallas de acero inoxidable o nylon segun producto.

## 5. Comparacion y flujo integrado

| Etapa | Entrada | Proceso | Salida | Equipo |
|---|---|---|---|---|
| Secado | Pasta 50% humedad | Evaporacion 10-20 s, 180 C | Polvo ~5% humedad | Spray dryer |
| Molienda | Polvo 100-200 μm | Impacto mecanico | Polvo desaglomerado | Molino martillos |
| Tamizado | Polvo heterogeneo | Vibracion sobre mallas | Polvo 100-200 mesh | Criba doble malla |

## 6. Notas de diseno

- **Humedad:** Post-secado debe ser &lt;5% para estabilidad microbiana; post-tamizado generalmente se mantiene si camara de secado es hermetica.
- **Energia:** Molienda y tamizado son moderados en consumo relativo (7 kW c/u vs. 378 kW del secador).
- **Escala:** Los calculos detallados se desarrollan en archivos separados, con ejemplos clasicos y aplicacion al caso de proteina de soya.

