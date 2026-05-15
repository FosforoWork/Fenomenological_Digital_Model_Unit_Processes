# Variables Operativas y Especificaciones de Equipos
## Proyecto: Producción de Proteína Aislada de Soya

---

## 1. ESCALA DE PRODUCCIÓN Y CÁLCULOS DE CAUDAL BASE

### 1.1 Parámetros Iniciales de Entrada
| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| **Capacidad de Producción** | 1 | ton/h grano soya |
| **Peso de Grano/Hora** | 1000 | kg/h |
| **Proteína Bruta en Grano de Soya** | 35-40 | % p/p |
| **Proteína Estimada Entrada** | 375 | kg proteína/h |

### 1.2 Cálculos de Caudales Estimados por Etapa

#### **Etapa 0: Preparación de Materias Primas**

| Corriente | Caudal | Cálculo |
|-----------|--------|---------|
| Grano de soya seco | 1000 kg/h | Entrada |
| Agua para extracción | 12000 kg/h | Relación 1:12 (p/v) soya:agua |
| Agua total en sistema | 12000-15000 L/h | ~12-15 m³/h |
| Solución NaOH (10-15%) | 50-100 kg/h | Para alcalización de agua |
| Solución HCl (37%) | 30-50 kg/h | Para ajustes iniciales de neutralización |

#### **Etapa 1: Extracción Alcalina**

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| **Caudal volumétrico entrada** | 13 | m³/h |
| **Caudal másico (harina + agua)** | 13000 | kg/h |
| **Tiempo de residencia** | 45-60 | min |
| **Volumen mínimo tanque agitado** | 9.75-13 | m³ |
| **Volumen de diseño (factor 1.2)** | 12-15.5 | m³ |
| **Proteína disuelta en extracto** | 320-350 | kg/h |
| **Eficiencia de extracción** | 85-92 | % |

#### **Etapa 1.2: Separación Sólido-Líquido**

| Corriente | Caudal | Composición |
|-----------|--------|-------------|
| **Lodo proteico (entrada)** | 13 | m³/h |
| **Extracto proteico (salida)** | 12.2-12.6 | m³/h (~92-97% del volumen) |
| **Okara húmedo (salida)** | 0.4-0.8 | m³/h (~700-1000 kg/h) |
| **Humedad en Okara** | 60-70 | % |
| **Peso seco Okara** | 300-400 | kg/h |
| **Recuperación de extracto** | 95-98 | % |
| **Proteína en extracto** | 320-340 | kg/h |

#### **Etapa 2: Neutralización y Pasteurización**

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| **Caudal de entrada** | 12.4 | m³/h |
| **Caudal de HCl para neutralizar** | 15-25 | kg/h |
| **Caudal extracto neutralizado** | 12.42 | m³/h (aumento ~2%) |
| **Temperatura entrada** | 25 | °C |
| **Temperatura pico pasteurización** | 75-85 | °C |
| **Temperatura salida** | 25 | °C |
| **Retención térmica** | 15-30 | seg |
| **Calor requerido** | 4.5-6.5 | MJ/h (transferencia neta) |

#### **Etapa 3: Concentración (Evaporador Vacío)**

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| **Caudal entrada (10% sólidos)** | 12.42 | m³/h |
| **Caudal entrada (masa sólidos)** | 1240 | kg sólidos/h |
| **Presión operativa** | 0.3-0.5 | bar abs |
| **Temperatura operativa** | 50-60 | °C |
| **Concentración salida (% sólidos)** | 20-25 | % |
| **Caudal salida (20% sólidos)** | 6.2 | m³/h |
| **Caudal salida (25% sólidos)** | 4.96 | m³/h |
| **Agua evaporada** | 6.2-7.44 | m³/h (~6200-7440 kg/h) |
| **Vapor producido** | 6200-7440 | kg/h |

#### **Etapa 4: Precipitación Isoeléctrica**

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| **Caudal de entrada (concentrado)** | 5.6 | m³/h (promedio 20-25% sólidos) |
| **pH ajuste** | 4.5 | - |
| **Caudal HCl para precipitación** | 25-35 | kg/h |
| **Caudal lodo precipitado** | 5.66 | m³/h (aumento ~1% por precipitado) |
| **Proteína precipitada** | 318-335 | kg/h (~98% de extracto) |
| **Flóculo promedio** | 200-500 | μm |

#### **Etapa 4.2: Centrifugación Decanter**

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| **Caudal lodo entrada** | 5.66 | m³/h |
| **Caudal pasta proteica salida** | 1.8-2.2 | m³/h (~50-55% humedad residual) |
| **Caudal suero residual** | 3.46-3.86 | m³/h |
| **Humedad en pasta** | 50-55 | % |
| **Masa proteína en pasta** | 313-328 | kg/h |
| **Factor centrífugo** | 1500-2000 | g |
| **Recuperación de sólidos** | 98-99 | % |

