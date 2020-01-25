# Results from the breadth first search with beam search algorithm

## Overall best stability per protein string
Using beamsearch of highest stability every level, and 60% discard after 2 consecutive P's, 70% after 3, 75% after 4 and 80% after 5 or more. After 100 runs these are the best results:
String 0, 3D results in a best stability of -3
String 1, 3D results in a best stability of -7
String 2, 3D results in a best stability of -11
String 3, 3D results in a best stability of -18
String 4, 3D results in a best stability of -31
String 5, 3D results in a best stability of -33
String 6, 3D results in a best stability of -59
String 7, 3D results in a best stability of -47
String 8, 3D results in a best stability of -51

## Upper bound of state space check
Chain length 12, 3D: 6989025 possible states (calculated: )
Chain length 10, 3D: 308981 possible states (calculated: 390625) (26% overestimation)
Chain length 9, 3D: 64661 possible states (calculated: 78125) (20% overestimation)

## String 0
STABILITY STATISTICS
N: 100
Mean: -3.0
Median: -3.0
Standard deviation: 0.0
Best result: -3.0
Worst result: -3.0

### Long run without random pruning
permutations:72 stability: -3.0
[H: (0,0,0), 1., H: (1,0,0), 1., P: (2,0,0), 2., H: (2,-1,0), -1., H: (1,-1,0), -1., H: (0,-1,0), -1., P: (-1,-1,0), -2., H: (-1,0,0),
None.]

## String 1

### Long run without random pruning
permutations:130 stability: -7.0
[H: (0,0,0), 1., H: (1,0,0), 1., P: (2,0,0), 2., H: (2,-1,0), -1., H: (1,-1,0), -1., H: (0,-1,0), -1., P: (-1,-1,0), -2., H: (-1,0,0),
3., P: (-1,0,-1), 1., H: (0,0,-1), 1., H: (1,0,-1), 2., H: (1,-1,-1), 1., P: (2,-1,-1), -2., H: (2,0,-1), None.]

## String 2

### Long run without random pruning
permutations:176 stability: -11.0
[H: (0,0,0), 1., P: (1,0,0), 2., H: (1,-1,0), 2., P: (1,-2,0), -1., P: (0,-2,0), -2., H: (0,-1,0), -1., H: (-1,-1,0), 3., P: (-1,-1,-1)
, 1., H: (0,-1,-1), 2., P: (0,-2,-1), 1., P: (1,-2,-1), -2., H: (1,-1,-1), -2., P: (1,0,-1), -1., H: (0,0,-1), -1., H: (-1,0,-1), -1.,
P: (-2,0,-1), -3., P: (-2,0,0), 1., H: (-1,0,0), -2., P: (-1,1,0), 1., H: (0,1,0), None.]

## String 3

### Long run without random pruning

## String 4
STABILITY STATISTICS
N: 99
Mean: -27.7979797979798
Median: -28.0
Mode: -28.0
Standard deviation: 1.498
Best result: -30.0
Worst result: -23.0

### Long run without random pruning
permutations:64 stability: -31.0
[H: (0,0,0), 1., H: (1,0,0), 2., P: (1,-1,0), -1., H: (0,-1,0), -1., P: (-1,-1,0), -2., H: (-1,0,0), -2., P: (-1,1,0), 1., H: (0,1,0),
1., P: (1,1,0), 3., H: (1,1,-1), -1., H: (0,1,-1), 2., H: (0,0,-1), 1., H: (1,0,-1), 2., P: (1,-1,-1), -1., H: (0,-1,-1), -1., P: (-1,-
1,-1), -1., P: (-2,-1,-1), -2., P: (-2,0,-1), 1., H: (-1,0,-1), 3., P: (-1,0,-2), 2., P: (-1,-1,-2), 1., P: (0,-1,-2), -2., H: (0,0,-2)
, 3., P: (0,0,-3), 2., P: (0,-1,-3), 1., P: (1,-1,-3), -3., P: (1,-1,-2), -2., H: (1,0,-2), 3., P: (1,0,-3), -2., P: (1,1,-3), -1., P:
(0,1,-3), -3., H: (0,1,-2), -1., P: (-1,1,-2), -1., P: (-2,1,-2), -3., P: (-2,1,-1), 1., H: (-1,1,-1), -2., P: (-1,2,-1), 1., H: (0,2,-
1), 3., H: (0,2,-2), 1., H: (1,2,-2), 2., H: (1,1,-2), 1., P: (2,1,-2), -2., H: (2,2,-2), -3., P: (2,2,-1), -1., H: (1,2,-1), -3., P: (
1,2,0), -1., H: (0,2,0), -2., P: (0,3,0), 3., H: (0,3,-1), 1., H: (1,3,-1), None.]

## String 6

