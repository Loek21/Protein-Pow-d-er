import random
from ..generalfunctions.generalfunctions import stability_calculator, make_move

def move_no_backtrack(list, index, moves):
    """Performs random movement without backtracking"""
    switch = True
    tries_counter = 0
    if index == 0:
        x_coord = 0
        y_coord = 0
        z_coord = 0
        list[0].set_coordinates(0, 0, 0)
    else:
        x_coord, y_coord, z_coord = list[index].get_location()

    # Tries finding the next valid position
    while switch == True:
        direction = random.choice(moves)
        new_x_coord, new_y_coord, new_z_coord = make_move(direction, x_coord, y_coord, z_coord)

        occupied = False
        for j in range(len(list) - 1):
            occupied_x, occupied_y, occupied_z = list[j].get_location()
            if (occupied_x, occupied_y, occupied_z) == (new_x_coord, new_y_coord, new_z_coord):
                occupied = True

        if occupied == False:
            list[index].set_direction(direction)
            if index + 1 != len(list):
                list[index + 1].set_coordinates(new_x_coord, new_y_coord, new_z_coord)
            switch = False

        # If 50 attempts have been made to move and all failed the chain is stuck
        if tries_counter == 50:
            return False
        tries_counter += 1

    return True

def sarw_dict(lattice, moves):
    """Performs self avoiding random walk on the given protein and determines the stability"""
    list = lattice.get_list()

    # performs each random step returns stability 1 if the walk gets stuck
    for i in range(len(list)):
        positions = move_no_backtrack(list, i, moves)
        if positions == False:
            return list, 0

    # Counts the stability per element of the protein
    stability = stability_calculator(list)

    return list, stability
