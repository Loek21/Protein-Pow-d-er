"""
Algorithm that calculates the highest stability of a given string according to a 'greedy algorithm'
"""

import random
import sys

def greedy(lattice, moves):

    # Build Matrix
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

        for move in moves:
            
            # pick a greedy move
            #if matrix[current_x][current_y][current_z].type == 'P':
                # P element placed randomly, since no change to stability
            #    move = random.choice(moves)
            
            #elif matrix[current_x][current_y][current_z].type == 'H':
                # make list of best_moves and choose randomly from list
            #    best_moves = []
            #    best_move_score = 0
                
            #    for move in moves:
            #        if matrix
            #        for mat in matrix:
            #            if matrix[current_x + move][current_y][current_z].type == 'H':
                        #matrix[current_x][current_y + move][current_z].type == 'H' or\
                        #matrix[current_x][current_y][current_z + move].type == 'H':
            #                best_moves.append(move)

             #   move = random.choice(best_moves)
            #else:
            #    print("Error. Element in Protein String not recognized")
            #    sys.exit(1)

            # update current coords
            if move == 1:
                future_x = current_x + 1
            
            elif move == -1:
                future_x = current_x -1
   
            elif move == 2:
                future_y = current_y - 1
                 
            elif move == -2:
                future_y = current_y + 1

            elif move == 3:
                future_z = current_z - 1
                 
            elif move == -3:
                future_z = current_z + 1

            boundary_switch = True
            if (future_x == 0) or (future_y == 0) or (future_z == 0) or (future_x == len(matrix) - 1) or (future_y == len(matrix) - 1) or (future_z == len(matrix) - 1):
                boundary_switch = False

            # if coordinate is not yet taken, place element there and update its coords
            if matrix[future_x][future_y][future_z] == None and (boundary_switch == True):
                #print(current_x, current_y, move)
                # update current x, y and z
                current_x = future_x
                current_y = future_y
                current_z = future_z
                
                # set element
                matrix[current_x][current_y][current_z] = lattice.lattice_list[set_elements]
                lattice.lattice_list[set_elements].set_coordinates(current_x, current_y, current_z)
                set_elements += 1
                
                # calculate h neighbours
                temp_stab = 0
                if matrix[current_x][current_y][current_z].type == 'H':
                    if matrix[i-1][j][k] != None:
                        if matrix[i-1][j][k].type == 'H':
                            temp_stab -= 1
                    if matrix[i+1][j][k] != None:
                        if matrix[i+1][j][k].type == 'H':
                            temp_stab -= 1
                    if matrix[i][j-1][k] != None:
                        if matrix[i][j-1][k].type == 'H':
                            temp_stab -= 1
                        if matrix[i][j+1][k] != None:
                            if matrix[i][j+1][k].type == 'H':
                                temp_stab -= 1
                        if matrix[i][j][k+1] != None:
                            if matrix[i][j][k+1].type == 'H':
                                temp_stab -= 1
                        if matrix[i][j][k-1] != None:
                            if matrix[i][j][k-1].type == 'H':
                                temp_stab -= 1

                        # divide stability by 2 since pairs are checked twice
                        stability /= 2
            
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
                 
    lattice.matrix = matrix

    return lattice.matrix, do_count

def matrix_stability(lattice):
    """calculates stability of lattice with matrix"""
    elements = lattice.lattice_list
    
    mat = lattice.matrix
    stability = 0

    # check for successive H's in chain itself and add 2 per pair found
    # since the matrix checker checks every pair twice, so need to compensate
    for element in range(len(elements) - 1):
        if elements[element].type == 'H' and elements[element + 1].type == 'H':
            stability += 2
    
    # check the neighbouring elements
    for element in range(len(elements)):
        i = elements[element].x_coord
        j = elements[element].y_coord
        k = elements[element].z_coord

        if mat[i][j][k].type == 'H':
            if mat[i-1][j][k] != None:
                if mat[i-1][j][k].type == 'H':
                    stability -= 1
            if mat[i+1][j][k] != None:
                if mat[i+1][j][k].type == 'H':
                    stability -= 1
            if mat[i][j-1][k] != None:
                if mat[i][j-1][k].type == 'H':
                    stability -= 1
            if mat[i][j+1][k] != None:
                if mat[i][j+1][k].type == 'H':
                    stability -= 1
            if mat[i][j][k+1] != None:
                if mat[i][j][k+1].type == 'H':
                    stability -= 1
            if mat[i][j][k-1] != None:
                if mat[i][j][k-1].type == 'H':
                    stability -= 1

    # divide stability by 2 since pairs are checked twice
    stability /= 2

    return stability