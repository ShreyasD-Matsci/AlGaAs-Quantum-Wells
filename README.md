# AlGaAs-Quantum-Wells

Simulation of an Al₀.₇₅Ga₀.₂₅As Quantum Well structure consisting of 128 atomic layers (64 primitive unit cells) to mimic typical quantum well stacks in QWIP (Quantum Well Infrared Photodetector) devices.

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `1QW_AlGaAs_128atoms.cif` | CIF file of the full quantum well slab |
| `1QW_AlGaAs_128atoms.xyz` | Same structure in XYZ format |
| `QW_structure.py` | ASE script to generate the 128-atom quantum well stack |
| `AlGaAs_Input.in` | Quantum ESPRESSO input file for SCF calculation |
| `QWscf.out` | SCF output file (Quantum ESPRESSO) |
| `atoms_clean.txt` | Cleaned position file (manual adjustments or parsing) |
| `positions_fixed.txt` | Final atomic coordinates used in DFT calculations |

## 🧪 Simulation Details

- **Material**: Al₀.₇₅Ga₀.₂₅As
- **Structure**: Quantum well with alternating AlAs–GaAs–AlAs layers (6–4–6 unit layers)
- **Atoms**: 128 total (64 cation + 64 anion)
- **Toolchain**:
  - [ASE (Atomic Simulation Environment)](https://wiki.fysik.dtu.dk/ase/)
  - [Quantum ESPRESSO](https://www.quantum-espresso.org/)
- **Applications**: Designed to model electronic behavior in QWIPs and similar infrared detection structures.

## ⚙️ How to Use

1. Generate structure using `QW_structure.py` (ASE required)
2. Run DFT using `AlGaAs_Input.in` in Quantum ESPRESSO (`pw.x`)
3. Analyze band structure, DOS, or export for post-processing.
- All pseudopotentials must be manually set in QE input files.
- The structure is unrelaxed and can be used for direct SCF → bands → DOS calculations for ideal comparison studies.
