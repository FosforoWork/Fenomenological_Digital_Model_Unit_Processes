# Formulario de Cálculo
## Proyecto: Producción de Proteína Aislada de Soya

---

## 1. BALANCES DE MASA GENERALES

### 1.1 Balance de Masa Global (Ley de Conservación)

$$\dot{m}_{entrada} = \dot{m}_{salida} + \dot{m}_{acumulación}$$

> En operación continua (estado estacionario): $\dot{m}_{acumulación} = 0$

### 1.2 Eficiencia / Rendimiento de Etapa

$$\eta = \frac{\dot{m}_{salida}}{\dot{m}_{entrada}} \times 100 \quad [\%]$$

### 1.3 Conversión de Caudal Másico a Volumétrico

$$\dot{V} = \frac{\dot{m}}{\rho} \quad \left[\frac{\text{m}^3}{\text{h}}\right]$$

### 1.4 Concentración de Sólidos en Corriente

$$C_{sólidos} = \frac{\dot{m}_{sólidos}}{\dot{m}_{total}} \times 100 \quad [\% \text{ p/p}]$$

### 1.5 Relación Sólido-Líquido (S/L)

$$R_{S/L} = \frac{m_{sólido}}{V_{líquido}} \quad \left[\frac{\text{kg}}{\text{L}} \text{ ó } \frac{\text{kg}}{\text{m}^3}\right]$$

> Para este proceso: $R_{S/L} = 1:12 \Rightarrow 1 \text{ kg soya} / 12 \text{ L agua}$

---

## 2. ETAPA 0 — PREPARACIÓN DE MATERIAS PRIMAS

### 2.1 Masa de Agua de Extracción

$$\dot{m}_{agua} = \dot{m}_{soya} \times R_{S/L} \quad [\text{kg/h}]$$

### 2.2 Concentración de Solución NaOH (% p/v)

$$C_{NaOH} = \frac{m_{NaOH}}{V_{solución}} \times 100 \quad [\% \text{ p/v}]$$

### 2.3 Preparación de Soluciones (Dilución)

$$C_1 \cdot V_1 = C_2 \cdot V_2$$

> Donde $C_1, V_1$ = concentración y volumen inicial; $C_2, V_2$ = concentración y volumen final.

### 2.4 Distribución Granulométrica (Tamaño de Malla)

$$d_{malla} = \frac{25.4 \text{ mm}}{N_{mesh}} \quad [\text{mm}]$$

> p. ej. 200 mesh $\Rightarrow d = 0.074 \text{ mm} = 74\ \mu\text{m}$

---

## 3. ETAPA 1 — EXTRACCIÓN ALCALINA (TANQUE AGITADO)

### 3.1 Volumen Mínimo del Tanque

$$V_{tanque} = \dot{V}_{entrada} \times \tau \times f_s \quad [\text{m}^3]$$

- $\dot{V}_{entrada}$: Caudal volumétrico de entrada $[\text{m}^3/\text{h}]$
- $\tau$: Tiempo de residencia (45–60 min = 0.75–1.0 h)
- $f_s$: Factor de seguridad (1.2)

### 3.2 Relación Altura / Diámetro del Tanque

$$\frac{H}{D} = 0.8 \text{ a } 0.9$$

$$V_{tanque} = \frac{\pi D^2}{4} \cdot H$$

### 3.3 Número de Reynolds para Agitador ($Re_{ag}$)

$$Re_{ag} = \frac{\rho \cdot N \cdot D_{ag}^2}{\mu}$$

- $\rho$: Densidad del fluido $[\text{kg/m}^3]$
- $N$: Velocidad de rotación $[\text{rev/s}]$
- $D_{ag}$: Diámetro del agitador $[\text{m}]$
- $\mu$: Viscosidad dinámica $[\text{Pa·s}]$

| Régimen | Valor $Re_{ag}$ |
|---------|----------------|
| Laminar | $< 10$ |
| Transicional | $10 - 10^4$ |
| Turbulento | $> 10^4$ |

