import sys
from prody import *
import numpy as np

prody.LOGGER._setverbosity('none')

def calculate_top_differences(pdb_id):
    structure = parsePDB(pdb_id)
    
    gnm, gnm_atoms = calcGNM(structure)
    anm, anm_atoms = calcANM(structure)
    
    gnm_fluctuations = calcSqFlucts(gnm)
    anm_fluctuations = calcSqFlucts(anm)
    
    gnm_norm = gnm_fluctuations / np.max(gnm_fluctuations)
    anm_norm = anm_fluctuations / np.max(anm_fluctuations)
    
    abs_diff = np.abs(gnm_norm - anm_norm)
    
    top_indices = np.argsort(abs_diff)[-10:][::-1]  
    top_diffs = abs_diff[top_indices]
    
   
    for i, idx in enumerate(top_indices):
        residue = gnm_atoms[idx].getResname()
        resnum = gnm_atoms[idx].getResnum()
        print(f"{top_diffs[i]:.3f} {idx} {residue}{resnum}")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python fluctuation-diff-index.py <PDB ID>")
        sys.exit(1)
    
    pdb_id = sys.argv[1]
    calculate_top_differences(pdb_id)
