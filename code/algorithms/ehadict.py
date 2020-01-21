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
        
        # the piece will end if there's a P after a C (if cysteine is added) or H, and if the piece length is still managable
        if (chain[i+2].type == 'P' or chain[i+2].type == 'H') and chain[i+1].type == 'C' and len(piece) > subchain_length - 3 and len(piece) <= subchain_length + 1:
            piece_list.append(piece)
            piece = []
        
        elif chain[i+2].type == 'P' and chain[i+1].type == 'H' and len(piece) > subchain_length - 3 and len(piece) <= subchain_length + 1:
            piece_list.append(piece)
            piece = []
        
        piece.append(chain[i+2])

        # if the piece exceeds the given length by 2, end piece anyway
        if len(piece) > subchain_length + 1:
            piece_list.append(piece)
            piece = []

        # at the final element, end the piece that's left over
        if i == len(chain[2:]) - 1 and len(piece) > 0:
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

    # fix first 2 elements in the matrix, setting first coords to the origin of the grid
    current_x, current_y, current_z = 0, 0, 0

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

                # update coords according to move
                future_x, future_y, future_z = make_move(move, future_x, future_y, future_z)

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

            # calculate stability at end of moveset
            stability = stability_checker(chain)
            
            # if stability equal to highest found, 5% chance to accept this configuration
            if stability == best_stability and random.random() < 0.05:
                best_stability, best_moves = stability, elements_coords

            # if stability better than current best, accept this new configuration
            elif stability < best_stability:
                print("NEW STAB", stability)
                best_stability, best_moves = stability, elements_coords
        
        # update the element coordinates corresponding to best moves found
        for (element, coords) in zip(piece, best_moves):
            element.set_coordinates(coords[0], coords[1], coords[2])
            current_x, current_y, current_z = coords

    return best_stability, chain


def stability_checker(chain):
    """takes a list of elements and calculates the stability of the configuration"""
    stability = 0

    # check for successive H's in chain itself and add 2 per pair found
    # since the matrix checker checks every pair twice, so need to compensate
    for element in range(len(chain) - 1):
        if chain[element].type == 'H' and chain[element + 1].type == 'H':
            stability += 2
        
        elif chain[element].type == 'H' and chain[element + 1].type == 'C':
            stability += 2

        elif chain[element].type == 'C' and chain[element + 1].type == 'C':
            stability += 10

        elif chain[element].type == 'C' and chain[element + 1].type == 'H':
            stability += 2
    
    # check the neighbouring elements
    for element in chain:
        if element.type == 'H' or element.type == 'C':
            i = element.x_coord
            j = element.y_coord
            k = element.z_coord

            if (i or j or k) == None:
                break
            
            # C-C connections get 5 points, all other connections get 1 point
            for other_element in chain:
                if other_element.type == 'H' or other_element.type == 'C':
                    if other_element.get_location() == (i - 1, j, k) or \
                    other_element.get_location() == (i + 1, j, k)  or \
                    other_element.get_location() == (i, j - 1, k)  or \
                    other_element.get_location() == (i, j + 1, k)  or \
                    other_element.get_location() == (i, j, k - 1) or \
                    other_element.get_location() == (i, j, k + 1):

                        if element.type == 'C' and other_element.type == 'C':
                            stability -= 5
                        else:
                            stability -= 1
    
    # divide stability by 2 since all pairs are checked twice
    stability /= 2

    return stability


def make_move(move, x, y, z):
    """takes a move and updates x, y, z coordinates based on move made"""

    if move == 1:
        x += 1
    
    elif move == -1:
        x -= 1

    elif move == 2:
        y -=  1
        
    elif move == -2:
        y += 1

    elif move == 3:
        z -= 1
        
    elif move == -3:
        z += 1

    return x, y, z


