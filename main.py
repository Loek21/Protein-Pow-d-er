
"""
main.py
Made by Team Shire Peasants 3
"""

import csv
import sys
import copy
import datetime
import numpy as np
from code.algorithms import randomizematrix, randomizedict
from code.classes import lattice, element
from code.visualisation import visualise


# Step 1, Import string of amino-acid

# Step 2, Initilize grid

# Step 3, Place amino acid on grid

# Step 4, Calculate 'stability'. More negative = more better

# Step 5, Output result in CSV format


if __name__ == '__main__':
    TwoD_moves = [1, -1, 2, -2]
    ThreeD_moves = [1, -1, 2, -2, 3, -3]
    protein_string_list = ["HHPHHHPH", "HHPHHHPHPHHHPH", "HPHPPHHPHPPHPHHPPHPH", "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP",
                            "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP",
                            "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC", "HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH",
                            "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"]

    # Checks if the correct number of arguments have been given
    if len(sys.argv) != 4:
        print("usage: python main.py datastructure string_nr iterations")
        sys.exit(0)
    data_structure = sys.argv[1]
    iterations = int(sys.argv[3])
    data_structures = ["dict", "matrix"]

    # Checks if data_structure is available
    if data_structure not in data_structures:
        print("You must choose either 'dict' or 'matrix'")
        sys.exit(0)

    # Checks to see if given index corresponds to a protein string
    if int(sys.argv[2]) < 0 or int(sys.argv[2]) > 8:
        print("Choose a string number between 0 and 8.")
        sys.exit(0)
    protein_string = protein_string_list[int(sys.argv[2])]

    # Checks if iterations is above 0
    if iterations <= 0:
        print("You must choose a positive number.")
        sys.exit(0)

    # Sets up list, dictionary and matrix for given protein string
    test_lattice = lattice.Lattice(protein_string)
    test_lattice.load_dict()
    test_lattice.load_matrix()
    test_lattice.load_list()

    if data_structure == "matrix":
        #good_count = 0
        for i in range(iterations):
            
            random_matrix = randomizematrix.matrixrandomizer(test_lattice, ThreeD_moves)
            if random_matrix[1] != False:
                stability = randomizematrix.matrix_stability(test_lattice)
                # print(stability)
                # good_count += 1
                
                
            test_lattice = lattice.Lattice(protein_string)
            test_lattice.load_matrix()
            test_lattice.load_list()
                # for row in range(len(random_matrix)):
                #     for element in range(len(random_matrix)):
                #         if random_matrix[row][element] == None:
                #             random_matrix[row][element] = 0.0

                #         elif random_matrix[row][element].type == 'H':
                #             random_matrix[row][element] = 5.0

                #         else:
                #             random_matrix[row][element] = 10.0

                # new_matrix = np.zeros((len(random_matrix), len(random_matrix)))
                # for row in range(len(random_matrix)):
                #     for element in range(len(random_matrix)):
                #         new_matrix[row][element] = random_matrix[row][element]

                # visualise.matrix_plot(new_matrix)
        #print(good_count)

    if data_structure == "dict": 
        # best_stability = 1
        # best_dict = {}
        for i in range(iterations):
            random_dict, stability = randomizedict.sarw_dict(test_lattice, ThreeD_moves)
            #print(stability)
            # if stability < best_stability:
            #     best_stability = stability
            #     best_dict = copy.deepcopy(random_dict)

        # Gets data from best folded protein and plots it
        # x_list = []
        # y_list = []
        # for i in range(len(test_lattice.get_list())):
        #     x_coord, y_coord, z_coord = best_dict[i].get_location()
        #     x_list.append(x_coord)
        #     y_list.append(y_coord)
        # visualise.dict_plot(test_lattice.elements, x_list, y_list, best_stability)
