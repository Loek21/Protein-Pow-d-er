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

    matrix = lattice.get_matrix_twoD()
    list = lattice.get_list()

    # Sets first and second element in the middle of the matrix
    current_x = int(len(matrix) * 0.5 - 1)
    current_y = int(len(matrix) * 0.5 - 1)
    current_z = 0
    matrix[current_x][current_y] = lattice.lattice_list[0]
    matrix[current_x][current_y].set_coordinates(current_x, current_y, current_z)
    matrix[current_x][current_y].set_direction(1)
    current_x += 1
    matrix[current_x][current_y] = lattice.lattice_list[1]
    matrix[current_x][current_y].set_coordinates(current_x, current_y, current_z)

    depth = 4
    Queue = queue.Queue()
    Queue.put(matrix)

    element_counter = 2

    while not Queue.empty():
        state = Queue.get()
        # TODO: get current x and y location of last element.
        print(state)
        if element_counter < depth:
            for i in moves:
                child = copy.deepcopy(state)
                new_x_coord, new_y_coord, new_z_coord = coordinates(current_x, current_y, current_z, i)
                if child[new_x_coord][new_y_coord] == None:
                    list[element_counter].set_coordinates(new_x_coord, new_y_coord, new_z_coord)
                    child[new_x_coord][new_y_coord] = lattice.lattice_list[element_counter]
                    child[current_x][current_y].set_direction(i)
                    new_state = copy.deepcopy(child)
                    Queue.put(new_state)
            element_counter += 1
