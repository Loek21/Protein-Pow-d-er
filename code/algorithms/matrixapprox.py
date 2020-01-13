# Linear approximation method based on Alantha Newman's article
# A new algorithm for protein folding in HP model
# It guartees a solution with approximation factor of 1/3

import random

def approximation():

    matrix = lattice.get_matrix_twoD
    list = lattice.get_list

    even_H_counter = 0
    odd_H_counter = 0

    for element in list:
        type = element.get_type()
        even_odd = element.get_even_odd()
        if type == "H" and even_odd == "even":
            even_H_counter += 1
        elif type == "H" and even_odd == "odd":
            odd_H_counter += 1

    # Alters the chain so it has equal number of odd and even H's
    if odd_H_counter != even_H_counter:
        if odd_H_counter > even_H_counter:
            number_of_changes = odd_H_counter - even_H_counter
            change_even_odd = "odd"

        if even_H_counter > odd_H_counter:
            number_of_changes = even_H_counter - odd_H_counter
            change_even_odd = "even"

        # Changes a random even or odd H into a P
        counter = 0
        while counter < number_of_changes:
            randomnr = random.randint(0, len(list) - 1)
            type = list[randomnr].get_type()
            even_odd = list[randomnr].get_even_odd()
            if type == "H" and change_even_odd == even_odd:
                list[randomnr].type = "P"
                counter += 1
