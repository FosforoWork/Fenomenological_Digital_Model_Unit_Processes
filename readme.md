# Proyecto Final Unitarios

## Produccion de proteina aislada de soya

Proyecto academico de Procesos Unitarios (Ingenieria Industrial, UCB Santa Cruz) orientado al diseno, calculo y simulacion de una planta para obtener proteina aislada de soya en polvo grado alimentario.

## Objetivo general

Disenar y validar un proceso integrado para extraer, concentrar, precipitar y secar proteina de soya, manteniendo calidad funcional, seguridad microbiologica y trazabilidad de calculo por etapa.

## Alcance del proyecto

- Materia prima base: grano de soya (caso principal) con posibilidad de adaptar a arveja.
- Producto objetivo: proteina aislada en polvo para suplemento alimenticio.
- Base de diseno: 1000 kg/h de grano y relacion de extraccion 1:12 (12000 kg/h de agua).
- Incluye: planteamiento tecnico, balances de masa/energia, seleccion preliminar de equipos, control operativo, estimacion economica preliminar y simulacion digital.
- No incluye en esta etapa: detalle de ingenieria civil, diseno mecanico de fabricacion, ni evaluacion financiera completa del negocio.

## Caso base de simulacion

| Variable | Valor base |
|---|---:|
| Alimentacion de soya | 1000 kg/h |
| Proteina en grano | 37.5 % p/p |
| Proteina de entrada | 375 kg/h |
| Agua de extraccion | 12000 kg/h |
| pH extraccion | 8.75 |
| Temperatura extraccion | 55 C |
| Pasteurizacion | 80 C por 22 s |
| Presion evaporacion | 0.40 bar abs |
| Solidos salida evaporador | 23 % p/p |

## Proceso integrado por etapas

### Etapa 0. Preparacion y servicios
- Captacion de agua de red industrial a 12 m3/h.
- Tanque de agua de 15 m3 (autonomia de 1 h + 20% reserva).
- Bombeo sanitario de alimentacion (0.60 kW calculados; 1.5 kW seleccionado).
- Molienda y tamizado inicial de harina.

### Etapa 1. Extraccion alcalina
- Suspension de harina en medio alcalino (pH 8.5-9.0) a 50-60 C.
- Tiempo de residencia de 45-60 min en tanque agitado.
- Eficiencia base de extraccion proteica: 88%.

### Etapa 1.2. Separacion solido-liquido
- Separacion de okara y extracto proteico con centrifugacion/filtracion.
- Recuperacion de extracto en rango 95-98%.

### Etapa 2. Neutralizacion y pasteurizacion
- Ajuste de pH hacia 7.0 con dosificacion controlada de acido.
- Pasteurizacion HTST: 75-85 C por 15-30 s (caso base: 80 C y 22 s).

### Etapa 2.5. Osmosis inversa (OI)
- Preconcentracion del extracto para reducir carga termica de evaporacion.
- Variable clave de operacion: recuperacion OI y flujo de permeado (LMH/TMP).

### Etapa 3. Evaporacion al vacio
- Concentracion termica bajo vacio para proteger proteina.
- Operacion objetivo en 0.40 bar abs y 50-60 C de ebullicion equivalente.

### Etapa 4. Precipitacion isoelectrica y centrifugacion
- Ajuste a pH 4.5 para precipitar proteina.
- Recuperacion de precipitacion cercana al 98%.
- Separacion de pasta humeda y suero residual.

### Etapa 5. Secado final y clasificacion
- Secado por atomizacion para alcanzar humedad final menor a 5%.
- Molienda/tamizado final para especificacion 100-200 mesh.

### Etapa 6. Envasado y almacenamiento
- Envasado en formato industrial (20-25 kg) con barrera de humedad.
- Almacenamiento recomendado: 15-25 C y HR &lt; 70%.

## Resultados tecnicos de referencia

Estos valores se usan como referencia operacional y de validacion en la app:

| KPI de proceso | Valor |
|---|---:|
| Proteina extraida (Etapa 1) | 330.0 kg/h |
| Proteina precipitada (Etapa 4) | 323.4 kg/h |
| Polvo final (Etapa 5) | 364.6 kg/h |
| Proteina final | 323.4 kg/h |
| Humedad final | 5.0 % |
| Pureza aproximada del polvo | 88.7 % |
| Cierre de masa esperado | error absoluto &lt;= 0.5 % |

## Balance de masa y energia (resumen)

- Flujo principal de proceso: 1000 kg/h de grano + 12000 kg/h de agua.
- Evaporacion de agua dominante en demanda energetica de planta.
- OI reduce carga termica aguas abajo (menos agua a evaporar).
- El secado por atomizacion define la condicion final de humedad y capacidad de despacho.

## Equipos principales de diseno preliminar

- TK-001 + P-001: tanque y bomba de agua de extraccion.
- TK-101: tanque agitado de extraccion alcalina.
- CF-102A/B: centrifugas decantadoras post-lixiviacion.
- HX-201: intercambiador de placas para pasteurizacion.
- OI-250: modulo de osmosis inversa (innovacion del esquema).
- EV-301A/B: evaporador de doble efecto bajo vacio.
- PR-401 + CF-401: precipitacion isoelectrica y separacion final.
- SD-501: spray dryer.
- ML-601 + CR-601: molienda y tamizado final.

## Variables criticas de control

- Extraccion: pH, temperatura, tiempo de residencia, relacion solido/liquido y agitacion.
- Pasteurizacion: temperatura objetivo y tiempo de retencion.
- OI: TMP, flujo cruzado, SDI y pH de alimentacion.
- Evaporacion: presion absoluta y solidos objetivo.
- Precipitacion: pH 4.5 y tiempo de coagulado.
- Secado: temperatura de secado y residencia.

## Calidad, seguridad y materiales

- Material recomendado de contacto: acero inoxidable 304/316L; evitar acero al carbono en contacto con corrientes de proceso.
- Control de pH en linea con alarmas para zonas alcalinas/acidas.
- Ventilacion y procedimientos de seguridad para manejo de NaOH/HCl.
- Control de calidad minimo: pH, solidos, humedad final, proteina y verificacion microbiologica por lote.

## Integracion con la aplicacion Streamlit

La app principal [app.py](../app.py) implementa el **Gemelo Digital AJAX** para el caso base y escenarios de sensibilidad:

- Operacion: ajuste de variables, limites de capacidad y dimensionamiento.
- Monitoreo: KPIs por etapa con historico.
- Validacion: corroboracion contra referencias base.
- Proyecto Final: vista documental integrada de este README.

## Entregables consolidados

- Planteamiento tecnico y alcance de ingenieria del proceso.
- Calculos trazables por etapa con criterios de diseno.
- Informe tecnico simplificado para presentacion.
- Simulador interactivo para analisis operativo y de sensibilidad.

