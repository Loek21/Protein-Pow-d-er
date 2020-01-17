from .element import Element
import numpy as np

"""Creates list or dictionary version of the protein string containing AA (amino acid) element objects"""

class Lattice:
    def __init__(self, element_string):
        self.elements = element_string
        self.lattice_list = []
        self.lattice_dict = {}
        self.matrix = None
        self.matrix_twoD = None

    def load_list(self):
        """Takes string and adds element objects to a list"""
        for i in range(len(self.elements)):
            self.lattice_list.append(Element(self.elements[i]))
            if i % 2 == 0:
                self.lattice_list[i].set_even_odd("even")
            else:
                self.lattice_list[i].set_even_odd("odd")

    def load_dict(self):
        """Takes string and adds element objects to a dictionary, the dictionary key is based on the index"""
        for i in range(len(self.elements)):
            self.lattice_dict[i] = Element(self.elements[i])

    def load_matrix(self):
        """Loads a 3D empty matrix which can be filled with objects, big enough so straight chains don't hit borders"""
# <<<<<<< HEAD
        dimension = int(len(self.elements)*2)
# =======
        dimension = int(len(self.elements)*0.8)
# >>>>>>> 606ff26f3cbdbd05b9da5c10c078e2dfded15892
        self.matrix = np.empty((dimension, dimension, dimension), dtype=object)

    def load_TwoD_matrix(self):
        """Loads a 2D empty matrix which can be filled with objects"""
        dimension = int(len(self.elements)*2)
        self.matrix_twoD = np.empty((dimension, dimension), dtype=object)

    def get_list(self):
        """Returns list of elements"""
        return self.lattice_list

    def get_dict(self):
        """Returns dictionary of elements"""
        return self.lattice_dict

    def get_matrix(self):
        """Returns 3D matrix of elements"""
        return self.matrix

    def get_matrix_twoD(self):
        """Returns 2D matrix of elements"""
        return self.matrix_twoD

    def __str__(self):
        return f"{self.lattice_list}"
