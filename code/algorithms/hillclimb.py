from .generalfunctions import stability_calculator, make_move
import copy
import random

def pullmove(chain, stability, iterations):
    """Hill climb algorithm based on diagonal pull moves"""

    # save current best chains and stabilities
    best_chain = chain
    best_stability = stability

    i = 0

    max_reached = False
    while i < iterations:
        if max_reached == True:
            break

        new_chain = copy.deepcopy(best_chain)
        new_chain_stability = copy.deepcopy(best_stability)
        moves_tried = 0
        for element in range(1, len(new_chain)):
            new_chain = copy.deepcopy(best_chain)
            new_chain_stability = copy.deepcopy(best_stability)

            amino = new_chain[element]
            previous_amino = new_chain[element - 1]
            move = makepull(new_chain, new_chain[element])

            if move == None:
                moves_tried += 1
                if moves_tried == len(chain):
                    max_reached = True
                continue

            i += 1
            moves_tried = 0

            diagonal = move[0]
            adjacent = move[1]

            # set current element and the previous one to the move made
            amino.set_coordinates(diagonal[0], diagonal[1], diagonal[2])
            previous_amino.set_coordinates(adjacent[0], adjacent[1], adjacent[2])

            for other_element in range(element - 2):
                other_amino = new_chain[other_element]
                amino_ahead = new_chain[other_element + 2]

                x, y, z = amino_ahead.get_location()

                other_amino.set_coordinates(x, y, z)

            new_chain_stability = stability_calculator(new_chain)
            print(new_chain)
            print(new_chain_stability)

            if new_chain_stability <= best_stability:
                print(new_chain_stability, best_stability)
                best_stability = new_chain_stability
                best_chain = new_chain

    print(best_chain)
    return best_chain, best_stability

    

def makepull(chain, element):

    x, y, z = element.get_location()

    possible_diagonals = []

    taken_coords = []
    for element in chain:
        taken_coords.append(element.get_location())

    for coords in ((x + 1, y, z + 1), (x + 1, y, z - 1), (x + 1, y - 1, z), (x + 1, y + 1, z), (x, y - 1, z - 1), (x, y - 1, z + 1), (x - 1, y - 1, z), (x - 1, y, z + 1), (x - 1, y, z - 1), (x - 1, y + 1, z), (x, y + 1, z + 1), (x, y + 1, z - 1)):
        
        if coords not in taken_coords:

            if coords == (x + 1, y, z + 1):
                if (x, y, z + 1) not in taken_coords:
                    possible_diagonals.append((coords, (x, y, z + 1)))
                if (x + 1, y, z) not in taken_coords:
                    possible_diagonals.append((coords, (x + 1, y, z)))


            elif coords == (x + 1, y, z - 1):
                if (x, y, z - 1) not in taken_coords:
                    possible_diagonals.append((coords, (x, y, z - 1)))
                if (x + 1, y, z) not in taken_coords:
                    possible_diagonals.append((coords, (x + 1, y, z)))

            elif coords == (x + 1, y - 1, z):
                if (x + 1, y, z) not in taken_coords:
                    possible_diagonals.append((coords, (x + 1, y, z)))
                if (x, y - 1, z) not in taken_coords:
                    possible_diagonals.append((coords, (x, y - 1, z)))

            elif coords == (x + 1, y + 1, z):
                if (x + 1, y, z) not in taken_coords:
                    possible_diagonals.append((coords, (x + 1, y, z)))
                if (x, y + 1, z) not in taken_coords:
                    possible_diagonals.append((coords, (x, y + 1, z)))

            elif coords == (x, y - 1, z - 1):
                if (x, y - 1, z) not in taken_coords:
                    possible_diagonals.append((coords, (x, y - 1, z)))
                if (x, y, z - 1) not in taken_coords:
                    possible_diagonals.append((coords, (x, y, z - 1)))

            elif coords == (x, y - 1, z + 1):
                if (x, y - 1, z) not in taken_coords:
                    possible_diagonals.append((coords, (x, y - 1, z)))
                if (x, y, z + 1) not in taken_coords:
                    possible_diagonals.append((coords, (x, y, z + 1)))

            elif coords == (x - 1, y - 1, z):
                if (x - 1, y, z) not in taken_coords:
                    possible_diagonals.append((coords, (x - 1, y, z)))
                if (x, y - 1, z) not in taken_coords:
                    possible_diagonals.append((coords, (x, y - 1, z)))

            elif coords == (x - 1, y, z + 1):
                if (x - 1, y, z) not in taken_coords:
                    possible_diagonals.append((coords, (x - 1, y, z)))
                if (x, y, z + 1) not in taken_coords:
                    possible_diagonals.append((coords, (x, y, z + 1)))

            elif coords == (x - 1, y, z - 1):
                if (x - 1, y, z) not in taken_coords:
                    possible_diagonals.append((coords, (x - 1, y, z)))
                if (x, y, z - 1) not in taken_coords:
                    possible_diagonals.append((coords, (x, y, z - 1)))

            elif coords == (x - 1, y + 1, z):
                if (x - 1, y, z) not in taken_coords:
                    possible_diagonals.append((coords, (x - 1, y, z)))
                if (x, y + 1, z) not in taken_coords:
                    possible_diagonals.append((coords, (x, y + 1, z)))

            elif coords == (x, y + 1, z + 1):
                if (x, y + 1, z) not in taken_coords:
                    possible_diagonals.append((coords, (x, y + 1, z)))
                if (x, y, z + 1) not in taken_coords:
                    possible_diagonals.append((coords, (x, y, z + 1)))

            elif coords == (x, y + 1, z - 1):
                if (x, y + 1, z) not in taken_coords:
                    possible_diagonals.append((coords, (x, y + 1, z)))
                if (x, y, z - 1) not in taken_coords:
                    possible_diagonals.append((coords, (x, y, z - 1)))

    if len(possible_diagonals) > 0:
        move = random.choice(possible_diagonals)
        return move


    return None
            



    




