import itertools
import copy
import random

def permutations_maker(moves, piece_length):
    permutations = [p for p in itertools.product(moves, repeat=piece_length)]

    # for moveset in range(len(permutations) - 1):
    #     for move in range(len(moveset) - 1):
    #         if moveset[move] == - moveset[move + 1]:
    #             moveset.remove()



    return permutations


def eha(lattice, moves, subchain_length):
    """
    Extended Heuristic Algorithm version.
    Cuts chain up in smaller pieces and goes
    through all permutations per chain to find
    optimal fold.
    """

    # get a matrix to work in and save elements into
    matrix = lattice.get_matrix()

    # get current HP-chain
    chain = lattice.get_list()

    # define a length of the pieces
    piece_length = subchain_length

    # get all permutations of moves you can make
    permutations = permutations_maker(moves, subchain_length)

    # fix first 2 elements in the matrix
    current_x = int(len(matrix) * 0.5 - 1)
    current_y = int(len(matrix) * 0.5 - 1)
    current_z = int(len(matrix) * 0.5 - 1)
    matrix[current_x][current_y][current_z] = lattice.lattice_list[0]

    # give these element objects the corresponding coordinates
    lattice.lattice_list[0].set_coordinates(current_x, current_y, current_z)
    current_x += 1
    matrix[current_x][current_y][current_z] = lattice.lattice_list[1]
    lattice.lattice_list[1].set_coordinates(current_x, current_y, current_z)

    # getting all the pieces of the remaining chain into separate lists
    piece_list = []
    piece = []
    for i in range(len(chain[2:])):
        piece.append(chain[i+2])
        if len(piece) % piece_length == 0:
            piece_list.append(piece)
            piece = []

        if i == len(chain[2:]) - 1:
            piece_list.append(piece)

        
    best_matrix = None
    best_stability = 1
    print(piece_list)
    # run until all pieces have been set
    for piece in piece_list:

        # since some piece lists contain an empty last list due to final append, just break when there is one
        if len(piece) == 0:
            break
        
        # save the best moves made for a piece, 
        # so the elements can take over those coordinates at the end of the loop
        best_moves = []
        print(f"PIECE {piece}")
        counter = 0
        for moveset in permutations:
            counter += 1
            # print(f"MOVESET {counter}")
            dummy_matrix = copy.deepcopy(matrix)
            elements_coords = []
            check_score = True

            # set up 'future' coords
            future_x = current_x
            future_y = current_y
            future_z = current_z

            # loop over moves and elements simultaneously since they pair up
            for (move, element) in zip(moveset, piece):
                # ADD ALL ELEMENTS OF PIECE TO GRID

                # update coords according to move
                if move == 1:
                    future_x += 1
                
                elif move == -1:
                    future_x -= 1
    
                elif move == 2:
                    future_y -=  1
                    
                elif move == -2:
                    future_y += 1

                elif move == 3:
                    future_z -= 1
                    
                elif move == -3:
                    future_z += 1
                
                # if move hits the border, cancel the move
                if (future_x == 0) or (future_y == 0) or (future_z == 0) or (future_x == len(matrix) - 1) or (future_y == len(matrix) - 1) or (future_z == len(matrix) - 1):
                    continue

                # if the coords aren't yet occupied, set element there
                if dummy_matrix[future_x][future_y][future_z] == None:
                    dummy_matrix[future_x][future_y][future_z] = element
                    element.set_coordinates(future_x, future_y, future_z)
                    elements_coords.append([future_x, future_y, future_z])
                
                # else break out of this moveset and try the next one
                else:
                    check_score = False
                    break
            
            # if check score is False, don't check the stability
            if check_score == False:
                continue
            
            # at the end of the moveset, count the score, saving the best score and setting up the elements with the coords of best score
            stability = 0

            # check for successive H's in chain itself and add 2 per pair found
            # since the matrix checker checks every pair twice, so need to compensate
            for element in range(len(chain) - 1):
                if chain[element].type == 'H' and chain[element + 1].type == 'H':
                    stability += 2
            
            # check the neighbouring elements
            for element in range(len(chain)):
                i = chain[element].x_coord
                j = chain[element].y_coord
                k = chain[element].z_coord

                if not hasattr(dummy_matrix[i][j][k], 'type'):
                    break
                
                if dummy_matrix[i][j][k].type == 'H':
                    if dummy_matrix[i-1][j][k] != None:
                        if dummy_matrix[i-1][j][k].type == 'H':
                            stability -= 1
                    if dummy_matrix[i+1][j][k] != None:
                        if dummy_matrix[i+1][j][k].type == 'H':
                            stability -= 1
                    if dummy_matrix[i][j-1][k] != None:
                        if dummy_matrix[i][j-1][k].type == 'H':
                            stability -= 1
                    if dummy_matrix[i][j+1][k] != None:
                        if dummy_matrix[i][j+1][k].type == 'H':
                            stability -= 1
                    if dummy_matrix[i][j][k+1] != None:
                        if dummy_matrix[i][j][k+1].type == 'H':
                            stability -= 1
                    if dummy_matrix[i][j][k-1] != None:
                        if dummy_matrix[i][j][k-1].type == 'H':
                            stability -= 1

            # divide stability by 2 since pairs are checked twice
            stability /= 2
            #print(stability)
            if stability <= best_stability:
                if stability == best_stability and random.random() < 0.05:
                    best_stability = stability
                    best_matrix = dummy_matrix
                    best_moves = elements_coords

                else:
                    best_stability = stability
                    best_matrix = dummy_matrix
                    best_moves = elements_coords

        # update the element coordinates corresponding to best moves found
        for (element, coords) in zip(piece, best_moves):
            element.set_coordinates(coords[0], coords[1], coords[2])
            current_x = coords[0]
            current_y = coords[1]
            current_z = coords[2]

        # update the matrix to be the best one with the piece in place
        #print(best_matrix)

        matrix = best_matrix

    return best_stability, chain



