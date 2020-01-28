"""Greedymatrix.py"""

import random
import sys
from .generalfunctions import make_move, stability_calculator

def greedy(lattice, moves):
    """This algorithm constructively fills a matrix with elements.
    Each element is randomly placed, choices limited by a greedy algorithm"""

    matrix = lattice.get_matrix()

    # set the first 2 elements in the matrix since all possibilities result in the same structure
    current_x = int(len(matrix) * 0.5 - 1)
    current_y = int(len(matrix) * 0.5 - 1)
    current_z = int(len(matrix) * 0.5 - 1)
    matrix[current_x][current_y][current_z] = lattice.lattice_list[0]

    # give these element objects the corresponding coordinates
    lattice.lattice_list[0].set_coordinates(current_x, current_y, current_z)
    current_x += 1
    matrix[current_x][current_y][current_z] = lattice.lattice_list[1]
    lattice.lattice_list[1].set_coordinates(current_x, current_y, current_z)

    # 2 elements have been set in the matrix
    set_elements = 2

    while set_elements < len(lattice.elements):

        # set up 'future' coords
        future_x = current_x
        future_y = current_y
        future_z = current_z

        # to circumvent getting stuck and losing time, try a max of 50 moves

        moves_tried = 0

        while moves_tried < 50:

            # pick a greedy move
            # if next element is 'P', move is random because no influence on stability
            if lattice.elements[set_elements] == 'P':
                move = random.choice(moves)

            # if next element is 'H' or 'C', check each surrounding spot
            elif lattice.elements[set_elements] == 'H' or 'C':

                best_moves = []
                best_stab = 0
                test_stab = 0

                for move in moves:
                    if move == 1:
                        test_stab = element_stability(lattice.matrix, lattice.elements[set_elements],
                                                      current_x + 1, current_y, current_z)
                        best_moves, best_stab = compare_stability(move, test_stab, best_stab, best_moves)
                    if move == -1:
                        test_stab = element_stability(lattice.matrix, lattice.elements[set_elements],
                                                      current_x - 1, current_y, current_z)
                        best_moves, best_stab = compare_stability(move, test_stab, best_stab, best_moves)
                    if move == 2:
                        test_stab = element_stability(lattice.matrix, lattice.elements[set_elements], current_x, current_y + 1, current_z)
                        best_moves, best_stab = compare_stability(move, test_stab, best_stab, best_moves)
                    if move == -2:
                        test_stab = element_stability(lattice.matrix, lattice.elements[set_elements], current_x, current_y - 1, current_z)
                        best_moves, best_stab = compare_stability(move, test_stab, best_stab, best_moves)
                    if move == 3:
                        test_stab = element_stability(lattice.matrix, lattice.elements[set_elements], current_x, current_y, current_z + 1)
                        best_moves, best_stab = compare_stability(move, test_stab, best_stab, best_moves)
                    if move == -3:
                        test_stab = element_stability(lattice.matrix, lattice.elements[set_elements], current_x, current_y, current_z - 1)
                        best_moves, best_stab = compare_stability(move, test_stab, best_stab, best_moves)

                move = random.choice(best_moves)

            # error, element is not P, H or C
            else:
                print("Error: Amino Acid in String not recognized. Ensure that input only contains H/P/C characters")
                sys.exit(1)

            # update current coords
            future_x, future_y, future_z = make_move(move, current_x, current_y, current_z)

            boundary_switch = True
            if (future_x == 0) or (future_y == 0) or (future_z == 0) or (future_x == len(matrix) - 1) or (future_y == len(matrix) - 1) or (future_z == len(matrix) - 1):
                boundary_switch = False

            # if coordinate is not yet taken, place element there and update its coords
            if (matrix[future_x][future_y][future_z]) is None and boundary_switch:
                # update current x, y and z
                current_x = future_x
                current_y = future_y
                current_z = future_z

                # set element
                matrix[current_x][current_y][current_z] = lattice.lattice_list[set_elements]
                lattice.lattice_list[set_elements].set_coordinates(current_x, current_y, current_z)
                set_elements += 1
                break
            
            else:
                # reset 'future' coords for next loop
                future_x = current_x
                future_y = current_y
                future_z = current_z
                moves_tried += 1

        do_count = True
        if moves_tried == 50:
            do_count = False
            #print("WHILE BROKEN")
            break
                 
    #lattice.matrix = matrix
    
    # calculate stability
    stability = 0
    if do_count == True:
        stability = stability_calculator(lattice.lattice_list)
        print(stability)

    return lattice.lattice_list, stability


def element_stability(matrix, element, x_coord, y_coord, z_coord):
    """calculates stability of one given element by checking surroundings """
    stability = 0
    if element == 'H':
        if matrix[x_coord-1][y_coord][z_coord] != None:
            if matrix[x_coord-1][y_coord][z_coord].type == 'H':
                stability -= 1
        if matrix[x_coord+1][y_coord][z_coord] != None:
            if matrix[x_coord+1][y_coord][z_coord].type == 'H':
                stability -= 1
        if matrix[x_coord][y_coord-1][z_coord] != None:
            if matrix[x_coord][y_coord-1][z_coord].type == 'H':
                stability -= 1
        if matrix[x_coord][y_coord+1][z_coord] != None:
            if matrix[x_coord][y_coord+1][z_coord].type == 'H':
                stability -= 1
        if matrix[x_coord][y_coord][z_coord+1] != None:
            if matrix[x_coord][y_coord][z_coord+1].type == 'H':
                stability -= 1
        if matrix[x_coord][y_coord][z_coord-1] != None:
            if matrix[x_coord][y_coord][z_coord-1].type == 'H':
                stability -= 1

    return stability

def compare_stability(move, test_stab, best_stab, best_moves):
    """Compares the stability of a potential move against the up till now best stability and amends best_moves accordingly"""
    # if potential move has stability equal to up till now best stability, append move to best_moves
    if test_stab == best_stab:
        best_moves.append(move)
    
    # if potential move has higher stability then up till now best stability, amend up till now best calculated stability,
    # clear best_moves of lower stability potential moves and append the potential move with higher stability
    elif test_stab < best_stab:
        best_stab = test_stab
        best_moves = []
        best_moves.append(move)
    
    # if potential move has lower stability then up till now best stability of other potential moves, 
    # disregard move and do not append to best_moves
    else:
        pass

    return best_moves, best_stab