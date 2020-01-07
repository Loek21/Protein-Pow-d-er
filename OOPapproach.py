"""
OOP based approach 
"""

class Element:
    """ Creates a new element given a new letter. Afterwards, the location must be set manually. """
    # Initialize element
    def __init__(self, letter):
        self.letter = letter
        self.x_coord = 0
        self.y_coord = 0
    
    def __str__(self):
        print(f"this is {self.letter} at {self.x_coord}, {self.y_coord}")

    ## Setters
    def set_coordinates(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    # Getters
    def get_letter(self):
        return self.letter

    def get_location(self):
        return self.x_coord, self.y_coord