### 3.4 Potencia del Agitador

$$P = N_p \cdot \rho \cdot N^3 \cdot D_{ag}^5 \quad [\text{W}]$$

- $N_p$: Número de potencia (adimensional; $\approx 1.3 \text{ a } 2.0$ para PBT 6 palas)
- $N$: Velocidad de rotación $[\text{rev/s}]$
- $D_{ag}$: Diámetro del agitador $[\text{m}]$

### 3.5 Potencia con Corrección por Deflectores (Baffles)

$$P_{real} = P \cdot f_{baffles} \quad (f_{baffles} \approx 1.1\text{–}1.3)$$

### 3.6 Calor Generado por Agitación

$$Q_{agit} = P \cdot \eta_{motor} \quad [\text{W}]$$

### 3.7 Eficiencia de Extracción Proteica

$$\eta_{ext} = \frac{m_{proteína,\ extracto}}{m_{proteína,\ entrada}} \times 100 \quad [\%]$$

---

## 4. ETAPA 1.2 — SEPARACIÓN SÓLIDO-LÍQUIDO (CENTRÍFUGA DECANTADORA)

### 4.1 Factor Centrífugo (G)

$$G = \frac{\omega^2 \cdot r}{g} = \frac{(2\pi N/60)^2 \cdot r}{9.81}$$

- $\omega$: Velocidad angular $[\text{rad/s}]$
- $r$: Radio del tambor $[\text{m}]$
- $g$: Aceleración gravitacional $= 9.81\ \text{m/s}^2$
- $N$: RPM del tambor

### 4.2 Velocidad de Sedimentación — Ley de Stokes

$$v_s = \frac{d_p^2 \cdot (\rho_p - \rho_f) \cdot g}{18 \cdot \mu} \quad [\text{m/s}]$$

- $d_p$: Diámetro de partícula $[\text{m}]$
- $\rho_p$: Densidad de partícula $[\text{kg/m}^3]$
- $\rho_f$: Densidad del fluido $[\text{kg/m}^3]$
- $\mu$: Viscosidad del fluido $[\text{Pa·s}]$

> Válida para $Re_p < 1$ (flujo laminar alrededor de partícula)

### 4.3 Velocidad de Sedimentación en Centrífuga

$$v_{c} = v_s \cdot G = v_s \cdot \frac{\omega^2 \cdot r}{g} \quad [\text{m/s}]$$

### 4.4 Número de Reynolds de Partícula

$$Re_p = \frac{\rho_f \cdot v_s \cdot d_p}{\mu}$$

### 4.5 Balance de Sólidos en Centrífuga

$$\dot{m}_{sólidos,\ entrada} = \dot{m}_{sólidos,\ descarga} + \dot{m}_{sólidos,\ efluente}$$

$$\text{Recuperación} = \frac{\dot{m}_{sólidos,\ descarga}}{\dot{m}_{sólidos,\ entrada}} \times 100 \quad [\%]$$

---

## 5. ETAPA 2 — NEUTRALIZACIÓN Y PASTEURIZACIÓN

### 5.1 Calor Sensible para Calentamiento/Enfriamiento

$$Q = \dot{m} \cdot C_p \cdot \Delta T \quad [\text{W ó kJ/h}]$$

- $\dot{m}$: Caudal másico $[\text{kg/s ó kg/h}]$
- $C_p$: Calor específico $\approx 3800\ \text{J/kg·K}$ para extracto proteico
- $\Delta T$: Diferencia de temperatura $[\text{K ó °C}]$

### 5.2 Diferencia de Temperatura Logarítmica Media (LMTD)

$$\Delta T_{lm} = \frac{\Delta T_1 - \Delta T_2}{\ln\left(\frac{\Delta T_1}{\Delta T_2}\right)} \quad [\text{K}]$$

- $\Delta T_1 = T_{h,entrada} - T_{c,salida}$
- $\Delta T_2 = T_{h,salida} - T_{c,entrada}$