#### **Etapa 5: Secado por Atomización (Spray Dryer)**

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| **Caudal pasta proteica entrada** | 2.0 | m³/h (50% humedad = 1000 kg sólidos + 1000 kg agua) |
| **Masa entrada (sólidos + agua)** | 2000 | kg/h |
| **Masa sólidos proteicos** | ~890 | kg/h (~280 kg H₂O residual) |
| **Humedad final especificada** | <5 | % |
| **Masa agua a remover** | 1880-1900 | kg/h |
| **Masa polvo final (5% humedad)** | 935-945 | kg/h |
| **Rendimiento global grano → polvo** | 93.5-94.5 | % (en sólidos proteicos) |
| **Temperatura aire entrada (Inlet)** | 180-200 | °C |
| **Temperatura aire salida (Outlet)** | 80-90 | °C |
| **Tiempo de residencia en cámara** | 10-20 | seg |

#### **Etapa 5.2: Molienda y Tamizado Final**

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| **Caudal entrada** | 945 | kg/h |
| **Tamaño objetivo** | 100-200 | mesh |
| **Diámetro medio final** | 74-149 | μm |
| **Recuperación en tamizado** | 95-98 | % |
| **Caudal polvo final** | 895-925 | kg/h |

#### **Etapa 6: Envasado**

| Parámetro | Valor |
|-----------|-------|
| **Caudal producto final** | 895-925 kg/h |
| **Formato bolsa** | 20-25 kg |
| **Número de bolsas/hora** | 36-46 bolsas/h |
| **Pallets/hora** | 0.9-1.2 pallets/h (si 40 bolsas/pallet) |

---

## 2. VARIABLES FISICOQUÍMICAS CRÍTICAS POR ETAPA

### Etapa 0: Preparación de Materias Primas

#### Variables Físicas
| Variable | Valor Típico | Unidad | Método de Control |
|----------|--------------|--------|-------------------|
| Humedad grano entrada | 10-12 | % | Secador termogravimétrico |
| Densidad del grano | 1.12-1.15 | g/cm³ | Densímetro/picnómetro |
| Tamaño partícula molienda inicial | 100-200 | mesh | Análisis granulométrico |
| Densidad aparente harina | 0.70-0.80 | g/cm³ | Picnómetro/taza graduada |
| Viscosidad agua tratada | 1.0 | cP (a 20°C) | Viscosímetro Brookfield |

#### Variables Químicas
| Variable | Valor Típico | Unidad | Especificación |
|----------|--------------|--------|----------------|
| pH agua captada | 6.5-7.5 | - | Potenciómetro |
| Dureza agua (CaCO₃) | <50 | mg/L | Tras ablandamiento |
| Concentración NaOH | 10-15 | % p/v | Solución preparada |
| Concentración HCl | 37 | % p/v | Reactivo grado análisis |
| Cloro residual | <0.5 | mg/L | Testigo DPD |

#### Variables Fisicoquímicas
| Variable | Valor Típico | Unidad | Rango Operativo |
|----------|--------------|--------|-----------------|
| Densidad agua + NaOH (pH 8.5) | 1.008-1.012 | g/cm³ | Según % NaOH |
| Densidad suspensión inicial (1:12) | 1.05-1.10 | g/cm³ | Hidrometría |

---

### Etapa 1: Extracción Alcalina

#### Variables Físicas
| Variable | Valor Especificado | Unidad | Notas |
|----------|-------------------|--------|-------|
| pH operativo | 8.5-9.0 | - | Crítico para solubilidad proteica |
| Temperatura | 50-60 | °C | Evitar >65°C para prevenir desnaturalización |
| Relación S/L | 1:10 a 1:15 | p/v | Balance viscosidad-extracción |
| Tiempo de residencia | 45-60 | min | Optimización cinética |
| Velocidad agitación | 50-100 | rpm | Según volumen y tipo agitador |
| Viscosidad lodo alcalino | 15-30 | cP | A 55°C, fluido no newtoniano |
| Densidad lodo | 1.04-1.08 | g/cm³ | Hidrometría en proceso |

#### Variables Químicas
| Variable | Valor | Unidad | Control |
|----------|-------|--------|---------|
| Concentración NaOH en agua | 0.2-0.4 | % p/v | Titulación |
| Proteína disuelta | 25-27 | kg/m³ (25-27 g/L) | Método Kjeldahl |
| Aminoácidos libres | <0.5 | kg/m³ | Cromatografía HPLC |

#### Variables Fisicoquímicas
| Variable | Valor | Unidad | Implicancia |
|----------|-------|--------|-------------|
| Osmolalidad | 80-120 | mOsm/kg | Influye en presión osmótica |
| Conductividad | 1.5-2.5 | mS/cm | Monitoreo en línea |
| Índice de fluidez (no newtoniano) | 0.7-0.85 | - | Para cálculos de transferencia |
| Densidad aparente proteína dispersa | ~1.35 | g/cm³ | Datos literatura |

---

### Etapa 2: Neutralización y Pasteurización

#### Variables Físicas
| Variable | Valor | Unidad | Especificación |
|----------|-------|--------|----------------|
| Temperatura entrada neutralización | 55-60 | °C | Desde lixiviación |
| Temperatura neutralizado | 25-30 | °C | Tras enfriamiento |
| Temperatura entrada pasteurización | 20-25 | °C | Entre tanques |
| Temperatura pico pasteurización | 75-85 | °C | Retención 15-30 seg |
| Velocidad de adición HCl | <5 | mL/min/100L | Para evitar cristalización |
| Viscosidad post-neutralización | 12-20 | cP | 25°C, menos viscoso |
| Densidad post-neutralización | 1.01-1.05 | g/cm³ | Reducción por dilución |

