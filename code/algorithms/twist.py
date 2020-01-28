import random
from ..generalfunctions.generalfunctions import stability_calculator, make_move

def twist(lattice, moves, border_size):
    """Fills grid with elements randomly, but restricts their freedom of movement with a border"""

    chain = lattice.lattice_list

    # Fix first 2 elements in the matrix, setting first coords to the origin of the grid
    current_x, current_y, current_z = 0, 0, 0

    # Give these element objects the corresponding coordinates
    chain[0].set_coordinates(current_x, current_y, current_z)
    current_x += 1
    chain[1].set_coordinates(current_x, current_y, current_z)

    # Set up a boundary
    boundary = int(len(chain) * border_size)

    # 2 Elements have been set in the matrix
    set_elements = 2

    while set_elements < len(chain):

        # Set up 'future' coords
        future_x = current_x
        future_y = current_y
        future_z = current_z

        # To circumvent getting stuck and losing time, try a max of 50 moves
        moves_tried = 0

        while moves_tried < 50:

            # Pick a random move
            move = random.choice(moves)

            # Update coords according to move
            future_x, future_y, future_z = make_move(move, future_x, future_y, future_z)

            # Check if move crosses boundary, if so, don't make the move
            boundary_switch = True
            if abs(future_x) == boundary or abs(future_y) == boundary or abs(future_z) == boundary:
                boundary_switch = False

            # Check if the coords are taken
            occupied = False
            for amino in chain:
                if amino.get_location() == (future_x, future_y, future_z):
                    occupied = True
                    break

            # If coordinate is not yet taken and boundary not crosses,
            # place element there and update its coords
            if not occupied and boundary_switch:

                # Update current x, y and z
                current_x = future_x
                current_y = future_y
                current_z = future_z

                # Set element
                lattice.lattice_list[set_elements].set_coordinates(current_x, current_y, current_z)
                set_elements += 1
                break

            else:
                # Reset 'future' coords for next loop
                future_x = current_x
                future_y = current_y
                future_z = current_z
                moves_tried += 1

        # If more than 50 moves are made and thus problem is stuck, don't bother checking stability
        do_count = True
        if moves_tried == 50:
            do_count = False
            break

    # Calculate stability
    stability = None
    if do_count:
        stability = stability_calculator(lattice.lattice_list)

    return lattice.lattice_list, stability

def matrix_stability(lattice):
    """calculates stability of lattice with matrix"""
    elements = lattice.lattice_list

    mat = lattice.matrix
    stability = 0

    # Check for successive H's in chain itself and add 2 per pair found
    # since the matrix checker checks every pair twice, so need to compensate
    for element in range(len(elements) - 1):
        if elements[element].type == 'H' and elements[element + 1].type == 'H':
            stability += 2

    # Check the neighbouring elements
    for element in enumerate(elements):
        i = elements[element].x_coord
        j = elements[element].y_coord
        k = elements[element].z_coord

        if mat[i][j][k].type == 'H':
            if mat[i-1][j][k] is not None:
                if mat[i-1][j][k].type == 'H':
                    stability -= 1
            if mat[i+1][j][k] is not None:
                if mat[i+1][j][k].type == 'H':
                    stability -= 1
            if mat[i][j-1][k] is not None:
                if mat[i][j-1][k].type == 'H':
                    stability -= 1
            if mat[i][j+1][k] is not None:
                if mat[i][j+1][k].type == 'H':
                    stability -= 1
            if mat[i][j][k+1] is not None:
                if mat[i][j][k+1].type == 'H':
                    stability -= 1
            if mat[i][j][k-1] is not None:
                if mat[i][j][k-1].type == 'H':
                    stability -= 1

    # Divide stability by 2 since pairs are checked twice
    stability /= 2

    return stability
