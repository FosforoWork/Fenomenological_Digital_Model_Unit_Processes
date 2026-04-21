# Informe Academico-Tecnico del Proyecto
## Proyecto 4to Bloque - Linea de Procesamiento de Polvo Vegetal

Fecha: 2026-04-21

## Resumen ejecutivo

Este informe presenta el desarrollo tecnico del Proyecto 4to Bloque para una linea de procesamiento de polvo vegetal que integra operaciones unitarias de molienda, tamizado, preparacion de suspension, filtracion y secado. El objetivo tecnico fue transformar una alimentacion humeda inicial de 10.0 kg hasta un producto final con humedad especificada de 8% bh y tamano de particula controlado.

Los resultados clave del calculo integrado son:

- Diametro promedio de particula post-molienda: 0.3674 mm.
- Relacion de reduccion: 10.8873.
- Energia de molienda (Bond): 14.9474 kWh/ton.
- D50 de tamizado: 0.4017 mm.
- Eficiencia de tamizado (fraccion objetivo): 35.0%.
- Concentracion de solidos en suspension: 18.18% (0.1818 kg/kg).
- Resistencia de torta: $\alpha=8.9171\times10^8$ m/kg.
- Resistencia del medio: $R_m=1.9403\times10^{11}$ 1/m.
- Masa final de producto: 1.5217 kg.
- Agua evaporada de secado: 2.6363 kg.
- Cierre de balance global de masa: 0.0000%.

El proceso cumple los requerimientos de planteamiento y presenta consistencia numerica alta, con trazabilidad metodologica explicitada para los puntos de mayor sensibilidad (ajuste de filtracion y dispersion puntual en secado).

## 1. Introduccion

La produccion de polvos vegetales estables requiere integrar fenomenos de reduccion de tamano, clasificacion granulometrica, separacion solido-liquido y remocion termica de humedad. En un entorno academico de operaciones unitarias, el proyecto permite evaluar:

- Conservacion de masa en sistemas secuenciales.
- Seleccion y aplicacion de modelos de ingenieria por etapa.
- Coherencia entre datos experimentales y supuestos de diseno.
- Calidad metodologica de la documentacion tecnica.

Este informe consolida la version final sincronizada de los calculos del 4to bloque y documenta su interpretacion tecnica.

## 2. Objetivos

### 2.1 Objetivo general

Disenar y verificar tecnicamente una mini-linea de procesamiento de polvo vegetal que cumpla especificacion de granulometria y humedad final, con cierre de masa global del sistema.

### 2.2 Objetivos especificos

1. Determinar parametros de molienda: $d_{prom}$, relacion de reduccion y energia especifica.
2. Construir la distribucion granulometrica y obtener $D_{50}$ y eficiencia de tamizado.
3. Definir la suspension de proceso en base de masa y concentracion de solidos.
4. Estimar parametros de filtracion por modelo de Ruth ($\alpha$, $R_m$).
5. Estimar desempeno de secado para 8% bh y energia minima teorica.
6. Verificar cierre de masa por etapa y global.

## 3. Alcance, criterio y metodologia

### 3.1 Alcance

El alcance cubre el lote de referencia de 10.0 kg de materia prima, incluyendo agua agregada en preparacion y corrientes de salida por rechazo, filtrado, evaporacion y producto final.

### 3.2 Criterio oficial de calculo

Se adopta la base oficial del documento integrado del 4to bloque:

- Humedad de torta en balance integrado: calculada desde $X_i=1.97$ kg agua/kg solido seco (66.33% bh).
- Cierre global reportado con base experimental trazable y unica.
- En secado se mantiene la misma base de masa usada en suspension y filtracion ($m_s=1.40$ kg).
- En filtracion se reporta ajuste de 8 puntos y contraste estadistico de subrango $V\ge5$ L.

### 3.3 Metodologia

1. Transcripcion de datos base y normalizacion de unidades.
2. Calculo por operacion unitaria con ecuaciones de referencia.
3. Reconciliacion de corrientes inter-etapa.
4. Auditoria de consistencia numerica y metodologica.
5. Consolidacion final en formato academico-tecnico.

## 4. Datos base de entrada

| Parametro | Valor |
|---|---|
| Masa inicial de materia prima | 10.0 kg |
| Humedad inicial de referencia | 60% bh |
| Tamano inicial promedio | 4.0 mm |
| Indice de Bond, $W_i$ | 13 kWh/ton |
| Fraccion objetivo tamizado | 0.25-0.42 mm |
| Relacion agua/solido | 1.2 kg/kg |
| Presion de filtracion, $\Delta P$ | 50 kPa |
| Area de filtro, $A$ | 0.05 m^2 |
| Viscosidad, $\mu$ | $1\times10^{-3}$ Pa*s |
| Concentracion de solidos, $C$ | 454 kg/m^3 |
| Humedad final objetivo | 8% bh |

