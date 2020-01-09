import random

def random_direction():
    """Returns random direction"""
    directions = [1, 1, 2, 2, 3, 3]
    direction = random.choice(directions)
    return direction
    
print(random_direction)