#### Variables Químicas
| Variable | Valor | Unidad | Rango Aceptable |
|----------|-------|--------|-----------------|
| pH post-neutralización | 7.0 ± 0.2 | - | 6.8-7.2 |
| Proteína remanente | 25-27 | kg/m³ | ~99% recuperada |
| Residuos Na⁺ | 100-200 | mg/L | De NaOH anterior |
| Residuos Cl⁻ | 80-150 | mg/L | De HCl agregado |
| Concentración microorganismos | <10³ | UFC/mL | Post-pasteurización |

#### Variables Fisicoquímicas
| Variable | Valor | Unidad | Observación |
|----------|-------|--------|-------------|
| Coeficiente global de transferencia calor (U) | 400-600 | W/m²K | Placas, fluido no newtoniano |
| Número de Reynolds (Re) | 100-500 | - | Flujo laminar/transicional |
| Número de Prandtl (Pr) | 150-300 | - | Típico fluidos viscosos |
| NTU (DTR) | 0.02-0.05 | - | Desviación diámetro nozzle |
| Caída de presión intercambiador | 0.5-1.5 | bar | Ambos lados circulación |

---

### Etapa 3: Concentración (Evaporador Vacío)

#### Variables Físicas
| Variable | Valor | Unidad | Control |
|----------|-------|--------|---------|
| Presión absoluta operativa | 0.3-0.5 | bar | Vacuómetro |
| Temperatura de ebullición | 50-60 | °C | Sensor PT100 |
| Concentración sólidos entrada | 10 | % p/p | Refractómetro/secador |
| Concentración sólidos salida | 20-25 | % p/p | Secador termogravimétrico |
| Viscosidad concentrado (20% sólidos) | 50-100 | cP | A 55°C, muy viscoso |
| Densidad concentrado | 1.10-1.15 | g/cm³ | Hidrómetro |
| Tamaño medio gota/película | 2-5 | mm | Film descendente |

#### Variables Químicas
| Variable | Valor | Unidad | Notas |
|----------|-------|--------|-------|
| pH concentrado | 7.0 ± 0.2 | - | Mantener neutral |
| Proteína en concentrado | 240-280 | kg/m³ | Concentración 10x |
| Minerales (cenizas) | 2-4 | % p/p | Aumento relativo |
| Sales disueltas | 50-100 | g/L | De proceso anterior |

#### Variables Fisicoquímicas
| Variable | Valor | Unidad | Implicancia |
|----------|-------|--------|-------------|
| Coeficiente película externa (h) | 200-400 | W/m²K | Baja presión, film laminar |
| Coeficiente película interna vapor | 500-1500 | W/m²K | Condensación vapor |
| U global evaporación | 150-300 | W/m²K | Mucho menor que intercambiador |
| Calor latente vaporización (50-60°C) | 2350-2370 | kJ/kg | Agua a bajo vacío |
| Consumo de vapor (saturado 2-3 bar) | 1.8-2.2 | kg vapor/kg agua evaporada | Aprox. eficiencia 50-55% |

---

### Etapa 4: Precipitación Isoeléctrica y Separación

#### Variables Físicas
| Variable | Valor | Unidad | Especificación |
|----------|-------|--------|----------------|
| pH punto isoeléctrico soya | 4.5 ± 0.2 | - | Rango óptimo 4.3-4.7 |
| Temperatura precipitación | 20-25 | °C | Ambiente controlado |
| Tamaño flóculo formado | 200-500 | μm | Optimización velocidad adición |
| Vel. Sedimentación laminar | 0.1-0.5 | mm/seg | Flujo Stokes |
| Viscosidad lodo precipitado | 100-200 | cP | 25°C |
| Densidad pasta proteica | 1.08-1.15 | g/cm³ | Con 50-60% humedad |

#### Variables Químicas
| Variable | Valor | Unidad | Control |
|----------|-------|--------|---------|
| Concentración proteína precipitable | 24-27 | kg/m³ | Método Kjeldahl |
| pH residual suero | 4.5-4.8 | - | Potenciómetro |
| Proteína residual en suero | 0.3-0.7 | kg/m³ | <3% original |
| Concentración Na⁺ en suero | 200-400 | mg/L | Residuos NaOH |
| Concentración Cl⁻ en suero | 400-800 | mg/L | Del HCl agregado |

#### Variables Fisicoquímicas
| Variable | Valor | Unidad | Consideración |
|----------|-------|--------|----------------|
| Fuerza iónica (I) | 0.05-0.15 | mol/L | Aumenta con sales |
| Carga neta proteína @ pH 4.5 | ~0 | - | Presupuesto isoelectricidad |
| Potencial zeta @ pH 4.5 | -2 a +2 | mV | Cercano a cero (sin repulsión) |

---

### Etapa 5: Secado por Atomización

