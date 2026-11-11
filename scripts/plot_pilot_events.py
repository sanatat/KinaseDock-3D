#!/usr/bin/env python3
"""Plot observed RAMD force-assisted exit times from a small CSV summary.

Right-censored runs are marked with a right arrow, not drawn as exit events.
This is NOT equilibrium koff, τRAMD ensemble fitting, or an atomistic rerun.
"""
from pathlib import Path
import csv

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "pilot_event_summary.csv"
OUT = ROOT / "figures" / "ramd_force_summary.png"

with CSV_PATH.open(newline="") as f:
    observations = list(csv.DictReader(f))

fig, ax = plt.subplots(figsize=(8.5, 4.7))
colors = {"WT": "#305b99", "T790M": "#bf651f"}
for system in ("WT", "T790M"):
    rows = [r for r in observations if r["system"] == system]
    for row in rows:
        force, duration = float(row["force_kJ_mol_nm"]), float(row["time_ps"])
        censored = row["status"] == "right_censored"
        ax.scatter(force, duration, s=95, marker=">" if censored else "o",
                   color=colors[system], zorder=3)
        ax.annotate(("≥" if censored else "") + f"{duration:g} ps",
                    (force, duration), xytext=(6, 5), textcoords="offset points",
                    fontsize=9)
    ax.plot([], [], "o", color=colors[system], label=system)

ax.set(xlabel="Applied RAMD force (kJ mol⁻¹ nm⁻¹)",
       ylabel="Observed exit or censoring time (ps)",
       title="Exploratory EGFR–erlotinib RAMD force sweep (seed 42)")
ax.grid(alpha=0.25)
ax.legend()
fig.tight_layout()
OUT.parent.mkdir(exist_ok=True, parents=True)
fig.savefig(OUT, dpi=180)
print(f"Saved {OUT}")
