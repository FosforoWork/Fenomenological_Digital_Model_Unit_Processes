# Gemelo Digital Fenomenológico para Procesos de Biorefinería

Una arquitectura modular en Python para el diseño, simulación y validación de gemelos digitales de procesos químicos y de biorefinería. Desarrollada desde cero como proyecto de ingeniería, validada con una planta de Proteína Aislada de Soya (ISP) de 1000 kg/h.

[![Tests](https://img.shields.io/badge/tests-11%2F11-passing-brightgreen)](#)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#)
[![Monte Carlo](https://img.shields.io/badge/success-99.88%25-brightgreen)](#)

---

## Visión General

La arquitectura se organiza en tres módulos independientes y acoplados, desarrollados en Python 3.10+:

| Módulo | Función |
|---|---|
| `core/stage_equations.py` | Núcleo fenomenológico: balances de materia y energía por etapa |
| `core/equipment_constraints.py` | Motor de restricciones: evaluación de capacidad vs. demanda |
| `core/equipment_specs.py` | Configuración externalizada de equipos con validación automática |

La interfaz visual (`app.py`) integra el bucle de simulación inercial, KPIs en tiempo real y panel de alarmas FMEA. Once pruebas unitarias (`tests/`) verifican la integridad del sistema ante modificaciones.

## Arquitectura

### Configuración Externalizada y Validación en Tres Capas

Los parámetros de proceso están externalizados con validación automática:

1. **Valores nominales** — capacidades de diseño recomendadas (`EQUIPMENT_SPEC_DEFAULTS`)
2. **Límites físicos** — rangos que garantizan realizabilidad física (`EQUIPMENT_SPEC_LIMITS`)
3. **Límites operativos** — factores de seguridad antes de disparar alarmas (`CAPACITY_LIMIT_DEFAULTS`)

Las variables de control se validan contra `CONTROL_LIMITS` antes de ejecutar el modelo, asegurando que ningún valor fuera de especificación alcance el núcleo fenomenológico.

### Núcleo de Cálculo

Cada etapa del proceso se implementa como una función pura:

```python
def stage_n(controls: dict, specs: dict) -> dict:
    # balances de materia y energía
    return {"output_var": valor, ...}
```

La función `run_process_model` orquesta la ejecución secuencial y aplica el motor de restricciones. La inercia dinámica de primer orden modela la respuesta transitoria del proceso.

## Caso de Validación: Planta ISP 1000 kg/h

### Balance de Materia Base

| KPI | Valor |
|---|---:|
| Alimentación de soya | 1000 kg/h |
| Proteína extraída (Etapa 1) | 330.0 kg/h |
| Polvo proteico final | 301.6 kg/h (286.5 kg/h proteína) |
| Rendimiento global de proteína | 76.40% |
| Humedad residual | 5.0% |
| Cierre de masa | error < 0.5% |

### Diagnóstico Estocástico

Se ejecutó Monte Carlo sobre el diseño base y sobre la configuración optimizada:

| Métrica | Diseño Base | Diseño Optimizado |
|---|---:|---:|
| Tasa de éxito | 4.70% ± 0.18% | **99.88% ± 0.026%** |
| Nivel sigma (bruto) | — | 3.03σ |
| Nivel sigma (con shift 1.5) | — | **4.53σ** |
| DPMO equivalente | — | ~340 |

Los cuellos de botella identificados en el diseño base (TK-101: 78.2%, TK-100: 69.5%, EV-301: 57.1%, HX-201: 40.7%) fueron eliminados mediante redimensionamiento, dejando solo una falla residual en TK-101 (0.12%) en condiciones extremas de residencia > 100 min.

### Análisis Energético

La integración de ósmosis inversa (OI) como preconcentración logra:

- Agua removida por OI: 2,718 kg/h (fase líquida, 8.5 kW eléctricos)
- Reducción de carga térmica del evaporador: 836 kW (19.5%)
- Ahorro neto equivalente: 827.7 kW

## Pruebas

Once pruebas unitarias verifican la consistencia del balance de materia, la detección de cada restricción de capacidad y la validación de rangos de control. Ejecutar:

```bash
python -m unittest discover tests -v
```

## Reproducir Resultados

```bash
python scripts/run_monte_carlo.py --batches 10 --trials 300000
```

## Requisitos

- Python 3.10+
- streamlit, numpy, scipy, matplotlib, plotly
- (Ver `requirements.txt` para versión completa)

## Estructura del Repositorio

```
├── core/
│   ├── equipment_specs.py        # Configuración de equipos
│   ├── equipment_constraints.py  # Motor de restricciones
│   └── stage_equations.py        # Balances fenomenológicos
├── scripts/
│   └── run_monte_carlo.py        # Campaña de simulación estocástica
├── docs/
│   └── PaperGemeloDigital.tex    # Artículo de arquitectura
├── tests/                        # 11 pruebas unitarias
├── app.py                        # Interfaz Streamlit (sala de control)
└── README.md
```

## Referencias

Grieves & Vickers (2017), *Digital Twin: Mitigating Unpredictable Behavior*; ISO 23247:2021; IEC 63278:2023; Lusas & Riaz (1995), *Soy protein products: processing and use*.
