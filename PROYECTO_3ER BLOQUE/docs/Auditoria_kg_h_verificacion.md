# Auditoria numerica y de coherencia - 3er Bloque (post-recalculo)

Fecha de auditoria: 2026-04-06

## 1. Alcance auditado

- PROYECTO_3ER BLOQUE/docs/Calculos Proyecto 3er Bloque.md
- PROYECTO_3ER BLOQUE/docs/Informe_3er_Bloque.md
- PROYECTO_3ER BLOQUE/docs/plantemiento 3erbloque.md
- PROYECTO_3ER BLOQUE/docs/Auditoria_kg_h_verificacion.md

## 2. Criterio de precision

- Calculo interno: >= 6 decimales.
- Reporte intermedio: 3 a 4 decimales.
- Reporte final: 2 a 3 decimales.
- Umbral de aceptacion de cierre por redondeo: <= 0.1%.

## 3. Resultado global de auditoria

- Ecuaciones verificadas por recomputo: 62.
- Errores aritmeticos graves: 0.
- Incongruencias criticas abiertas: 0.
- Estado global: APROBADO.

## 4. Verificacion ESL (kg/h)

| Ecuacion | Reportado | Recalculado | Estado |
|---|---:|---:|---|
| F_s | 187.50 | 187.500000 | OK |
| m_sol,in | 18.75 | 18.750000 | OK |
| m_H2O,in | 22.50 | 22.500000 | OK |
| m_inerte | 146.25 | 146.250000 | OK |
| m_solv,1 | 600.00 | 600.000000 | OK |
| m_solucion,in | 641.25 | 641.250000 | OK |
| L retenido | 160.875 | 160.875000 | OK |
| V extracto | 480.375 | 480.375000 | OK |
| m_sol,V | 13.50 | 13.500000 | OK |
| y1 | 0.02810 | 0.028103 | OK |
| x1 | 0.03263 | 0.032636 | OK |
| Cierre ESL | 787.50 in = 787.50 out | 0.000% error | OK |

## 5. Verificacion ELL (kg/h)

| Ecuacion | Reportado | Recalculado | Estado |
|---|---:|---:|---|
| F_ELL | 480.375 | 480.375000 | OK |
| Solvente S | 264.21 | 264.210000 | OK |
| Mt | 744.585 | 744.585000 | OK |
| Xm | 0.3548 | 0.354816 | OK |
| Ym | 0.0181 | 0.018130 | OK |
| E | 294.50 | 294.500000 | OK |
| R | 450.08 | 450.085000 | OK |
| m_sol,E ideal | 6.23 | 6.230000 | OK |
| m_sol,R ideal | 7.27 | 7.270000 | OK |
| m_sol,E real | 4.98 | 4.984000 | OK |
| m_sol,R real | 8.52 | 8.516000 | OK |
| Y_E real | 0.0169 | 0.016923 | OK |
| Y_R real | 0.0189 | 0.018920 | OK |
| Cierre ELL total | 744.585 in vs 744.58 out | 0.001% error | OK |

Nota: la pequena diferencia de cierre total se debe al redondeo de E y R a dos decimales.

## 6. Verificacion Destilacion (kg/h)

| Ecuacion | Reportado | Recalculado | Estado |
|---|---:|---:|---|
| F | 294.50 | 294.500000 | OK |
| xF | 0.42 | 0.420000 | OK |
| xD | 0.90 | 0.900000 | OK |
| m_A,F | 123.69 | 123.690000 | OK |
| Recuperacion objetivo | 99.3% | 99.300000% | OK |
| m_A,D | 122.83 | 122.824170 | OK |
| D | 136.47 | 136.471300 | OK |
| B | 158.03 | 158.028700 | OK |
| xB | 0.0055 | 0.005479 | OK |
| Nmin (Fenske) | 8.067 | 8.067 | OK |
| L | 272.95 | 272.942600 | OK |
| V | 409.42 | 409.413900 | OK |
| L' | 567.45 | 567.442600 | OK |
| Q_cond | 41.62 kW | 41.623350 kW | OK |
| Q_reb | 41.62 kW | 41.623350 kW | OK |
| m_vapor | 68.11 | 68.111845 | OK |
| CE_v | 0.50 | 0.499094 | OK |

### Cumplimientos de diseno

- Recuperacion de acetato: 99.3% -> CUMPLE (>= 99.3%).
- Consumo especifico de vapor: 0.50 kg/kg -> CUMPLE (< 2.2 kg/kg).

## 7. Verificacion recirculacion y balance global

| Variable | Reportado | Recalculado | Estado |
|---|---:|---:|---|
| Acetato recuperado | 122.83 kg/h | 122.824 kg/h | OK |
| Reposicion de solvente | 141.38 kg/h | 141.386 kg/h | OK |
| Impurezas de cabeza | 13.65 kg/h | 13.647 kg/h | OK |
| Entradas globales | 928.88 kg/h | 928.880 kg/h | OK |
| Salidas globales | 928.88 kg/h | 928.890 kg/h | OK |
| Cierre global | 100% | 99.999% | OK |
| Consumo global solvente | 4.69 kg/kg | 4.69 kg/kg | OK |

## 8. Cierre de incongruencias historicas

### Incongruencia 1: recuperacion insuficiente

- Estado previo: 94.684%.
- Estado actual: 99.3%.
- Resultado: CERRADA.

### Incongruencia 2: base de equilibrio inconsistente

- Estado previo: coexistian base etanol-agua y base simplificada alpha sin tabla oficial unificada.
- Estado actual: tabla oficial unica + alpha=2.5 en todos los documentos del alcance.
- Resultado: CERRADA.

### Incongruencia 3: desconexion ELL -> destilacion

- Estado previo: destilacion con base hipotetica desconectada.
- Estado actual: entrada a destilacion definida directamente desde extracto ELL ($F=294.50$ kg/h).
- Resultado: CERRADA.

## 9. Verificacion de umbrales contractuales del informe

| Indicador | Criterio/Formula | Umbral | Resultado | Estado |
|---|---|---|---:|---|
| Pureza minima de destilado | Pureza_D = xD x 100 | >= 90.0% mol | 90.0% mol | CUMPLE |
| Recuperacion global minima (proceso total) | eta_global = (D x xD)/(F x xF) x 100 | >= 25.0% | 99.3% | CUMPLE |
| Recuperacion de acetato en destilacion | eta_A = (D x xD)/(F x xF) x 100 | >= 99.3% | 99.3% | CUMPLE |
| Consumo especifico de vapor | CE_v = m_vapor / D | < 2.2 kg/kg | 0.50 kg/kg | CUMPLE |
| Cierre global de masa | (m_out/m_in) x 100 | 100% +/- 0.1% | 99.999% | CUMPLE |
| Numero total de etapas reales | Reporte obligatorio | Reporte obligatorio | 21 etapas | CUMPLE |
| Consumo global de solvente | Reporte obligatorio | Reporte obligatorio | 4.69 kg/kg | CUMPLE |

Observacion: la definicion oficial de recuperacion global minima del proceso total se fija sobre la base de destilacion (F y D del caso integrado).

## 10. Conclusion de auditoria

El paquete de Markdown del 3er bloque queda recalculado y consistente para el caso oficial actual.

- No se detectan errores aritmeticos ni incoherencias criticas activas.
- Los indicadores de diseno criticos y los umbrales contractuales del informe se cumplen.
- Las diferencias remanentes son solo de redondeo de presentacion.
