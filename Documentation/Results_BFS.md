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
String 8, 3D results in a best stability of -50

## Upper bound of state space check
Chain length 12, 3D: 6989025 possible states (calculated: )
Chain length 10, 3D: 308981 possible states (calculated: 390625) (26% overestimation)
Chain length 9, 3D: 64661 possible states (calculated: 78125) (20% overestimation)

## String 4
STABILITY STATISTICS
Mean: -27.978021978021978
Median: -28.0
Mode: -28.0
Standard deviation: 1.325
Best result: -30.0
Worst result: -25.0
