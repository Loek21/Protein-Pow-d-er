# Programming Theory: Protein-Pow(d)er

Team: Shire Peasants 3
Authors: Mark Dzoljic, Sebastiaan Kruize & Loek van Steijn

## Introduction
The aim of this project is to find the most stable form of HP(C) protein strings in a square (2D) or cubic (3D) lattice. The stability of the protein strings is based on the number of hydrogen bonds that can be formed between two elements within the protein string. hydrogen bonds can only form between two topological neighbours, two protein elements are considered to be topological neighbours if they are adjacent to each other but not in consecutive order within the protein string. For a P-P and P-C bond the stability decreases by -1 and for a C-C bond the stability decreases by -5. The state with the lowest stability is considered to be the most stable state.

This is a well-known NP-hard problem in bioinformatics, to achieve the aim of this project several algorithms based on different constructive and iterative methods were created. Each algorithm will be briefly explained in the following subchapters of this file along with a brief explanation on how to operate and navigate the algorithms.

## Navigation

### Code
The following folders can be found in the folder code.

#### Classes
The algorithms are created with two classes which can be found in the classes folder.
The Element class which holds all the information regarding one protein element. The type of the protein element (P, H or C), the location of the element in the square or cubic lattice (X, Y, Z coordinates), and the direction to the next element (1, -1 for movements in de x-direction, 2, -2 for movements in de y-direction and 3, -3 for movements in the z-direction).
The Lattice class which holds a list of Element objects in the correct sequence.

#### Algorithms
The created algorithms can be found in the folder algorithms. A brief explanation of each algorithm can be found in the succeeding chapters. Along side the algorithms once can find the general functions file in which all functions are written that are used in many of the algorithms such as calculating the stability of a protein string.

#### Generalfunctions
This folder contains generalfunctions.py. It serves as a placeholder for general functions, such as making moves based on directions, that all algorithms use.

#### Visualisation
Contains functions that are used to visualise the folding of a certain protein string in a 3D plot. In the plot the red points are representing P elements, the blue points represent H and the green points represent C elements.

## Operation
Before running any code it is important to update your python modules by installing requirements.txt found in the main folder. Ensure that you have Python and Pip installed. You can download Python [here](https://www.python.org/downloads/). You can install the neccessary Python modules by running:

```command
pip install -r requirements.txt
```

Every algorithm can be selected and run on any of the preselected protein strings from main.py. It works on the basis of command line arguments. The correct format for using command line arguments in calling a specific algorithm is:

```command
python main.py algorithm protein_string_nr iterations dimension
```

In addition one will be prompted with the message if one wants to have a printed list of coordinates and a graph displaying the solution, this can be answered with a `y` or `yes` or a `n` or `no` depending on ones wishes. Lastly if one executes `python main.py help` an explanation will also be printed in the terminal itself.

### Algorithm
One can select any of the algorithms mentioned in the next chapters. Choose "random", "twist", "greedy", "breadth", "eha" or "pull" to use any of the respective algorithms.

### Protein string number
One can select any of the following numbers with the respective protein string. Where the numbers 0 through 8 originate from the given assignment and the numbers 10 through 13 originate from available literature. String number 9 is reserved for a custom string input from the user. If this option is chosen, the user will be asked to fill in either
their own custom string, or a length and model (HP or HPC) to create a random string.

0: HHPHHHPH

1: HHPHHHPHPHHHPH

2: HPHPPHHPHPPHPHHPPHPH

3: PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP

4: HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH

5: PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP

6: CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC

7: HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH

8: HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH

9: CUSTOM

10: HHPPHPPHPPHPPHPPHPPHPPHH

11: PPHHHPHHHPPPHPHHPHHPPHPHHHHPHPPHHHHHPHPHHPPHHP

12: PPHPPHHPPHHPPPPPHHHHHHHHHHPPPPPPHHPPHHPPHPPHHHHH

13: PPHHHPHHHHHHHHPPPHHHHHHHHHHPHPPPHHHHHHHHHHHHPPPPHHHHHHPHHPHP

### Iterations
One can select any number higher than 0. If one selects 2 or higher statistical information about the found stabilities will be printed in the terminal, this includes the total number of found solutions (N), the average, the median, the standard deviation, the best found stability and the worst found stability.

### Dimension
One can select either "2" for a 2D square lattice or "3" for a 3D cubic lattice.

## Algorithms
A brief explanation of the algorithms can be found here.

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
