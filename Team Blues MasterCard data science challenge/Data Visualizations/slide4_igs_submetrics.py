"""
Slide 4 — Economic Conditions Driving Healthcare Access — IGS Platform Data
Team Blues | Mastercard IGS Data Challenge 2026 | Dillard University

Chart: Two-panel figure
  Left panel  — Grouped bar chart: CT 22071-003308 actual sub-metric scores
                vs. Urban-Rural Base Benchmark (Mastercard IGS Platform, 2025)
  Right panel — Horizontal bar chart: Gap (points below benchmark) per metric

Source: Mastercard Inclusive Growth Score Platform — CT 22071-003308 (2025)
        Urban-Rural Benchmark

Dependencies: pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────────────
# All values from the Mastercard IGS Platform sub-metric scores, 2025
metrics_df = pd.DataFrame({
    "Metric": [
        "Min/Women\nBusiness",
        "Labor Market\nEngagement",
        "Personal\nIncome",
        "New\nBusinesses",
        "Internet\nAccess",
        "Female Above\nPoverty",
        "Health Insurance\nCoverage",
        "Gini\nCoefficient",
    ],
    "Tract":     [1,  9,  16, 7,  6,  23, 23, 20],   # CT 22071-003308 actual scores
    "Benchmark": [52, 68, 50, 39, 64, 79, 70, 45],   # Urban-Rural Base Benchmark
})

# Right-panel: gap data (points below benchmark, sorted as shown on slide)
gap_df = pd.DataFrame({
    "Metric": [
        "Min/Women\nBusiness",
        "Labor Market\nEngagement",
        "Personal\nIncome",
        "New\nBusinesses",
        "Internet\nAccess",
        "Female Above\nPoverty",
        "Health Insurance\nCoverage",
        "Gini\nCoefficient",
    ],
    "Gap": [51, 59, 34, 32, 58, 56, 47, 25],   # points below benchmark
})
# Sort gap chart descending by gap size (largest gap at bottom = Labor Market)
gap_df = gap_df.sort_values("Gap", ascending=True).reset_index(drop=True)

# ── Figure: two panels ────────────────────────────────────────────────────────
fig, (ax_left, ax_right) = plt.subplots(
    1, 2, figsize=(16, 7),
    gridspec_kw={"width_ratios": [1.4, 1]},
)
fig.patch.set_facecolor("white")

# ── LEFT PANEL: grouped bar chart ─────────────────────────────────────────────
x = np.arange(len(metrics_df))
w = 0.38

bars_base = ax_left.bar(x - w / 2, metrics_df["Benchmark"], width=w,
                        color="#3498DB", label="Base Benchmark", zorder=3)
bars_tract = ax_left.bar(x + w / 2, metrics_df["Tract"], width=w,
                         color="#C0392B", label="CT 22071-003308", zorder=3)

# Value labels on tract bars
for bar in bars_tract:
    h = bar.get_height()
    ax_left.text(
        bar.get_x() + bar.get_width() / 2, h + 0.8,
        str(int(h)), ha="center", va="bottom", fontsize=8.5, fontweight="bold",
    )

# Divider line between economic drivers and health metrics
divider_x = 3.5   # between "New Businesses" and "Internet Access"
ax_left.axvline(divider_x, color="#555", linewidth=1, linestyle="--", alpha=0.6)
ax_left.text(1.5, 76, "← ECONOMIC DRIVERS", ha="center", fontsize=8, color="#555")
ax_left.text(5.5, 76, "HEALTH METRICS →",   ha="center", fontsize=8, color="#555")

ax_left.set_xticks(x)
ax_left.set_xticklabels(metrics_df["Metric"], fontsize=8.5)
ax_left.set_ylabel("IGS Sub-Metric Score (0–100)", fontsize=11)
ax_left.set_ylim(0, 85)
ax_left.set_title(
    "CT 22071-003308 vs. Base Benchmark\nActual IGS Platform Sub-Metric Scores (2025)",
    fontsize=11, fontweight="bold",
)
ax_left.legend(fontsize=10, loc="upper right")
ax_left.spines[["top", "right"]].set_visible(False)
ax_left.grid(axis="y", linestyle="--", alpha=0.3)

# ── RIGHT PANEL: horizontal gap bar chart ─────────────────────────────────────
colors_gap = ["#E74C3C" if g >= 50 else "#E67E22" for g in gap_df["Gap"]]
bars_gap = ax_right.barh(gap_df["Metric"], gap_df["Gap"],
                         color=colors_gap, zorder=3)

# Gap labels
for bar, gap_val in zip(bars_gap, gap_df["Gap"]):
    ax_right.text(
        bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2,
        f"−{gap_val} pts", va="center", fontsize=9, fontweight="bold", color="#1A252F",
    )

# Highlight the worst gap (Labor Market)
worst_idx = gap_df[gap_df["Metric"].str.contains("Labor")].index[0]
ax_right.get_children()[worst_idx].set_facecolor("#922B21")  # darker red
ax_right.text(
    gap_df.loc[worst_idx, "Gap"] / 2, worst_idx,
    "Worst gap:\nLabor Market", ha="center", va="center",
    fontsize=7.5, color="white", fontweight="bold",
)

ax_right.set_xlabel("Points Below Benchmark", fontsize=11)
ax_right.set_xlim(0, 78)
ax_right.set_title("Gap vs. Benchmark\n(pts below base)", fontsize=11, fontweight="bold")
ax_right.spines[["top", "right"]].set_visible(False)
ax_right.grid(axis="x", linestyle="--", alpha=0.3)
ax_right.tick_params(axis="y", labelsize=8.5)

plt.suptitle(
    "Economic Conditions Driving Healthcare Access — IGS Platform Data\n"
    "Actual sub-metric scores from the Mastercard IGS Platform, CT 22071-003308 (2025)",
    fontsize=12, fontweight="bold", y=1.01,
)

plt.tight_layout()
plt.savefig("slide4_igs_submetrics.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved → slide4_igs_submetrics.png")
