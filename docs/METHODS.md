# Methods — exploratory pilot

## Docking

- EGFR ATP-binding kinase domain from PDB [1M17](https://www.rcsb.org/structure/1M17), erlotinib ligand AQ4.
- The original research workflow used AutoDock Vina with multiple seeds and compared redocked ligand poses with the crystal pose.
- Previously reported top-pose redocking RMSDs were below 2 Å. Original logs and receptor/ligand inputs are **not yet published in this repository**, so these reported values should not be treated as independently revalidated from the files here.

## MD

- Amber-family protein parameterization; GAFF2/AM1-BCC ligand, TIP3P water and approximately 0.15 M salt.
- Approximately 10.48–10.49 nm cubic periodic box and NVT/NPT equilibration.
- Both systems completed a 1 ns unrestrained MD segment using a CUDA-enabled GROMACS-RAMD development build on GTX 960M.
- Analysis: protein Cα RMSD, protein-aligned ligand heavy-atom RMSD, nearest protein–ligand atom distance and counts of atomic pairs within 0.4 nm.
- The WT **additional** MD segment was stopped early; it is excluded from matched comparisons.

## RAMD

- GROMACS-RAMD development build around commit `9d0336d`, time step `0.002 ps`.
- RAMD input states were generated from the completed 1 ns MD checkpoint through `gmx grompp -t`. Starting standard-MD checkpoints must **not** be passed as `mdrun -cpi` after switching to RAMD.
- One seed (`42`) per listed condition; tested forces: 300, 400, 600 kJ mol⁻¹ nm⁻¹.
- Algorithmic exit threshold set to 4.0 nm. The reported event time equals `(exit_step - 550000) × 0.002 ps`.
- WT/F300 at 400 ps is a **right-censored** no-event trajectory.
- Final contacts were checked with periodic-boundary-aware `gmx mindist`; a final checkpoint was additionally inspected for T790M/F300.

## Reproducibility boundary

The published pilot summary permits **reanalysis and transparent interpretation of the event table** but not atomistic rerunning of simulations from scratch. To make all simulations fully reproducible, deposit original topology and included ITP force-field files, input coordinate and seed files, MDP settings, exact software revision and the raw run logs/trajectories in a suitable large-data archive.
