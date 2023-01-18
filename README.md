# Calculating helical twist in G-quadruplexes

Script for calculating helical twist in a G-quadruplex given a PDB file. 

## Methodology
1) Extract the coordinates of all atoms from the PDB file.
2) Represent every guanine base as a vector from C8 to the midpoint between N1 and C2 (Figure 1).
3) Calculate angle between the vectors corresponding to every pair of stacked guanines to determine helical twist.

Note: please see comments in script for possible modifications needed to customize the script to analyze your G-quadruplex.

<img width="300" alt="image" src="https://user-images.githubusercontent.com/46332183/213093273-7b0466f1-bfe6-4988-b5ad-2e16fb2c1328.png">
Figure 1. Representation of guanine as a vector (green) from C8 to the midpoint of N1 and C2 used to calculate helical twist between stacked guanines.

## As referenced and described in
- Guédin, A.; Lin, L. Y.; Armane, S.; Lacroix, L.; Mergny, J.-L.; Thore, S.; Yatsunyk, L. A. Quadruplexes in ‘Dicty’: Crystal structure of a four-quartet G-quadruplex formed by G-rich motif found in the Dictyostelium discoideum genome. Nucleic Acids Research 2018, 46 (10), 5297–5307. [doi.org/10.1371/journal.pone.0241513](https://doi.org/10.1371/journal.pone.0241513). PMID: 29718337.
- Lin, L. Y.; McCarthy, S.; Powell, B. M.; Manurung, Y.; Xiang, I. M.; Dean, W. L.; Chaires, B.; Yatsunyk, L. A. Biophysical and X-ray structural studies of the (GGGTT)3GGG G-quadruplex in complex with N-methyl mesoporphyrin IX. PLoS ONE 2020, 15 (11), e0241513. [doi.org/10.1093/nar/gky290](https://doi.org/10.1093/nar/gky290). PMID: 33206666.

## Contacts
- Linda Lin (linda.yq.lin@yale.edu)
- Dr. Liliya Yatsunyk (lyatsun1@swarthmore.edu)