Distribucion de tamizado usada:

| Tamano (mm) | Masa (kg) |
|---:|---:|
| 0.85 | 1.50 |
| 0.42 | 3.20 |
| 0.25 | 3.50 |
| 0.10 | 1.80 |

## 5. Desarrollo tecnico por operacion unitaria

## 5.1 Molienda

Se calculo el diametro promedio ponderado por masa retenida:

$$
 d_{prom}=\frac{\sum (d_i m_i)}{\sum m_i}=0.3674\ \text{mm}
$$

La relacion de reduccion obtenida fue:

$$
R_r=\frac{4.0}{0.3674}=10.8873
$$

Para energia se adopto Bond con base consistente en mm:

$$
E_{Bond}=W_i\left(\frac{1}{\sqrt{d_f}}-\frac{1}{\sqrt{d_i}}\right)=14.9474\ \text{kWh/ton}
$$

Adicionalmente, Kick y Rittinger se calibraron para equivalencia en el punto de diseno.

Interpretacion tecnica:

- La reduccion de tamano es alta y adecuada para alimentar tamizado selectivo.
- La energia especifica reportada es consistente con la escala de lote academico usada.

## 5.2 Tamizado

Se obtuvieron fraccion retenida, acumulada y porcentaje pasante para cada tamiz. El diametro medio de corte se calculo por interpolacion logaritmica:

$$
D_{50}=0.4017\ \text{mm}
$$

La eficiencia, definida como recuperacion de la fraccion objetivo sobre alimentacion total, fue:

$$
\eta_{tam}=\frac{3.50}{10.0}\times100=35.0\%
$$

Interpretacion tecnica:

- El sistema separa correctamente la fraccion de interes para proceso posterior.
- El criterio de eficiencia fue documentado explicitamente para evitar ambiguedad con definiciones alternativas de separacion.

## 5.3 Preparacion de suspension

Se adopto como base de solido la fraccion objetivo de 3.50 kg, con adicion de agua segun 1.2 kg/kg:

$$
m_s=3.50(1-0.60)=1.40\ \text{kg},\qquad m_w=4.20\ \text{kg}
$$

Concentracion de solidos en mezcla:

$$
C_{s,kg/kg}=\frac{1.40}{7.70}=0.1818
$$

$$
C_{s,\%}=18.18\%
$$

Aproximacion volumetrica:

$$
C_s\approx181.8\ \text{kg/m}^3
$$

Interpretacion tecnica:

- La concentracion de suspension del lote queda definida en base seca de forma trazable.
- Esta consistencia evita errores de arrastre entre unidades.

## 5.4 Filtracion

Se aplico el modelo lineal de Ruth:

$$
\frac{t}{V}=mV+b
$$

Ajuste oficial con los 8 puntos de laboratorio (en SI):

$$
m=1{,}619{,}338.2757\ \frac{s}{m^6},\qquad b=77{,}611.8410\ \frac{s}{m^3}
$$

Calidad del ajuste:

- $R^2$ global (8 puntos): 0.2141.
- $R^2$ en subrango $V\ge5$ L: 0.9996.

Con:

$$
\frac{t}{V}=\frac{\mu\alpha C}{2A^2\Delta P}V+\frac{\mu R_m}{A\Delta P}
$$

se obtuvo:

$$
\alpha=8.9171\times10^8\ \text{m/kg}
$$

$$
R_m=1.9403\times10^{11}\ \text{m}^{-1}
$$

Para balance integrado del lote (base experimental trazable):

$$
m_{torta,hum}=4.1580\ \text{kg},\qquad m_{filtrado}=3.5420\ \text{kg}
$$

Interpretacion tecnica:

- Los parametros calculados son consistentes con la recta oficial reportada.
- El contraste de $R^2$ muestra transitorio inicial en bajo volumen; se documento sin romper trazabilidad con la serie completa.

## 5.5 Secado

Meta final: 8% bh.

Conversion a base seca:

$$
X_f=\frac{0.08}{1-0.08}=0.0869565\ \frac{\text{kg agua}}{\text{kg solido seco}}
$$

Con $m_s=3.50$ kg:

$$
m_{producto}=1.40(1+0.0869565)=1.5217\ \text{kg}
$$

