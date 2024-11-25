import sys
from prody import *
import numpy as np

def calculate_gnm_fluctuation(pdb_id):
    prody.LOGGER._setverbosity('none')
    structure = parsePDB(pdb_id)
    gnm, _ = calcGNM(structure)
    sq_fluctuations = calcSqFlucts(gnm)
    return sq_fluctuations

def calculate_anm_fluctuation(pdb_id):
    prody.LOGGER._setverbosity('none')
    structure = parsePDB(pdb_id)
    anm, _ = calcANM(structure)
    sq_fluctuations = calcSqFlucts(anm)
    return sq_fluctuations

def main():
    if len(sys.argv) != 2:
        print("Usage: python fluctuation-diff.py <PDB ID>")
        sys.exit(1)

    pdb_id = sys.argv[1]
    
    
    gnm_fluctuations = calculate_gnm_fluctuation(pdb_id)
    anm_fluctuations = calculate_anm_fluctuation(pdb_id)

    
    abs_diff = np.abs(gnm_fluctuations - anm_fluctuations)
    max_abs_diff = np.max(abs_diff)

    
    gnm_norm = gnm_fluctuations / np.max(gnm_fluctuations)
    anm_norm = anm_fluctuations / np.max(anm_fluctuations)
    
    abs_norm_diff = np.abs(gnm_norm - anm_norm)
    max_abs_norm_diff = np.max(abs_norm_diff)


    print(f"Max Abs Difference: {max_abs_diff:.3f}")
    print(f"Max Abs Norm Difference: {max_abs_norm_diff:.3f}")

if __name__ == "__main__":
    main()
