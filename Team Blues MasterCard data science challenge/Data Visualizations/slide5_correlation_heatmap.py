"""
Slide 5 — Key Findings: Correlation Heatmap
Team Blues | Mastercard IGS Data Challenge 2026 | Dillard University

Chart: Seaborn correlation heatmap — economic conditions vs. healthcare
       outcomes across Orleans Parish census tracts.

Key findings:
  r =  0.82  — Personal Income → Health Insurance Coverage (strongest positive)
  r = −0.91  — Female Above Poverty → Health Insurance Tract % (strongest negative)

Source: Team Blues analysis · Mastercard IGS Dataset (Orleans Parish census tracts)
        Python (seaborn, pandas)

Dependencies: pip install pandas numpy seaborn matplotlib
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ── Correlation matrix ────────────────────────────────────────────────────────
# Values read directly from the heatmap cells on Slide 5.
# Rows/columns represent IGS sub-metrics for Orleans Parish census tracts (2025).
variables = [
    "Personal Income",
    "Economy Score",
    "Min/Women Business",
    "Small Biz Loans",
    "Health Ins. Coverage",
    "Female Above Poverty",
    "New Businesses",
    "Health Ins. Tract %",
]

corr_values = np.array([
    [ 1.00,  0.35,  0.63, -0.14,  0.82,  0.54,  0.43, -0.48],
    [ 0.35,  1.00,  0.13,  0.48, -0.00,  0.04,  0.53,  0.25],
    [ 0.63,  0.13,  1.00,  0.30,  0.28,  0.72, -0.15, -0.47],
    [-0.14,  0.48,  0.30,  1.00, -0.62, -0.07, -0.33,  0.42],
    [ 0.82, -0.00,  0.28, -0.62,  1.00,  0.52,  0.56, -0.68],
    [ 0.54,  0.04,  0.72, -0.07,  0.52,  1.00,  0.34, -0.91],
    [ 0.43,  0.53, -0.15, -0.33,  0.56,  0.34,  1.00, -0.37],
    [-0.48,  0.25, -0.47,  0.42, -0.68, -0.91, -0.37,  1.00],
])

corr_df = pd.DataFrame(corr_values, index=variables, columns=variables)

# ── Plot ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 8))
fig.patch.set_facecolor("white")

# Diverging palette: dark blue (negative) → white → dark orange/red (positive)
cmap = sns.diverging_palette(220, 20, as_cmap=True)

sns.heatmap(
    corr_df,
    annot=True,
    fmt=".2f",
    cmap=cmap,
    center=0,
    vmin=-1, vmax=1,
    linewidths=0.5,
    linecolor="white",
    annot_kws={"size": 10, "weight": "bold"},
    ax=ax,
)

ax.set_title(
    "Economic Conditions & Healthcare Outcomes — Orleans Parish\n"
    "Every Economic Variable Is Correlated With Health",
    fontsize=13, fontweight="bold", pad=14,
)
ax.tick_params(axis="x", labelsize=9, rotation=40)
ax.tick_params(axis="y", labelsize=9, rotation=0)

# Key finding callout boxes (matching slide annotations)
fig.text(
    0.915, 0.72,
    "r = 0.82\nIncome → Health\nStrongest link\nin dataset",
    fontsize=9.5, color="#1A5276", ha="center", va="center",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#D6EAF8", edgecolor="#2980B9", alpha=0.9),
)
fig.text(
    0.915, 0.40,
    "r = −0.91\nPoverty → No Coverage\nStrongest suppressor\nof health access",
    fontsize=9.5, color="#7B241C", ha="center", va="center",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#FADBD8", edgecolor="#C0392B", alpha=0.9),
)

plt.tight_layout(rect=[0, 0, 0.87, 1])
plt.savefig("slide5_correlation_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved → slide5_correlation_heatmap.png")