Agua evaporada en secado:

$$
m_{evap}=1.40(1.97-0.0869565)=2.6363\ \text{kg}
$$

Verificacion por balance de agua en torta:

$$
m_{evap}=2.7580-0.1217=2.6363\ \text{kg}
$$

Tiempo para alcanzar 8% bh por extrapolacion del ultimo tramo (100-120 min):

$$
t_{objetivo}=126.8921\ \text{min}
$$

Energia minima teorica de secado ($\lambda=2257$ kJ/kg):

$$
Q_{min}=2.6363\times2257=5950.0408\ \text{kJ}=1.6528\ \text{kWh}
$$

Interpretacion tecnica:

- Para cierre global de masa y energia del proceso, se usa una sola base experimental trazable.
- Esta base conserva continuidad entre suspension, filtracion y secado sin dualidad de supuestos.

## 6. Balance de masa y verificacion de integridad

### 6.1 Balance por etapas

| Etapa | Entrada (kg) | Salida (kg) | Cierre |
|---|---:|---:|---:|
| Tamizado | 10.0000 | 10.0000 | 0.0000% |
| Suspension | 7.7000 | 7.7000 | 0.0000% |
| Filtracion | 7.7000 | 7.7000 | 0.0000% |
| Secado | 4.1580 | 4.1580 | 0.0000% |

### 6.2 Balance global

Entradas:

$$
m_{in}=10.0+4.2=14.2\ \text{kg}
$$

Salidas:

$$
m_{out}=6.5+3.5420+1.5217+2.6363=14.2\ \text{kg}
$$

Error de cierre:

$$
\%\,cierre=\left|\frac{m_{out}-m_{in}}{m_{in}}\right|\times100=0.0000\%
$$

Interpretacion tecnica:

- El cierre exacto valida consistencia matematica del flujo integrado.
- No se detectan perdidas no modeladas en el nivel de precision reportado.

## 7. Analisis critico academico

## 7.1 Fortalezas del desarrollo

1. Trazabilidad numerica completa entre etapas.
2. Coherencia de unidades y conversiones.
3. Criterios metodologicos explicitados en los puntos de mayor riesgo.
4. Cierre global robusto para defensa academica.

## 7.2 Fuentes principales de incertidumbre

1. No linealidad inicial de la curva de filtracion.
2. Dispersion puntual en la serie de secado (tramo 10-20 min).
3. Sensibilidad de la extrapolacion lineal del ultimo tramo para estimar tiempo objetivo.

## 7.3 Tratamiento de incertidumbre en el informe

- Se documento una base unica de calculo para secado alineada con suspension y filtracion.
- Se reportaron dos indicadores de ajuste en filtracion.
- Se separaron claramente datos medidos, supuestos y valores derivados.

## 8. Implicaciones tecnicas para escalado

Aunque el proyecto es academico y por lote, los resultados permiten inferencias de diseno:

1. La etapa de secado domina requerimiento energetico del sistema.
2. La calidad de alimentacion a filtracion depende fuertemente de la consistencia de suspension.
3. La definicion de eficiencia de tamizado debe mantenerse fija en todo escalado para comparar campanas.
4. La validacion de curva de filtracion deberia reforzarse con mas puntos en el rango bajo de volumen.

## 9. Conclusiones

1. El proyecto cumple los requerimientos de calculo para molienda, tamizado, suspension, filtracion y secado.
2. El sistema cierra masa globalmente con error 0.0000%, lo que confirma integridad de reconciliacion.
3. La base experimental trazable permite reportar resultados oficiales coherentes para balance de masa y energia.
4. La documentacion final queda apta para evaluacion academica, defensa tecnica y auditoria de reproducibilidad.

## 10. Recomendaciones

1. Mantener el criterio oficial de base experimental trazable en futuras actualizaciones del documento.
2. Conservar en filtracion el reporte dual de $R^2$ para transparencia metodologica.
3. Repetir experimentalmente puntos iniciales de filtracion para mejorar robustez estadistica de ajuste global.
4. Si se escala el proceso, priorizar optimizacion energetica en secado antes que en etapas mecanicas.

## 11. Referencias internas del proyecto

- PROYECTO_4TO BLOQUE/docs/planteamiento 4to bloque.md
- PROYECTO_4TO BLOQUE/docs/Calculos Proyecto 4to Bloque.md
- PROYECTO_4TO BLOQUE/docs/Auditoria_Integridad_4to_Bloque.md
- PROYECTO_4TO BLOQUE/docs/Calculos_Gemini.md