### 5.3 Ecuación Fundamental del Intercambiador de Calor

$$Q = U \cdot A \cdot \Delta T_{lm} \quad [\text{W}]$$

- $U$: Coeficiente global de transferencia $[\text{W/m}^2\text{K}]$ — típico: 400–600 para placas con fluido viscoso
- $A$: Área de transferencia $[\text{m}^2]$

### 5.4 Área de Intercambiador Requerida

$$A = \frac{Q}{U \cdot \Delta T_{lm}} \quad [\text{m}^2]$$

### 5.5 Número de Unidades de Transferencia (NTU)

$$NTU = \frac{U \cdot A}{\dot{m} \cdot C_p}$$

### 5.6 Eficiencia del Intercambiador ($\varepsilon$)

$$\varepsilon = \frac{Q_{real}}{Q_{max}} = \frac{\dot{m}_c \cdot C_{p,c} \cdot (T_{c,sal} - T_{c,ent})}{\dot{m}_{min} \cdot C_{p,min} \cdot (T_{h,ent} - T_{c,ent})}$$

### 5.7 Número de Placas del Intercambiador

$$N_{placas} = \frac{A}{A_{placa}} + 1$$

### 5.8 Número de Reynolds en Placas

$$Re_{placas} = \frac{\rho \cdot v \cdot D_h}{\mu} = \frac{4 \cdot \dot{m}}{b_{canal} \cdot \mu}$$

- $D_h$: Diámetro hidráulico $= 2b$ ($b$ = separación entre placas)

### 5.9 Número de Prandtl

$$Pr = \frac{C_p \cdot \mu}{\lambda}$$

- $\lambda$: Conductividad térmica del fluido $[\text{W/m·K}]$

### 5.10 Coeficiente de Convección en Placas (Dittus-Boelter)

$$Nu = 0.023 \cdot Re^{0.8} \cdot Pr^{0.4} \quad (\text{calentamiento})$$

$$h = \frac{Nu \cdot \lambda}{D_h} \quad [\text{W/m}^2\text{K}]$$

### 5.11 Coeficiente Global de Transferencia (Resistencias en Serie)

$$\frac{1}{U} = \frac{1}{h_c} + \frac{e}{\lambda_{placa}} + \frac{1}{h_h} + R_{incrustación}$$

- $e$: Espesor de placa (0.6–0.8 mm)
- $h_c$, $h_h$: Coeficientes convectivos lado frío y caliente

### 5.12 Criterio de Pasteurización — Valor D

$$\log\left(\frac{N_t}{N_0}\right) = -\frac{t}{D}$$

- $N_t$: Microorganismos a tiempo $t$
- $N_0$: Microorganismos iniciales
- $D$: Tiempo de reducción decimal $[\text{s}]$

> Para 5–7 ciclos logarítmicos: $t \geq 5D$ a la temperatura de pasteurización.

---

## 6. ETAPA 3 — CONCENTRACIÓN (EVAPORADOR AL VACÍO)

### 6.1 Balance de Masa en Evaporador

$$\dot{m}_{entrada} = \dot{m}_{vapor} + \dot{m}_{concentrado}$$

$$\dot{m}_{entrada} \cdot x_{entrada} = \dot{m}_{concentrado} \cdot x_{salida}$$

- $x$: Fracción másica de sólidos

### 6.2 Caudal de Vapor Generado

$$\dot{m}_{vapor} = \dot{m}_{entrada} \cdot \left(1 - \frac{x_{entrada}}{x_{salida}}\right) \quad [\text{kg/h}]$$

### 6.3 Temperatura de Ebullición bajo Vacío (Ecuación de Antoine)

$$\log_{10}(P) = A - \frac{B}{T + C}$$

| Constante | Valor (T en °C, P en mmHg) |
|-----------|---------------------------|
| A | 8.10765 |
| B | 1750.286 |
| C | 235.000 |

> A 0.3–0.5 bar abs $\Rightarrow T_{ebull} \approx 69\text{–}81\ °C$

