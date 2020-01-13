# Process

## Random solutions

### Method 1
Using dict structure with coordinates, fold and element. Randomly fold elements.
pivot algorithm, self avoiding (random) walk

### Method 2
Using matrix structure with enumerated elements. Randomly fold elements.

### Method 3
Element objects


## Basic info over 2D protein folding algorithms (self-avoiding walk etc.)
Misschien niet helemaal relevant, maar wellicht interessant.
http://math.mit.edu/classes/18.417/Slides/HP-protein-prediction.pdf
misschien wel een goed idee voor een algorithm
http://dimacs.rutgers.edu/~alantha/papers2/string_fold.pdf
https://www.brown.edu/Research/Istrail_Lab/papers/1995/p157-hart.pdf


## Planning:
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

string[1] stability -7  (100000)
string[2] stability -9  (100000)
string[3] stability -13 (500000)

Dict, random, 3D, string[1], found in iterations: 3064, 1103, 2196, 532, 2353, 9225, 4170, 5860, 389, 11868
Dict, random, 3D, string[2], found in iterations: 33204, 20245, 152066, 193148, 45333, 92293, 14024, 198964, 9161, 110380
Dict, random, 3D, string[3], found in iterations: 2601, 536228, 715283, 130287, 1315365, 1197597, 546335, 461616, 145622, 251594
Matrix, size restriction 0.5 chain length, 3D, string[1], found in iterations: 1012, 120, 207, 1025, 280, 107, 338, 1235, 596, 636
Matrix, size restriction 0.5 chain length, 3D, string[2], found in iterations: 15944, 11761, 43390, 94921, 140415, 356, 109729, 55086, 284228, 6894
Matrix, size restriction 0.3 chain length, 3D, string[3], found in iterations: 139667, 568768, 192735, 229475, 135025, 6610, 114089, 210465, 15869, 102333
