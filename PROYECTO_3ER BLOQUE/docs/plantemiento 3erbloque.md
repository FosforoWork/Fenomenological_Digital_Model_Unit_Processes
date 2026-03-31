# Planta industrial para la produccion de extractos naturales

## 1. Objetivo general

Disenar una planta industrial para obtener extracto concentrado de compuestos fenolicos a partir de materia prima vegetal seca (flor de Jamaica), incorporando recuperacion real de solventes y verificacion completa de balances de materia y energia.

La planta operara en regimen continuo durante 8 horas diarias y procesara la capacidad asignada en la variante correspondiente.

## 2. Operaciones unitarias obligatorias

- Extraccion solido-liquido (ESL) en contracorriente.
- Extraccion liquido-liquido (ELL) en contracorriente.
- Destilacion para recuperacion de solventes.

## 3. Condiciones de diseno y restricciones

El diseno debe cumplir de manera simultanea:

- Recuperacion global minima del soluto.
- Pureza minima del producto final.
- Recuperacion minima de solventes.
- Restricciones energeticas del proceso.

Adicionalmente:

- El sistema debe operar con recirculacion real de solventes.
- Los balances de materia deben cerrar en cada etapa y en el global del proceso.
- No se permiten supuestos no justificados ni ajustes arbitrarios entre operaciones.

## 4. Alcance obligatorio del proyecto

1. Formular el diagrama de bloques y el diagrama de flujo completo.
2. Realizar el balance global de masa del sistema integrado.
3. Disenar las etapas de ESL mediante modelo analitico.
4. Disenar la etapa de ELL mediante metodo grafico triangular.
5. Disenar la columna de destilacion mediante:
   - modelo analitico,
   - metodo de McCabe-Thiele.
6. Determinar numero de platos teoricos y reales.
7. Calcular cargas termicas en rehervidor y condensador.
8. Estimar el diametro preliminar de la columna por criterio hidraulico.
9. Integrar recirculaciones de solventes en el esquema global.
10. Evaluar los indicadores globales del proceso.
11. Para la solucion flor de Jamaica-acetato de etilo, obtener el producto final por destilacion al vacio, considerando:
   - Balance de masa.
   - Numero minimo de etapas (Fenske).
   - Numero real de etapas (McCabe-Thiele aproximado).
   - Flujos internos de vapor y liquido.
   - Diametro de columna.
   - Altura de columna.

## 5. Datos de operacion para destilacion al vacio

- Presion de trabajo: 300 mmHg.
- Volatilidad relativa: $\alpha = 2.5$.
- Relacion de reflujo: $R = 2$.
- Alimentacion: liquido saturado ($q=1$).
- Temperatura de ebullicion del acetato de etilo: 77 C.
- Recuperacion objetivo de acetato de etilo: 99.3%.

El diseno final debe ser tecnica y energeticamente coherente.

## 6. Indicadores obligatorios a reportar

- Recuperacion global del soluto.
- Pureza final del producto.
- Consumo especifico de vapor (kg vapor/kg producto).
- Consumo especifico de solvente fresco (kg/kg producto).
- Numero total de etapas reales de los sistemas.

## 7. Tabla de equilibrio etanol-agua (formato Markdown)

Usar esta tabla como referencia obligatoria para curvas de equilibrio y escalonamiento de McCabe-Thiele.

| x (liquido) | y (vapor) |
|---:|---:|
| 0.000 | 0.000 |
| 0.050 | 0.210 |
| 0.100 | 0.340 |
| 0.200 | 0.510 |
| 0.300 | 0.630 |
| 0.400 | 0.720 |
| 0.500 | 0.790 |
| 0.600 | 0.850 |
| 0.700 | 0.890 |
| 0.800 | 0.920 |
| 0.900 | 0.950 |
| 0.956 | 0.956 |

## 8. Formula de aproximacion para la tabla (interpolacion lineal por tramos)

Para cualquier $x$ dentro del intervalo de la tabla, se recomienda usar:

$$
y(x) \approx y_i + \frac{y_{i+1}-y_i}{x_{i+1}-x_i}(x-x_i), \quad x \in [x_i, x_{i+1}]
$$

donde $(x_i, y_i)$ y $(x_{i+1}, y_{i+1})$ son dos puntos consecutivos de la tabla.

Pendientes por tramo ($m_i$):

| Tramo de x | $m_i$ |
|---|---:|
| 0.000 - 0.050 | 4.200 |
| 0.050 - 0.100 | 2.600 |
| 0.100 - 0.200 | 1.700 |
| 0.200 - 0.300 | 1.200 |
| 0.300 - 0.400 | 0.900 |
| 0.400 - 0.500 | 0.700 |
| 0.500 - 0.600 | 0.600 |
| 0.600 - 0.700 | 0.400 |
| 0.700 - 0.800 | 0.300 |
| 0.800 - 0.900 | 0.300 |
| 0.900 - 0.956 | 0.107 |

Ejemplo rapido en el tramo $0.40 \le x \le 0.50$:

$$
y(x) \approx 0.72 + 0.70(x-0.40)
$$

## 9. Referencia grafica

![Curva de equilibrio](image.png)