### 6.4 Calor Latente de Vaporización del Agua

$$\lambda_{vap} = 2501 - 2.37 \cdot T \quad [\text{kJ/kg}]$$

> Aproximación: a 50–60 °C, $\lambda_{vap} \approx 2350\text{–}2370\ \text{kJ/kg}$

### 6.5 Calor Requerido para Evaporación

$$Q_{evap} = \dot{m}_{vapor} \cdot \lambda_{vap} \quad [\text{kJ/h ó kW}]$$

### 6.6 Área de Evaporación Requerida

$$A_{evap} = \frac{Q_{evap}}{U \cdot \Delta T} \quad [\text{m}^2]$$

- $U$: 150–300 W/m²K (película descendente)
- $\Delta T = T_{vapor\ calefacción} - T_{ebullición\ producto}$

### 6.7 Economía de Vapor

$$E = \frac{\dot{m}_{vapor\ evaporado}}{\dot{m}_{vapor\ calefacción}} \quad [\text{kg agua evaporada / kg vapor consumido}]$$

> Típico efecto simple: $E \approx 0.8\text{–}0.9$

### 6.8 Consumo de Vapor de Calefacción

$$\dot{m}_{vapor,\ cal} = \frac{Q_{evap}}{\lambda_{vapor\ saturado}} \quad [\text{kg/h}]$$

### 6.9 Elevación del Punto de Ebullición (BPR)

$$\Delta T_{BPR} = T_{ebullición\ solución} - T_{ebullición\ solvente\ puro}$$

> La fuerza impulsora efectiva se reduce: $\Delta T_{ef} = \Delta T - \Delta T_{BPR}$

---

## 7. ETAPA 4 — PRECIPITACIÓN ISOELÉCTRICA

### 7.1 Punto Isoeléctrico (pI)

En el pI, la carga neta de la proteína es cero:

$$pI = \frac{pK_{a1} + pK_{a2}}{2}$$

> Para proteína de soya: $pI \approx 4.5$

### 7.2 Carga Neta de Proteína vs. pH

$$Z_{neta} \propto (pH - pI)$$

| Condición | Comportamiento |
|-----------|----------------|
| $pH < pI$ | Carga positiva → soluble |
| $pH = pI$ | Carga neta = 0 → **precipita** |
| $pH > pI$ | Carga negativa → soluble |

### 7.3 Fuerza Iónica de la Solución

$$I = \frac{1}{2} \sum_i c_i \cdot z_i^2 \quad [\text{mol/L}]$$

- $c_i$: Concentración del ion $i$ $[\text{mol/L}]$
- $z_i$: Carga del ion $i$

### 7.4 Longitud de Debye-Hückel

$$\kappa^{-1} = \sqrt{\frac{\varepsilon_0 \varepsilon_r k_B T}{2 N_A e^2 I}} \quad [\text{nm}]$$

- A 25 °C en agua: $\kappa^{-1} \approx \dfrac{0.304}{\sqrt{I}}$ nm

### 7.5 Potencial Zeta ($\zeta$)

$$\zeta = \frac{\sigma}{\varepsilon \cdot \kappa} \quad [\text{mV}]$$

- $\sigma$: Densidad superficial de carga
- $\varepsilon$: Permitividad del medio

> A pH 4.5: $\zeta \approx -2$ a $+2$ mV → sin repulsión electrostática → precipitación espontánea

### 7.6 Velocidad de Sedimentación del Flóculo (Stokes)

$$v_s = \frac{d_f^2 \cdot (\rho_f - \rho_{liq}) \cdot g}{18 \cdot \mu} \quad [\text{m/s}]$$

- $d_f$: Diámetro de flóculo (200–500 µm $= 2\text{–}5 \times 10^{-4}$ m)

### 7.7 Moles de HCl para Ajuste de pH

$$n_{HCl} = V_{solución} \cdot \Delta [H^+] \approx V \cdot (10^{-pH_{final}} - 10^{-pH_{inicial}}) \quad [\text{mol}]$$

