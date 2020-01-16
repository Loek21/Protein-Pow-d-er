import queue
import copy

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

def bfs(lattice, moves):

    matrix = lattice.get_matrix()
    list = lattice.get_list()
    length_string = len(list)
    result_list = []
    stability_list = []

    # Sets first and second element in the middle of the matrix
    current_x = int(len(matrix) * 0.5 - 1)
    current_y = int(len(matrix) * 0.5 - 1)
    current_z = 0
    matrix[current_x][current_y][current_z] = lattice.lattice_list[0]
    matrix[current_x][current_y][current_z].set_coordinates(current_x, current_y, current_z)
    matrix[current_x][current_y][current_z].set_direction(1)
    current_x += 1
    matrix[current_x][current_y][current_z] = lattice.lattice_list[1]
    matrix[current_x][current_y][current_z].set_coordinates(current_x, current_y, current_z)

    depth = length_string
    Queue_matrix = queue.Queue()
    Queue_matrix.put(matrix)
    Queue_list = queue.Queue()
    Queue_list.put(list)
    Queue_string = queue.Queue()
    Queue_string.put("RR")
    Queue_stability = queue.Queue()
    Queue_stability.put(0)

    counter = 0

    while not Queue_matrix.empty():

        element_counter = 0

        # Gets the next state in the queue
        state_matrix = Queue_matrix.get()
        state_list = Queue_list.get()
        state_string = Queue_string.get()
        state_stability = Queue_stability.get()

        for j in range(length_string):
            x_coord, y_coord, z_coord = state_list[j].get_location()
            direction = state_list[j].get_direction()
            if x_coord != None:
                element_counter += 1

        # Gets the location of the last placed element in this state
        current_x, current_y, current_z = state_list[element_counter - 1].get_location()

        if counter % 1000 == 0:
            print(counter)
        counter += 1

        # Adds all final states to a list
        if element_counter == length_string:
            result_list.append(state_list)
            stability_list.append(state_stability)

        if len(state_string) < depth:
            # Loops through all available moves and creates the additional states
            for i in moves:
                child_matrix = copy.deepcopy(state_matrix)
                child_list = copy.deepcopy(state_list)
                child_string = copy.deepcopy(state_string)
                child_stability = copy.deepcopy(state_stability)

                # Create new coordinates
                new_x_coord, new_y_coord, new_z_coord = coordinates(current_x, current_y, current_z, i)
                if child_matrix[new_x_coord][new_y_coord][new_z_coord] == None:

                    # Sets the coordinates for the current element and the direction from the previous element
                    if element_counter != length_string:
                        child_list[element_counter].set_coordinates(new_x_coord, new_y_coord, new_z_coord)
                        child_matrix[new_x_coord][new_y_coord][new_z_coord] = child_list[element_counter]

                    child_list[element_counter - 1].set_direction(i)
                    child_matrix[current_x][current_y][current_z].set_direction(i)

                    child_string += "R"

                    stability = matrix_stability(child_matrix, child_list, len(child_string))
                    child_stability = stability

                    # Saves new states and adds them to the queue
                    new_state_matrix = copy.deepcopy(child_matrix)
                    new_state_list = copy.deepcopy(child_list)
                    Queue_matrix.put(new_state_matrix)
                    Queue_list.put(new_state_list)
                    Queue_string.put(child_string)
                    Queue_stability.put(child_stability)
            element_counter += 1

    return result_list, stability_list

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
