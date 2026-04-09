# Planta industrial para produccion de extractos naturales - Planteamiento oficial 3er Bloque

## 1. Objetivo general

Disenar una planta industrial para obtener extracto concentrado de compuestos naturales a partir de flor de Jamaica, con recuperacion real de solventes y verificacion completa de balances de materia y energia.

La planta opera en regimen continuo durante 8 h/d y procesa la capacidad asignada de 1500 kg/d de materia prima.

## 2. Operaciones unitarias obligatorias

- Extraccion solido-liquido (ESL) en contracorriente.
- Extraccion liquido-liquido (ELL) por etapa de contacto y separacion de fases.
- Destilacion al vacio para recuperacion de solvente.
- Recirculacion de solventes con reposicion y cierre global de masa.

## 3. Restricciones obligatorias de diseno

El diseno debe cumplir en simultaneo:

- Pureza minima en destilado: xD >= 0.90 (90.0% mol).
- Recuperacion global minima del proceso total: eta_global >= 25.0%.
- Recuperacion minima de acetato en destilacion: eta >= 99.3%.
- Restriccion energetica de vapor: CE_v < 2.2 kg vapor/kg producto.
- Cierre de masa en cada etapa y en el balance global.
- Trazabilidad explicita de la corriente ELL -> Destilacion.
- Sin supuestos desconectados entre operaciones.

Definiciones oficiales de verificacion:

- Pureza de destilado: Pureza_D = xD x 100.
- Recuperacion global del proceso total: eta_global = (D x xD)/(F x xF) x 100, con F como alimentacion a destilacion desde ELL.

Regla de base para ESL:

- Cuando se use $S/F=3.2$, la base es la alimentacion total horaria ($F_s=187.5$ kg/h).

## 4. Alcance minimo del proyecto

1. Formular diagrama de bloques y diagrama de flujo integrado.
2. Resolver balances por etapa y balance global del sistema.
3. Calcular ESL con base horaria oficial.
4. Calcular ELL con punto de mezcla y reparto de fases.
5. Calcular destilacion por:
   - balance de masa,
   - Fenske,
   - McCabe-Thiele,
   - conversion a etapas reales.
6. Determinar flujos internos L/V, cargas termicas y consumo de vapor.
7. Estimar diametro y altura preliminar de columna.
8. Integrar recirculacion de solventes y reposicion.
9. Reportar indicadores globales de desempeno.

## 5. Datos oficiales de operacion del caso recalculado

### 5.1 ESL y ELL

- Capacidad: 1500 kg/d (8 h/d).
- Alimentacion horaria: 187.50 kg/h.
- Soluto inicial: 10% p/p.
- Humedad inicial: 12% p/p.
- ESL: $S/F=3.2$, retencion en inerte $=1.1$ kg/kg, eficiencia real 72%.
- ELL: solvente fresco $S=264.21$ kg/h, eficiencia real de etapa 80%.

### 5.2 Destilacion al vacio

- Alimentacion desde ELL: $F=294.50$ kg/h.
- Fraccion de acetato en alimentacion: $x_F=0.42$.
- Fraccion de acetato en destilado: $x_D=0.90$.
- Fraccion de acetato en fondos objetivo: $x_B\approx0.0055$.
- Presion de operacion: 300 mmHg.
- Volatilidad relativa de diseno: $\alpha=2.5$.
- Relacion de reflujo: $R=2$.
- Alimentacion liquido saturado: $q=1$.
- Recuperacion minima exigida: $\eta_A\ge99.3\%$.

## 6. Indicadores obligatorios a reportar

- Recuperacion global de proceso total (umbral: >= 25.0%).
- Pureza de destilado (umbral: >= 90.0% mol).
- Recuperacion de acetato en destilacion (umbral: >= 99.3%).
- Consumo especifico de vapor (umbral: < 2.2 kg/kg).
- Consumo global de solvente (reporte obligatorio).
- Numero total de etapas reales del sistema de separacion (reporte obligatorio).
- Cierre global de masa (umbral: 100% +/- 0.1%).

## 7. Tabla de equilibrio oficial para McCabe-Thiele

Tabla oficial del caso de diseno (base del recalculo 3er bloque):

| x (liquido) | y (vapor) |
|---:|---:|
| 0.0030 | 0.0080 |
| 0.0070 | 0.0180 |
| 0.0140 | 0.0350 |
| 0.0270 | 0.0640 |
| 0.0480 | 0.1120 |
| 0.0820 | 0.1830 |
| 0.1340 | 0.2780 |
| 0.2020 | 0.3880 |
| 0.2820 | 0.4950 |
| 0.3590 | 0.5830 |
| 0.4240 | 0.6480 |
| 0.5220 | 0.7320 |
| 0.6480 | 0.8220 |
| 0.7830 | 0.9000 |
| 1.0000 | 1.0000 |

## 8. Ecuaciones guia obligatorias

Fenske:

$$
N_{min}=\frac{\ln\left[\left(\frac{x_D}{1-x_D}\right)\left(\frac{1-x_B}{x_B}\right)\right]}{\ln(\alpha)}
$$

Linea de enriquecimiento:

$$
y = \frac{R}{R+1}x + \frac{x_D}{R+1}
$$

Linea de agotamiento (con q=1 y punto de cruce en $x_F$):

$$
y = m_s x + b_s
$$

Consumo especifico de vapor:

$$
CE_v = \frac{\dot m_{vapor}}{\dot m_{destilado}}
$$

Recuperacion global minima del proceso total:

$$
\eta_{global} = \frac{D x x_D}{F x x_F} x 100
$$

Pureza minima de destilado:

$$
Pureza_D = x_D x 100
$$

## 9. Criterio de aceptacion final

El caso se considera aceptado si simultaneamente:

1. Se cumple Pureza_D >= 90.0% mol en destilado.
2. Se cumple eta_global >= 25.0% en proceso total.
3. Se cumple eta_A >= 99.3% en destilacion.
4. Se cumple CE_v < 2.2 kg/kg.
5. Hay cierre de masa por etapa y cierre global del 100% dentro de tolerancia de redondeo.
6. El informe corto y el documento maestro reportan exactamente los mismos KPIs.