$$m_{HCl} = \frac{n_{HCl} \cdot M_{HCl}}{\text{Pureza}_{HCl}} \quad [\text{kg}]$$

---

## 8. ETAPA 4.2 — CENTRIFUGACIÓN DECANTADORA (POST-PRECIPITACIÓN)

> Ver Sección 4 para Factor G, Ley de Stokes y balance de sólidos.

### 8.1 Humedad Residual en Pasta

$$H_r = \frac{m_{agua,\ pasta}}{m_{pasta,\ total}} \times 100 \quad [\%]$$

### 8.2 Concentración de Proteína en Pasta

$$C_{prot,\ pasta} = \frac{m_{proteína}}{m_{pasta}} \times 100 \quad [\% \text{ p/p}]$$

### 8.3 Diferencial de Velocidad Tornillo-Tambor

$$\Delta N = N_{tambor} - N_{tornillo} \quad [\text{rpm}]$$

> Rango típico: $\Delta N = 50\text{–}100$ rpm

---

## 9. ETAPA 5 — SECADO POR ATOMIZACIÓN (SPRAY DRYER)

### 9.1 Balance de Masa en Secador

$$\dot{m}_{pasta} = \dot{m}_{polvo} + \dot{m}_{agua\ evaporada}$$

$$\dot{m}_{pasta} \cdot (1 - H_{entrada}) = \dot{m}_{polvo} \cdot (1 - H_{salida})$$

- $H$: Humedad en fracción másica (p. ej. $H = 0.50$ para 50%)

### 9.2 Caudal de Agua Evaporada en Secador

$$\dot{m}_{H_2O} = \dot{m}_{pasta} \cdot \left(1 - \frac{1 - H_{entrada}}{1 - H_{salida}}\right) \quad [\text{kg/h}]$$

### 9.3 Caudal de Aire Requerido

$$\dot{m}_{aire} = \frac{Q_{evaporación}}{C_{p,aire} \cdot (T_{inlet} - T_{outlet})} \quad [\text{kg/h}]$$

Con $C_{p,aire} = 1.005\ \text{kJ/kg·K}$

### 9.4 Balance de Energía en Spray Dryer

$$Q_{total} = \dot{m}_{aire} \cdot C_{p,aire} \cdot (T_{inlet} - T_{ambiente})$$

$$Q_{evaporación} = \dot{m}_{H_2O} \cdot \lambda_{vap} \quad [\text{kJ/h}]$$

### 9.5 Temperatura de Salida del Aire (Verificación)

$$T_{outlet} = T_{inlet} - \frac{Q_{evaporación}}{\dot{m}_{aire} \cdot C_{p,aire}} \quad [°\text{C}]$$

### 9.6 Velocidad Periférica del Atomizador (Disco Rotativo)

$$v_{disco} = \pi \cdot D_{disco} \cdot N_{disco} \quad [\text{m/s}]$$

- $D_{disco}$: Diámetro del disco $[\text{m}]$ (80–120 mm)
- $N_{disco}$: Velocidad $[\text{rev/s}]$

### 9.7 Tamaño de Gota (Correlación Atomizador de Disco)

$$d_{gota} = K \cdot \left(\frac{\dot{m}_{pasta}}{\rho_L \cdot N \cdot D_{disco}^2}\right)^{0.6} \cdot \left(\frac{\sigma}{\rho_L}\right)^{0.2} \quad [\mu\text{m}]$$

- $\sigma$: Tensión superficial del líquido $[\text{N/m}]$
- $K$: Constante empírica $\approx 0.4\text{–}0.6$

### 9.8 Eficiencia Térmica del Secador

$$\eta_{térmica} = \frac{T_{inlet} - T_{outlet}}{T_{inlet} - T_{ambiente}} \times 100 \quad [\%]$$

---

## 10. ETAPA 5.2 — MOLIENDA Y TAMIZADO

### 10.1 Ley de Bond (Energía de Molienda)

