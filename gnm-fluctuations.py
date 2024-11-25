import sys
from prody import *
import numpy as np

def calculate_max_gnm_fluctuation(pdb_id):
    
    prody.LOGGER._setverbosity('none')
    
    
    structure = parsePDB(pdb_id)
    
    
    gnm, atoms = calcGNM(structure)
    
    
    sq_fluctuations = calcSqFlucts(gnm)
    
    
    max_fluctuation = max(sq_fluctuations)
    
    
    print(f"max gnm sqfluct: {max_fluctuation:.3f}")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python gnm-fluctuations.py <PDB ID>")
        sys.exit(1)
        
    pdb_id = sys.argv[1]
    calculate_max_gnm_fluctuation(pdb_id)
