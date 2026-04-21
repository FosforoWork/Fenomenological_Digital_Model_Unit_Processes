# Auditoria de Integridad de Calculos
## Proyecto 4to Bloque - Documento Integrado

Fecha de auditoria: 2026-04-21
Documento auditado: PROYECTO_4TO BLOQUE/docs/Calculos Proyecto 4to Bloque.md
Alcance: verificacion integral de todos los calculos del documento integrado.

---

## 1. Metodologia de verificacion

1. Se tomo como fuente unica el documento integrado del 4to bloque.
2. Se recalculo de forma independiente cada expresion numerica reportada.
3. Se comparo valor reportado vs valor recalculado con error absoluto y relativo.
4. Se audito consistencia entre bloques (continuidad de masa y unidades).
5. Se clasificaron constantes en: dadas, estandar de ingenieria, calculadas e inferidas.

Criterio de integridad numerica:
- Integridad alta: error relativo <= 0.1% (o diferencia explicable por redondeo).
- Integridad media: error relativo > 0.1% y <= 1%.
- Integridad baja: error relativo > 1%.

Resultado general:
- Integridad numerica global: ALTA.
- Desviaciones: solo por redondeo.
- Hallazgos metodologicos: advertencias documentales resueltas en version sincronizada.

---

## 2. Bloque de Molienda

### 2.1 Que hace este bloque y por que
La molienda reduce el tamano de particula para favorecer clasificacion posterior y mejorar transferencia en operaciones subsiguientes.

### 2.2 Verificacion numerica

| Variable | Reportado | Recalculado | Error relativo |
|---|---:|---:|---:|
| Diametro promedio ponderado, d_prom (mm) | 0.3674 | 0.367400 | 0.0000% |
| Diametro geometrico, d_geom (mm) | 0.3007 | 0.300699 | 0.0004% |
| Relacion de reduccion, R_r | 10.8873 | 10.887316 | 0.0001% |
| Energia Bond, E_Bond (kWh/ton) | 14.9474 | 14.947357 | 0.0003% |
| Constante Kick calibrada, K_k (kWh/ton) | 6.2604 | 6.260415 | 0.0002% |
| Constante Rittinger calibrada, K_r (kWh*mm/ton) | 6.0471 | 6.047083 | 0.0003% |

Estado del bloque: INTEGRO (alta concordancia).

### 2.3 Constantes elegidas y por que
- Wi = 13 kWh/ton: dato base transcrito; representa resistencia energetica del material a la conminucion.
- d_i = 4.0 mm: tamano inicial promedio de la alimentacion.
- d_f = d_prom = 0.3674 mm: tamano de salida adoptado para energia especifica.

### 2.4 Valores no proporcionados y como se resolvieron
- d_geom: calculado por media geometrica ponderada de fracciones.
- K_k y K_r: no vienen dados; se obtienen calibrando Kick y Rittinger para igualar Bond en el punto de diseno.

### 2.5 Procedimientos adicionales realizados
- Calibracion de modelos Kick/Rittinger para coincidir con Bond.
- Control de coherencia de unidades dentro de la misma base de longitud.

Comentario tecnico:
- Kick y Rittinger calibrados aqui no son predicciones independientes fuera del punto de diseno; sirven como equivalencia local.

---

## 3. Bloque de Tamizado

### 3.1 Que hace este bloque y por que
Clasifica la mezcla molida por tamano para seleccionar una fraccion objetivo y estabilizar la materia prima de suspension.

### 3.2 Verificacion numerica

| Variable | Reportado | Recalculado | Error relativo |
|---|---:|---:|---:|
| D50 (mm) | 0.4017 | 0.401733 | 0.0081% |
| Eficiencia de tamizado (%) | 35.0 | 35.0000 | 0.0000% |
| Fracciones retenidas y acumuladas | Tabla | Coincide | 0.0000% |

Estado del bloque: INTEGRO.

### 3.3 Constantes elegidas y por que
- Fraccion objetivo 0.25-0.42 mm: criterio de especificacion del proceso.
- Base total 10.0 kg: alimentacion de referencia del lote.

### 3.4 Valores no proporcionados y como se resolvieron
- D50: obtenido por interpolacion logaritmica entre 53% y 18% pasante.

### 3.5 Procedimientos adicionales realizados
- Construccion de fraccion acumulada y porcentaje pasante.
- Transformacion log10(d) para trazado granulometrico.

Comentario tecnico:
- La eficiencia reportada corresponde al criterio definido en el documento (masa objetivo/masa total).
- En terminos clasicos de separacion, esto se interpreta mejor como rendimiento de fraccion objetivo sobre alimentacion total.

---

## 4. Bloque de Preparacion de Suspension

### 4.1 Que hace este bloque y por que
Define la composicion solido-liquido antes de filtracion; condiciona viscosidad aparente, formacion de torta y carga hidraulica.

### 4.2 Verificacion numerica