### Long run without random pruning
permutations:11 stability: -51.0
[C: (0,0,0), 1., P: (1,0,0), 2., P: (1,-1,0), -1., C: (0,-1,0), -1., H: (-1,-1,0), -1., P: (-2,-1,0), -2., P: (-2,0,0), 1., C: (-1,0,0)
, 3., H: (-1,0,-1), -2., P: (-1,1,-1), 1., P: (0,1,-1), 2., C: (0,0,-1), 1., P: (1,0,-1), 2., P: (1,-1,-1), -1., H: (0,-1,-1), -1., H:
(-1,-1,-1), -1., H: (-2,-1,-1), 2., H: (-2,-2,-1), 1., H: (-1,-2,-1), 1., H: (0,-2,-1), -3., C: (0,-2,0), -1., C: (-1,-2,0), -3., P: (-
1,-2,1), 1., C: (0,-2,1), -2., H: (0,-1,1), 1., P: (1,-1,1), -2., P: (1,0,1), -1., C: (0,0,1), -2., P: (0,1,1), 3., C: (0,1,0), -1., H:
 (-1,1,0), -1., P: (-2,1,0), 3., P: (-2,1,-1), 2., H: (-2,0,-1), -1., P: (-3,0,-1), 2., C: (-3,-1,-1), None.]

## String 7

### Long run, without random pruning
permutations:8 stability: -43.0
[H: (0,0,0), 1., C: (1,0,0), 2., P: (1,-1,0), -1., H: (0,-1,0), -1., P: (-1,-1,0), -2., C: (-1,0,0), -2., P: (-1,1,0), 1., H: (0,1,0),
1., P: (1,1,0), 3., C: (1,1,-1), -1., H: (0,1,-1), 2., C: (0,0,-1), 1., H: (1,0,-1), 2., P: (1,-1,-1), -1., H: (0,-1,-1), 2., P: (0,-2,
-1), -1., P: (-1,-2,-1), -2., P: (-1,-1,-1), -2., H: (-1,0,-1), -1., P: (-2,0,-1), 3., P: (-2,0,-2), 1., P: (-1,0,-2), 1., H: (0,0,-2),
 3., P: (0,0,-3), 1., P: (1,0,-3), 2., P: (1,-1,-3), -1., P: (0,-1,-3), -3., H: (0,-1,-2), 1., P: (1,-1,-2), -2., C: (1,0,-2), -2., P:
(1,1,-2), -1., H: (0,1,-2), -1., P: (-1,1,-2), -1., P: (-2,1,-2), -3., P: (-2,1,-1), 1., H: (-1,1,-1), -2., P: (-1,2,-1), 1., H: (0,2,-
1), 1., H: (1,2,-1), 1., H: (2,2,-1), 2., C: (2,1,-1), 2., C: (2,0,-1), 3., H: (2,0,-2), -2., C: (2,1,-2), 1., H: (3,1,-2), -3., C: (3,
1,-1), 2., H: (3,0,-1), 3., C: (3,0,-2), 1., H: (4,0,-2), -2., H: (4,1,-2), None.]

## String 8
STABILITY STATISTICS
N: 94
Mean: -45.712765957446805
Median: -46.0
Standard deviation: 1.788
Best result: -50.0
Worst result: -41.0

### Long run, without random pruning
permutations:54 stability: -48.0
[H: (0,0,0), 1., C: (1,0,0), 2., P: (1,-1,0), -1., H: (0,-1,0), -1., P: (-1,-1,0), -2., H: (-1,0,0), -2., P: (-1,1,0), 1., H: (0,1,0),
1., C: (1,1,0), 3., H: (1,1,-1), -1., H: (0,1,-1), 2., H: (0,0,-1), 1., H: (1,0,-1), 1., P: (2,0,-1), -3., C: (2,0,0), -2., C: (2,1,0),
 1., P: (3,1,0), 3., P: (3,1,-1), -1., H: (2,1,-1), -2., P: (2,2,-1), 3., P: (2,2,-2), -1., P: (1,2,-2), -3., H: (1,2,-1), -2., P: (1,3
,-1), 1., P: (2,3,-1), -3., P: (2,3,0), 2., P: (2,2,0), -1., C: (1,2,0), -2., P: (1,3,0), -1., P: (0,3,0), 3., P: (0,3,-1), 2., H: (0,2
,-1), -3., P: (0,2,0), -3., P: (0,2,1), 1., P: (1,2,1), 2., H: (1,1,1), 1., P: (2,1,1), 2., H: (2,0,1), -1., H: (1,0,1), -1., H: (0,0,1
), -2., H: (0,1,1), -1., C: (-1,1,1), 2., H: (-1,0,1), 2., P: (-1,-1,1), 1., H: (0,-1,1), 2., P: (0,-2,1), 3., H: (0,-2,0), 3., P: (0,-
2,-1), -2., H: (0,-1,-1), 1., H: (1,-1,-1), None.]
