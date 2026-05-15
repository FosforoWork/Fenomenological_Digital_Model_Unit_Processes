import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

css_new = '''@st.cache_data
def get_visual_theme_css(mode: str) -> str:
    bg_deep = "#0a0a0c"
    bg_surface = "#111216"
    text_main = "#d4d4d8"
    text_muted = "#71717a"
    accent = "#00f0ff"
    border = "#27272a"
    glow = "rgba(0, 240, 255, 0.2)"

    return f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=JetBrains+Mono:wght@400;600;700&display=swap');

            :root {{
                --bg-deep: {bg_deep};
                --bg-surface: {bg_surface};
                --text-main: {text_main};
                --text-muted: {text_muted};
                --accent: {accent};
                --border: {border};
                --glow: {glow};
                --font-sans: 'Inter', sans-serif;
                --font-mono: 'JetBrains Mono', monospace;
            }}

            /* Base App Styling */
            .stApp {{
                background-color: var(--bg-deep);
                color: var(--text-main);
                font-family: var(--font-sans);
            }}

            [data-testid="stSidebar"] {{
                background-color: var(--bg-surface);
                border-right: 1px solid var(--border);
            }}

            /* Typography */
            h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {{
                font-family: var(--font-sans) !important;
                color: var(--text-main) !important;
            }}

            div[data-testid="stMetricValue"] > div {{
                font-family: var(--font-mono) !important;
                font-weight: 700 !important;
                color: var(--accent) !important;
                text-shadow: 0 0 8px var(--glow);
            }}

            /* Custom Cards for KPIs */
            div[data-testid="stMetric"] {{
                background-color: var(--bg-surface);
                border: 1px solid var(--border);
                border-radius: 4px;
                padding: 1rem !important;
                transition: border-color 0.15s ease, box-shadow 0.15s ease;
            }}

            .kpi-meta {{
                font-family: var(--font-mono) !important;
                font-size: 0.75rem;
                color: var(--text-muted);
                margin-top: 4px;
                text-transform: uppercase;
            }}

            .kpi-status {{
                font-family: var(--font-mono) !important;
                font-size: 0.75rem;
                font-weight: 600;
                margin-top: 4px;
                padding: 2px 6px;
                border-radius: 2px;
                display: inline-block;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}

            .kpi-stable {{
                background-color: rgba(57, 255, 20, 0.1);
                color: #39ff14;
                border: 1px solid rgba(57, 255, 20, 0.3);
            }}

            .kpi-unstable {{
                background-color: rgba(255, 0, 60, 0.1);
                color: #ff003c;
                border: 1px solid rgba(255, 0, 60, 0.3);
            }}

            div[data-testid="stMetric"]:hover {{
                border-color: var(--accent);
                box-shadow: 0 0 12px var(--glow), inset 0 0 8px var(--glow);
            }}

            /* Buttons */
            .stButton > button {{
                width: 100%;
                background-color: var(--bg-deep);
                color: var(--accent);
                border: 1px solid var(--border);
                border-radius: 4px;
                padding: 0.5rem 1rem;
                font-family: var(--font-mono);
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                transition: all 0.15s ease;
            }}

            .stButton > button:hover {{
                border-color: var(--accent);
                background-color: rgba(0, 240, 255, 0.05);
                box-shadow: 0 0 8px var(--glow);
            }}

            .stButton > button:active {{
                transform: scale(0.98);
            }}

            /* Inputs and Sliders */
            div[data-baseweb="input"], div[data-baseweb="select"], div[data-baseweb="textarea"] {{
                background-color: var(--bg-deep) !important;
                border-radius: 2px !important;
                border: 1px solid var(--border) !important;
                transition: border-color 0.15s ease, box-shadow 0.15s ease;
            }}
            
            div[data-baseweb="input"]:focus-within {{
                border-color: var(--accent) !important;
                box-shadow: 0 0 8px var(--glow) !important;
            }}

            div[data-baseweb="input"] input {{
                color: var(--accent) !important;
                font-family: var(--font-mono) !important;
            }}

            div[role="slider"] {{
                background-color: var(--accent) !important;
                box-shadow: 0 0 6px var(--glow) !important;
            }}

            div[data-testid="stExpander"] {{
                background-color: var(--bg-surface) !important;
                border: 1px solid var(--border) !important;
                border-radius: 4px !important;
                margin-bottom: 1rem !important;
            }}

            div[data-testid="stExpander"] summary:hover {{
                color: var(--accent) !important;
            }}
            
            div[data-testid="stExpander"] summary {{
                font-family: var(--font-mono) !important;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}

            div[data-testid="stDataFrame"] {{
                background-color: var(--bg-surface) !important;
                border: 1px solid var(--border) !important;
                border-radius: 4px !important;
            }}

            /* Hero Panel & Chips */
            .hero-panel {{
                background: linear-gradient(135deg, var(--bg-surface) 0%, var(--bg-deep) 100%);
                border: 1px solid var(--border);
                border-left: 2px solid var(--accent);
                border-radius: 4px;
                padding: 1.5rem;
                margin-bottom: 2rem;
                box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
            }}

            .note-chip {{
                background-color: rgba(0, 240, 255, 0.05);
                border: 1px solid rgba(0, 240, 255, 0.2);
                color: var(--accent);
                border-radius: 2px;
                padding: 0.75rem 1rem;
                margin-bottom: 1.5rem;
                font-size: 0.85rem;
                font-family: var(--font-mono);
            }}

            /* Tabs Custom Styling */
            div[data-baseweb="tab-list"] {{
                background-color: transparent !important;
                gap: 0.5rem !important;
            }}

            div[data-baseweb="tab"] {{
                background-color: var(--bg-deep) !important;
                border: 1px solid var(--border) !important;
                border-bottom: none !important;
                border-radius: 4px 4px 0 0 !important;
                color: var(--text-muted) !important;
                padding: 0.5rem 1rem !important;
                font-family: var(--font-mono) !important;
                text-transform: uppercase;
                font-size: 0.8rem !important;
            }}

            div[data-baseweb="tab"][aria-selected="true"] {{
                border-color: var(--accent) !important;
                color: var(--accent) !important;
                background-color: var(--bg-surface) !important;
                box-shadow: inset 0 4px 0 var(--accent);
            }}

            /* Scrollbar */
            ::-webkit-scrollbar {{
                width: 6px;
                height: 6px;
            }}
            ::-webkit-scrollbar-track {{
                background: var(--bg-deep);
            }}
            ::-webkit-scrollbar-thumb {{
                background: var(--border);
                border-radius: 0;
            }}
            ::-webkit-scrollbar-thumb:hover {{
                background: var(--accent);
            }}

            /* Animations - disabled for faster updates */
            .stMarkdown, .stButton {{
                animation: none !important;
            }}

            div[data-testid="stMetric"] {{
                animation: none !important;
            }}

            /* Status Indicators */
            .status-pill {{
                width: 8px;
                height: 8px;
                border-radius: 50%;
                display: inline-block;
                margin-right: 8px;
            }}
            .status-running {{ background-color: #39ff14; box-shadow: 0 0 8px #39ff14; }}
            .status-paused {{ background-color: #ff003c; box-shadow: 0 0 8px #ff003c; }}

        </style>
"""'''

# Replace the specific block of get_visual_theme_css
content = re.sub(
    r'@st\.cache_data\s+def get_visual_theme_css\(mode: str\) -> str:.*?(?=def apply_visual_theme_css)', 
    css_new + '\n\n', 
    content, 
    flags=re.DOTALL
)

# Remove _render_range_bar definition
content = re.sub(
    r'def _render_range_bar\(key: str, vmin: float, vmax: float, current_val: float\):.*?st\.markdown\(html, unsafe_allow_html=True\)\n*',
    '',
    content,
    flags=re.DOTALL
)

# Remove calls to _render_range_bar (handling optional indentation)
content = re.sub(
    r'^[ \t]*_render_range_bar\(.*?\)\n*',
    '',
    content,
    flags=re.MULTILINE
)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
