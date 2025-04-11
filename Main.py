from rdkit import Chem
from rdkit.Chem import Descriptors
import pandas as pd

# List of SMILES (you can also read from a file)
smiles_list = [
    "CC1=C2COC(=O)C2=C(C(=C1OC)CC=C(C)C3=CC=CC=C3C(=O)O)O",
    "CC1=C2COC(=O)C2=C(C(=C1OC)CC=C3CCCC[C@H]3CC(=O)O)O",
    "CC1=C2COC(=O)C2=C(C(=C1OC)CC=C(C)CC(C)(C#N)P(=O)(O)O)O",
    "CC1=C2COC(=O)C2=C(C(=C1OC)CC=C3CCCCC3[C@H](C)C(=O)O)O",
    "CC1=C2COC(=O)C2=C(C(=C1OC)C/C=C(\\C)/CC(C)(C#N)P(=O)(O)O)O",
    "CCOC(=O)C(C)(C)C(C(=CCC1C2=C(C(=CC(=C2C)OC)O)C(=O)O1)C)O"
]

# Data storage
data = []

# Extract molecular descriptors
for smi in smiles_list:
    mol = Chem.MolFromSmiles(smi)
    if mol:
        data.append({
            "SMILES": smi,
            "MW": Descriptors.MolWt(mol),
            "LogP": Descriptors.MolLogP(mol),
            "HBD": Descriptors.NumHDonors(mol),
            "HBA": Descriptors.NumHAcceptors(mol),
            "TPSA": Descriptors.TPSA(mol),
            "RotBonds": Descriptors.NumRotatableBonds(mol)
        })

# Save as DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("output.xlsx", index=False)

print("✅ Data extraction complete. Check 'output.xlsx'")
