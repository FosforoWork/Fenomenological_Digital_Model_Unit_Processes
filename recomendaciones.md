# Recomendaciones para el Desarrollo del Gemelo Digital (AJAX V1)
**Quédate en Streamlit, pero exige a Jules que use componentes avanzados.**

Tu proyecto es un **gemelo digital de proceso**, no una app de consumo masivo. Streamlit con componentes correctos puede verse 80% profesional con 20% del esfuerzo de una reingeniería.

### **Plan de Sesiones para Jules (Streamlit Potenciado)**

#### **Sesión 1: Estilo Profesional + Layout Power BI**
**Instrucción para Jules:**
> "Usando Streamlit + CSS custom injection + `st.columns` + `st.metric`, replica el layout de las capturas. Paleta: fondo #0f172a, superficies #1e293b, texto #f8fafc, acentos #38bdf8. Tipografía: Inter para textos, JetBrains Mono para números. Crea un tema dark mode consistente en todo el app. NO usar widgets genéricos de Streamlit sin estilar."

**Entregable:** Dashboard con header, grid de KPIs tipo tarjeta, y secciones colapsables por etapa.

#### **Sesión 2: Variables de Control Interactivas + Semáforos**
**Instrucción:**
> "Reemplaza los sliders genéricos de Streamlit por controles custom usando `st.number_input` + barras de progreso CSS que representen rangos documentales (rojo/amarillo/verde). Implementar `st.session_state` para que los cambios en inputs persistan entre interacciones. Agregar indicadores de estado (semáforo) que calculen desviación vs. setpoint usando desviación estándar (1σ, 2σ)."

**Entregable:** Panel de control funcional con validación visual en tiempo real.

#### **Sesión 3: Sparklines + Tendencias**
**Instrucción:**
> "Integrar Plotly para micro-gráficas (sparklines) debajo de cada KPI principal. Simular datos históricos de 60 segundos usando listas en `st.session_state`. En modo exploratorio, mostrar dos líneas: valor actual (sólida) y predicción del modelo (punteada)."

**Entregable:** KPIs con contexto de tendencia, modo comparativo activo.

#### **Sesión 4: Fluidograma + Cálculo de Proceso**
**Instrucción:**
> "Crear representación del fluidograma usando Plotly Sankey o SVG inline con `st.image`/`st.markdown`. Que los grosores de flechas cambien según caudales calculados. Implementar inercia térmica: cuando el usuario cambia temperatura, el valor real se aproxima al setpoint con curva de primer orden (usar `st.session_state` para simular el tiempo)."

**Entregable:** Visualización de proceso dinámica, cálculos con dinámica realista.

---

## 4. Cómo Evitar que Jules se Desvíe (Prompt Específico para Streamlit)

> **Contexto:** Trabajamos en Streamlit puro. Python es el único lenguaje. No hay HTML/CSS/JS separado (salvo CSS injection dentro de Streamlit). No hay backend aparte. No hay FastAPI. No hay servidores.
>
> **Reglas:**
> 1. Todo el código debe ser ejecutable con `streamlit run app.py`.
> 2. Si necesitas estilos, usa `st.markdown(..., unsafe_allow_html=True)` con CSS inline.
> 3. Si necesitas gráficas interactivas, usa Plotly o Altair (integrados en Streamlit).
> 4. Si necesitas layout complejo, usa `st.columns`, `st.tabs`, `st.container` o `streamlit-elements`.
> 5. La lógica de proceso se ejecuta en Python nativo dentro del script. Cero APIs externas.
>
> **Objetivo de esta sesión:** [Especificar]