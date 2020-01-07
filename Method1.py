import random
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

protein_string = "HPHHHPPHPPH"

def listify(string):
    """Creates list from string"""
    protein_list = []
    for i in range(len(string)):
        protein_list.append(string[i])
    return protein_list

def randomify():
    """Creates random number used for a random direction"""
    random_nr = 0
    while random_nr == 0:
        random_nr = random.randint(-2, 2)
    return random_nr

def coordinates(x_coord, y_coord, direction):
    """Uses old coordinates and direction to create new coordinates"""
    if direction == 1:
        new_x_coord = x_coord + 1
        new_y_coord = y_coord
    elif direction == -1:
        new_x_coord = x_coord - 1
        new_y_coord = y_coord
    elif direction == 2:
        new_x_coord = x_coord
        new_y_coord = y_coord + 1
    elif direction == -2:
        new_x_coord = x_coord
        new_y_coord = y_coord - 1
    return new_x_coord, new_y_coord

def plot(dict, stability):
    """Plots the data"""
    length = len(dict["positions"])
    x_list = []
    y_list = []
    color_list = []
    for i in range(length):
        x_coord = dict[i][2]
        y_coord = dict[i][3]
        x_list.append(x_coord)
        y_list.append(y_coord)
        if dict[i][1] == "H":
            plt.scatter(x_coord, y_coord, color="blue")
        else:
            plt.scatter(x_coord, y_coord, color="red")
    plt.plot(x_list, y_list, color="black")
    plt.title(f"stability = {stability}")
    plt.show()

def H_bridge(dict, list, coords):
    """determines if a H-bridge is present"""
    for j in range(len(list)):
        if dict["positions"][j] == coords:
            element = j
            break
    return element

def main():
    for x in range(100):
        counter = 0
        dict = {"positions": []}
        protein_list = listify(protein_string)
        for i in range(len(protein_list)):
            if counter != 25:
                counter = 0
            else:
                break

            # at first iteration set the coordinates as (0,0)
            if i == 0:
                x_coord = 0
                y_coord = 0
                dict[i] = [i, protein_list[i], x_coord, y_coord, 0]
            else:
                x_coord = dict[i][2]
                y_coord = dict[i][3]
            switch = True

            # Loops untill a valid position has been found
            while switch == True:

                # Make new direction
                direction = randomify()
                new_x_coord, new_y_coord = coordinates(x_coord, y_coord, direction)

                # Checks if new direction aims at an occupied space
                coords = f"{new_x_coord},{new_y_coord}"
                if coords not in dict["positions"]:
                    dict[i][4] = direction
                    if i + 1 != len(protein_list):
                        dict[i + 1] = [i + 1, protein_list[i + 1], new_x_coord, new_y_coord, 0]
                    dict["positions"].append(f"{x_coord},{y_coord}")
                    switch = False
                counter += 1
                if counter == 25:
                    print("stuck")
                    break

        # Skips this part if protein folding is invalid/overlaps
        if counter != 25:
            stability = 0
            for i in range(len(protein_list)):
                if dict[i][1] == "P":
                    x_coord = dict[i][2]
                    y_coord = dict[i][3]
                    coords = f"{x_coord},{y_coord}"
                    coords_left = f"{x_coord - 1},{y_coord}"
                    coords_right = f"{x_coord + 1},{y_coord}"
                    coords_up = f"{x_coord},{y_coord + 1}"
                    coords_down = f"{x_coord},{y_coord - 1}"
                    if i != 0:
                        coords_prev = dict["positions"][i - 1]
                    else:
                        coords_prev = None
                    if i != len(protein_list) - 1:
                        coords_next = dict["positions"][i + 1]
                    else:
                        coords_next = None
                    if coords_left != coords_next and coords_left != coords_prev and coords_left in dict["positions"]:
                        element = H_bridge(dict, protein_list, coords_left)
                        if dict[element][1] == "P":
                            stability -= 1
                    if coords_right != coords_next and coords_right != coords_prev and coords_right in dict["positions"]:
                        element = H_bridge(dict, protein_list, coords_right)
                        if dict[element][1] == "P":
                            stability -= 1
                    if coords_up != coords_next and coords_up != coords_prev and coords_up in dict["positions"]:
                        element = H_bridge(dict, protein_list, coords_up)
                        if dict[element][1] == "P":
                            stability -= 1
                    if coords_down != coords_next and coords_down != coords_prev and coords_down in dict["positions"]:
                        element = H_bridge(dict, protein_list, coords_down)
                        if dict[element][1] == "P":
                            stability -= 1
        print(x)

        # Prints graph if stability is lower than 0
        if stability != 0:
            stability = stability / 2
            plot(dict, stability)
            break
    return

main()
