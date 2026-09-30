![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Channel Sinuosity Classifier
 
*For geomorphologists and hydrologists: enter channel length and valley length to instantly compute the sinuosity index and classify the channel planform.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geomorphology
 
**Inputs:**
- Total channel length (Lc): a positive float, units in km or m (user chooses units, but calculation is ratio so units cancel).
- Straight-line valley length (Lv): a positive float, same units as channel length. Must be less than or equal to channel length; validation ensures Lv <= Lc, else an error message is shown.

**Core calculation:**
Sinuosity Index (SI) = Lc / Lv.

**Classification thresholds:**
- SI < 1.05: "Straight"
- 1.05 ≤ SI < 1.5: "Sinuous"
- 1.5 ≤ SI < 2.0: "Meandering"
- SI ≥ 2.0: "Highly Meandering"

**Gradio UI layout:**
- Two number input fields side by side, labeled "Channel Length (Lc)" and "Valley Length (Lv)", with unit selectors (km / m) beside each.
- A "Calculate" button.
- Output area below: a text box showing "Sinuosity Index: X.XX (Classification)" and a small matplotlib figure. The figure shows a schematic: a horizontal dashed line (valley length) with endpoint markers, and a sine wave-like curve (channel) that is longer and wavy above it, with labels "Lv" and "Lc". The plot is purely illustrative, not to scale, and automatically adjusts the sine wave amplitude/wavelength based on the SI value (higher SI -> more waves/amplitude). Also display the classification thresholds as a small table or bullet list below the plot.
- No AI; pure calculation and classification logic.

**Output:**
- A numeric SI value rounded to two decimals.
- A classification label with colour coding: green for straight, yellow for sinuous, orange for meandering, red for highly meandering.
- The schematic plot and threshold table.

No downloadable files, but the plot can be exported via Gradio's built-in save feature.
 
## Run it
 
```bash
docker build -t channel-sinuosity-classifier .
docker run -p 7860:7860 channel-sinuosity-classifier
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-30.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