#### Variables Físicas
| Variable | Valor | Unidad | Control |
|----------|-------|--------|---------|
| Temperatura aire entrada (Inlet) | 180-200 | °C | Termopar entrada |
| Temperatura aire salida (Outlet) | 80-90 | °C | Termopar salida |
| Humedad aire entrada | 10-20 | % | Psicrómetro |
| Flujo aire | 8000-12000 | m³/h | Anemómetro/medidor vacío |
| Velocidad atomización (disco) | 250-500 | m/seg | RPM disco atomizador |
| Tamaño partícula aerosol inicial | 20-100 | μm | Laser diffraction |
| Tamaño partícula polvo final | 74-149 | μm (100-200 mesh) | Granulometría |
| Densidad aparente polvo | 0.50-0.65 | g/cm³ | Picnómetro de helio |
| Humedad final producto | <5 | % | Karl Fischer |

#### Variables Químicas
| Variable | Valor | Unidad | Especificación |
|----------|-------|--------|----------------|
| Proteína en polvo | 88-92 | % p/p | Protein as-is |
| Grasa residual | 1-3 | % p/p | Soxhlet |
| Cenizas (minerales) | 4-6 | % p/p | Calcinación 600°C |
| Carbohidratos residuales | 2-4 | % p/p | Por diferencia |
| Aminoácidos libres | <0.5 | % p/p | Preservación térmica |

#### Variables Fisicoquímicas
| Variable | Valor | Unidad | Implicancia |
|----------|-------|--------|-------------|
| Número de Drying (Nd) | 50-100 | - | Ratio tasa evaporación/dilatación |
| Coeficiente transf. calor (h) | 80-150 | W/m²K | Baja densidad partícula |
| Humedad crítica | 15-25 | % | Punto inflexión curva secado |
| Tiempo residencia teórico | 10-20 | seg | Para alcanzar <5% H₂O |

---

### Etapa 5.2: Molienda y Tamizado

#### Variables Físicas
| Variable | Valor | Unidad | Control |
|----------|-------|--------|---------|
| Tamaño entrada molino | 50-200 | μm | Polvo aglomerado posible |
| Tamaño salida molino | 74-149 | μm | Objetivo |
| Eficiencia tamizado | 95-98 | % | Recuperación |
| Densidad aparente final | 0.55-0.70 | g/cm³ | Picnómetro |
| Porosidad | 30-40 | % | Volumen poro/total |
| Ángulo de reposo | 35-45 | grados | Fluidez evaluada |
| Densidad lecho embalado | 0.65-0.80 | g/cm³ | Depende compactación |

#### Variables Químicas
| Variable | Valor | Unidad | Post-Molienda |
|----------|-------|--------|---------------|
| Proteína | 88-92 | % p/p | Sin cambios |
| Humedad | <5 | % | Mantener <5% |
| Peróxidos | <10 | meq/kg | Oxidación durante molienda |

---

### Etapa 6: Envasado y Almacenamiento

#### Variables Físicas
| Variable | Valor | Unidad | Especificación |
|----------|-------|--------|----------------|
| Peso empaque bolsa | 20-25 | kg | Estándar comercial |
| Volumen bolsa requerido | 30-40 | L | Densidad aparente 0.6-0.7 |
| Espesor lámina interior PE | 100-150 | μm | Barrera humedad |
| Peso bolsa kraft | 80-150 | g/m² | Según capas |
| Temperatura almacenamiento | 15-25 | °C | Ambiente controlado |
| Humedad relativa almacén | <70 | % RH | Evitar aglomeración |
| Permeabilidad O₂ (bolsa) | <0.5 | cm³/m²·día | Barrera oxidación |
| Permeabilidad H₂O | <5 | g/m²·día | Barrera humedad |

#### Variables Químicas
| Variable | Valor | Unidad | Contenido Final |
|----------|-------|--------|-----------------|
| Proteína garantizado | ≥88 | % p/p | Especificación técnica |
| Humedad máxima | ≤5 | % | ISO 1248 |
| Cenizas máximas | ≤6 | % | Contaminantes minerales |
| Grasa máxima | ≤3 | % | Residuos lipídicos |
| Agentes anti-aglomerantes | variables | ppm | CaSiO₃ o SiO₂ coloidal |
| Antioxidantes | 100-500 | ppm | BHA, BHT o natural |

#### Variables Fisicoquímicas
| Variable | Valor | Unidad | Almacenamiento |
|----------|-------|--------|-----------------|
| Actividad de agua (aw) | <0.65 | - | Seguridad microbiológica |
| Vida útil con N₂ | 18-24 | meses | Bajo atmósfera inerte |
| Vida útil aire | 12-18 | meses | Bolsa estándar |
| Degradación proteica/mes | <1 | % | A 20°C, conditios óptimas |

---

## 3. ESPECIFICACIONES DE EQUIPOS Y MATERIALES

### 3.1 TANQUE AGITADO DE EXTRACCIÓN ALCALINA

#### Dimensiones y Capacidad
```
Capacidad esperada:      12-15 m³ (con factor seguridad 1.2×1 ton/hr × 45-60 min de residencia)
Tipo de tanque:          Cilíndrico con fondo cónico
Material:                Acero inoxidable 316L
Espesor pared:           8-10 mm (presión atmosférica + sobrepresión)
Diámetro (D):            2.5-2.8 m
Altura líquido (H):      2.0-2.5 m
Relación H/D:            0.8-0.9 (optimizado para agitación)
```

