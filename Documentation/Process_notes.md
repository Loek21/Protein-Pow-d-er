# Process

## Random solutions

### Method 1
Using dict structure with coordinates, fold and element. Randomly fold elements.
pivot algorithm, self avoiding (random) walk

### Method 2
Using matrix structure with enumerated elements. Randomly fold elements.

### Method 3
Element objects


# Basic info over 2D protein folding algorithms (self-avoiding walk etc.)
Misschien niet helemaal relevant, maar wellicht interessant.
http://math.mit.edu/classes/18.417/Slides/HP-protein-prediction.pdf


Planning:
Week 1
Monday: Experimenting
Tuesday: 13:00 DL for primary experimenting


Aantekeningen Mentormeeting, Week 1
Code structuur in voorbeeld.
String helemaal uitleggen en daarna folden in plaats van stapje voor stapje.
OOP combineren

Main script klein houden. Voorbeeld repo heeft al die structuur.
Verwerk je algoritme in een class, en werk met OOP.

Eerst de hele string uitwerken en rest folden.

Grid of een dictionairy

qvdpost@gmail.com

## Time test
Matrix, random, 2D, 500000 tries, chain length=8: 23s
Dict, random, 2D, 500000 tries, chain length=8: 30s

Matrix, random, 2D, 100000 tries, chain length=50: 30s
Dict, random, 2D. 100000 tries, chain length=50: 34s

Matrix, random, 3D, 10000 tries, chain length=50: 1:47m
Dict, random, 3D, 10000 tries, chain length=50: 5s
