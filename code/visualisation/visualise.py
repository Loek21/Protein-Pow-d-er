import matplotlib.pyplot as plt

def matrix_plot(matrix):
    """Plots matrix plot of lattice"""
    plt.matshow(matrix)
    plt.show()

def dict_plot(list, x_list, y_list, stability):
    """Plots scatter plot of lattice"""
    for i in range(len(x_list)):
        if list[i] == "H":
            plt.scatter(x_list[i], y_list[i], color="red")
        else:
            plt.scatter(x_list[i], y_list[i], color="blue")
    plt.plot(x_list, y_list, color="black")
    plt.title(f"stability = {stability}")
    plt.show()