$$W = W_i \cdot \left(\frac{1}{\sqrt{d_{salida}}} - \frac{1}{\sqrt{d_{entrada}}}\right) \quad [\text{kWh/ton}]$$

- $W_i$: Índice de trabajo de Bond $\approx 10\text{–}20\ \text{kWh/ton}$ para sólidos blandos
- $d$: Diámetro en $\mu\text{m}$

### 10.2 Ley de Rittinger (Energía proporcional a superficie nueva)

$$E = K_R \cdot \left(\frac{1}{d_{salida}} - \frac{1}{d_{entrada}}\right)$$

### 10.3 Ley de Kick (Energía proporcional a reducción de tamaño)

$$E = K_K \cdot \ln\left(\frac{d_{entrada}}{d_{salida}}\right)$$

### 10.4 Relación de Reducción

$$R_{reducción} = \frac{d_{entrada}}{d_{salida}}$$

### 10.5 Eficiencia de Tamizado

$$\eta_{tamiz} = \frac{\dot{m}_{pasante\ real}}{\dot{m}_{pasante\ teórico}} \times 100 \quad [\%]$$

### 10.6 Conversión Tamaño de Malla a Micrométros

$$d_{malla} = \frac{25400\ \mu\text{m}}{N_{mesh}}$$

| Malla | $d_{malla}$ |
|-------|-------------|
| 100 mesh | 149 µm |
| 200 mesh | 74 µm |

---

## 11. MECÁNICA DE FLUIDOS — TUBERÍAS Y BOMBAS

### 11.1 Número de Reynolds en Tuberías

$$Re = \frac{\rho \cdot v \cdot D}{\mu} = \frac{4 \cdot \dot{m}}{\pi \cdot D \cdot \mu}$$

| Régimen | Valor $Re$ |
|---------|-----------|
| Laminar | $< 2100$ |
| Transicional | $2100\text{–}4000$ |
| Turbulento | $> 4000$ |

### 11.2 Velocidad Promedio en Tubería

$$v = \frac{\dot{V}}{A_{trans}} = \frac{4 \cdot \dot{V}}{\pi \cdot D^2} \quad [\text{m/s}]$$

### 11.3 Ecuación de Bernoulli Extendida (con pérdidas y bomba)

$$\frac{P_1}{\rho g} + \frac{v_1^2}{2g} + z_1 + H_{bomba} = \frac{P_2}{\rho g} + \frac{v_2^2}{2g} + z_2 + h_L$$

### 11.4 Pérdida de Carga — Darcy-Weisbach

$$h_L = f \cdot \frac{L}{D} \cdot \frac{v^2}{2g} \quad [\text{m}]$$

$$\Delta P = f \cdot \frac{L}{D} \cdot \frac{\rho \cdot v^2}{2} \quad [\text{Pa}]$$

### 11.5 Factor de Fricción — Flujo Laminar

$$f = \frac{64}{Re}$$

### 11.6 Factor de Fricción — Flujo Turbulento (Colebrook-White)

$$\frac{1}{\sqrt{f}} = -2 \log\left(\frac{\varepsilon/D}{3.7} + \frac{2.51}{Re \sqrt{f}}\right)$$

- $\varepsilon$: Rugosidad de tubería; para acero inoxidable: $\varepsilon \approx 0.046\ \mu\text{m}$

### 11.7 Potencia de la Bomba

$$P_{bomba} = \frac{\dot{V} \cdot \Delta P}{\eta_{bomba}} = \frac{\dot{m} \cdot g \cdot H_{bomba}}{\eta_{bomba}} \quad [\text{W}]$$

- $\eta_{bomba}$: Eficiencia de la bomba (0.65–0.80 típico)

### 11.8 Caudal de Diseño de la Bomba (con factor de servicio)

$$\dot{V}_{diseño} = \dot{V}_{proceso} \times f_{servicio} \quad (f_{servicio} = 1.1\text{–}1.25)$$

---

## 12. TRANSFERENCIA DE CALOR EN TUBERÍAS AISLADAS

