import queue
import copy
import random
from .generalfunctions import stability_calculator, make_move

def bfs(lattice, P, H, C, moves):

    protein_string = lattice.elements
    list = lattice.get_list()
    protein_length = len(protein_string)
    result_list = []
    stabilities = []
    stability_to_beat = 0

    # Setting coordinates from first two elements
    current_x = 0
    current_y = 0
    current_z = 0
    lattice.load_element(protein_string[0])
    list[0].set_coordinates(current_x, current_y, current_z)
    list[0].set_direction(1)
    current_x += 1
    lattice.load_element(protein_string[1])
    list[1].set_coordinates(current_x, current_y, current_z)

    depth = protein_length
    list_queue = queue.Queue()
    stability = queue.Queue()
    list_queue.put(list)
    stability.put(0)


    while not list_queue.empty():
        protein_state = list_queue.get()
        stability_state = stability.get()
        # print(best_stability)

        current_x, current_y, current_z = protein_state[len(protein_state) - 1].get_location()

        # Adds all final states and stabilities to a list
        if len(protein_state) == protein_length:
            result_list.append(protein_state)
            stabilities.append(stability_state)

        if len(protein_state) < depth:
            current_length = len(protein_state)
            for i in moves:
                protein_child = copy.deepcopy(protein_state)
                stability_child = copy.deepcopy(stability_state)

                new_x_coord, new_y_coord, new_z_coord = make_move(i, current_x, current_y, current_z)
                occupied = False
                for j in range(current_length - 1):
                    occupied_x, occupied_y, occupied_z = protein_child[j].get_location()
                    if (occupied_x, occupied_y, occupied_z) == (new_x_coord, new_y_coord, new_z_coord):
                        occupied = True

                if occupied == False:
                    element = protein_string[len(protein_child)]
                    protein_child.append(amino_selector(P, H, C, element))
                    protein_child[len(protein_child) - 1].set_coordinates(new_x_coord, new_y_coord, new_z_coord)
                    protein_child[len(protein_child) - 2].set_direction(i)

                    # For benchmarking upper bound
                    # stability_child = stability_calculator(current_length, protein_child)
                    #
                    # stability_child_copy = copy.deepcopy(stability_child)
                    # protein_child_copy = copy.deepcopy(protein_child)
                    #
                    # list_queue.put(protein_child_copy)
                    # stability.put(stability_child_copy)

                    # For regular testing
                    mirror_switch = mirror_prune(current_length, protein_child, i)
                    if mirror_switch == True:
                        stability_child = stability_calculator(protein_child)
                        random_switch = random_prune()
                        if current_length < 21:
                            if stability_child <= stability_to_beat:
                                stability_to_beat = stability_child

                                stability_child_copy = copy.deepcopy(stability_child)
                                protein_child_copy = copy.deepcopy(protein_child)

                                list_queue.put(protein_child_copy)
                                stability.put(stability_child_copy)
                        else:
                            if stability_child <= stability_to_beat and random_switch == True:
                                stability_to_beat = stability_child

                                stability_child_copy = copy.deepcopy(stability_child)
                                protein_child_copy = copy.deepcopy(protein_child)

                                list_queue.put(protein_child_copy)
                                stability.put(stability_child_copy)


    return result_list, stabilities

def mirror_prune(length, list, move):
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

def random_prune():
    choice = random.random()
    if choice < 0.05:
        return True
    return False

def amino_selector(P, H, C, element):
    if element == "P":
        return P
    if element == "H":
        return H
    if element == "C":
        return C
