from .element import Element

"""Creates list version of the protein string containing AA (amino acid) element objects"""

class Lattice:
    def __init__(self, element_string):
        self.elements = element_string
        self.lattice_list = []

    def load_element(self, type):
        """Loads element object at the end of list"""
        self.lattice_list.append(Element(type))

    def load_list(self):
        """Takes string and adds element objects to a list"""
        for i in range(len(self.elements)):
            self.lattice_list.append(Element(self.elements[i]))

    def get_list(self):
        """Returns list of elements"""
        return self.lattice_list

    def __str__(self):
        return f"{self.lattice_list}"
