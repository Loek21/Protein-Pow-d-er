# Algorithms
## Introduction
This folder contains all the algorithms that can be called from main.py.

## Algorithms
A brief explanation of the algorithms is given here.

### Random
This is an incomplete, constructive algorithm based on an entirely random move. Each next protein element is attached to the previous protein element based on a random direction. If the selected direction leads to an already occupied location in the lattice, the direction is randomly chosen again until protein element finds an unoccupied location, if no locations are open the algorithm will terminate. In short this algorithm is a self avoiding random walk.

The stability is calculated at the end.

### Random + Space Confinement
This algorithm is built on the random algorithm, but has an extra heuristic built in. The moves chosen are still random, but freedom of movement is limited in the sense that there are borders which the protein string cannot pass; it is confined within a box. This extra heuristic results in better stabilities compared with the random algorithm, but they are still random in nature and therefore suboptimal when compared to the results of our other algorithms. 

### Greedy
This is an incomplete, constructive algorithm that randomly chooses a move from a selected moveset that would result in the highest stability based on the next move. In essence, like random, each next protein element is attached to the previous protein element. However, before placing the next protein, the algorithm 'looks 1 possibility ahead' and creates a moveset that would result in the highest temporary stability. It then chooses a move randomly from that moveset. Like random, if no locations are open the algorithm will terminate. In short this algorithm is similar to random but with a greedy look-ahead element.

### Breadth First with Beam Search
This is an incomplete, constructive algorithm based on Breadth First Search (BFS). The plain version of BFS will often carry too many permutations for it to be a viable option in tackling the preceding problem. To solve this a Beam Search was added. The algorithm will only save the permutations with the best stability. With this alone the algorithm is able to run but will still take up to several hours to complete one calculation. The main reason for this are the substrings with consecutive P elements (P's do not contribute to an improved stability) and therefore the Beam Search no longer prunes any permutations within these substrings. To overcome this a random feature was added with a decreasing acceptance probability based on the number of consecutive P's. Now each calculation can be completed within several minutes (for protein strings up to a length of 60). Produced results are in line with the best known results found in literature.

### Extended Heuristic Algorithm Plus (EHA Plus)
This is an incomplete, constructive algorithm based on an article by M. Traykov [1]. In this article, the protein string is divided into several substrings of fixed length. The first string is then folded into the best available solution and the subsequent strings are folded against the previous, already folded piece(s) in the most optimal fold available. Where the EHA Plus algorithm differs is that the subchains aren't divided into pieces of a fixed length, but are instead divided in such a way that the subchain always ends with either an 'H' in the HP model, and either an 'H' or a 'C' in the HPC model. This results in more stable solutions, since when a subchain ends on a 'P' element, the position of said last element doesn't influence the stability of the subchain, and thus may result in suboptimal folding when keeping in mind that the next subchain has to bind itself to that - now suboptimally positioned - 'P'. Furthermore, many configurations have the same stability, so a second heuristic was added to give each configuration that's equal to the current best to be accepted and become the new current best. This gives each iteration a random element, which may result in a better solution. The produced results after 100 iterations are in line with the best known results found in literature, surpassing Traykov's results in some cases, except for the protein string of length 60, in which case Traykov has the better solution.

### Pull with Simulated Annealing
This is an incomplete, iterative algorithm based on an article by C. Chira [2]. This article describes using an iterative pull move to change an already valid state of the protein string (obtained from the random algorithm). The pull move entails a diagonal movement of an element where the previous element gets moved to a free adjacent position. shifting the entirety of the previous string up two locations to join it to the previous element. It selects the best possible pull move based on the stability. If the pull move decreased the stability the new state is automatically accepted, if the pull move increases the stability the new state is accepted based on an acceptance probability according to the simulated annealing protocol. The entire process is repeated 10000 and the temperature of the acceptance probability is decreased every by 0.01 every 100 iterations.

## References
1: Traykov, Metodi, et al. "Algorithm for protein folding problem in 3D lattice HP model." International Journal of Biology and Biomedicine 3 (2018).

2: Chira, Camelia. "Hill-climbing search in evolutionary models for protein folding simulations." Stud Univ Babe s-Bolyai Inform 55 (2010): 29-40.