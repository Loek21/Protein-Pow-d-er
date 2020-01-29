"""
main.py
Made by Team Shire Peasants 3
"""

import sys
from code.algorithms import twist, randomize, greedy, breadthfirst, ehaplus, hillclimb
from code.classes import lattice, element
from code.visualisation import visualise
from code.generalfunctions import generalfunctions

if __name__ == '__main__':
    TwoD_moves = [1, -1, 2, -2]
    ThreeD_moves = [1, -1, 2, -2, 3, -3]
    protein_string_list = ["HHPHHHPH", "HHPHHHPHPHHHPH", "HPHPPHHPHPPHPHHPPHPH", "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP",
                           "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP",
                           "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC", "HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH",
                           "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH", "CUSTOM", "HHPPHPPHPPHPPHPPHPPHPPHH",
                           "PPHHHPHHHPPPHPHHPHHPPHPHHHHPHPPHHHHHPHPHHPPHHP", "PPHPPHHPPHHPPPPPHHHHHHHHHHPPPPPPHHPPHHPPHPPHHHHH",
                           "PPHHHPHHHHHHHHPPPHHHHHHHHHHPHPPPHHHHHHHHHHHHPPPPHHHHHHPHHPHP"]

    # Checks if the correct number of arguments have been given
    if len(sys.argv) != 5:

        # Prints operation explanation if one requires it
        if len(sys.argv) == 2 and sys.argv[1] == "help":
            print("Select any of the following algorithms:\n'random', 'twist', 'greedy', 'breadth', 'pull' and 'eha'")
            print("Select any of the following string numbers:")
            for i in enumerate(protein_string_list):
                print(f"{i}: {protein_string_list[i]}")
            print("Number of iterations:\nAny number higher than 0 will work.\n When you select 1 or higher some statistical results will be displayed.")
            print("Dimension:\nType '2' for 2D and '3' for 3D.")
        else:
            print("usage: python main.py algorithm string_nr iterations dimension\nFor more information type 'python main.py help'")

        sys.exit(1)

    # Asks user if they want the list and graphical result for the best found solution
    want_list_graph = input("Would you like a list and graph of the best found solution? (y/n)\n")

    algorithm = sys.argv[1]
    iterations = int(sys.argv[3])
    dimension = int(sys.argv[4])
    algorithms = ["random", "twist", "greedy", "breadth", "pull", "eha"]

    # Checks if data_structure is available
    if algorithm not in algorithms:
        print("You must choose either 'random', 'twist', 'greedy', 'breadth', 'pull', 'eha'")
        sys.exit(1)

    # Checks to see if given index corresponds to a protein string
    if int(sys.argv[2]) < 0 or int(sys.argv[2]) > 13:
        print("Choose a string number between 0 and 13.")
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

    # If string chosen is number 9, allow the user to create a custom or random string
    if int(sys.argv[2]) == 9:
        custom_prompt = input("Would you like to submit your own string? (y/n)\n")
        if custom_prompt == 'y' or custom_prompt == 'yes':
            custom_string = str(input("Submit your own string here. Make sure it contains only H, P, or C elements.\n"))
            protein_string = custom_string.upper()
        else:
            protein_length = int(input("What length should the protein be?\n"))
            model = str(input("Which elements should the protein contain? Choose either HP or HPC.\n")).upper()

            if model != ('HP' and 'HPC'):
                sys.exit(1)

            protein_string = generalfunctions.stringmaker(protein_length, model)

    # Sets up lattice with its element list
    test_lattice = lattice.Lattice(protein_string)
    test_lattice.load_list()

    state_list = []
    stability_list = []

    ## -- Start algorithms --
    if algorithm == "twist":

        # Get border size from user
        border_size = float(input("Enter a size restriction (in chain lengths) between 0-1. Default is 0.5\n"))

        # Set default to 0.5 if lower/higher than 0/1 are chosen
        if (border_size < 0) or (border_size > 1):
            print("Border size not valid, setting to 0.5.")
            border_size = 0.5

        while len(stability_list) < iterations:

            # Get solution from twist algorithm
            chain, stability = twist.twist(test_lattice, moves, border_size)

            # Save solution if it's not a 'stuck' configuration
            if stability is not None:
                stability_list.append(stability)
                state_list.append(chain)

            # Reset the lattice
            test_lattice = lattice.Lattice(protein_string)
            test_lattice.load_list()
        generalfunctions.write_to_worksheet(stability_list, int(sys.argv[2]), algorithm)

    if algorithm == "random":
        while len(stability_list) < iterations:

            # Get random solution
            random_list, stability = randomize.sarw_dict(test_lattice, moves)

            # Save solution if not a 'stuck' config
            if stability is not None:
                state_list.append(random_list)
                stability_list.append(stability)

            # Reset the lattice
            test_lattice = lattice.Lattice(protein_string)
            test_lattice.load_list()

    if algorithm == "breadth":

        # This algorithm requires an empty string to run and will add protein element objects as the algorithm progressses
        test_lattice_breadth = lattice.Lattice(protein_string)
        element_P = element.Element("P")
        element_H = element.Element("H")
        element_C = element.Element("C")

        # Asks user to enter a number to determine after how many consecutive P elements the random pruning will start
        P_number = int(input("Enter a number between 2 and 5 to indicate after how many consecutive P's in the protein string the random\npruning will start. The higher the number the longer the algorithm will need to run.\n"))

        # If user entered an invalid number random pruning will start after 2 consecutive P's
        if P_number < 2 or P_number > 5:
            print("You have entered an invalid number, the random pruning will start after 2 consecutive P's.")
            P_number = 2

        # Runs the algorithm a predetermined number of times and saves the best solutions in a list
        for i in range(iterations):
            result_states, stabilities = breadthfirst.bfs(test_lattice_breadth, element_P, element_H, element_C, moves, P_number)
            if len(result_states) != 0:
                best_state_iteration, best_stability_iteration = generalfunctions.get_best_state(stabilities, result_states)
                state_list.append(best_state_iteration)
                stability_list.append(best_stability_iteration)
            test_lattice_breadth = lattice.Lattice(protein_string)

    if algorithm == "greedy":

        # Start iterations of greedy algorithm
        while len(stability_list) < iterations:
            greedy_state, stability = greedy.greedy(test_lattice, moves)

            # Append states and stability to lists
            if stability is not None:
                state_list.append(greedy_state)
                stability_list.append(stability)

            # Reset the lattice
            test_lattice = lattice.Lattice(protein_string)
            test_lattice.load_list()
        generalfunctions.write_to_worksheet(stability_list, int(sys.argv[2]), algorithm)

    if algorithm == "eha":

        # Get subchain length from user
        subchain_length = int(input("Enter subchain length between 5-8. This length is +/- 2 in the algorithm, so 6 means subchains of 4-8.\nRecommended length is 6, higher lengths result in much longer runtimes (up to hours).\n"))

        # If subchain length not within boundaries, set to 6
        if (subchain_length < 5) or (subchain_length > 8):
            print("Subchain length chosen not valid, setting to default value of 6.")
            subchain_length = 6

        while len(stability_list) < iterations:
            print(len(stability_list))

            # Get solution from the ehaplus algorithm
            stability, chain = ehaplus.ehaplus(test_lattice, moves, subchain_length)

            # Save the first iteration
            if len(stability_list) == 0:
                stability_list.append(stability)
                state_list.append(chain)

            # Some results are 'stuck' configurations, these aren't valid and will not be saved.
            elif stability < min(stability_list) / 2:
                stability_list.append(stability)
                state_list.append(chain)

            # Reset the lattice
            test_lattice = lattice.Lattice(protein_string)
            test_lattice.load_list()
        #generalfunctions.write_to_worksheet(stability_list, int(sys.argv[2]), algorithm)

    if algorithm == "pull":

        while len(stability_list) < iterations:
            print(len(stability_list))
            # Gets random solution and stability
            twist_chain, twist_stability = twist.twist(test_lattice, moves, 2)

            solution, stability = hillclimb.pullmove(twist_chain, twist_stability)
            if stability is not None:
                state_list.append(solution)
                stability_list.append(stability)
        
        #generalfunctions.write_to_worksheet(stability_list, int(sys.argv[2]), algorithm)

    # Calculates best found state and stability
    best_state, best_stability = generalfunctions.get_best_state(stability_list, state_list)

    # If 2 or more iterations are selected, it will print stability statistics
    if iterations >= 2:
        print(generalfunctions.list_stats(stability_list, algorithm))

    # If y or yes is selected the user will get a list and graph of the best found solution
    if want_list_graph == "y" or want_list_graph == "yes":
        print(f"Best State: {best_state}")
        visualise.chain_list_3Dplot(best_state, best_stability)