### 12.1 Pérdida de Calor en Tubería con Aislamiento Cilíndrico

$$Q_{pérd} = \frac{2 \pi \lambda_{aislante} \cdot L \cdot (T_{fluido} - T_{amb})}{\ln\left(\dfrac{r_2}{r_1}\right)} \quad [\text{W}]$$

- $r_1$: Radio externo del tubo; $r_2$: Radio externo del aislamiento $[\text{m}]$

### 12.2 Resistencia Total de Pared Cilíndrica Compuesta

$$R_{total} = \frac{1}{h_i A_i} + \frac{\ln(r_2/r_1)}{2\pi \lambda_{pared} L} + \frac{\ln(r_3/r_2)}{2\pi \lambda_{aislante} L} + \frac{1}{h_o A_o}$$

---

## 13. BALANCE HÍDRICO GLOBAL

$$\sum \dot{m}_{entrada,\ agua} = \sum \dot{m}_{salida,\ agua}$$

| Corriente de Salida | Fórmula |
|---------------------|---------|
| Vapor evaporado (Etapa 3) | $\dot{m}_{vapor} = \dot{m}_{ent} \cdot \left(1 - \dfrac{x_{ent}}{x_{sal}}\right)$ |
| Agua en okara | $\dot{m}_{H_2O,\ okara} = \dot{m}_{okara} \cdot H_{okara}$ |
| Agua en suero (Etapa 4.2) | $\dot{m}_{H_2O,\ suero} = \dot{m}_{suero} \cdot (1 - C_{sólidos,\ suero})$ |
| Agua en producto final | $\dot{m}_{H_2O,\ polvo} = \dot{m}_{polvo} \cdot H_{polvo}$ |

---

## 14. BALANCE ENERGÉTICO GLOBAL

$$\dot{E}_{total} = Q_{pasteurización} + Q_{evaporación} + Q_{secado} + P_{agitación} + P_{bombas} + P_{centrífugas}$$

### Consumo Específico de Energía

$$e_{específico} = \frac{\dot{E}_{total}}{\dot{m}_{proteína\ final}} \quad [\text{kWh/kg ó MJ/kg}]$$

### Valores de Referencia para 1 ton/h Grano

| Operación | Consumo Estimado |
|-----------|-----------------|
| Pasteurización (neta c/recuperación) | ~330 kW |
| Evaporación al vacío | ~7 200 kW |
| Secado por atomización | ~1 029 kW |
| **TOTAL** | **~8 560 kW (8.6 MW)** |
| Consumo específico | ~2.4 kWh/kg proteína |

---

## 15. ETAPA 6 — ENVASADO Y ALMACENAMIENTO

### 15.1 Número de Bolsas por Hora

$$N_{bolsas} = \frac{\dot{m}_{polvo}}{m_{bolsa}} \quad [\text{bolsas/h}]$$

### 15.2 Número de Pallets por Hora

$$N_{pallets} = \frac{N_{bolsas}}{N_{bolsas/pallet}} \quad [\text{pallets/h}]$$

### 15.3 Volumen Requerido por Bolsa

$$V_{bolsa} = \frac{m_{bolsa}}{\rho_{aparente}} \quad [\text{L}]$$

- $\rho_{aparente}$: 0.55–0.70 g/cm³ para proteína de soya en polvo

### 15.4 Actividad de Agua ($a_w$)

$$a_w = \frac{P_{vapor,\ producto}}{P_{vapor,\ agua\ pura}} \quad (0 \leq a_w \leq 1)$$

> Seguridad microbiológica requiere: $a_w < 0.65$

### 15.5 Vida Útil (Modelo de Arrhenius)

$$k = k_0 \cdot e^{-E_a / RT}$$

$$t_{vida\ útil} = \frac{1}{k \cdot C_0^{n-1}} \quad (\text{para reacción de orden } n)$$

---

## 16. CONSTANTES Y PROPIEDADES DE REFERENCIA

