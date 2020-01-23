from .generalfunctions import stability_calculator, make_move
import copy

def pullmove(chain, stability, iterations):
    """Hill climb algorithm based on diagonal pull moves"""

    # save current best chains and stabilities
    best_chain = chain
    best_stability = stability

    i = 0
    while i < iterations:
        i += 1
        new_chain = copy.deepcopy(best_chain)
        new_chain_stability = best_stability

        for element in new_chain:

            """
            LOGIC FOR THE PULL MOVE HERE
            """

            new_chain_stability = stability_calculator(new_chain)

            if new_chain_stability < best_stability:
                best_stability = new_chain_stability
                best_chain = new_chain

    

def makepull(chain, element):

    x, y, z = element.get_location()

    do_move = False

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

    return possible_diagonals
            



    




