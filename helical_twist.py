"""
Calculates the helical twist in THM.
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
    nucleotide_coordinates = {}
    for i in range(1,19):                           #TODO change 19 to number of nucleotides in your structure + 1
        nucleotide_coordinates[i] = []

    #parse pdb file
    filename = "T1_A.pdb"                           #TODO change T1_A.pdb to your file name + .pdb
    print()
    pdb = open(filename, "r")
    for line in pdb:
        info = line.split()
        atom = info[2]
        nucleotide_number = int(info[5])
        x = float(info[6])
        y = float(info[7])
        z = float(info[8])
        if (atom == "C8") or (atom == "C2") or (atom == "N1"):
            coordinates = [atom, x, y, z]
            nucleotide_coordinates[nucleotide_number].append(coordinates)
        pdb.readline()                              #TODO remove if no ANISOU lines in pdb file
    pdb.close()

                                                    #TODO quartet Gs in order (G1 stacks on G2 stacks on G3 in this example); num quartets
    quartet1 = [1,6,11,16]
    quartet2 = [2,7,12,17]
    quartet3 = [3,8,13,18]
    quartets = [quartet1, quartet2, quartet3]
    Gs = quartet1 + quartet2 + quartet3

    #Make vector for each nucleotide
    nucleotide_vectors = {}
    for G in Gs:
        C8 = nucleotide_coordinates[G][0][1:4]
        N1 = nucleotide_coordinates[G][2]
        C2 = nucleotide_coordinates[G][1]
        midpt = [(N1[1]+C2[1])/2, (N1[2]+C2[2])/2, (N1[3]+C2[3])/2]
        vector = [midpt[0]-C8[0], midpt[1]-C8[1], midpt[2]-C8[2]]
        nucleotide_vectors[G] = vector

    for i in range(0,2): #access pairs of stacked quartets  #TODO change 2 to number of quartets in your structure
        print("Quartets " + str(i+1) + "+" + str(i+2))
        topQuartet = quartets[i] #top quartet
        bottomQuartet = quartets[i+1] #bottom quartet
        angles = []
        for j in range(0,4): #access each guanine pair
            topG = nucleotide_vectors[topQuartet[j]]
            bottomG = nucleotide_vectors[bottomQuartet[j]]
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
