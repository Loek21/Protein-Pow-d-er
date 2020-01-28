import random
from ..generalfunctions.generalfunctions import stability_calculator, make_move

def greedy(lattice, moves):
    """Performs self avoiding Greedy walk on the given protein and determines the stability"""
    chain_list = lattice.get_list()

    # Performs each random step returns stability None if the walk gets stuck
    for i in range(len(chain_list)):
        positions = greedy_move_no_backtrack(chain_list, i, moves)
        if not positions:
            return chain_list, None

    # Counts the stability per element of the protein
    stability = stability_calculator(chain_list)

    return chain_list, stability

def greedy_move_no_backtrack(chain_list, index, moves):
    """ Performs greedy movement for 1 element with 1 lookahead without backtracking """
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
        # Make new list of moves that return highest stability
        greedy_moves = greedy_calc_move(chain_list, index, moves)

        # Select move out of greedy_moves
        direction = random.choice(greedy_moves)
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

def greedy_calc_move(chain_list, index, moves):
    """ Returns stability of an assumed move """

    # If next element is P, return random move, because no impact on stability
    if chain_list[index].type == 'P':
        return moves

    # If next element is H or C, start checking for stability per move.
    if chain_list[index].type == 'H' or 'C':
        best_moves = []
        best_stab = 0

        for move in moves:
            # Define lookahead coords
            lookahead_x, lookahead_y, lookahead_z = make_move(move, chain_list[index].x_coord,
                                                              chain_list[index].y_coord,
                                                              chain_list[index].z_coord)
            test_stab = 0

            for i in chain_list:
                # Start iteration over list to check for neighour H/C elements
                if i is None:
                    if i.get_location() == (lookahead_x - 1, lookahead_y, lookahead_z) or \
                    i.get_location() == (lookahead_x + 1, lookahead_y, lookahead_z)  or \
                    i.get_location() == (lookahead_x, lookahead_y - 1, lookahead_z)  or \
                    i.get_location() == (lookahead_x, lookahead_y + 1, lookahead_z)  or \
                    i.get_location() == (lookahead_x, lookahead_y, lookahead_z - 1) or \
                    i.get_location() == (lookahead_x, lookahead_y, lookahead_z + 1):

                        # Amend test_stab accordingly to found neigbours
                        if chain_list[index].type == 'C' and i.type == 'C':
                            test_stab -= 5
                        else:
                            test_stab -= 1
            # Adjust best moveset and highest stability accordingly
            best_moves, best_stab = compare_stability(move, test_stab, best_stab, best_moves)

        return best_moves

def compare_stability(move, test_stab, best_stab, best_moves):
    """
    Compares the stability of a potential move against the up till now best stability and amends
    best_moves accordingly
    """
    # If potential move has stability equal to up till now best stability, append move to best_moves
    if test_stab == best_stab:
        best_moves.append(move)

    # If potential move has higher stability then up till now best stability,
    # amend up till now best calculated stability and moveset
    elif test_stab < best_stab:
        best_stab = test_stab
        best_moves = []
        best_moves.append(move)

    # If potential move has lower stability then up till now best stability of other
    # potential moves, do not append to best_moves
    else:
        pass

    return best_moves, best_stab
