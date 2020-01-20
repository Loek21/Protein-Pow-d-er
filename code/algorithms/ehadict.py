import itertools
import copy
import random

def permutations_maker(moves, piece_length):
    """Makes all permutations for a chain and prunes some easy mistakes"""
    permutations = [p for p in itertools.product(moves, repeat=piece_length)]
    perms_pruned = []

    # prune the permutation list
    for moveset in permutations:
        take_moves = True

        # filter out back and forth moves
        for move in range(len(moveset) - 1):
            if moveset[move] == - moveset[move + 1]:
                take_moves = False
                break
        
        # filter out too large straight moves
        for move in range(len(moveset) - 3):
            if moveset[move] == moveset[move + 1] and moveset[move] == moveset[move + 2] and moveset[move] == moveset[move + 3]:
                take_moves = False
                break
        
        # filter out circular moves
        for move in range(len(moveset) - 3):
            if moveset[move] == -moveset[move + 2] and moveset[move + 1] == -moveset[move + 3]:
                take_moves = False
                break

        if take_moves == True:
            perms_pruned.append(moveset) 

    print(len(permutations))
    print(len(perms_pruned))

    return perms_pruned

def chain_divider(chain, subchain_length):
    """Divides a chain such that the last element is an H"""

    # lists to create and save the pieces
    piece_list = []
    piece = []

    # go through the entire chain, making pieces that end with an H and saving those pieces
    for i in range(len(chain[2:])):
        
        # the piece will end if there's a P after an H and if the piece length is still managable
        if chain[i+2].type == 'P' and chain[i+1].type == 'H' and len(piece) > subchain_length - 3 and len(piece) <= subchain_length + 1:
            piece_list.append(piece)
            piece = []
        
        piece.append(chain[i+2])

        # if the piece exceeds the given length by 2, end piece anyway
        if len(piece) > subchain_length + 1:
            piece_list.append(piece)
            piece = []

        # at the final element, end the piece that's left over
        if i == len(chain[2:]) - 1:
            piece_list.append(piece)
            
    return piece_list


def eha_list(lattice, moves, subchain_length):
    """
    Extended Heuristic Algorithm version.
    Cuts chain up in smaller pieces and goes
    through all permutations per chain to find
    optimal fold.
    """

    # get current HP-chain
    chain = lattice.get_list()

    # cut the chain in pieces according to the subchain_length
    piece_list = chain_divider(chain, subchain_length)

    # fix first 2 elements in the matrix
    current_x = int(len(chain) * 0.5 - 1)
    current_y = int(len(chain) * 0.5 - 1)
    current_z = int(len(chain) * 0.5 - 1)

    # give these element objects the corresponding coordinates
    lattice.lattice_list[0].set_coordinates(current_x, current_y, current_z)
    current_x += 1
    lattice.lattice_list[1].set_coordinates(current_x, current_y, current_z)
    
    # give upper bound to stability to start with
    best_stability = 100

    # run until all pieces have been set
    for piece in piece_list:

        # get the permutations according to the length of the piece
        permutations = permutations_maker(moves, len(piece))

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
            if counter % 50000 == 0:
                print("MOVESET", counter)
            elements_coords = []
            check_score = True

            # reset the piece's elements' locations to None
            for element in piece:
                element.set_coordinates(None, None, None)

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
                if (future_x == 0) or (future_y == 0) or (future_z == 0) or (future_x == len(chain) - 1) or (future_y == len(chain) - 1) or (future_z == len(chain) - 1):
                    check_score = False
                    break

                # if the coords aren't yet occupied, set element there
                occupied = False
                for amino in chain:
                    if amino.get_location() == (future_x, future_y, future_z):
                        occupied = True
                        break

                if occupied == False:
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
            for element in chain:
                if element.type == 'H':
                    i = element.x_coord
                    j = element.y_coord
                    k = element.z_coord

                    if (i or j or k) == None:
                        break

                    for other_element in chain:
                        if other_element.type == 'H':
                            if other_element.get_location() == (i - 1, j, k) or \
                            other_element.get_location() == (i + 1, j, k)  or \
                            other_element.get_location() == (i, j - 1, k)  or \
                            other_element.get_location() == (i, j + 1, k)  or \
                            other_element.get_location() == (i, j, k - 1) or \
                            other_element.get_location() == (i, j, k + 1):
                                stability -= 1


            # divide stability by 2 since pairs are checked twice
            stability /= 2
            
            if stability == best_stability and random.random() < 0.05:
                best_stability = stability
                best_moves = elements_coords

            elif stability < best_stability:
                print("NEW STAB", stability)
                best_stability = stability
                best_moves = elements_coords
        
        # update the element coordinates corresponding to best moves found
        for (element, coords) in zip(piece, best_moves):
            element.set_coordinates(coords[0], coords[1], coords[2])
            current_x = coords[0]
            current_y = coords[1]
            current_z = coords[2]

        # update the matrix to be the best one with the piece in place
        #print(best_matrix)

        #matrix = best_matrix

    return best_stability, chain



