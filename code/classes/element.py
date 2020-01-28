"""
Element object, contains 3D coordinates, the direciton for the next object and type of the element (H,P or C)
"""

class Element:
    """ Creates a new element given a new type. Afterwards, the location must be set manually. """
    def __init__(self, type):
        self.type = type
        self.x_coord = None
        self.y_coord = None
        self.z_coord = None
        self.direction = None

    def set_coordinates(self, x_coord, y_coord, z_coord):
        """Sets object coordinates"""
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord

    def set_direction(self, direction):
        """Sets object direction"""
        self.direction = direction

    def get_type(self):
        """Gets object type"""
        return self.type

    def get_location(self):
        """Gets object location"""
        return self.x_coord, self.y_coord, self.z_coord

    def get_direction(self):
        """Gets object direction"""
        return self.direction

    def __repr__(self):
        """Returns string representation of object"""
        return f"{self.type}: ({self.x_coord},{self.y_coord},{self.z_coord})"
