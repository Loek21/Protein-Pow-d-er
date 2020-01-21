
"""
main.py
Made by Team Shire Peasants 3
"""

import csv
import sys
import copy
import datetime
import numpy as np
from code.algorithms import randomizematrix, randomizedict, matrixapprox, greedymatrix, breadthfirst, eha, ehadict
from code.classes import lattice, element
from code.visualisation import visualise

if __name__ == '__main__':
    TwoD_moves = [1, -1, 2, -2]
    ThreeD_moves = [1, -1, 2, -2, 3, -3]
    protein_string_list = ["HHPHHHPH", "HHPHHHPHPHHHPH", "HPHPPHHPHPPHPHHPPHPH", "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP",
                            "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP",
                            "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC", "HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH",
                            "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH", "HPPCH"]

    # Checks if the correct number of arguments have been given
    if len(sys.argv) != 5:
        print("usage: python main.py algorithm string_nr iterations dimension")
        sys.exit(1)
    data_structure = sys.argv[1]
    iterations = int(sys.argv[3])
    dimension = int(sys.argv[4])
    data_structures = ["random", "matrix", "greedy", "approx", "breadth", "eha", "ehalist"]

    # Checks if data_structure is available
    if data_structure not in data_structures:
        print("You must choose either 'random', 'matrix', 'greedy', 'breadth', 'eha', 'ehalist'")
        sys.exit(1)

    # Checks to see if given index corresponds to a protein string
    if int(sys.argv[2]) < 0 or int(sys.argv[2]) > 9:
        print("Choose a string number between 0 and 9.")
        sys.exit(1)
    protein_string = protein_string_list[int(sys.argv[2])]

    # Checks if iterations is above 0
    if iterations <= 0:
        print("You must choose a positive number.")
        sys.exit(1)

    if dimension == 2:
        moves = TwoD_moves
    elif dimension == 3:
        moves = ThreeD_moves
    else:
        print("You must choose '2' for 2D or '3' for 3D.")
        sys.exit(1)

    # Sets up list, dictionary and matrix for given protein string
    test_lattice = lattice.Lattice(protein_string)
    test_lattice.load_dict()
    test_lattice.load_matrix()
    test_lattice.load_TwoD_matrix()
    test_lattice.load_list()

    if data_structure == "matrix":
        # good_count = 0
        best_stab = 1
        for i in range(iterations):
            try:

                random_matrix = randomizematrix.matrixrandomizer(test_lattice, ThreeD_moves)
                if random_matrix[1] != False:
                    stability = randomizematrix.matrix_stability(test_lattice)
                    #print(stability)
                    # if stability == -16:
                    #     print("MATRIX FOUND AT", i)
                    #     break
                    if stability < best_stab:
                        best_stab = stability
                    #good_count += 1


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

                    #visualise.matrix_plot(new_matrix)

            except IndexError:
                pass
        print(best_stab)

    if data_structure == "random":
        best_stability = 1
        best_list = 0
        for i in range(iterations):
            random_list, stability = randomizedict.sarw_dict(test_lattice, moves)
            if stability < best_stability:
                best_stability = stability
                best_list = copy.deepcopy(random_list)


        visualise.chain_list_3Dplot(best_list, best_stability)

    if data_structure == "approx":
        pass

    if data_structure == "breadth":
        test_lattice_breadth = lattice.Lattice(protein_string)
        element_P = element.Element("P")
        element_H = element.Element("H")
        element_C = element.Element("C")

        result_states, stabilities = breadthfirst.bfs(test_lattice_breadth, element_P, element_H, element_C, ThreeD_moves)
        print(len(result_states))
        best_stability = 1
        best_state = 0
        for i in range(len(result_states)):
            if stabilities[i] < best_stability:
                best_stability = stabilities[i]
                best_state = result_states[i]

        visualise.chain_list_3Dplot(best_state, best_stability)


    if data_structure == "greedy":
        # Set up variables
        successful_iterations = 0
        best_stability = 0

        # Start iterations of greedy algorithm
        try:
            for i in range(iterations):
                greedymat = greedymatrix.greedy(test_lattice, ThreeD_moves)
                if greedymat[1] != False:
                    stability = greedymatrix.matrix_stability(test_lattice)

                # Modify best_stability if a higher stability was found.
                if stability < best_stability:
                    best_stability = stability
                successful_iterations += 1

                test_lattice = lattice.Lattice(protein_string)
                test_lattice.load_matrix()
                test_lattice.load_list()
        except IndexError:
            pass

        # Print results
        print(f"Completed {successful_iterations} iterations")
        print(f"Best found stability: {best_stability}")
        #visualise.matrix_plot(greedymat)
        sys.exit()

    if data_structure == "eha":
        stability, chain = eha.eha(test_lattice, ThreeD_moves, 6)
        print(stability)
        print(chain)
        element_list = []
        x_list = []
        y_list = []
        z_list = []
        for element in chain:
            element_list.append(element.type)
            x_list.append(element.x_coord)
            y_list.append(element.y_coord)
            z_list.append(element.z_coord)
        visualise.dict_plot_ThreeD(element_list, x_list, y_list, z_list, stability)

    if data_structure == "ehalist":
        best_stability_eha = 0
        best_chain = []
        for i in range(iterations):
            stability, chain = ehadict.eha_list(test_lattice, ThreeD_moves, 6)
            print(stability)
            print(chain)
            if stability < best_stability_eha:
                best_stability_eha = stability
                best_chain = chain

            test_lattice = lattice.Lattice(protein_string)
            test_lattice.load_list()

        visualise.chain_list_3Dplot(best_chain, best_stability_eha)