#### Especificaciones de Agitador
| Parámetro | Especificación |
|-----------|----------------|
| Tipo | Turbina de palas inclinadas (Pitched Blade Turbine - PBT) 6-8 palas |
| Material eje | Acero inoxidable 316L |
| Material palas | Hierro fundido revestido o acero 316L |
| Diámetro agitador | 0.85-1.0 m (40-50% diámetro tanque) |
| Velocidad rotación | 50-100 rpm |
| Potencia motor | 5.5-7.5 kW |
| Tipo motor | Acoplamiento flexible (elastómero) |
| Deflectores (Baffles) | 4 unidades, altura total, ancho = D/10 = 250-280 mm |
| Sello mecanismo | Sello mecánico double-face (FDA approved) |

#### Sistemas Auxiliares
| Sistema | Especificación |
|---------|----------------|
| Control pH | Sonda de pH (rango 6-10) + transmisor 4-20 mA |
| Control Temperatura | PT100 RTD clase A + transmisor |
| Dosificación NaOH | Bomba centrífuga 10-50 L/min @ 3 bar |
| Dosificación HCl | Bomba símbolo/peristáltica 5-20 L/min |
| Aislamiento térmico | Lana de vidrio 50 mm + aluminio reflectivo |
| Conexiones | Bridas ANSI 150 # acero inoxidable |
| Válvulas de descarga | Bola 3 vías, acero inoxidable 316L, diámetro nominal 50 mm |

---

### 3.2 CENTRÍFUGA DECANTADORA (Post-Lixiviación)

#### Especificaciones Técnicas
| Parámetro | Valor |
|-----------|-------|
| Tipo | Decantadora horizontal 2-fase (sólido/líquido) |
| Capacidad | 5-8 m³/h |
| Material cuerpo | Acero inoxidable 316L |
| Factor centrífugo (G) | 1500-2000 g |
| Velocidad tambor | 1500-3600 rpm (varía con modelo) |
| Velocidad tornillo | 1450-3500 rpm (diferencial 50-100 rpm) |
| Diámetro tambor | 500-700 mm |
| Largo tambor | 1200-1500 mm |
| Recuperación sólidos | ~95-97% |
| Tiempo retención | 3-5 min |
| Potencia motor | 11-15 kW |
| Sello mecánico | Double-face carbón/acero inox |
| Conexiones entrada/salida | Tuberías acero inox 316L |
| Requerimiento servicio | Aire comprimido 6 bar (drenaje) |

#### Materiales Internos
| Componente | Material |
|------------|----------|
| Cilindro rotativo | Acero inoxidable 316L |
| Tornillo (screw) | Acero inoxidable 316L endurecido |
| Tubo central | Acero inoxidable 316L |
| Casquillos de apoyo | Nylatron GS, bronce o acero inox 316L |

---

### 3.3 INTERCAMBIADOR DE CALOR (Neutralización + Pasteurización)

#### Tipo: Intercambiador de Placas

#### Especificaciones Generales
| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| Tipo placas | Brasadas o ligadas pernos | - |
| Material placas | Titanio o acero inoxidable 316L | - |
| Juntas | Elastómero alimentario (Viton, EPDM) | - |
| Presión máxima | 25-30 | bar |
| Capacidad térmica | 150-300 | kW (según configuración) |
| Área interfacial | 20-40 | m² |
| Número placas | 40-80 (aproximado) |
| Canales por lado | 20-40 | - |
| Ancho junta | 3-4 | mm |
| Espesor placa | 0.6-0.8 | mm |
| Caída presión aceptable | 0.5-1.5 | bar (cada lado) |

#### Condiciones Operacionales
| Lado | Temperatura Entrada | Temperatura Salida | Presión |
|------|-------------------|-------------------|---------|
| **Caliente (vapor)** | Variable (~120°C) | 75-85°C | 2-3 bar |
| **Frío (proteína)** | 20-25°C | 75-85°C | 1-2 bar |

#### Sistema de Control
| Componente | Especificación |
|------------|----------------|
| Válvula 3 vías | Acero inoxidable 316L, actuador neumático |
| Válvula antiretorno | En línea salida calefacción |
| Manómetros | Por cada lado (0-30 bar) |
| Termómetros | PT100 entrada/salida cada lado |
| Purga aire | Válvula manual en punto alto |
| Drenaje | Válvula de bola baja cada lado |

---

### 3.4 EVAPORADOR AL VACÍO (Tipo Película Descendente)

#### Especificaciones Técnicas
| Parámetro | Valor |
|-----------|-------|
| Tipo | Película descendante (Falling Film) |
| Material cuerpo | Acero inoxidable 304/316L |
| Área de evaporación | 15-25 m² |
| Presión operativa | 0.3-0.5 bar abs |
| Temperaturas | Entrada 25-30°C, Salida 50-60°C |
| Tubos (sección calefacción) | Cobre/latón-níquel, diámetro 20-25 mm |
| Número de tubos | 30-50 |
| Altura útil tubos | 2.0-3.0 m |
| Velocidad película | 0.05-0.15 m/seg |
| Coeficiente transferencia (U) | 150-300 W/m²K |
| Separador de película | Tipo gravedad + centrífugo (breve) |
| Separador vapor | Ciclón/malla coalescente |

