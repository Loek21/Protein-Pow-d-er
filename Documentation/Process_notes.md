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



# New best structure found for the 50 length chain. Better than literature with -27. The element list is:
[H: (24,24,24), None., H: (25,24,24), None., P: (25,24,25), None., H: (24,24,25), None., P: (24,23,25), None., H: (24,23,24), None., P: (23,23,24), None., H: (23,24,24), None., P: (23,25,24), None., H: (24,25,24), None., H: (25,25,24), None., H: (25,25,25), None., H: (24,25,25), None., P: (23,25,25), None., H: (23,24,25), None., P: (23,23,25), None., P: (23,23,26), None., P: (24,23,26), None., H: (24,24,26), None., P: (25,24,26), None., P: (25,23,26), None., P: (25,23,25), None., H: (25,23,24), None., P: (25,23,23), None., P: (25,22,23), None., P: (24,22,23), None., P: (24,22,24), None., H: (25,22,24), None., P: (25,22,25), None., P: (26,22,25), None., P: (26,23,25), None., H: (26,23,24), None., P: (26,24,24), None., P: (26,24,23), None., P: (25,24,23), None., H: (25,25,23), None., P: (25,26,23), None., H: (25,26,24), None., H: (24,26,24), None., H: (24,26,25), None., H: (25,26,25), None., P: (26,26,25), None., H: (26,25,25), None., P: (27,25,25), None., H: (27,25,24), None., P: (27,26,24), None., H: (26,26,24), None., P: (26,26,23), None., H: (26,25,23), None., H: (26,25,24), None.]

Double checked the outcome with the coords of all H's: [(24,24,24), (25,24,24), (24,24,25), (24,23,24), (23,24,24), (24,25,24), (25,25,24), (25,25,25), (24,25,25), (23,24,25), (24,24,26), (25,23,24), (25,22,24), (26,23,24), (25,25,23), (25,26,24), (24,26,24), (24,26,25), (25,26,25), (26,25,25), (27,25,24), (26,26,24), (26,25,23), (26,25,24)]
Ran a neighbour check and subtracted all consecutive H's of the string itself. -27 is the final answer. -26 was the previous record for this chain. Done with cutting chain into pieces of 8 long.

# Best structure found so far for the 36 length chain. Score is -17 so far, element list is:
[P: (17,17,17), None., P: (18,17,17), None., P: (18,17,18), None., H: (18,17,19), None., H: (18,17,20), None., P: (18,18,20), None., P: (17,18,20), None., H: (17,17,20), None., H: (17,17,19), None., P: (17,17,18), None., P: (17,16,18), None., P: (17,15,18), None., P: (18,15,18), None., P: (18,15,19), None., H: (18,16,19), None., H: (18,16,20), None., H: (18,16,21), None., H: (18,17,21), None., H: (17,17,21), None., H: (17,16,21), None., H: (17,16,20), None., P: (17,16,19), None., P: (16,16,19), None., H: (16,16,20), None., H: (16,16,21), None., P: (15,16,21), None., P: (15,16,22), None., P: (16,16,22), None., P: (16,17,22), None., H: (16,17,21), None., H: (16,17,20), None., P: (16,18,20), None., P: (16,18,19), None., H: (16,17,19), None., P: (16,17,18), None., P: (15,17,18), None.]

Was done with cutting chain into pieces of 7 long.