import queue
import copy
import random

def coordinates(x_coord, y_coord, z_coord, direction):
    """Uses old coordinates and direction to create new coordinates"""
    if direction == 1:
        new_x_coord = x_coord + 1
        new_y_coord = y_coord
        new_z_coord = z_coord
    elif direction == -1:
        new_x_coord = x_coord - 1
        new_y_coord = y_coord
        new_z_coord = z_coord
    elif direction == 2:
        new_x_coord = x_coord
        new_y_coord = y_coord + 1
        new_z_coord = z_coord
    elif direction == -2:
        new_x_coord = x_coord
        new_y_coord = y_coord - 1
        new_z_coord = z_coord
    elif direction == 3:
        new_x_coord = x_coord
        new_y_coord = y_coord
        new_z_coord = z_coord + 1
    elif direction == -3:
        new_x_coord = x_coord
        new_y_coord = y_coord
        new_z_coord = z_coord - 1
    return new_x_coord, new_y_coord, new_z_coord

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

        if len(protein_state) % 3 == 0:
            check_stability = True
        else:
            check_stability = False

        if len(protein_state) < depth:
            current_length = len(protein_state)
            for i in moves:
                protein_child = copy.deepcopy(protein_state)
                stability_child = copy.deepcopy(stability_state)

                new_x_coord, new_y_coord, new_z_coord = coordinates(current_x, current_y, current_z, i)
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

                    mirror_switch = mirror_prune(current_length, protein_child, i)
                    if mirror_switch == True:
                        stability_child = stability_calculator(current_length, protein_child)
                        random_switch = random_prune()
                        if current_length < 22:
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
    if choice < 0.3:
        return True
    return False

def amino_selector(P, H, C, element):
    if element == "P":
        return P
    if element == "H":
        return H
    if element == "C":
        return C

def stability_calculator(current_length, list):
    stability = 0

    # check for successive H's in chain itself and add 2 per pair found
    # since the matrix checker checks every pair twice, so need to compensate
    for element in range(current_length):
        if list[element].type == 'H' and list[element + 1].type == 'H':
            stability += 2
        if list[element].type == 'C' and list[element + 1].type == 'C':
            stability += 10
        if list[element].type == 'C' and list[element + 1].type == 'H':
            stability += 2
        if list[element].type == 'H' and list[element + 1].type == 'C':
            stability += 2

    # check the neighbouring elements
    for element in list:
        if element.type == 'H':
            x = element.x_coord
            y = element.y_coord
            z = element.z_coord

            for other_element in list:
                if other_element.type == 'H' or other_element.type == 'C':
                    if other_element.get_location() == (x - 1, y, z) or \
                    other_element.get_location() == (x + 1, y, z)  or \
                    other_element.get_location() == (x, y - 1, z)  or \
                    other_element.get_location() == (x, y + 1, z)  or \
                    other_element.get_location() == (x, y, z - 1) or \
                    other_element.get_location() == (x, y, z + 1):
                        stability -= 1

        if element.type == 'C':
            x = element.x_coord
            y = element.y_coord
            z = element.z_coord

            for other_element in list:
                if other_element.type == 'H':
                    if other_element.get_location() == (x - 1, y, z) or \
                    other_element.get_location() == (x + 1, y, z)  or \
                    other_element.get_location() == (x, y - 1, z)  or \
                    other_element.get_location() == (x, y + 1, z)  or \
                    other_element.get_location() == (x, y, z - 1) or \
                    other_element.get_location() == (x, y, z + 1):
                        stability -= 1
                if other_element.type == 'C':
                    if other_element.get_location() == (x - 1, y, z) or \
                    other_element.get_location() == (x + 1, y, z)  or \
                    other_element.get_location() == (x, y - 1, z)  or \
                    other_element.get_location() == (x, y + 1, z)  or \
                    other_element.get_location() == (x, y, z - 1) or \
                    other_element.get_location() == (x, y, z + 1):
                        stability -= 5

    # divide stability by 2 since pairs are checked twice
    stability /= 2
    return stability

def matrix_stability(matrix, list, length):
    """calculates stability of lattice with matrix"""
    stability = 0

    # check for successive H's in chain itself and add 2 per pair found
    # since the matrix checker checks every pair twice, so need to compensate
    for element in range(length - 1):
        if list[element].type == 'H' and list[element + 1].type == 'H':
            stability += 2

    # check the neighbouring elements
    for element in range(length):
        i = list[element].x_coord
        j = list[element].y_coord
        k = list[element].z_coord

        if matrix[i][j][k].type == 'H':
            if matrix[i-1][j][k] != None:
                if matrix[i-1][j][k].type == 'H':
                    stability -= 1
            if matrix[i+1][j][k] != None:
                if matrix[i+1][j][k].type == 'H':
                    stability -= 1
            if matrix[i][j-1][k] != None:
                if matrix[i][j-1][k].type == 'H':
                    stability -= 1
            if matrix[i][j+1][k] != None:
                if matrix[i][j+1][k].type == 'H':
                    stability -= 1
            if matrix[i][j][k+1] != None:
                if matrix[i][j][k+1].type == 'H':
                    stability -= 1
            if matrix[i][j][k-1] != None:
                if matrix[i][j][k-1].type == 'H':
                    stability -= 1

    # divide stability by 2 since pairs are checked twice
    stability /= 2

    return stability
