# Interpretation and limitations

1. **Force-assisted exit is not equilibrium kinetics.** Do not compute experimental `koff = 1/13 ps` or infer residence-time ratios from this pilot.
2. **One trajectory per condition.** The tested force sweep has seed 42 in each condition. It provides no uncertainty estimate and no statistical τRAMD comparison.
3. **Right-censored WT.** WT at 300 kJ mol⁻¹ nm⁻¹ had no algorithmic exit in its 400 ps window; 400 ps is **not** an observed WT exit time.
4. **Loss of close contacts can be temporary.** T790M/F300 lost contacts within 4 Å at roughly 219 ps, but some contacts returned before eventual exit detection.
5. **Residual proximity.** The final T790M/F300 checkpoint at 1334.302 ps showed minimum heavy-atom distance 0.9374081 nm and three atomic pairs within 1 nm. Their nearest-image shifts were all [0,0,0] at that snapshot. This is pocket departure with residual proximity, not proof of complete protein–ligand separation.
6. **PBC not globally eliminated.** A single final-frame check is not comprehensive validation against all image interactions during the entire trajectory.
7. **MD length.** One nanosecond of conventional MD is a structural pilot, not proof of convergence.
8. **Mutation context.** Single T790M vs WT does not independently model the clinical EGFR activating-mutant context or effects of ATP competition.
9. **Partial sources.** Original raw docking logs and full MD force-field provenance are not included in this minimal repository yet.
10. **Publication type.** Research software/methodological demonstration, not a peer-reviewed article.
