"""
Slide 6 — Key Findings: Chronic Disease Data Analysis
Team Blues | Mastercard IGS Data Challenge 2026 | Dillard University

Chart: Grouped bar chart — Diabetes, Hypertension, and Obesity prevalence (%)
       across National, Louisiana, New Orleans Avg, and ZIP 70122 (Gentilly).

Key findings (NOHD 2024 Health Disparity Report + CDC PLACES):
  • ZIP 70122 Hypertension: 36% — above national (32.4%), LA (29.3%), and NOLA avg
  • ZIP 70127 Diabetes: 19.6% — nearly double the national rate of 9.3%
  • Both ZIPs are 80%+ Black; all 3 diseases are preventable

Source: Team Blues chronic disease analysis · CDC PLACES · NOHD 2024 Health
        Disparity Report · Python (matplotlib, pandas)

Dependencies: pip install pandas matplotlib numpy
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────────────
# Prevalence (%) from CDC PLACES and NOHD 2024 Health Disparity Report
data = pd.DataFrame({
    "Geography":    ["National", "Louisiana", "New Orleans\nAvg", "ZIP 70122\n(Gentilly)"],
    "Diabetes":     [9.3,        12.8,         13.5,               19.6],
    "Hypertension": [32.4,       29.3,         31.0,               36.0],
    "Obesity":      [34.3,       36.7,         34.0,               33.5],
})

diseases = ["Diabetes", "Hypertension", "Obesity"]
colors   = ["#3498DB", "#C0392B", "#E67E22"]   # blue, red, orange (matches slide)

# ── Plot ──────────────────────────────────────────────────────────────────────
x     = np.arange(len(data))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor("white")

for i, (disease, color) in enumerate(zip(diseases, colors)):
    bars = ax.bar(
        x + (i - 1) * width,
        data[disease],
        width=width,
        color=color,
        zorder=3,
        label=disease,
    )
    # Value label on each bar
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2, h + 0.3,
            f"{h}", ha="center", va="bottom", fontsize=8, color="#1A252F",
        )

# Annotation: highlight the 36% hypertension bar for ZIP 70122
zip_x  = len(data) - 1                          # last group index
htn_h  = data.loc[zip_x, "Hypertension"]        # 36.0
bar_cx = zip_x + 0 * width                      # center of hypertension bar (i=1 → offset 0)
ax.annotate(
    "36% — above\nevery benchmark",
    xy=(bar_cx, htn_h),
    xytext=(bar_cx + 0.55, htn_h + 2.0),
    fontsize=9.5, fontweight="bold", color="#7B241C",
    arrowprops=dict(arrowstyle="->", color="#7B241C", lw=1.3),
)

# Reference lines for national benchmarks
for disease, color, ls in [
    ("Diabetes",     "#3498DB", "--"),
    ("Hypertension", "#C0392B", "--"),
]:
    nat_val = data.loc[0, disease]
    ax.axhline(nat_val, color=color, linestyle=ls, linewidth=0.9, alpha=0.45)

# ── Axes & styling ────────────────────────────────────────────────────────────
ax.set_xticks(x)
ax.set_xticklabels(data["Geography"], fontsize=11)
ax.set_ylabel("Prevalence (%)", fontsize=12)
ax.set_ylim(0, 45)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.35)
ax.tick_params(axis="y", labelsize=11)

ax.set_title(
    "ZIP 70122 Hypertension Crisis — All Three Diseases Are Preventable\n"
    "Source: CDC PLACES · NOHD 2024 Health Disparity Report",
    fontsize=12, fontweight="bold", pad=14,
)

legend_patches = [mpatches.Patch(color=c, label=d) for c, d in zip(colors, diseases)]
ax.legend(handles=legend_patches, loc="upper left", fontsize=11)

# Footnote
fig.text(
    0.5, -0.02,
    "Note: ZIP 70122 = Gentilly, LA. ZIP 70127 diabetes rate (19.6%) nearly double the national rate (9.3%). "
    "Both ZIPs are 80%+ Black.\n"
    "Data: CDC PLACES 2023 release · NOHD 2024 Health Disparity Report · Mastercard IGS Platform",
    ha="center", fontsize=8, color="#555", style="italic",
)

plt.tight_layout()
plt.savefig("slide6_chronic_disease.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved → slide6_chronic_disease.png")
