# Data provenance

The five observations in [pilot_event_summary.csv](../data/pilot_event_summary.csv) were transcribed from the owner's Y700 GROMACS-RAMD logs and terminal QC reports shared in the research workflow.

| System | Force | Start step | Exit step | RAMD duration | Interpretation |
|:--|--:|--:|--:|--:|:--|
| WT | 600 | 550000 | 643000 | 186.0 ps | Exit event |
| T790M | 600 | 550000 | 556500 | 13.0 ps | Exit event |
| T790M | 400 | 550000 | 577200 | 54.4 ps | Exit event |
| WT | 300 | 550000 | — | ≥400.0 ps | Right-censored |
| T790M | 300 | 550000 | 667150 | 234.3 ps | Exit event |

Reported 1 ns MD results (201 frames per system):

| System | Mean Cα RMSD (Å) | Mean protein-aligned ligand RMSD (Å) | Mean atom-pair contacts <4 Å |
|:--|--:|--:|--:|
| WT | 1.539 | 1.367 | 55.985 |
| T790M | 1.468 | 1.225 | 55.463 |

Reported T790M F300 final checkpoint: 1334.302 ps, minimum heavy-atom distance 0.9374081 nm, three pairs within 1 nm, no periodic-image shift for those pairs. The three contacts involve the simulation's ILE residue index 20 and erlotinib ERL atom indices; simulation-local residue numbering must not be confused with canonical EGFR numbering.

**The numbers are researcher-reported original run outputs, not independently recomputed from trajectories within GitHub.** The raw files live in the original local Y700 workstation project and were intentionally excluded from this small-source release.
