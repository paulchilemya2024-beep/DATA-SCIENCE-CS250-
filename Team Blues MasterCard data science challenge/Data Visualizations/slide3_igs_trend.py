"""
Slide 3 — CT 22071-003308 Has Never Once Crossed the 45-Point Threshold
Team Blues | Mastercard IGS Data Challenge 2026 | Dillard University

Chart: Line chart of IGS scores (2017–2025) vs. 45-point threshold
Source: Mastercard IGS Platform (CT 22071-003308, 2017–2025) · Urban-Rural Benchmark

Dependencies: pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ── Data ──────────────────────────────────────────────────────────────────────
# IGS scores from the Mastercard IGS Platform (CT 22071-003308)
igs_df = pd.DataFrame({
    "Year": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "IGS":  [38.5, 38.9, 34.0, 40.5, 42.0, 44.8, 31.5, 33.8, 32.0],
})

THRESHOLD = 45      # Mastercard benchmark for inclusive growth

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor("white")

# 45-point threshold (flat red line)
ax.plot(
    igs_df["Year"], [THRESHOLD] * len(igs_df),
    color="#C0392B", linewidth=2.5,
    marker="o", markersize=8, markerfacecolor="#C0392B",
    label="45-Point Threshold", zorder=3,
)

# Tract IGS trend (blue line)
ax.plot(
    igs_df["Year"], igs_df["IGS"],
    color="#2980B9", linewidth=2.5,
    marker="o", markersize=8, markerfacecolor="#2980B9",
    label="CT 22071-003308 IGS", zorder=4,
)

# Shade the gap between the tract score and threshold
ax.fill_between(
    igs_df["Year"], igs_df["IGS"], THRESHOLD,
    where=(igs_df["IGS"] < THRESHOLD),
    alpha=0.08, color="#C0392B",
)

# Italic annotation matching slide
ax.text(2017.1, 51.5, "And Is Getting Worse",
        fontstyle="italic", fontsize=12, color="#C0392B")

# ── Axes & styling ────────────────────────────────────────────────────────────
ax.set_xlim(2016.5, 2025.5)
ax.set_ylim(20, 55)
ax.set_xticks(igs_df["Year"])
ax.set_xticklabels(igs_df["Year"].astype(str), fontsize=11)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.tick_params(axis="y", labelsize=11)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.35, color="gray")

ax.set_title(
    "CT 22071-003308 Has Never Once Crossed the 45-Point Threshold",
    fontsize=14, fontweight="bold", pad=14,
)
ax.set_ylabel("IGS Score (0–100)", fontsize=12)
ax.legend(loc="lower left", fontsize=11, framealpha=0.9)

# Key callout annotations
ax.annotate(
    "Lowest IGS Ever: 31.5 (2023)",
    xy=(2023, 31.5), xytext=(2020.5, 27.5),
    fontsize=9, color="#1A252F",
    arrowprops=dict(arrowstyle="->", color="#555", lw=1),
)
ax.annotate(
    "IGS 32 — 2025 Score (below threshold)",
    xy=(2025, 32.0), xytext=(2022.5, 24.5),
    fontsize=9, color="#1A252F",
    arrowprops=dict(arrowstyle="->", color="#555", lw=1),
)

plt.tight_layout()
plt.savefig("slide3_igs_trend.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved → slide3_igs_trend.png")