| Variable | Reportado | Recalculado | Error relativo |
|---|---:|---:|---:|
| m_s (kg) | 1.40 | 1.4000 | 0.0000% |
| m_w (kg) | 4.20 | 4.2000 | 0.0000% |
| Concentracion C (kg/kg) | 0.1818 | 0.181818 | 0.0100% |
| Concentracion C (%) | 18.18 | 18.1818 | 0.0100% |
| Equivalente C (kg/m3) | 181.8 | 181.818 | 0.0100% |

Estado del bloque: INTEGRO.

### 4.3 Constantes elegidas y por que
- Relacion agua/solido = 1.2 kg/kg: especificacion operativa de preparacion.
- Densidad de referencia ~1000 kg/m3: aproximacion para convertir base masica a volumetrica.

### 4.4 Valores no proporcionados y como se resolvieron
- C en kg/m3 no se mide directamente; se aproxima desde fraccion masica usando densidad de referencia.
- El valor $C=454$ kg/m3 del bloque Ruth se mantiene como dato experimental del ajuste, no como conversion directa de la suspension calculada.

### 4.5 Procedimientos adicionales realizados
- Conversion entre bases de concentracion (kg/kg, %, kg/m3).

---

## 5. Bloque de Filtracion

### 5.1 Que hace este bloque y por que
Separa la suspension en torta humeda y filtrado; el modelo de Ruth permite estimar resistencias del medio y del pastel.

### 5.2 Verificacion numerica

| Variable | Reportado | Recalculado | Error relativo |
|---|---:|---:|---:|
| Pendiente ajuste, m (s/m6) | 1,619,338.2757 | 1,619,338.275673 | 0.0000% |
| Intercepto ajuste, b (s/m3) | 77,611.8410 | 77,611.841021 | 0.0000% |
| Resistencia de torta, alpha (m/kg) | 8.9171e8 | 8.917060989e8 | 0.0004% |
| Resistencia del medio, Rm (1/m) | 1.9403e11 | 1.940296026e11 | 0.0002% |
| Masa torta humeda (kg) | 4.1580 | 4.158000 | 0.0000% |
| Filtrado integrado (kg) | 3.5420 | 3.542000 | 0.0000% |

Estado del bloque: INTEGRO EN ARITMETICA.

### 5.3 Constantes elegidas y por que
- mu = 1e-3 Pa*s: viscosidad del agua de referencia.
- A = 0.05 m2: area disponible del filtro.
- Delta P = 50 kPa: presion de operacion definida.
- C = 454 kg/m3: concentracion de solidos de alimentacion.
- Humedad de torta derivada de curva: $X_i=1.97$ kg agua/kg ss (66.33% bh).

### 5.4 Valores no proporcionados y como se resolvieron
- alpha y Rm: derivados por ajuste lineal de t/V vs V (en SI) y sustitucion en ecuacion de Ruth.

### 5.5 Procedimientos adicionales realizados
- Conversion de V de L a m3 para ajuste en SI.
- Regresion lineal por minimos cuadrados.
- Verificacion de calidad del ajuste (R2).

### 5.6 Hallazgo metodologico importante
- R2 del ajuste usando los 8 puntos = 0.2141 (baja linealidad global).
- Para V >= 5 L: R2 = 0.9996 (linealidad muy alta).

Interpretacion:
- Los parametros alpha y Rm estan bien calculados respecto a la recta reportada.
- Sin embargo, la serie completa incluye transitorios/no linealidad al inicio (bajo volumen), lo que reduce robustez de un ajuste unico para todo el rango.

Estado de trazabilidad (2026-04-21):
- El documento integrado ya incluye esta aclaracion metodologica en el bloque de filtracion.

---

## 6. Bloque de Secado

### 6.1 Que hace este bloque y por que
Reduce humedad hasta especificacion final (8% bh), asegurando estabilidad del producto y cumplimiento de calidad.

### 6.2 Verificacion numerica

| Variable | Reportado | Recalculado | Error relativo |
|---|---:|---:|---:|
| X_f (kg agua/kg ss) | 0.0869565 | 0.086957 | 0.0000% |
| Masa final producto (kg) | 1.5217 | 1.521739 | 0.0026% |
| Agua evaporada (kg) | 2.6363 | 2.636261 | 0.0015% |
| Tiempo objetivo 8% bh (min) | 126.8921 | 126.892110 | 0.0000% |
| Energia minima teorica (kWh) | 1.6528 | 1.652789 | 0.0007% |

Estado del bloque: INTEGRO EN ARITMETICA.

### 6.3 Constantes elegidas y por que
- Humedad final 8% bh: especificacion contractual del producto.
- lambda = 2257 kJ/kg: calor latente del agua de referencia para energia minima teorica.
- Tramo 100-120 min: usado para extrapolar tiempo objetivo por cercania al objetivo final de humedad.

