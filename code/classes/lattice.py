from .element import Element

"""Creates list or dictionary version of the protein string containing AA (amino acid) element objects"""

class Lattice:
    def __init__(self, element_string):
        self.elements = element_string
        self.lattice_list = []
        self.lattice_dict = {}

    def load_list(self):
        """Takes string and adds element objects to a list"""
        for i in range(len(self.elements)):
            self.lattice_list.append(Element(self.elements[i]))

    def load_dict(self):
        """Takes string and adds element objects to a dictionary"""
        for i in range(len(self.elements)):
            self.lattice_dict[i] = Element(self.elements[i])

    def __str__(self):
        return self.lattice_list
