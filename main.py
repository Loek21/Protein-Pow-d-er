
"""
main.py
Made by Team Shire Peasants 3
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
from code.algorithms import randomizematrix
from code.classes import lattice, element


# Step 1, Import string of amino-acid

# Step 2, Initilize grid

# Step 3, Place amino acid on grid

# Step 4, Calculate 'stability'. More negative = more better

# Step 5, Output result in CSV format


if __name__ == '__main__':
    moves = [1, -1, 2, -2]
    test_lattice = lattice.Lattice('HPPPPH')
    test_lattice.load_matrix()
    test_lattice.load_list()

    random_matrix = randomizematrix.matrixrandomizer(test_lattice, moves)
    print(random_matrix)

    for row in range(len(random_matrix)):
        for element in range(len(random_matrix)):
            if random_matrix[row][element] == None:
                random_matrix[row][element] = 0.0

            elif random_matrix[row][element].type == 'H':
                random_matrix[row][element] = 5.0
            
            else:
                random_matrix[row][element] = 10.0

    new_matrix = np.zeros((len(random_matrix), len(random_matrix)))
    for row in range(len(random_matrix)):
        for element in range(len(random_matrix)):
            new_matrix[row][element] = random_matrix[row][element]

    
    
    print(type(new_matrix))
    plt.matshow(new_matrix)
    plt.show()