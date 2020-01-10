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

def move_no_backtrack(list, dict, positions, index, moves):
    """Performs random movement without backtracking"""
    switch = True
    tries_counter = 0
    if index == 0:
        x_coord = 0
        y_coord = 0
        z_coord = 0
        dict[0].set_coordinates(0, 0, 0)
    else:
        x_coord, y_coord, z_coord = dict[index].get_location()

    # Tries finding the next valid position
    while switch == True:
        direction = random.choice(moves)
        new_x_coord, new_y_coord, new_z_coord = coordinates(x_coord, y_coord, z_coord, direction)
        new_coords = f"{new_x_coord},{new_y_coord},{new_z_coord}"

        if new_coords not in positions:
            dict[index].set_direction(direction)
            if index + 1 != len(list):
                dict[index + 1].set_coordinates(new_x_coord, new_y_coord, new_z_coord)
            positions.append(f"{x_coord},{y_coord},{z_coord}")
            switch = False

        # If 25 attempts have been made to move and all failed the chain is stuck
        if tries_counter == 25:
            return False
        tries_counter += 1

    return positions

def H_bridge(dict, positions, coords_next, coords_prev, coords):
    """determines if a H-bridge is present"""
    if coords != coords_next and coords != coords_prev and coords in positions:
        for i in range(len(positions)):
            element = 0
            if positions[i] == coords:
                element = i
                break
        if dict[element].get_type() == "H":
            return True
    return False

def stability(dict, index, positions):
    """Determines stability of protein"""

    stability = 0

    # Determines the neighbouring elements if element is able to form a H-bridge
    if dict[index].get_type() == "H":
        x_coord, y_coord, z_coord = dict[index].get_location()
        coords = f"{x_coord},{y_coord},{z_coord}"
        coords_x_plus = f"{x_coord + 1},{y_coord},{z_coord}"
        coords_x_min = f"{x_coord - 1},{y_coord},{z_coord}"
        coords_y_plus = f"{x_coord},{y_coord + 1},{z_coord}"
        coords_y_min = f"{x_coord },{y_coord - 1},{z_coord}"
        coords_z_plus = f"{x_coord},{y_coord},{z_coord + 1}"
        coords_z_min = f"{x_coord},{y_coord},{z_coord - 1}"

        if index != 0:
            coords_prev = positions[index - 1]
        else:
            coords_prev = None
        if index != len(positions) - 1:
            coords_next = positions[index + 1]
        else:
            coords_next = None

        # Checks if H-bridges have been formed
        if H_bridge(dict, positions, coords_next, coords_prev, coords_x_plus) == True:
            stability -= 1
        if H_bridge(dict, positions, coords_next, coords_prev, coords_x_min) == True:
            stability -= 1
        if H_bridge(dict, positions, coords_next, coords_prev, coords_y_plus) == True:
            stability -= 1
        if H_bridge(dict, positions, coords_next, coords_prev, coords_y_min) == True:
            stability -= 1
        if H_bridge(dict, positions, coords_next, coords_prev, coords_z_plus) == True:
            stability -= 1
        if H_bridge(dict, positions, coords_next, coords_prev, coords_z_min) == True:
            stability -= 1

    return stability


def sarw_dict(lattice, moves):
    """Performs self avoiding random walk on the given protein and determines the stability"""
    list = lattice.get_list()
    dict = lattice.get_dict()

    positions = []
    stability_count = 0

    # performs each random step returns stability 1 if the walk gets stuck
    for i in range(len(list)):
        positions = move_no_backtrack(list, dict, positions, i, moves)
        if positions == False:
            return dict, 1

    # Counts the stability per element of the protein
    for i in range(len(list)):
        stability_element = stability(dict, i, positions)
        stability_count += stability_element

    # Divided by 2 because all h-bridges are counted twice
    stability_count /= 2
    return dict, stability_count
