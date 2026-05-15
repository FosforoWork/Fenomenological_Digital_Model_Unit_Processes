import re

def patch_app_py():
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace VISUAL_THEMES dictionary
    unified_theme = """VISUAL_THEMES = {
    "Exploratorio": {
        "plot_template": "plotly_dark",
        "bg_start": "#121212",
        "bg_end": "#1e1e1e",
        "bg_glow": "#2d2d2d",
        "text": "#e0e0e0",
        "muted_text": "#a0a0a0",
        "accent": "#4a90e2",
        "card_bg": "rgba(30, 30, 30, 0.85)",
        "border": "#424242",
        "note_bg": "#2d2d2d",
        "note_border": "#4a90e2",
        "note_text": "#e0e0e0",
        "grid": "rgba(255, 255, 255, 0.1)",
        "stage_colors": {
            "s0": "#888888",
            "s1": "#888888",
            "s2": "#888888",
            "s3": "#888888",
            "s4": "#888888",
            "s5": "#888888",
        },
        "status": {"verde": "#4caf50", "amarillo": "#ffb300", "rojo": "#f44336"},
        "aux": ["#4a90e2", "#888888", "#4caf50"],
    },
    "Baluarte (CAT)": {
        "plot_template": "plotly_dark",
        "bg_start": "#121212",
        "bg_end": "#1e1e1e",
        "bg_glow": "#2d2d2d",
        "text": "#e0e0e0",
        "muted_text": "#a0a0a0",
        "accent": "#4a90e2",
        "card_bg": "rgba(30, 30, 30, 0.85)",
        "border": "#424242",
        "note_bg": "#2d2d2d",
        "note_border": "#4a90e2",
        "note_text": "#e0e0e0",
        "grid": "rgba(255, 255, 255, 0.1)",
        "stage_colors": {
            "s0": "#888888",
            "s1": "#888888",
            "s2": "#888888",
            "s3": "#888888",
            "s4": "#888888",
            "s5": "#888888",
        },
        "status": {"verde": "#4caf50", "amarillo": "#ffb300", "rojo": "#f44336"},
        "aux": ["#4a90e2", "#888888", "#4caf50"],
    }
}"""
    
    # Use regex to find and replace the VISUAL_THEMES dict
    # This regex attempts to match VISUAL_THEMES = { ... } up to the end of Baluarte (CAT) dict.
    content = re.sub(r'VISUAL_THEMES\s*=\s*\{.*?"Baluarte \(CAT\)":\s*\{.*?\n\}\n\}', unified_theme, content, flags=re.DOTALL)
    
    # Replace hardcoded CSS colors in app.py
    # Success (verde) -> #4caf50
    content = content.replace('#10b981', '#4caf50')
    content = content.replace('rgba(16, 185, 129,', 'rgba(76, 175, 80,')
    # Danger (rojo) -> #f44336
    content = content.replace('#ef4444', '#f44336')
    content = content.replace('rgba(239, 68, 68,', 'rgba(244, 67, 54,')
    # Accent -> #4a90e2
    content = content.replace('#38bdf8', '#4a90e2')
    content = content.replace('rgba(56, 189, 248,', 'rgba(74, 144, 226,')
    # Warning (amarillo) -> #ffb300
    content = content.replace('#f59e0b', '#ffb300')
    
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)

def patch_fluidograma():
    with open('visualizaciones/fluidograma_integrado.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new SCADA content for the colors
    scada_colors = """    text_color = "#e0e0e0"
    card_bg = "#1e1e1e"
    accent = "#4a90e2"
    danger = "#f44336"
    success = "#4caf50"

    node_palette = [
        _hex_to_rgba("#888888", 0.85), # Alimentacion
        _hex_to_rgba("#888888", 0.90), # S1
        _hex_to_rgba("#888888", 0.90), # S2
        _hex_to_rgba("#888888", 0.90), # OI
        _hex_to_rgba("#888888", 0.90), # S3
        _hex_to_rgba("#888888", 0.90), # S4
        _hex_to_rgba("#888888", 0.90), # S5
        _hex_to_rgba(success, 0.95),   # Producto
        _hex_to_rgba(danger, 0.90),    # Okara
        _hex_to_rgba(danger, 0.88),    # Evaporada
        _hex_to_rgba(danger, 0.88),    # Suero
        _hex_to_rgba(danger, 0.88),    # Agua Secado
        _hex_to_rgba(danger, 0.75),    # Mermas (Gris)
        _hex_to_rgba("#888888", 0.80), # Permeado OI
    ]"""

    # We will replace the block defining text_color to the end of node_palette
    # Find start and end
    pattern = r'    text_color = "#f8fafc".*?\]'
    content = re.sub(pattern, scada_colors, content, flags=re.DOTALL)
    
    with open('visualizaciones/fluidograma_integrado.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    patch_app_py()
    patch_fluidograma()
    print("Patch applied successfully.")
