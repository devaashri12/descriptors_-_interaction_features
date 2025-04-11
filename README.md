# Drug-Likeness Predictor

This project uses RDKit to extract molecular descriptors from SMILES strings. The output is saved as an Excel file for further drug-likeness analysis or QSAR modeling.

## 🔬 Features
- Calculate MW, LogP, TPSA, HBD, HBA, and rotatable bonds
- Input: List of SMILES
- Output: `output.xlsx` with descriptors

## 🛠 Installation

1. Install [Anaconda](https://www.anaconda.com/)
2. Create environment:

```bash
conda create -n chem_rdkit python=3.7
conda activate chem_rdkit
conda install -c rdkit rdkit
pip install pandas openpyxl
