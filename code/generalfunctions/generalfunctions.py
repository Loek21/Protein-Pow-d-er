import statistics
import random
import xlsxwriter

def make_move(move, x, y, z):
    """Takes a move and updates x, y, z coordinates based on move made"""

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
    """Takes a list of elements and calculates the stability of the configuration"""
    stability = 0

    # Check for successive H's in chain itself and add 2 per pair found
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

    # Check the neighbouring elements
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

    # Divide stability by 2 since all pairs are checked twice
    stability /= 2

    return stability

def get_best_state(stability_list, state_list):
    """Returns best state and stability from a list of states and stabilities"""
    best_stability = 1
    best_state = 0
    for i in range(len(state_list)):
        if stability_list[i] < best_stability:
            best_stability = stability_list[i]
            best_state = state_list[i]

    return best_state, best_stability


def list_stats(solutions_list, algorithm):
    """Gives a brief report on the statistics of a list"""
    mean = statistics.mean(solutions_list)
    median = statistics.median(solutions_list)
    stdev = round(statistics.stdev(solutions_list), 3)
    best_found = min(solutions_list)
    worst_found = max(solutions_list)

    return f"STABILITY STATISTICS FOR {algorithm}\nN: {len(solutions_list)} \nMean: {mean} \nMedian: {median} \nStandard deviation: {stdev} \nBest result: {best_found} \nWorst result: {worst_found}"


def stringmaker(protein_length, model, *args):
    """Allows user to create their own random string"""

    protein = ''
    elements = []

    if model == 'HP':
        elements = ['H', 'P']

    elif model == 'HPC':
        elements = ['H', 'P', 'C']

    for _ in range(protein_length):
        protein += str(random.choice(elements))

    return protein

def write_to_worksheet(stability_list, string_nr, algorithm):
    workbook = xlsxwriter.Workbook(f'Data/{algorithm}_{string_nr}.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(len(stability_list)):
        worksheet.write(i, 0, stability_list[i])
    workbook.close()
