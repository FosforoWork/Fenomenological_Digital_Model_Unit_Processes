# PFD Integrado - Produccion de proteina aislada de soya

Este diagrama integra el tren principal del caso base (1 ton/h de grano) y el nodo de operacion innovadora de preconcentracion por osmosis inversa (OI).

## Convenciones

- Corriente continua de proceso: flecha principal.
- Descarga lateral: subproducto o servicio.
- OI: modulo innovador de preconcentracion previo a evaporacion.

## Diagrama (Mermaid)

```mermaid
flowchart TD
    %% Definición de estilos
    classDef mainProcess fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#000
    classDef innovation fill:#fff9c4,stroke:#fbc02d,stroke-width:3px,color:#000
    classDef byProduct fill:#f1f8e9,stroke:#689f38,stroke-width:1px,color:#000,stroke-dasharray: 5 5
    classDef startEnd fill:#eceff1,stroke:#607d8b,stroke-width:2px,color:#000

    %% Nodos de inicio y fin
    Start(["Alimentación Soya + Agua 1:12"]):::startEnd
    End(["Despacho y Distribución"]):::startEnd

    subgraph Fase1 ["🌿 Fase 1: Extracción y Separación"]
        direction TB
        EXT["TK-101 & AG-101<br>Extracción Alcalina"]:::mainProcess
        SEP1{{"CF-102A/B<br>Separación Post-Lixiviación"}}:::mainProcess
        OKA[("Okara Húmedo<br>Subproducto")]:::byProduct
    end

    subgraph Fase2 ["🔥 Fase 2: Tratamiento Térmico y Concentración"]
        direction TB
        PAST["HX-201<br>Neutralización y Pasteurización"]:::mainProcess
        OI{{"✨ OI-250<br>Ósmosis Inversa (Preconcentración)"}}:::innovation
        PERM[("Permeado<br>Agua Servicio/CIP")]:::byProduct
        EVAP["EV-301A/B<br>Evaporación Doble Efecto"]:::mainProcess
        COND[("Condensado<br>Recuperación")]:::byProduct
    end

    subgraph Fase3 ["⚗️ Fase 3: Purificación y Acabado"]
        direction TB
        PREC["PR-401<br>Precipitación Isoeléctrica"]:::mainProcess
        SEP2{{"CF-401<br>Centrifugación"}}:::mainProcess
        SUERO[("Suero Residual<br>Efluentes")]:::byProduct
        SEC["SD-501<br>Secado por Atomización"]:::mainProcess
        MOL["ML-601 & CR-601<br>Molienda y Tamizado"]:::mainProcess
        ENV[["ENV-701<br>Envasado Final"]]:::mainProcess
    end

    %% Conexiones
    Start --> EXT
    EXT --> SEP1
    SEP1 -- Fase Líquida --> PAST
    SEP1 -.-> OKA
    
    PAST --> OI
    OI == Retentado ==> EVAP
    OI -. Permeado .-> PERM
    EVAP --> PREC
    EVAP -. Condensado .-> COND
    
    PREC --> SEP2
    SEP2 -- Proteína --> SEC
    SEP2 -. Suero .-> SUERO
    
    SEC --> MOL
    MOL --> ENV
    ENV --> End
```

## Resumen de corrientes principales

1. Proceso principal: extraccion -> separacion -> pasteurizacion -> OI -> evaporacion -> precipitacion -> centrifugacion -> secado -> molienda/tamizado -> envasado.
2. Corrientes laterales: okara, permeado OI, condensado de evaporador y suero residual.
3. Punto de control clave de innovacion: modulo OI para aliviar carga termica de EV-301A/B.
