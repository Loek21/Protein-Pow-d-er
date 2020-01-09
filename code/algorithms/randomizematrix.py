import random

def matrixrandomizer(lattice, moves):
    """Fills a matrix constructively with element objects"""

    matrix = lattice.get_matrix()

    # set the first 2 elements in the matrix since all possibilities result in the same structure
    current_x = int(len(matrix) * 0.5 - 1)
    current_y = int(len(matrix) * 0.5 - 1)
    matrix[current_x][current_y] = lattice.lattice_list[0]

    # give these element objects the corresponding coordinates
    lattice.lattice_list[0].set_coordinates(current_x, current_y, None)
    current_x += 1
    matrix[current_x][current_y] = lattice.lattice_list[1]
    lattice.lattice_list[1].set_coordinates(current_x, current_y, None)
    
    # 2 elements have been set in the matrix
    set_elements = 2

    while set_elements < len(lattice.elements):

        # set up 'future' coords
        future_x = current_x
        future_y = current_y

        # to circumvent getting stuck and losing time, try a max of 50 moves
        moves_tried = 0
        while moves_tried < 50:

            # pick a random move
            move = random.choice(moves)

            # update current coords
            if move == 1:
                future_x = current_x + 1
            
            elif move == -1:
                future_x = current_x -1
   
            elif move == 2:
                future_y = current_y - 1
                 
            elif move == -2:
                future_y = current_y + 1

            # if coordinate is not yet taken, place element there and update its coords
            if matrix[future_x][future_y] == None:
                print(current_x, current_y, move)
                # update current x and y
                current_x = future_x
                current_y = future_y
                print(current_x, current_y)
                # set element
                matrix[current_x][current_y] = lattice.lattice_list[set_elements]
                lattice.lattice_list[set_elements].set_coordinates(current_x, current_y, None)
                set_elements += 1
                break
            
            else:
                # reset 'future' coords for next loop
                future_x = current_x
                future_y = current_y
                print("FAIL")
                moves_tried += 1
                if moves_tried == 49:
                    print("BREAKING")
            
    
    lattice.matrix = matrix

    return lattice.matrix

