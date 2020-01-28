import queue
import copy
import random
from ..generalfunctions.generalfunctions import stability_calculator, make_move

def bfs(lattice, P, H, C, moves, P_number):
    """
    Breadth first with beam search based on minimalzing the stability, it requires the objects of each type of element (P, H, C),
    a move set depending on the 2D, 3D selection and a consecutive P number after which the random prune is added in.
    Returns a list of all states that haveachieved the best stability and the best stability.
    """
    protein_string = lattice.elements
    lattice_list = lattice.get_list()
    protein_length = len(protein_string)
    result_list = []
    stabilities = []
    stability_to_beat = 0

    # Loads coordinates for first and second element
    state_init(lattice, protein_string, lattice_list)

    # Creating Queues for the list of element objects, the stability and the number of consecutive P's
    lattice_queue, stability, P_counter = queue_init(lattice_list)

    # Continues making a new branch untill the queues are empty
    while not lattice_queue.empty():

        # Gets next state from the queue together with the stability and number of consecutive P's
        protein_state, stability_state, P_state = queue_get(lattice_queue, stability, P_counter)

        # Gets coordinates of the last element that was added to the string
        current_x, current_y, current_z = protein_state[len(protein_state) - 1].get_location()

        # Adds all states and stabilities of the final branch level to a list
        if len(protein_state) == protein_length:
            result_list.append(protein_state)
            stabilities.append(stability_state)

        # Continues untill the full proteins string and all the permutations have been created
        if len(protein_state) < protein_length:
            current_length = len(protein_state)

            # For each state it creates all possible locations for the next protein element
            for i in moves:
                protein_child, stability_child, P_child = deepcopy_generator(protein_state, stability_state, P_state)

                # Sets new coordinates for the new protein element based on the current move
                new_x_coord, new_y_coord, new_z_coord = make_move(i, current_x, current_y, current_z)

                # Checks if new coordinates already contain a protein element, if it does it returns True
                # and the state will not be saved
                occupied = check_occupation(current_length, protein_child, new_x_coord, new_y_coord, new_z_coord)

                if not occupied:

                    # If new coordinates are free, the next protein element will be made and the coordinates
                    # wil be added to its location and the direction will be added to the previous protein element
                    element = protein_string[len(protein_child)]
                    protein_child = setting_element_location(P, H, C, element, protein_child, new_x_coord, new_y_coord, new_z_coord, i)

                    # Adds to the consecutive P counter if the element is a P, else it resets the counter to 0
                    P_child = consecutive_P(element, P_child)

                    # Mirror prune cuts out all the mirrored versions of the same state in the first 4 elements
                    mirror_switch = mirror_prune(current_length, protein_child, i)
                    if mirror_switch:

                        # Calculates the stability of the new state
                        stability_child = stability_calculator(protein_child)

                        # Random switch randomly allows certain consecutive P states to pass, the threshold is
                        # dependent on the number of consecutive P's
                        random_switch = random_prune(P_child)
                        save_switch = False

                        # If the consecutive P's chain is longer than 2 and the state has passed through the random
                        # prune function it will be selected for saving
                        if P_child >= P_number and random_switch:
                            save_switch = True

                        # Else if the new stability is better or just as good as the current best stability it will be saved too
                        elif P_child < P_number and stability_child <= stability_to_beat:
                            stability_to_beat = stability_child
                            save_switch = True

                        # If state has been selected for saving it will add the new state to the queue
                        if save_switch == True:
                            queue_save(stability_child, protein_child, P_child, lattice_queue, stability, P_counter)

    return result_list, stabilities

def mirror_prune(length, chain_list, move):
    """Performs the mirror prune for the first four elements and partially the fifth"""
    if length == 3 and (move == -2 or move == -3 or move == 3):
        return False
    if length == 4:
        previous_move = chain_list[2].get_direction()

        # Following a move in the y direction a move in the z direction will be identical when the length is 4
        if previous_move == 2 and move == -3:
            return False

        # Similar to length is 3 situation
        if previous_move == 1 and (move == -2 or move == -3 or move == 3):
            return False
    if length == 5:
        previous_move = chain_list[3].get_direction()

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

def state_init(lattice, protein_string, lattice_list):
    """Initialise the lattice list by setting coordinates of first two elements at (0, 0, 0) and (1, 0, 0)"""

    # Loads first element and adds (0, 0, 0) coordinates and direction 1 (along the positive x axis)
    lattice.load_element(protein_string[0])
    lattice_list[0].set_coordinates(0, 0, 0)
    lattice_list[0].set_direction(1)

    # Loads second element and adds (1, 0, 0) coordinates
    lattice.load_element(protein_string[1])
    lattice_list[1].set_coordinates(1, 0, 0)

    return

def queue_init(lattice_list):
    """Initialises the queues for the state, the stability and the P_counter, returns all the queues"""
    lattice_queue = queue.Queue()
    stability = queue.Queue()
    P_counter = queue.Queue()

    # Adds the first state containing two elements in the queue, with initial stability 0 and no consecutive P's
    lattice_queue.put(lattice_list)
    stability.put(0)
    P_counter.put(0)

    return lattice_queue, stability, P_counter

def queue_get(lattice_queue, stability, P_counter):
    """Gets next item in the queue, returns that item"""
    protein_state = lattice_queue.get()
    stability_state = stability.get()
    P_state = P_counter.get()

    return protein_state, stability_state, P_state

def check_occupation(current_length, protein_child, new_x_coord, new_y_coord, new_z_coord):
    """Checks if new coordinates are occupied by a different element, returns true if it's occupied else false"""
    for j in range(current_length - 1):
        occupied_x, occupied_y, occupied_z = protein_child[j].get_location()
        if (occupied_x, occupied_y, occupied_z) == (new_x_coord, new_y_coord, new_z_coord):
            return True
    return False

def consecutive_P(element, P_child):
    """If current element is a P add 1 to the consecutive P counter"""
    if element == "P":
        P_child += 1
    else:
        P_child = 0
    return P_child

def deepcopy_generator(protein_state, stability_state, P_state):
    """Creates deepcopies of the current state, returns the copies"""
    protein_child = copy.deepcopy(protein_state)
    stability_child = copy.deepcopy(stability_state)
    P_child = copy.deepcopy(P_state)

    return protein_child, stability_child, P_child

def setting_element_location(P, H, C, element, protein_child, new_x_coord, new_y_coord, new_z_coord, move):
    """ Sets new element according to the protein string and then adds it's location and direction"""
    protein_child.append(amino_selector(P, H, C, element))
    protein_child[len(protein_child) - 1].set_coordinates(new_x_coord, new_y_coord, new_z_coord)
    protein_child[len(protein_child) - 2].set_direction(move)

    return protein_child

def queue_save(stability_child, protein_child, P_child, lattice_queue, stability, P_counter):
    """ Saves a new state in the queue """
    stability_child_copy = copy.deepcopy(stability_child)
    protein_child_copy = copy.deepcopy(protein_child)
    P_child_copy = copy.deepcopy(P_child)

    lattice_queue.put(protein_child_copy)
    stability.put(stability_child_copy)
    P_counter.put(P_child_copy)

    return
