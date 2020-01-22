
"""
main.py
Made by Team Shire Peasants 3
"""

import csv
import sys
import copy
import datetime
import numpy as np
from code.algorithms import twist, randomize, greedymatrix, breadthfirst, eha, ehadict
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
    algorithm = sys.argv[1]
    iterations = int(sys.argv[3])
    dimension = int(sys.argv[4])
    algorithms = ["random", "twist", "greedy", "breadth", "eha", "ehalist"]

    # Checks if data_structure is available
    if algorithm not in algorithms:
        print("You must choose either 'random', 'twist', 'greedy', 'breadth', 'eha', 'ehalist'")
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

    if algorithm == "twist":
        best_stab = 1
        best_configuration = []
        for i in range(iterations):


            random_mat = twist.matrixrandomizer(test_lattice, moves)
            chain = random_mat[0]
            stability = random_mat[1]

            if stability < best_stab:
                best_stab = stability
                best_configuration = chain

            test_lattice = lattice.Lattice(protein_string)
            test_lattice.load_matrix()
            test_lattice.load_list()

        visualise.chain_list_3Dplot(best_configuration, best_stab)

    if algorithm == "random":
        best_stability = 1
        best_list = 0
        for i in range(iterations):
            random_list, stability = randomize.sarw_dict(test_lattice, moves)
            if stability < best_stability:
                best_stability = stability
                best_list = copy.deepcopy(random_list)


        visualise.chain_list_3Dplot(best_list, best_stability)

    if algorithm == "breadth":
        test_lattice_breadth = lattice.Lattice(protein_string)
        element_P = element.Element("P")
        element_H = element.Element("H")
        element_C = element.Element("C")

        result_states, stabilities = breadthfirst.bfs(test_lattice_breadth, element_P, element_H, element_C, moves)
        print(len(result_states))
        best_stability = 1
        best_state = 0
        for i in range(len(result_states)):
            if stabilities[i] < best_stability:
                best_stability = stabilities[i]
                best_state = result_states[i]

        visualise.chain_list_3Dplot(best_state, best_stability)


    if algorithm == "greedy":
        # Set up variables
        successful_iterations = 0
        best_stability = 0
        

        # Start iterations of greedy algorithm
        try:
            for i in range(iterations):
                greedymat = greedymatrix.greedy(test_lattice, moves)
                print("DOEI")
                if greedymat[1] != False:
                    print("Jo")
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

    if algorithm == "eha":
        stability, chain = eha.eha(test_lattice, moves, 6)
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

    if algorithm == "ehalist":
        best_stability_eha = 0
        best_chain = []
        for i in range(iterations):
            stability, chain = ehadict.eha_list(test_lattice, moves, 6)
            print(stability)
            print(chain)
            if stability < best_stability_eha:
                best_stability_eha = stability
                best_chain = chain

            test_lattice = lattice.Lattice(protein_string)
            test_lattice.load_list()

        visualise.chain_list_3Dplot(best_chain, best_stability_eha)