### 6.4 Valores no proporcionados y como se resolvieron
- X_f en base seca: conversion desde base humeda.
- m_agua,final: derivado de masa final calculada.
- t_objetivo: extrapolacion lineal del ultimo tramo entre 100 y 120 min.

### 6.5 Procedimientos adicionales realizados
- Uso de una base unificada de calculo desde suspension hasta secado.
- Diferencias finitas para curva de velocidad de secado.

### 6.6 Hallazgos metodologicos
1. En la curva de velocidad aparece un tramo con N negativa (10-20 min), consistente con dispersion experimental puntual.
2. La extrapolacion del tramo final para tiempo objetivo requiere repetir puntos cercanos al objetivo para mayor robustez.

Estado de trazabilidad (2026-04-21):
- El documento integrado ya declara base experimental trazable como oficial para cierre global.

---

## 7. Balance de masa

### 7.1 Verificacion por etapas
- Tamizado: cierra exactamente.
- Suspension: cierra exactamente.
- Filtracion: cierra exactamente.
- Secado: cierra exactamente.

### 7.2 Verificacion global

| Variable | Valor |
|---|---:|
| Entrada total (kg) | 14.200000 |
| Salida total (kg) | 14.200000 |
| Error de cierre (%) | 0.000000 |

Estado del bloque: INTEGRO.

---

## 8. Constantes y supuestos: explicacion de eleccion

### 8.1 Constantes dadas directamente en el planteamiento/datos base
- Wi = 13 kWh/ton
- Relacion agua/solido = 1.2 kg/kg
- Delta P = 50 kPa
- A = 0.05 m2
- mu = 1e-3 Pa*s
- C = 454 kg/m3
- Condicion final = 8% bh

Uso:
- Son entradas de diseno y operacion para ejecutar los modelos de cada etapa.

### 8.2 Constantes estandar de ingenieria
- lambda agua = 2257 kJ/kg para energia minima teorica.
- rho aproximada 1000 kg/m3 para conversion simple de concentracion.

Uso:
- Permiten convertir resultados entre bases y obtener energia minima ideal.

### 8.3 Supuestos no medidos explicitamente
- No se usa supuesto fijo de 40% bh; la humedad de torta se calcula desde $X_i=1.97$ kg agua/kg ss.

Impacto:
- Afecta directamente m_torta, m_filtrado, m_evap y energia minima teorica de secado.

Sensibilidad cualitativa:
- Alta (si cambia este supuesto, cambia toda la parte integrada de filtracion-secado).

---

## 9. Valores no proporcionados y procedimientos adicionales

### 9.1 Valores derivados (no dados de forma directa)
- d_geom: calculado por media geometrica ponderada.
- D50: interpolacion logaritmica en curva granulometrica.
- alpha y Rm: obtenidos por ajuste lineal de Ruth.
- X_f en base seca: conversion de 8% bh.
- t_objetivo: extrapolacion lineal del ultimo tramo.

### 9.2 Procedimientos adicionales realizados para cerrar el calculo
1. Conversion de unidades a SI para ajuste de filtracion.
2. Calibracion Kick/Rittinger respecto a Bond en punto de diseno.
3. Diferencias finitas para velocidad de secado.
4. Verificacion estadistica de linealidad de Ruth (R2 global y por subrango).
5. Reconciliacion de balances por etapa y balance global.

---

## 10. Conclusiones de integridad

1. Todos los resultados del documento integrado fueron verificados y coinciden con recalculo independiente.
2. Las diferencias encontradas son de redondeo y no comprometen la integridad del procedimiento.
3. El cierre de masa por etapa y global es exacto en la base experimental trazable (14.2 kg entrada y 14.2 kg salida).
4. Existen tres puntos que deben aclararse para mejorar trazabilidad metodologica:
   - Ajuste de Ruth con baja linealidad global (R2 = 0.2141) pero alta linealidad en regimen V >= 5 L.
   - Eficiencia de tamizado definida como fraccion objetivo sobre alimentacion total (aclarar que es rendimiento segun criterio del planteamiento).
   - Diferencia entre $C_s$ de suspension calculada y $C$ usado en Ruth por origen experimental del ajuste.

Estado de cierre documental (2026-04-21):
- Los tres puntos anteriores quedaron explicitamente documentados en el archivo integrado.

Veredicto final:
- Integridad matematica: APROBADA.
- Integridad metodologica: APROBADA.

---

## 11. Recomendaciones de mantenimiento documental

1. Mantener la nota de base oficial unica en futuras revisiones para evitar reintroducir doble criterio en el cierre global.
2. Mantener en filtracion el par de indicadores $R^2$ (global y subrango) cuando se actualice la serie experimental.
3. Conservar la trazabilidad por bloque usando etiquetas de dato medido, supuesto, calculado e interpolado/extrapolado.

Con esto, el documento queda correcto numericamente, didactico y reproducible para auditoria externa.
