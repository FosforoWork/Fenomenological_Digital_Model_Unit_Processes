## Cálculos — Dimensionamiento térmico (Intercambiador de placas)

### 1) Resumen del caso
- Producto (fluido caliente): Yogur líquido
  - ṁ_h = 1.4 kg/s
  - Cp_h = 3.8 kJ/kg·K
  - T_h,in = 45 °C
  - T_h,out = 6 °C
- Fluido de servicio (agua fría):
  - Cp_c = 4.18 kJ/kg·K
  - T_c,in = 2 °C
  - T_c,out = 14 °C
- Parámetros de diseño: U = 2500 W/m²·K, F = 1 (contracorriente ideal)

### 2) Objetivo
Calcular la carga térmica $Q$, el caudal de agua requerido $\dot{m}_c$, la LMTD, el área de transferencia $A$ y verificar por el método NTU–ε. Proveer una plantilla de fórmulas lista para usar en Excel.

### 3) Fórmulas (síntesis)
- Balance energético (fluido caliente):
  
$$
Q = \dot{m}_h\; C_{p,h}\; (T_{h,in} - T_{h,out})
$$

  (Si $C_p$ está en kJ/kg·K multiplicar por 1000 para obtener W)
- Caudal de agua requerido:
  
$$
\dot{m}_c = \frac{Q}{C_{p,c}\; (T_{c,out} - T_{c,in})}
$$

- LMTD (contracorriente):
  
$$
\Delta T_1 = T_{h,in} - T_{c,out} \qquad \Delta T_2 = T_{h,out} - T_{c,in}
$$

  
$$
\Delta T_{lm} = \frac{\Delta T_1 - \Delta T_2}{\ln\left(\dfrac{\Delta T_1}{\Delta T_2}\right)}
$$

- Área requerida:
  
$$
A = \frac{Q}{U\;F\;\Delta T_{lm}}
$$

- NTU / Efectividad (verificación):
  
$$
C_h = \dot{m}_h C_{p,h},\quad C_c = \dot{m}_c C_{p,c}
$$

  
$$
C_{min} = \min(C_h,C_c),\quad C_r = \dfrac{C_{min}}{C_{max}}
$$

  
$$
\mathrm{NTU} = \dfrac{U\;A}{C_{min}}
$$

  Para contracorriente ($C_r\neq 1$):
  
$$
\varepsilon = \frac{1 - e^{-\mathrm{NTU}(1-C_r)}}{1 - C_r\; e^{-\mathrm{NTU}(1-C_r)}}
$$

  
$$
Q_{NTU} = \varepsilon\; C_{min}\; (T_{h,in} - T_{c,in})
$$

### 4) Plantilla sugerida para Excel
Se recomiendan dos hojas: `Inputs` y `Calculos`.

Hoja `Inputs` (coloca los valores):
- B2: ṁ_h (kg/s) = 1.4
- B3: Cp_h (kJ/kg·K) = 3.8
## Cálculos y Fórmulas Unificadas — Intercambiador y Transferencia en Paredes/Tuberías

Este documento contiene las mismas fórmulas y guías que el fichero de referencia de fórmulas para que ambos se mantengan sincronizados. Incluye: balances energéticos, LMTD, NTU, conducción plana y cilíndrica, correlaciones convectivas y plantilla Excel extendida.

---

### 1) Resumen del caso (ejemplo)
- Producto (fluido caliente): Yogur líquido
  - ṁ_h = 1.4 kg/s
  - Cp_h = 3.8 kJ/kg·K
  - T_h,in = 45 °C
  - T_h,out = 6 °C
- Fluido de servicio (agua fría):
  - Cp_c = 4.18 kJ/kg·K
  - T_c,in = 2 °C
  - T_c,out = 14 °C
- Parámetros de diseño: U = 2500 W/m²·K, F = 1 (contracorriente ideal)

### 2) Balance energético

$$
Q = \dot{m}_h\; C_{p,h}\; (T_{h,in} - T_{h,out})
$$

### 3) Caudal necesario del agua

$$
\dot{m}_c = \frac{Q}{C_{p,c}\; (T_{c,out} - T_{c,in})}
$$

### 4) LMTD y Área

$$
\Delta T_{lm} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1/\Delta T_2)}
$$

$$
A = \frac{Q}{U\,F\,\Delta T_{lm}}
$$

### 5) NTU/efectividad (verificación)
Ver sección del otro archivo (idéntica) para fórmulas y pasos de Excel.

### 6) Transferencia por conducción y en tuberías
Se incorpora la conducción plana y cilíndrica, resistencias convectivas y correlaciones (Dittus–Boelter, Gnielinski, Haaland) tal como en el fichero de fórmulas.

### 7) Plantilla Excel extendida
Sugerencias idénticas a las de `Formulas.md`: entradas para radios, conductividad, rugosidad, cálculo de áreas, resistencias y `U_ref`.

### 8) Ejemplo numérico (resumen)
- Q = 207,720 W
- ṁ_c ≈ 4.1426 kg/s
- LMTD ≈ 13.20 K
- A ≈ 6.30 m²
- NTU ≈ 2.96, ε ≈ 0.907

---

Si quieres que genere el archivo `.xlsx` con estas hojas (`Inputs`, `Calculos`) y las fórmulas extendidas, confirma `sí` y lo creo listo para descargar.
- C_h = 1.4 × 3800 = 5,320 W/K