#### Sistema de Vacío
| Componente | Especificación |
|------------|----------------|
| Bomba vacío | Rotativa tipo paletas 3-5 m³/min |
| Motor bomba vacío | 1.5-2.2 kW |
| Línea vacío | Tubo acero inox 40 mm |
| Válvula admisión aire | Reguladora 0-1 bar |
| Vacuómetro | Rango 0-1 bar abs |
| Válvula relevo | Resorte ajustable 0.4-0.5 bar |

#### Condensador Vapor
| Componente | Especificación |
|------------|----------------|
| Tipo | Intercambiador placas o tubular |
| Área condensación | 8-12 m² |
| Agua refrigeración | 15-25°C entrada, <40°C salida |
| Caudal agua | 20-40 m³/h |
| Presión agua | 2-3 bar |
| Material | Acero inoxidable 304L o titanio |

---

### 3.5 CENTRÍFUGA DECANTADORA (Post-Precipitación)

#### Especificaciones Técnicas (Similar a 3.2 pero diseño optimizado)
| Parámetro | Valor |
|-----------|-------|
| Tipo | Decantadora horizontal 2-fase |
| Capacidad | 3-6 m³/h |
| Factor centrífugo (G) | 1800-2500 g |
| Velocidad tambor | 2000-3600 rpm |
| Material | Acero inoxidable 316L (máxima corrosión por ácido) |
| Tiempo retención | 2-4 min |
| Recuperación sólidos | ~98-99% |
| Potencia motor | 15-22 kW |
| Acabado superficie interna | Pulido (preferente para ácidos) |
| Drenaje automático | Sistema nivel capacitivo |

---

### 3.6 SECADOR POR ATOMIZACIÓN (SPRAY DRYER)

#### Especificaciones de Cámara de Secado
| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| Tipo cámara | Cilíndrica + cono convergente | - |
| Diámetro cámara | 2.5-3.2 | m |
| Altura cámara (útil) | 4.0-5.5 | m |
| Volumen total | 25-40 | m³ |
| Material interno | Acero inoxidable 304 (recubrimiento) | - |
| Revestimiento | 50 mm lana vidrio + aluminio | - |
| Atomizador tipo | Disco (rotativo) | - |
| Diámetro disco | 80-120 | mm |
| Velocidad disco | 250-500 | m/seg (~15000-25000 rpm) |
| Soporte disco | Acero inoxidable, acoplamiento flexible | - |

#### Sistema de Aire Caliente
| Componente | Especificación |
|-----------|----------------|
| Generador calor | Quemador gas natural o eléctrico 100-200 kW |
| Aire entrada | Filtrado clase G4 |
| Temperatura Inlet | 180-200°C |
| Temperatura Outlet | 80-90°C |
| Flujo aire | 8000-12000 m³/h |
| Ventilador | Centrífugo directo, motor 5.5-7.5 kW |
| Control temperatura | PLC con termocupla tipo K |
| Válvula regulación flujo | 3-vías o válvula mariposa modular |

#### Colectores de Polvo
| Componente | Especificación |
|-----------|----------------|
| Ciclón primario | Eficiencia >95% partículas >10 μm |
| Filtro de bolsas | Polietileno teflonado (PTFE), área 20-30 m² |
| Pulsado aire reversible | Compresor 5.5-7.5 kW, 6 bar |
| Depósito polvos | Acero inoxidable 304, capacidad 500-800 L |
| Tornillo sin fin descarga | Acero inoxidable, motor 0.75 kW |

---

### 3.7 MOLINO Y CRIBA (Post-Secado)

#### Molino de Martillos
| Parámetro | Especificación |
|-----------|----------------|
| Capacidad | 1000-1500 kg/h |
| Tipo | Martillos pivotantes reversibles |
| Material carcaza | Acero al carbono con revestimiento |
| Material martillos | Acero templado o acero especial |
| Velocidad rotación | 1500-3000 rpm |
| Potencia motor | 7.5-11 kW |
| Malla descarga | 0.5-2 mm (ajustable) |
| Conexiones | Bridas acoplamiento flexible |

#### Criba Vibratoria
| Parámetro | Especificación |
|-----------|----------------|
| Tipo | Vibración lineal o elíptica |
| Capacidad | 800-1200 kg/h |
| Área malla | 1.5-2.5 m² |
| Mallas | 100 mesh (150 μm) y 200 mesh (74 μm) |
| Material malla | Acero inoxidable 316L o cobre |
| Bastidor | Acero al carbono recubierto |
| Frecuencia vibración | 1200-1800 cpm |
| Amplitud | 3-5 mm |
| Motor vibración | 1.5-3 kW |
| Separadores sólidos | 2 fracciones (rechazo >200 mesh, pasante) |

---

### 3.8 TUBERIAS Y CONEXIONES

#### Material Principal: Acero Inoxidable 316L

