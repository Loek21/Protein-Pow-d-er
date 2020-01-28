import copy
import random
import math
from ..generalfunctions.generalfunctions import stability_calculator

def pullmove(chain, stability):
    """
    Hill climb algorithm based on diagonal pull moves with simulated annealing,
    returns best state and best stability
    """

    # Save current best chains and stabilities
    best_chain = chain
    chain_length = len(best_chain)
    best_stability = stability

    # Iteration count and temperature decreasing factor
    i = 0
    temp_factor = 1

    max_reached = False
    while i < 1000:

        # Will break if the chain isn't able in creating any new pull moves
        if max_reached:
            break

        moves_tried = 0

        # Takes next element in the chain and gets a list of all possible pull moves
        for element in range(1, len(best_chain) - 1):
            new_chain = copy.deepcopy(best_chain)
            new_chain_stability = copy.deepcopy(best_stability)

            moves_list = makepull(new_chain, new_chain[element], new_chain[element+1])

            # If no moves are possible it will try again untill
            if len(moves_list) == 0:
                moves_tried += 1
                if moves_tried == len(chain) * 10:
                    max_reached = True
                continue

            # Counts iteration only if a move has actually been made
            i += 1

            # Every 10 iterations the temperature factor is lowered by 0.01 cannot go lower than 0.001
            if i % 10 == 0:
                temp_factor -= 0.01
                if temp_factor < 0:
                    temp_factor = 0.001

            # A move is possible so the moves tried counter resets
            moves_tried = 0

            # Moves all previous elements to the position of the element two places ahead
            for other_element in range(element - 1):

                other_amino = new_chain[other_element]
                amino_ahead = new_chain[other_element + 2]

                x, y, z = amino_ahead.get_location()

                other_amino.set_coordinates(x, y, z)

            # Checks which move out of the possible pull moves list will give the best stability
            best_move = 0
            best_stability_move = 0
            for move in moves_list:
                new_move = copy.deepcopy(new_chain)
                new_move_stability = copy.deepcopy(new_chain_stability)
                amino = new_move[element]
                previous_amino = new_move[element - 1]

                diagonal = move[0]
                adjacent = move[1]

                # Set current element and the previous one to the move made
                amino.set_coordinates(diagonal[0], diagonal[1], diagonal[2])
                previous_amino.set_coordinates(adjacent[0], adjacent[1], adjacent[2])

                # Calculates new stability and determines if its better than the old best stability
                new_move_stability = stability_calculator(new_move)

                # Saves best possible pull move
                if new_move_stability <= best_stability_move:
                    best_stability_move = new_move_stability
                    best_move = new_move

            # Determines the simulated annealing acceptance probability and saves the new state based on it
            acceptance = acceptance_probability(chain_length, temp_factor, best_stability_move, best_stability)
            if acceptance:
                best_stability = best_stability_move
                best_chain = best_move

    return best_chain, best_stability

def makepull(chain, element, next_element):
    """Makes the pull move in diagonal direction, returns a list of all possible pull movements"""
    x, y, z = element.get_location()
    x_next, y_next, z_next = next_element.get_location()

    possible_diagonals = []
    taken_coords = []
    selected_diagonals = []

    # All possible coordinates for a diagonal move from the current element
    diagonal_coords = [(x + 1, y, z + 1), (x + 1, y, z - 1), (x + 1, y - 1, z), (x + 1, y + 1, z), (x, y - 1, z - 1),
                       (x, y - 1, z + 1), (x - 1, y - 1, z), (x - 1, y, z + 1), (x - 1, y, z - 1), (x - 1, y + 1, z),
                       (x, y + 1, z + 1), (x, y + 1, z - 1)]

    # All possible coordinates that are adjacent to the next protein element
    next_element_adj_coords = [(x_next + 1, y_next, z_next), (x_next - 1, y_next, z_next), (x_next, y_next + 1, z_next),
                               (x_next, y_next - 1, z_next), (x_next, y_next, z_next + 1),
                               (x_next, y_next, z_next - 1)]

    # Determines all the coordinates that are occupied
    for element in chain:
        taken_coords.append(element.get_location())

    for coords in diagonal_coords:

        if coords not in taken_coords:

            # Determines if there a free space adjacent to the diagonal coordinates
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

    # Saves only the pull moves that are adjacent to the next protein element
    for coords in possible_diagonals:
        if coords[0] in next_element_adj_coords:
            selected_diagonals.append(coords)

    return selected_diagonals

def acceptance_probability(length, factor, new_stability, old_stability):
    """Simulated annealing acceptance probability, returns true if new state is accepted otherwise false"""
    # Probability parameters based on literature
    temp = 10 * length
    k = 6 * length

    # Always accepts a more stable state
    if new_stability < old_stability:
        return True

    # Otherwise acceptance is given by the simulated annealing probability function
    probability = math.exp(-(new_stability - old_stability) / (k * temp * factor))
    random_nr = random.random()
    if random_nr <= probability:
        return True
    else:
        return False
