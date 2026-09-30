import matplotlib.pyplot as plt
import numpy as np

def classify_sinuosity(lc, lv):
    """
    Returns (si, classification, color_hex).
    """
    si = lc / lv
    if si < 1.05:
        return si, "Straight", "#008000"
    elif si < 1.5:
        return si, "Sinuous", "#DAA520"
    elif si < 2.0:
        return si, "Meandering", "#FFA500"
    else:
        return si, "Highly Meandering", "#FF0000"

def generate_plot(si, lv, lc, figsize=(6, 4)):
    """
    Create a schematic matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Valley line (straight)
    x_valley = np.array([0, lv])
    y_valley = np.array([0, 0])
    ax.plot(x_valley, y_valley, 'k--', linewidth=2, label="Valley (Lv)")
    ax.plot(x_valley, y_valley, 'ko', markersize=8)  # endpoints

    # Channel sine wave (schematic)
    # Determine number of cycles and amplitude based on SI
    if si < 1.05:
        freq = 0.5
        amplitude = 0.02 * lv
    else:
        # More waves & higher amplitude for higher SI
        freq = 1.5 + (si - 1.0) * 3
        amplitude = 0.05 * lv + 0.02 * lv * (si - 1.0)
    # Ensure amplitude doesn't make sine cross valley line too much (just illustrative)
    # Generate x points from 0 to lv
    x_channel = np.linspace(0, lv, 500)
    # Phase shift to start and end on valley line (y=0)
    y_channel = amplitude * np.sin(2 * np.pi * freq * x_channel / lv)
    # Adjust to ensure endpoints at y=0 (already true because sin(0)=0 and sin(2πf)=0 if f integer multiples of 1/2? Actually need 2πf*n = multiple of π, so choose frequency as integer multiple of 0.5). We'll just enforce manually.
    y_channel[0] = 0
    y_channel[-1] = 0
    ax.plot(x_channel, y_channel, 'b-', linewidth=2, label="Channel (Lc)")

    # Annotations
    ax.text(lv/2, -amplitude*1.5, r"$L_v = $" + f"{lv}", ha='center', va='top', fontsize=10)
    # Approximate Lc label at a high point
    mid_idx = len(x_channel)//2
    ax.text(x_channel[mid_idx], y_channel[mid_idx] + amplitude*0.5, r"$L_c = $" + f"{lc}", ha='center', fontsize=10)

    # Aesthetics
    ax.set_xlim(-0.1*lv, lv*1.1)
    ax.set_ylim(-amplitude*2, amplitude*2)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f"Sinuosity Index = {si:.2f}", fontsize=12)
    ax.legend(loc='upper right')
    ax.axis('off')
    plt.tight_layout()
    return fig
