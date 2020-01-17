import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def matrix_plot(matrix):
    """Plots matrix plot of lattice"""
    plt.matshow(matrix)
    plt.show()

def dict_plot_ThreeD(list, x_list, y_list, z_list, stability):
    """Plots scatter plot of lattice (list is string of protein)"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(x_list)):
        if list[i] == "H":
            ax.scatter(x_list[i], y_list[i], z_list[i], c="red")
        else:
            ax.scatter(x_list[i], y_list[i], z_list[i], c="blue")
    ax.plot(x_list, y_list, z_list, c="black")
    plt.title(f"stability = {stability}")
    plt.show()

def dict_plot_TwoD(list, x_list, y_list, stability):
    for i in range(len(x_list)):
        if list[i] == "H":
            plt.scatter(x_list[i], y_list[i], c="red")
        else:
            plt.scatter(x_list[i], y_list[i], c="blue")
    plt.plot(x_list, y_list, c="black")
    plt.title(f"stability = {stability}")
    plt.show()
