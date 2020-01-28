import random
from ..generalfunctions.generalfunctions import stability_calculator, make_move

def move_no_backtrack(chain_list, index, moves):
    """Performs random movement without backtracking"""
    switch = True
    tries_counter = 0
    if index == 0:
        x_coord = 0
        y_coord = 0
        z_coord = 0
        chain_list[0].set_coordinates(0, 0, 0)
    else:
        x_coord, y_coord, z_coord = chain_list[index].get_location()

    # Tries finding the next valid position
    while switch:
        direction = random.choice(moves)
        new_x_coord, new_y_coord, new_z_coord = make_move(direction, x_coord, y_coord, z_coord)

        occupied = False
        for j in range(len(chain_list) - 1):
            occupied_x, occupied_y, occupied_z = chain_list[j].get_location()
            if (occupied_x, occupied_y, occupied_z) == (new_x_coord, new_y_coord, new_z_coord):
                occupied = True

        if not occupied:
            chain_list[index].set_direction(direction)
            if index + 1 != len(chain_list):
                chain_list[index + 1].set_coordinates(new_x_coord, new_y_coord, new_z_coord)
            switch = False

        # If 50 attempts have been made to move and all failed the chain is stuck
        if tries_counter == 50:
            return False
        tries_counter += 1

    return True

def sarw_dict(lattice, moves):
    """Performs self avoiding random walk on the given protein and determines the stability"""
    chain_list = lattice.get_list()

    # Performs each random step returns stability None if the walk gets stuck
    for i in range(len(chain_list)):
        positions = move_no_backtrack(chain_list, i, moves)
        if not positions:
            return chain_list, None

    # Counts the stability per element of the protein
    stability = stability_calculator(chain_list)

    return chain_list, stability
