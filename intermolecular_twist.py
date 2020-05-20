"""
Calculates the intermolecular helical twist (between the tetrads at the
dimer interface) in THM.

Linda Lin
5/19/20
"""

import numpy as np
import math
import statistics

def main():
    #dictionary of nucleotide coordinates in GQ chain
    #key = atom #
    #value = [C8, C2, N1] where each atom is a list: [name, x, y, z]
    nucleotide_coordinates_A = {}
    nucleotide_coordinates_B = {}
    for i in range(1,19):                           #TODO num nucleotides + 1
        nucleotide_coordinates_A[i] = []
        nucleotide_coordinates_B[i] = []

    #parse pdb file
    filename = "T1_symm.pdb"                        #TODO change file name to your file name + .pdb
    print()
    pdb = open(filename, "r")
    for line in pdb:
        info = line.split()
        atom = info[2]
        chain = info[4]
        nucleotide_number = int(info[5])
        x = float(info[6])
        y = float(info[7])
        z = float(info[8])
        if (atom == "C8") or (atom == "C2") or (atom == "N1"):
            coordinates = [atom, x, y, z]
            if chain == 'A':                        #TODO change chain label to desired chain label as appropriate
                nucleotide_coordinates_A[nucleotide_number].append(coordinates)
            elif chain == 'B':                      #TODO change chain label to desired chain label as appropriate
                nucleotide_coordinates_B[nucleotide_number].append(coordinates)
        pdb.readline()                              #TODO rm if no ANISOU lines
    pdb.close()

    G_A = [1,6,11,16]                               #TODO nt number in tetrad
    G_B = [16,11,6,1]

    #Make vector for each nucleotide
    nucleotide_vectors_A = {}
    nucleotide_vectors_B = {}
    for i in range(0,4):
        C8 = nucleotide_coordinates_A[G_A[i]][0][1:4]
        N1 = nucleotide_coordinates_A[G_A[i]][2]
        C2 = nucleotide_coordinates_A[G_A[i]][1]
        midpt = [(N1[1]+C2[1])/2, (N1[2]+C2[2])/2, (N1[3]+C2[3])/2]
        vector = [midpt[0]-C8[0], midpt[1]-C8[1], midpt[2]-C8[2]]
        nucleotide_vectors_A[i] = vector

        C8 = nucleotide_coordinates_B[G_B[i]][0][1:4]
        N1 = nucleotide_coordinates_B[G_B[i]][2]
        C2 = nucleotide_coordinates_B[G_B[i]][1]
        midpt = [(N1[1]+C2[1])/2, (N1[2]+C2[2])/2, (N1[3]+C2[3])/2]
        vector = [midpt[0]-C8[0], midpt[1]-C8[1], midpt[2]-C8[2]]
        nucleotide_vectors_B[i] = vector

    angles = []
    for i in range(0,4): #access each guanine pair
        topG = nucleotide_vectors_A[i]
        bottomG = nucleotide_vectors_B[i]
        twist = angle(topG, bottomG)
        angles.append(twist)
        print(twist)
    print("Mean: " + str(statistics.mean(angles)))
    print("SD: " + str(statistics.stdev(angles)))
    print()


def angle(v1, v2):
    """Calculates angle between 2 vectors in degrees
    """
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)
    angle = np.arccos(np.dot(v1, v2) / (mag1 * mag2))
    angle = math.degrees(angle)
    return angle

if __name__ == "__main__":
    main()
