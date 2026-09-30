import gradio as gr
from channel_sinuosity_classifier import classify_sinuosity, generate_plot

def process_input(lc, lv, unit_lc, unit_lv):
    try:
        lc = float(lc)
        lv = float(lv)
    except (TypeError, ValueError):
        return "Invalid input: please enter numeric values.", None
    if lc <= 0 or lv <= 0:
        return "Both lengths must be positive.", None
    if lv > lc:
        return "Valley length (Lv) must be less than or equal to channel length (Lc).", None

    si, classification, color = classify_sinuosity(lc, lv)
    result_text = f"Sinuosity Index: {si:.2f} ({classification})"
    # color code text via HTML
    color_map = {"Straight": "green", "Sinuous": "goldenrod", "Meandering": "orange", "Highly Meandering": "red"}
    hex_color = color_map.get(classification, "black")
    colored_text = f'<span style="color:{hex_color}; font-weight:bold;">{result_text}</span>'

    fig = generate_plot(si, lv, lc)
    thresholds_md = """
**Classification Thresholds:**
- SI < 1.05 → Straight (green)
- 1.05 ≤ SI < 1.5 → Sinuous (goldenrod)
- 1.5 ≤ SI < 2.0 → Meandering (orange)
- SI ≥ 2.0 → Highly Meandering (red)
"""
    return colored_text, fig, thresholds_md

with gr.Blocks(title="Channel Sinuosity Classifier") as demo:
    gr.Markdown("# Channel Sinuosity Classifier")
    with gr.Row():
        with gr.Column():
            lc_input = gr.Number(label="Channel Length (Lc)", value=10.0, minimum=0.001)
            lc_unit = gr.Dropdown(choices=["km", "m"], value="km", label="Unit (Lc)")
        with gr.Column():
            lv_input = gr.Number(label="Valley Length (Lv)", value=8.0, minimum=0.001)
            lv_unit = gr.Dropdown(choices=["km", "m"], value="km", label="Unit (Lv)")
    calc_btn = gr.Button("Calculate")
    result_html = gr.HTML()
    plot_output = gr.Plot()
    threshold_md = gr.Markdown()

    calc_btn.click(
        fn=process_input,
        inputs=[lc_input, lv_input, lc_unit, lv_unit],
        outputs=[result_html, plot_output, threshold_md]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
