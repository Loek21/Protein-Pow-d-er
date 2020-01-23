import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def chain_list_3Dplot(chain, stability):
    """Plots scatter plot of lattice (list is string of protein)"""
    element_list = []
    x_list = []
    y_list = []
    z_list = []
    for element in chain:
        element_list.append(element.type)
        x_list.append(element.x_coord)
        y_list.append(element.y_coord)
        z_list.append(element.z_coord)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(x_list)):
        if element_list[i] == "H":
            ax.scatter(x_list[i], y_list[i], z_list[i], c="red")
        elif element_list[i] == "C":
            ax.scatter(x_list[i], y_list[i], z_list[i], c="green")
        else:
            ax.scatter(x_list[i], y_list[i], z_list[i], c="blue")
    ax.plot(x_list, y_list, z_list, c="black")
    plt.title(f"stability = {stability}", fontsize=20)
    plt.show()
