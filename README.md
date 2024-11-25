# Protein Elastic Network Fluctuation Analysis

This project analyzes fluctuations in protein structures using **ProDy**, a Python package for protein structural dynamics analysis. It showcases the **Gaussian Network Model (GNM)** and **Anisotropic Network Model (ANM)** to predict protein motions based on their structures. The project includes scripts to calculate and compare fluctuations, normalized values, and their differences, with detailed outputs.

---

## Overview
Proteins exhibit inherent flexibility that is crucial for their biological functions. Predicting these motions using elastic network models helps us understand conformational changes and stability. This project implements **GNM** and **ANM** methods to calculate squared fluctuations for protein residues and analyzes differences in their predicted values.

This repository contains the following scripts:
1. `gnm-fluctuations.py` - Computes squared fluctuations using GNM.
2. `anm-fluctuations.py` - Computes squared fluctuations using ANM.
3. `fluctuation-diff.py` - Compares GNM and ANM fluctuations.
4. `fluctuation-diff-index.py` - Identifies top residues with the largest differences between GNM and ANM fluctuations.

---

## Features
- **GNM Fluctuations:** Predicts fluctuations using the Gaussian Network Model.
- **ANM Fluctuations:** Predicts fluctuations using the Anisotropic Network Model.
- **Difference Analysis:** Compares and normalizes GNM and ANM fluctuations.
- **Residue Ranking:** Highlights residues with the largest fluctuation differences.

---

## Usage

### Prerequisites
Ensure you have the following installed:
- Python (3.7 or higher)
- ProDy library

Install ProDy via pip:
```bash
pip install prody
