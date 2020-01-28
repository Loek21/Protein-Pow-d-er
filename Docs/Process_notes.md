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



# New best structure found for the 50 length chain. Better than literature with -27. Down the paragraphs = better results. The element list is:
[H: (24,24,24), None., H: (25,24,24), None., P: (25,24,25), None., H: (24,24,25), None., P: (24,23,25), None., H: (24,23,24), None., P: (23,23,24), None., H: (23,24,24), None., P: (23,25,24), None., H: (24,25,24), None., H: (25,25,24), None., H: (25,25,25), None., H: (24,25,25), None., P: (23,25,25), None., H: (23,24,25), None., P: (23,23,25), None., P: (23,23,26), None., P: (24,23,26), None., H: (24,24,26), None., P: (25,24,26), None., P: (25,23,26), None., P: (25,23,25), None., H: (25,23,24), None., P: (25,23,23), None., P: (25,22,23), None., P: (24,22,23), None., P: (24,22,24), None., H: (25,22,24), None., P: (25,22,25), None., P: (26,22,25), None., P: (26,23,25), None., H: (26,23,24), None., P: (26,24,24), None., P: (26,24,23), None., P: (25,24,23), None., H: (25,25,23), None., P: (25,26,23), None., H: (25,26,24), None., H: (24,26,24), None., H: (24,26,25), None., H: (25,26,25), None., P: (26,26,25), None., H: (26,25,25), None., P: (27,25,25), None., H: (27,25,24), None., P: (27,26,24), None., H: (26,26,24), None., P: (26,26,23), None., H: (26,25,23), None., H: (26,25,24), None.]

Double checked the outcome with the coords of all H's: [(24,24,24), (25,24,24), (24,24,25), (24,23,24), (23,24,24), (24,25,24), (25,25,24), (25,25,25), (24,25,25), (23,24,25), (24,24,26), (25,23,24), (25,22,24), (26,23,24), (25,25,23), (25,26,24), (24,26,24), (24,26,25), (25,26,25), (26,25,25), (27,25,24), (26,26,24), (26,25,23), (26,25,24)]
Ran a neighbour check and subtracted all consecutive H's of the string itself. -27 is the final answer. -26 was the previous record for this chain. Done with cutting chain into pieces of 8 long.

Another -27 found with an added heuristic, seems to be reproducible now! Element list is:
[H: (24,24,24), None., H: (25,24,24), None., P: (25,25,24), None., H: (24,25,24), None., P: (24,25,25), None., H: (24,24,25), None., P: (24,23,25), None., H: (23,23,25), None., P: (23,23,24), None., H: (23,24,24), None., H: (23,24,25), None., H: (23,25,25), None., H: (23,25,24), None., P: (23,26,24), None., H: (24,26,24), None., P: (25,26,24), None., P: (25,26,25), None., P: (25,25,25), None., H: (25,24,25), None., P: (25,23,25), None., P: (25,23,26), None., P: (25,24,26), None., H: (24,24,26), None., P: (24,24,27), None., P: (23,24,27), None., P: (23,25,27), None., P: (23,25,26), None., H: (23,24,26), None., P: (22,24,26), None., P: (21,24,26), None., P: (21,24,25), None., H: (22,24,25), None., P: (22,24,24), None., P: (21,24,24), None., P: (21,25,24), None., H: (22,25,24), None., P: (22,25,23), None., H: (23,25,23), None., H: (24,25,23), None., H: (24,24,23), None., H: (23,24,23), None., P: (23,23,23), None., H: (24,23,23), None., P: (25,23,23), None., H: (25,24,23), None., P: (26,24,23), None., H: (26,24,24), None., P: (26,23,24), None., H: (25,23,24), None., H: (24,23,24), None.]

Found -28 with it too, doesn't happen all the time, but it is there! Element list is:
[H: (24,24,24), None., H: (25,24,24), None., P: (25,24,23), None., H: (24,24,23), None., P: (24,25,23), None., H: (24,25,24), None., P: (23,25,24), None., H: (23,24,24), None., P: (23,24,25), None., H: (24,24,25), None., H: (24,25,25), None., H: (25,25,25), None., H: (25,25,24), None., P: (26,25,24), None., H: (26,25,25), None., P: (26,25,26), None., P: (26,24,26), None., P: (26,24,25), None., H: (25,24,25), None., P: (25,24,26), None., P: (25,24,27), None., P: (24,24,27), None., H: (24,24,26), None., P: (23,24,26), None., P: (23,24,27), None., P: (23,25,27), None., P: (24,25,27), None., H: (24,25,26), None., P: (25,25,26), None., P: (25,26,26), None., P: (26,26,26), None., H: (26,26,25), None., P: (27,26,25), None., P: (28,26,25), None., P: (28,25,25), None., H: (27,25,25), None., P: (27,25,24), None., H: (27,26,24), None., H: (26,26,24), None., H: (25,26,24), None., H: (25,26,25), None., P: (24,26,25), None., H: (24,26,24), None., P: (24,27,24), None., H: (25,27,24), None., P: (25,27,25), None., H: (26,27,25), None., P: (27,27,25), None., H: (27,27,24), None., H: (26,27,24), None.]