| Propiedad | Símbolo | Valor | Unidad |
|-----------|---------|-------|--------|
| Gravedad estándar | $g$ | 9.81 | m/s² |
| Constante de gases ideales | $R$ | 8.314 | J/mol·K |
| Calor específico agua líquida | $C_{p,H_2O}$ | 4 180 | J/kg·K |
| Calor específico extracto proteico | $C_{p,ext}$ | ~3 800 | J/kg·K |
| Calor específico aire seco | $C_{p,aire}$ | 1 005 | J/kg·K |
| Calor latente agua a 100 °C | $\lambda_{100}$ | 2 257 | kJ/kg |
| Calor latente agua a 55 °C | $\lambda_{55}$ | ~2 360 | kJ/kg |
| Viscosidad agua a 20 °C | $\mu_{20}$ | 1.002 × 10⁻³ | Pa·s |
| Viscosidad agua a 60 °C | $\mu_{60}$ | 4.7 × 10⁻⁴ | Pa·s |
| Densidad agua a 20 °C | $\rho_{20}$ | 998 | kg/m³ |
| Densidad agua a 60 °C | $\rho_{60}$ | 983 | kg/m³ |
| Densidad lodo alcalino | $\rho_{lodo}$ | 1 040–1 080 | kg/m³ |
| Densidad pasta proteica (50% H₂O) | $\rho_{pasta}$ | 1 080–1 150 | kg/m³ |
| Conductividad acero inox 316L | $\lambda_{316L}$ | 16 | W/m·K |
| Conductividad lana de vidrio | $\lambda_{lv}$ | 0.035–0.040 | W/m·K |
| Conductividad agua a 60 °C | $\lambda_{agua}$ | 0.653 | W/m·K |
| Rugosidad acero inoxidable | $\varepsilon$ | 0.046 | µm |

---

## 17. ACRÓNIMOS Y NOMENCLATURA

| Símbolo | Significado | Unidades |
|---------|-------------|---------|
| $\dot{m}$ | Caudal másico | kg/h ó kg/s |
| $\dot{V}$ | Caudal volumétrico | m³/h |
| $\rho$ | Densidad | kg/m³ |
| $\mu$ | Viscosidad dinámica | Pa·s ó cP |
| $\nu$ | Viscosidad cinemática ($= \mu/\rho$) | m²/s |
| $C_p$ | Calor específico | J/kg·K |
| $U$ | Coeficiente global transferencia calor | W/m²K |
| $h$ | Coeficiente convectivo local | W/m²K |
| $\lambda$ | Conductividad térmica ó calor latente | W/m·K ó kJ/kg |
| $\tau$ | Tiempo de residencia | h ó min |
| $\eta$ | Eficiencia / Rendimiento | % ó adimensional |
| $Re$ | Número de Reynolds | — |
| $Nu$ | Número de Nusselt | — |
| $Pr$ | Número de Prandtl | — |
| $G$ | Factor centrífugo | — |
| $\Delta T_{lm}$ | Diferencia de temperatura logarítmica media | K |
| $NTU$ | Número de unidades de transferencia | — |
| $pI$ | Punto isoeléctrico | — |
| $\zeta$ | Potencial zeta | mV |
| $I$ | Fuerza iónica | mol/L |
| $a_w$ | Actividad de agua | — |
| $f_s$ | Factor de seguridad de diseño | — |
| $x$ | Fracción másica de sólidos | kg/kg |
| $H$ | Humedad (fracción másica de agua) | kg/kg |
| $E$ | Economía de vapor | kg/kg |
| $W_i$ | Índice de trabajo de Bond | kWh/ton |
| $D_h$ | Diámetro hidráulico | m |
| PBT | Pitched Blade Turbine (agitador palas inclinadas) | — |
| LMTD | Log Mean Temperature Difference | K |
| BPR | Boiling Point Rise (elevación punto ebullición) | K |

---

**Proyecto:** Producción de Proteína Aislada de Soya | **Capacidad:** 1 ton/h grano
**Versión:** 1.0 | **Fecha:** Marzo 2026