#### Dimensiones por Etapa
| Corriente | Diámetro Nominal | Espesor Pared | Schedule |
|-----------|------------------|---------------|----------|
| Agua alimentación | 50 mm (2") | 2.1 mm | 40 |
| Lodo proteico (lixiviación) | 75 mm (3") | 2.8 mm | 40 |
| Extracto (post-filtración) | 50 mm (2") | 2.1 mm | 40 |
| Vapor sanitización | 40 mm (1.5") | 2.4 mm | 40 |
| Condensado retorno | 25 mm (1") | 1.9 mm | 40 |
| Dosificación ácido/base | 12 mm (0.5") | 1.5 mm | 80 |
| Salida secador | 100 mm (4") | 3.4 mm | 40 |

#### Especificaciones de Tubería Acero Inoxidable 316L
- **Norma:** ASTM A312 / DIN 17458
- **Acabado:** Decapado y pasivado conforme ASTM A967
- **Rugosidad superficial:** Ra ≤ 0.8 μm (pulido sanitario)
- **Conexiones:** Bridas ANSI B16.5 RF (flat face) o soldadas
- **Válvulas:** Bola tipo full-port acero inoxidable 316L
- **Acoples rápidos:** Acero inoxidable con elastómeros FDA

#### Materiales no permitidos directamente en contacto con fluidos
- ❌ Acero al carbono (excepto estructuras de soporte)
- ❌ Cobre puro (excepto en tubos de intercambiadores sin contacto directo con proteína)
- ❌ Latón estándar (solo latón-níquel en intercambiadores)
- ❌ PVC (solo para tuberías de aire/servicios)

#### Aislamiento de Tuberías
- **Lixiviación (50-60°C):** Lana vidrio 30 mm
- **Pasteurización (75-85°C):** Lana vidrio 50 mm
- **Concentración (50-60°C):** Lana vidrio 40 mm
- **Revestimiento exterior:** Aluminio reflectivo 0.5 mm

---

## 4. RESUMEN DE CAUDALES CRÍTICOS Y PUNTOS DE CONTROL

### Tabla Resumen Caudales por Etapa (para 1 ton/h grano soya)

| Etapa | Corriente | Caudal Másico | Caudal Volumétrico | Sólidos | Observaciones |
|-------|-----------|---------------|-------------------|---------|---------------|
| **0** | Grano entrada | 1000 kg/h | 0.89 m³/h | 100% | Materia prima base |
| **1** | Agua extracción | 12000 kg/h | 12.0 m³/h | 0% | Relación 1:12 |
| **1** | Lodo alcalino | 13000 kg/h | 13.0 m³/h | 7.7% | Tiempo res. 45-60 min |
| **1.2** | Extracto proteico | 12400 kg/h | 12.4 m³/h | 2.6% | ~340 kg proteína/h |
| **1.2** | Okara residuo | 600 kg/h | 0.6 m³/h | 40% | Subproducto alimento |
| **2** | Extracto neutralizado | 12500 kg/h | 12.5 m³/h | 2.5% | Post-neutralización |
| **2.2** | Extracto pasteurizado | 12500 kg/h | 12.5 m³/h | 2.5% | Seguridad microbiológica |
| **3** | Concentrado 20% | 6200 kg/h | 6.2 m³/h | 20% | Entrada evaporador |
| **3** | Concentrado 23% | 5400 kg/h | 5.4 m³/h | 23% | Salida evaporador |
| **3** | Vapor evap. | 6100 kg/h | 7.7 m³/h | - | Agua condensada |
| **4** | Lodo precipitado | 5430 kg/h | 5.43 m³/h | 21% | pH 4.5 |
| **4.2** | Pasta proteica húmeda | 1700 kg/h | 1.7 m³/h | 50% | 850 kg proteína/h (~314 kg prot/h reco) |
| **4.2** | Suero residual | 3730 kg/h | 3.73 m³/h | 3% | Residuo bajo proteína |
| **5** | Entrada spray dryer | 1700 kg/h | 1.7 m³/h | 50% | Pasta concentrada |
| **5** | Polvo final (5% H₂O) | 920 kg/h | 1.38 m³/h | 95% | Producto comercial |
| **5** | Aire exhaust | 11500 kg/h | 20 m³/h | - | Aire húmedo outlet |
| **6** | Polvo envasado | 920 kg/h | 1.38 m³/h | 95% | 36-46 bolsas/h |

---

## 5. PUNTOS CRÍTICOS DE CONTROL Y MEDICIÓN

### Instrumentación Recomendada

| Ubicación | Parámetro | Instrumento | Rango | Acción Correctiva |
|-----------|-----------|-------------|-------|------------------|
| **Tanque lixiviación** | pH | Sonda pH digital + transmisor | 6-10 | Ajustar NaOH si <8.5 o >9.0 |
| **Tanque lixiviación** | Temperatura | PT100 clase A + indicador | 0-100°C | Mantener 50-60°C ± 2°C |
| **Post-filtración** | Turbidez/claridad | Turbidímetro | 0-100 NTU | Rechazar si >20 NTU |
| **Intercambiador entrada** | Temperatura | Termocupla tipo K | -50 a 150°C | Monitoreo contínuo |
| **Intercambiador salida** | Temperatura | Termocupla tipo K | -50 a 150°C | Asegurar 75-85°C |
| **Evaporador** | Presión vacío | Vacuómetro digital | 0-1 bar abs | Mantener 0.3-0.5 bar |
| **Evaporador** | % Sólidos | Refractómetro en línea | 0-30 Brix | Controlar entrada/salida |
| **Precipitación** | pH | Sonda pH | 3-6 | Mantener 4.5 ± 0.2 |
| **Spray dryer Inlet** | Temperatura aire | Termopar K | 100-250°C | Mantener 180-200°C |
| **Spray dryer Outlet** | Temperatura aire | Termopar K | 50-150°C | Verificar 80-90°C |
| **Producto final** | Humedad | Medidor Karl Fischer | 0-10% | Rechazar si >5% |
| **Producto final** | Proteína | Analizador NIR | 85-95% | Asegurar ≥88% |

---

## 6. BALANCE DE AGUA Y ENERGÍA ESTIMADO

### Balance Hídrico (para 1 ton/h grano soya)

```
ENTRADA:
- Agua extracción: 12,000 kg/h
- Agua neutralización (dilución): ~100 kg/h
- Agua servicios (enjuagues): ~500 kg/h
TOTAL ENTRADA AGUA: 12,600 kg/h

SALIDA:
- Vapor evaporación: 6,200 kg/h ✓
- Okara húmedo (70% H₂O): 420 kg/h
- Agua en pasta centrifugación: 850 kg/h
- Agua en polvo final (5%): 49 kg/h
- Pérdidas en suero: ~1,500 kg/h
- Agua residual/purgas: ~581 kg/h
TOTAL SALIDA AGUA: 9,600 kg/h

DIFERENCIA: 3,000 kg/h (agua de cristalización + no contabilizada = margen de error)
```

### Balance Energético Aproximado (para 1 ton/h grano soya)

```
ETAPA 2 (Pasteurización):
- Energía para calentar extracto 25°C → 75°C: 
  Q = m·Cp·ΔT = 12,500 kg/h × 3.8 kJ/kg·K × 50 K = 2,375 MJ/h = 659 kW
- Energía para enfriar posterior: ~-659 kW (recuperable)
- Neto si hay recuperación: ~330 kW (50% eficiencia)

ETAPA 3 (Evaporación):
- Energía latente evaporación: 6,200 kg vapor/h × 2,360 kJ/kg = 14,632 MJ/h = 4,064 kW
- Con eficiencia típica 50-55%: consumo vapor ≈ 7,000-7,500 kW
- (Equivalente a 1.8-2.2 kg vapor saturado por kg agua evaporada)

ETAPA 5 (Spray dryer):
- Energía para calentar aire ambiente (25°C) a 180°C:
  Q = ṁ_aire × Cp × ΔT = 11,500 kg aire/h × 1.005 kJ/kg·K × 155 K = 1,794 MJ/h = 498 kW
- Energía latente evaporación: 1,700 kg entrada - 920 kg salida = 780 kg agua a remover
  E_latente = 780 × 2,450 kJ/kg (a ~75°C promedio) = 1,911 MJ/h = 531 kW
- TOTAL aprox: 1,029 kW (gases calientes recuperables parcialmente)

CONSUMO TOTAL ESTIMADO:
- Pasteurización (neta): 330 kW
- Evaporación: 7,200 kW
- Secado: 1,029 kW
TOTAL bruto: ~8,559 kW ≈ 8.6 MW
Específico: ~8.6 MJ/kg proteína final (~2.4 kWh/kg) 

(Considerando 1 ton grano → 920 kg polvo final con 90% proteína = 828 kg proteína/h)
```

---

## 7. REFERENCIAS Y CONSIDERACIONES FINALES

### Normas Aplicables
- **FDA CFR 21 Part 110:** Current Good Manufacturing Practice (CGMP) para alimentos
- **ISO 9001:2015:** Sistema de gestión de calidad
- **ISO 22000:2018:** Seguridad alimentaria
- **ASME B73.1:** Centrifugas industriales
- **TEMA (Tubular Exchanger Manufacturers Association):** Estándares intercambiadores
- **DIN 17458 / ASTM A312:** Tuberías acero inoxidable austeníteco

### Bibliografía Recomendada
- Singh, R. P., & Heldman, D. R. (2014). *Introduction to Food Engineering* (5th ed.). Elsevier.
- McCabe, W. L., Smith, J. C., & Harriott, P. (2005). *Unit Operations of Chemical Engineering* (7th ed.). McGraw-Hill.
- Toledo, R. T. (2007). *Fundamentals of Food Process Engineering* (3rd ed.). Springer.

### Consideraciones de Seguridad Críticas
1. **Personal debe estar certificado** en manejo de ácidos/bases concentrados (NaOH y HCl)
2. **Sistemas de ventilación local** en zonas de dosificación de químicos
3. **Detectores de vapor** (CO₂, O₂) en áreas de riesgo
4. **Sistema de parada de emergencia** accesible desde puntos críticos
5. **Inspecciones periódicas** de tuberías, válvulas y bridas (mensual mínimo)

---

**Documento generado para: Producción de Proteína Aislada de Soya | 1 tonelada/hora | Escala Piloto/Industrial**

**Versión:** 1.0 | Fecha: Marzo 2026

---