## -29!! found. Element list:
[H: (24,24,24), None., H: (25,24,24), None., P: (25,23,24), None., H: (24,23,24), None., P: (23,23,24), None., H: (23,24,24), None., P: (23,24,25), None., H: (24,24,25), None., P: (24,24,26), None., H: (24,23,26), None., H: (24,23,25), None., H: (25,23,25), None., H: (25,24,25), None., P: (25,24,26), None., H: (25,23,26), None., P: (25,23,27), None., P: (25,22,27), None., P: (25,22,26), None., H: (25,22,25), None., P: (25,22,24), None., P: (25,21,24), None., P: (24,21,24), None., H: (24,22,24), None., P: (23,22,24), None., P: (22,22,24), None., P: (22,22,25), None., P: (23,22,25), None., H: (24,22,25), None., P: (24,21,25), None., P: (25,21,25), None., P: (26,21,25), None., H: (26,22,25), None., P: (26,22,26), None., P: (26,23,26), None., P: (26,24,26), None., H: (26,24,25), None., P: (27,24,25), None., H: (27,23,25), None., H: (26,23,25), None., H: (26,23,24), None., H: (26,24,24), None., P: (27,24,24), None., H: (27,23,24), None., P: (27,22,24), None., H: (26,22,24), None., P: (26,22,23), None., H: (26,23,23), None., P: (25,23,23), None., H: (25,24,23), None., H: (26,24,23), None.]

## -30 found, element list missing because it was part of an iterated run where the lists weren't saved. Graph is saved though.

# Best structure found so far for the 36 length chain. Score is -17 so far. Down the paragraphs = better results. Element list is:
[P: (17,17,17), None., P: (18,17,17), None., P: (18,17,18), None., H: (18,17,19), None., H: (18,17,20), None., P: (18,18,20), None., P: (17,18,20), None., H: (17,17,20), None., H: (17,17,19), None., P: (17,17,18), None., P: (17,16,18), None., P: (17,15,18), None., P: (18,15,18), None., P: (18,15,19), None., H: (18,16,19), None., H: (18,16,20), None., H: (18,16,21), None., H: (18,17,21), None., H: (17,17,21), None., H: (17,16,21), None., H: (17,16,20), None., P: (17,16,19), None., P: (16,16,19), None., H: (16,16,20), None., H: (16,16,21), None., P: (15,16,21), None., P: (15,16,22), None., P: (16,16,22), None., P: (16,17,22), None., H: (16,17,21), None., H: (16,17,20), None., P: (16,18,20), None., P: (16,18,19), None., H: (16,17,19), None., P: (16,17,18), None., P: (15,17,18), None.]

Was done with cutting chain into pieces of 7 long.


New heuristic found the literature's best of -18, element list is:
[P: (17,17,17), None., P: (18,17,17), None., P: (18,17,18), None., H: (18,16,18), None., H: (18,16,19), None., P: (18,17,19), None., P: (19,17,19), None., H: (19,16,19), None., H: (19,16,18), None., P: (19,16,17), None., P: (19,16,16), None., P: (18,16,16), None., P: (18,16,17), None., P: (18,15,17), None., H: (18,15,18), None., H: (18,15,19), None., H: (19,15,19), None., H: (19,15,18), None., H: (20,15,18), None., H: (20,16,18), None., H: (20,16,19), None., P: (21,16,19), None., P: (21,15,19), None., H: (20,15,19), None., H: (20,14,19), None., P: (20,13,19), None., P: (20,13,18), None., P: (21,13,18), None., P: (21,14,18), None., H: (20,14,18), None., H: (19,14,18), None., P: (19,13,18), None., P: (19,13,19), None., H: (19,14,19), None., P: (19,14,20), None., P: (19,15,20), None.]


# Some stats for the eha_list algorithm, 5 iterations per chain for best solution, all times more or less equal for every iteration:

## Chain 0 - length 8, subchain_length = 4-8:
Best found: -3
Runtime: < 0.5 sec

## Chain 0 - length 8, subchain_length = 5-9:
Best found: -3
Runtime: < 1.5 sec

## Chain 1 - length 14, subchain_length = 4-8:
Best found: -7
Runtime: < 2.5 sec

## Chain 1 - length 14, subchain_length = 5-9:
Best found: -7
Runtime: < 3.5 sec

## Chain 2 - length 20, subchain_length = 4-8:
Best found: -11
Runtime: < 2.3 sec

## Chain 2 - length 20, subchain_length = 5-9:
Best found: -11
Runtime: < 2.6 sec

## Chain 3 - length 36, subchain_length = 4-8:
Best found: -18
Runtime: < 1:06 minutes

## Chain 3 - length 36, subchain_length = 5-9:
Best found: -16
Runtime: < 5:30 minutes

## Chain 4 - length 50, subchain_length = 4-8:
Best found: -30
Runtime: < 26.8 sec

## Chain 4 - length 50, subchain_length = 5-9:
Best found: -26
Runtime: < 6:25 minutes

## Upper bound tests
Chain length 12, 3D: 6989025 possible states (calculated: )
Chain length 10, 3D: 308981 possible states (calculated: 390625) (26% overestimation)
Chain length 9, 3D: 64661 possible states (calculated: 78125) (20% overestimation)

## Beam search results
Using beamsearch of highest stability every level, and 60% discard after 2 consecutive P's, 70% after 3, 75% after 4 and 80% after 5 or more. After 100 runs these are the best results:
String 0, 3D results in a best stability of -3
String 1, 3D results in a best stability of -7
String 2, 3D results in a best stability of -11
String 3, 3D results in a best stability of -18
String 4, 3D results in a best stability of -31
String 5, 3D results in a best stability of -33
String 6, 3D results in a best stability of -59
String 7, 3D results in a best stability of -47
String 8, 3D results in a best stability of -50
