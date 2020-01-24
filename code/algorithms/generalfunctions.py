import statistics

# This file contains all the functions that have a function in all of the algorithms
# It contains:
# Next coordinate function, which takes the current position and direction and give the new position
# Stability calculator function, which takes the

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

def stability_calculator(chain):
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


def list_stats(solutions_list):
    """Gives a brief report on the statistics of a list"""
    mean = statistics.mean(solutions_list)
    stdev = round(statistics.stdev(solutions_list), 3)
    best_found = min(solutions_list)
    worst_found = max(solutions_list)

    return f"STABILITY STATISTICS \nMean: {mean} \nStandard deviation: {stdev} \nBest result: {best_found} \nWorst result: {worst_found}"

