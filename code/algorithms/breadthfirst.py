import queue
import copy
import random
from .generalfunctions import stability_calculator, make_move

def bfs(lattice, P, H, C, moves):
    """
    Breadth first with beam search based on minimalzing the stability, returns list of all states that have
    achieved the best stability and the best stability.
    """
    protein_string = lattice.elements
    list = lattice.get_list()
    protein_length = len(protein_string)
    result_list = []
    stabilities = []
    stability_to_beat = 0

    # Setting coordinates of first two elements
    current_x = 0
    current_y = 0
    current_z = 0
    lattice.load_element(protein_string[0])
    list[0].set_coordinates(current_x, current_y, current_z)
    list[0].set_direction(1)
    current_x += 1
    lattice.load_element(protein_string[1])
    list[1].set_coordinates(current_x, current_y, current_z)

    # Creating Queues for the list of element objects, the stability and the number of consecutive P's
    depth = protein_length
    list_queue = queue.Queue()
    stability = queue.Queue()
    P_counter = queue.Queue()
    list_queue.put(list)
    stability.put(0)
    P_counter.put(0)

    # Continues making a new branch untill the queues are empty
    while not list_queue.empty():

        # Gets next state from the queue together with the stability and number of consecutive P's
        protein_state = list_queue.get()
        stability_state = stability.get()
        P_state = P_counter.get()

        # Gets coordinates of the last element that was added to the string
        current_x, current_y, current_z = protein_state[len(protein_state) - 1].get_location()

        # Adds all states and stabilities of the final branch level to a list
        if len(protein_state) == protein_length:
            result_list.append(protein_state)
            stabilities.append(stability_state)

        # Continues untill the full proteins string and all the permutations have been created
        if len(protein_state) < depth:
            current_length = len(protein_state)

            # For each state it creates all possible locations for the next protein element
            for i in moves:
                protein_child = copy.deepcopy(protein_state)
                stability_child = copy.deepcopy(stability_state)
                P_child = copy.deepcopy(P_state)

                # Sets new coordinates for the new protein element based on the current move
                new_x_coord, new_y_coord, new_z_coord = make_move(i, current_x, current_y, current_z)

                # Checks if new coordinates already contain a protein element, if it does it returns True
                # and the state will not be saved
                occupied = False
                for j in range(current_length - 1):
                    occupied_x, occupied_y, occupied_z = protein_child[j].get_location()
                    if (occupied_x, occupied_y, occupied_z) == (new_x_coord, new_y_coord, new_z_coord):
                        occupied = True

                if occupied == False:

                    # If new coordinates are free, the next protein element will be made and the coordinates
                    # wil be added to its location and the direction will be added to the previous protein element
                    element = protein_string[len(protein_child)]
                    protein_child.append(amino_selector(P, H, C, element))
                    protein_child[len(protein_child) - 1].set_coordinates(new_x_coord, new_y_coord, new_z_coord)
                    protein_child[len(protein_child) - 2].set_direction(i)

                    # For benchmarking upper bound
                    # stability_child = stability_calculator(protein_child)
                    #
                    # stability_child_copy = copy.deepcopy(stability_child)
                    # protein_child_copy = copy.deepcopy(protein_child)
                    #
                    # list_queue.put(protein_child_copy)
                    # stability.put(stability_child_copy)

                    # For regular testing
                    # Adds to the consecutive P counter if the element is a P, else it resets the counter to 0
                    if element == "P":
                        P_child += 1
                    else:
                        P_child = 0

                    # Mirror prune cuts out all the mirrored versions of the same state in the first 4 elements
                    mirror_switch = mirror_prune(current_length, protein_child, i)
                    if mirror_switch == True:

                        # Calculates the stability of the new state
                        stability_child = stability_calculator(protein_child)

                        # Random switch randomly allows certain consecutive P states to pass, the threshold is
                        # dependent on the number of consecutive P's
                        random_switch = random_prune(P_child)
                        save_switch = False

                        # If the consecutive P's chain is longer than 2 and the state has passed through the random
                        # prune function it will be selected for saving
                        if P_child >= 2 and random_switch == True:
                            save_switch = True

                        # Else if the new stability is better or just as good as the current best stability it will be saved too
                        elif P_child < 2 and stability_child <= stability_to_beat:
                            stability_to_beat = stability_child
                            save_switch = True

                        # If state has been selected for saving it will add the new state to the queue
                        if save_switch == True:
                            stability_child_copy = copy.deepcopy(stability_child)
                            protein_child_copy = copy.deepcopy(protein_child)
                            P_child_copy = copy.deepcopy(P_child)

                            list_queue.put(protein_child_copy)
                            stability.put(stability_child_copy)
                            P_counter.put(P_child_copy)

    return result_list, stabilities

def mirror_prune(length, list, move):
    """Performs the mirror prune for the first four elements and partially the fifth"""
    if length == 3 and (move == -2 or move == -3 or move == 3):
        return False
    if length == 4:
        previous_move = list[2].get_direction()

        # Following a move in the y direction a move in the z direction will be identical when the length is 4
        if previous_move == 2 and move == -3:
            return False

        # Similar to length is 3 situation
        if previous_move == 1 and (move == -2 or move == -3 or move == 3):
            return False
    if length == 5:
        previous_move = list[3].get_direction()

        # Similar to length is 3 situation
        if previous_move == 1 and (move == -2 or move == -3 or move == 3):
            return False
    return True

def random_prune(P_counter):
    """Randomly prunes with a threshold depending on the number of consecutive P's"""
    choice = random.random()
    if choice < 0.4 and P_counter == 2:
        return True
    if choice < 0.3 and P_counter == 3:
        return True
    if choice < 0.25 and P_counter == 4:
        return True
    if choice < 0.2 and P_counter >= 5:
        return True
    return False

def amino_selector(P, H, C, element):
    """Returns an element object depending on the letter in the protein string"""
    if element == "P":
        return P
    if element == "H":
        return H
    if element == "C":
        return C
