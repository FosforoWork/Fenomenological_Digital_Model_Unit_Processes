# Operaciones Unitarias del Proyecto

Este documento resume las operaciones unitarias solicitadas para el proyecto: lixiviacion, destilacion, extraccion y absorcion. La idea es conectar la teoria con criterios de diseno que se usan en ingenieria de procesos.

## 1. Contexto rapido

Una operacion unitaria es una etapa fisica de un proceso industrial donde domina un fenomeno de transporte (momento, calor o masa). Desde el enfoque clasico de Arthur D. Little (1915), los procesos complejos se pueden descomponer en operaciones repetibles y escalables.

## 2. Lixiviacion (Extraccion Solido-Liquido)

### 2.1 Definicion
La lixiviacion separa un soluto de una matriz solida usando un solvente liquido. En el caso del proyecto, se usa agua alcalina para extraer proteina de harina de soya.

### 2.2 Fenomeno dominante
- Transferencia de masa solido-liquido por gradiente de concentracion.
- Disolucion del soluto + difusion interna en poros + transporte externo por agitacion.

### 2.3 Variables criticas
- Relacion solido-liquido (S/L): tipico 1:10 a 1:15 (p/v).
- pH: en soya, zona alcalina 8.5-9.0 mejora solubilidad.
- Temperatura: tipico 50-60 C.
- Tiempo de residencia: 45-60 min.
- Intensidad de mezcla (rpm, potencia de agitador).

### 2.4 Ecuaciones guia
Balance de masa de soluto en extractor:

$$
\dot m_{s,in} = \dot m_{s,out} + \dot m_{s,acum}
$$

En estado estacionario:

$$
\dot m_{s,in} = \dot m_{s,out}
$$

Rendimiento de extraccion:

$$
\eta_{ext} = \frac{m_{soluto,extraido}}{m_{soluto,inicial}}\times 100\%
$$

### 2.5 Equipos y materiales tipicos
- Tanque agitado con deflectores (baffles).
- Agitador tipo PBT o turbina radial.
- Material: acero inoxidable 304/316L en aplicaciones alimentarias.

## 3. Destilacion

### 3.1 Definicion
La destilacion separa componentes de una mezcla liquida por diferencias de volatilidad (o punto de ebullicion), mediante contacto repetido vapor-liquido en equilibrio.

### 3.2 Fenomeno dominante
- Transferencia simultanea de calor y masa.
- Equilibrio de fases liquido-vapor en cada etapa teorica.

### 3.3 Variables criticas
- Volatilidad relativa $\alpha$.
- Relacion de reflujo $R$.
- Numero de etapas teoricas $N_t$.
- Condicion termica de alimentacion (q-line).
- Presion de operacion (afecta equilibrio y temperatura).

### 3.4 Ecuaciones guia
Definicion de volatilidad relativa para sistema binario A/B:

$$
\alpha_{AB}=\frac{(y_A/x_A)}{(y_B/x_B)}
$$

Aproximacion para numero minimo de etapas (Fenske, reflujo total):

$$
N_{min}=\frac{\ln\left[\left(\frac{x_D}{1-x_D}\right)\left(\frac{1-x_B}{x_B}\right)\right]}{\ln(\alpha_{AB})}
$$

### 3.5 Equipos y materiales tipicos
- Columna de platos o empacada.
- Condensador + rehervidor.
- Materiales: acero al carbono/inoxidable segun corrosividad.

## 4. Extraccion Liquido-Liquido

### 4.1 Definicion
La extraccion liquido-liquido transfiere un soluto desde una fase liquida alimentacion hacia otra fase liquida inmiscible (solvente extractante) con mayor afinidad.

### 4.2 Fenomeno dominante
- Transferencia de masa entre dos liquidos en equilibrio de particion.
- Eficiencia influida por mezcla, coalescencia y separacion de fases.

### 4.3 Variables criticas
- Coeficiente de distribucion $K_D$.
- Selectividad del solvente.
- Relacion solvente/alimentacion (S/F).
- Numero de etapas de extraccion.
- Temperatura y tiempo de contacto.

### 4.4 Ecuaciones guia
Coeficiente de distribucion:

$$
K_D=\frac{C_{soluto,extracto}}{C_{soluto,refinado}}
$$

Fraccion remanente en una extraccion simple ideal:

$$
\frac{x_R}{x_F}=\frac{1}{1+K_D\left(\frac{S}{F}\right)}
$$

### 4.5 Equipos y materiales tipicos
- Mezclador-decanter (mixer-settler).
- Columna pulsada o contactor centrifugo.
- Materiales compatibles con el solvente organico usado.

## 5. Absorcion Gas-Liquido

### 5.1 Definicion
La absorcion remueve un componente de una corriente gaseosa al ponerla en contacto con un liquido absorbente.

### 5.2 Fenomeno dominante
- Transferencia de masa gas-liquido con doble pelicula.
- Fuerza impulsora por diferencia entre concentracion real y equilibrio (ley de Henry o relacion de equilibrio y*=mx).

### 5.3 Variables criticas
- Caudales de gas (G) y liquido (L).
- Coeficiente global de transferencia $K_Ga$ o $K_La$.
- Solubilidad del gas y temperatura.
- Tipo de empaque/plato y altura efectiva de contacto.

### 5.4 Ecuaciones guia
Flujo de transferencia de masa (base gas):

$$
N_A=K_Ga\,(y-y^*)
$$

Altura de torre por metodo HTU-NTU:

$$
Z = HTU\times NTU
$$

### 5.5 Equipos y materiales tipicos
- Torre empacada a contracorriente.
- Torre de platos para altos caudales.
- Materiales: FRP, inox o acero revestido segun quimica del sistema.

## 6. Comparacion rapida de las 4 operaciones

| Operacion | Fase de entrada | Fuerza impulsora principal | Equipo comun |
|---|---|---|---|
| Lixiviacion | Solido + liquido | Gradiente de concentracion | Tanque agitado |
| Destilacion | Liquido (mezcla) | Volatilidad + gradiente termico | Columna con rehervidor y condensador |
| Extraccion L-L | Liquido + liquido inmiscible | Reparto de soluto entre fases | Mixer-settler |
| Absorcion | Gas + liquido | Diferencia respecto a equilibrio | Torre empacada |

## 7. Cierre

Para diseno conceptual: primero define balances de materia y energia, luego selecciona condicion operativa (T, P, pH, S/F, L/G), y finalmente realiza dimensionamiento preliminar del equipo. En este proyecto, los calculos detallados se desarrollan en archivos separados por operacion.
