# Protein-Pow(d)er
Shire Peasants 3: Mark Dzoljic, Sebastiaan Kruize & Loek van Steijn

## Introduction
The aim of this project is to find the most stable form of HP(C) protein strings in a square (2D) or cubic (3D) lattice. The stability of the protein strings is based on the number of hydrogen bonds that can be formed between two elements within the protein string. hydrogen bonds can only form between two topological neighbours, two protein elements are considered to be topological neighbours if they are adjacent to each other but not in consecutive order within the protein string. For a P-P and P-C bond the stability decreases by -1 and for a C-C bond the stability decreases by -5. The state with the lowest stability is considered to be the most stable state.

This is a well-known NP-hard problem in bioinformatics, to achieve the aim of this project several algorithms based on different constructive and iterative methods were created. Each algorithm will be briefly explained in the following subsections of this file along with a brief explanation on how to operate and navigate the algorithms.

## Navigation & Operation

### Code
The following folders can be found in the folder code.

#### Classes
The algorithms are created with two classes which can be found in the classes folder.
The Element class which holds all the information regarding one protein element. The type of the protein element (P, H or C), the location of the element in the square or cubic lattice (X, Y, Z coordinates), and the direction to the next element (1, -1 for movements in de x-direction, 2, -2 for movements in de y-direction and 3, -3 for movements in de z-direction).
The Lattice class which holds a list of Element objects in the correct sequence.

#### Algorithms
The created algorithms can be found in the folder algorithms. A brief explanation of each algorithm can be found in the succeeding chapters. Along side the algorithms once can find the general functions file in which all functions are written that are used in many of the algorithms such as calculating the stability of a protein string.

#### Visualisation
Contains functions that are used to visualise the folding of a certain protein string in a 3D plot. In the plot the red points are representing P elements, the blue points represent H and the green points represent C elements.

### Operation
Before running any code it is important to update your python modules by installing requirements.txt found in the main folder.
Every algorithm can be selected and run on any of the preselected protein strings from main.py. It works on the basis of command line arguments. The correct format for using command line arguments in calling a specific algorithm is: python main.py algorithm protein_string_nr iterations dimension. In addition one will be prompted with the message if one wants to have a printed list of coordinates and a graph displaying the solution, this can be answered with a "y" or "yes" or a "n" or "no" depending on ones wishes. Lastly if one executes python main.py help an explanation will also be printed in the terminal itself.

#### Algorithm
One can select any of the algorithms mentioned in the next chapters. Choose "random", "twist", "greedy", "breadth", "eha" or "pull" to use any of the respective algorithms.

#### Protein string number
One can select any of the following numbers with the respective protein string. Where the numbers 0 through 8 originate from the given assignment and the numbers 9 through 13 originate from available literature. \n
0: HHPHHHPH

1: HHPHHHPHPHHHPH

2: HPHPPHHPHPPHPHHPPHPH

3: PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP

4: HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH

5: PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP

6: CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC

7: HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH

8: HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH

9: PPHPPPHPPPHPHHHHPHPHPHPHH

10: HHPPHPPHPPHPPHPPHPPHPPHH

11: PPHHHPHHHPPPHPHHPHHPPHPHHHHPHPPHHHHHPHPHHPPHHP

12: PPHPPHHPPHHPPPPPHHHHHHHHHHPPPPPPHHPPHHPPHPPHHHHH

13: PPHHHPHHHHHHHHPPPHHHHHHHHHHPHPPPHHHHHHHHHHHHPPPPHHHHHHPHHPHP

#### Iterations
One can select any number higher than 0. If one selects 2 or higher statistical information about the found stabilities will be printed in the terminal, this includes the total number of found solutions (N), the average, the median, the standard deviation, the best found stability and the worst found stability.

#### Dimension
One can select either "2" for a 2D square lattice or "3" for a 3D cubic lattice.

## Algorithms
A brief explanation of the algorithms can be found here.

### Random
This is an incomplete, constructive algorithm based on an entirely random move. Each next protein element is attached to the previous protein element based on a random direction. If the selected direction leads to an already occupied location in the lattice, the direction is randomly chosen again until protein element finds an unoccupied location, if no locations are open the algorithm will terminate. In short this algorithm is a self avoiding random walk.

The stability is calculated at the end.

### Twist

### Greedy

### Breadth First with Beam Search
This is an incomplete, constructive algorithm based on Breadth First Search (BFS). The plain version of BFS will often carry too many permutations for it to be a viable option in tackling the preceding problem. To solve this a Beam Search was added. The algorithm will only save the permutations with the best stability. With this alone the algorithm is able to run but will still take up to several hours to complete one calculation. The main reason for this are the substrings with consecutive P elements (P's do not contribute to an improved stability) and therefore the Beam Search no longer prunes any permutations within these substrings. To overcome this a random feature was added with a decreasing acceptance probability based on the number of consecutive P's. Now each calculation can be completed within several minutes (for protein strings up to a length of 60). Produced results are in line with the best known results found in literature.

### Upgraded Extended Heuristic Algorithm (EHA)

### Pull with Simulated Annealing
This is an incomplete, iterative algorithm based on an article by C. Chira [2]. This article describes using an iterative pull move to change an already valid state of the protein string (obtained from the random algorithm). The pull move entails a diagonal movement of an element where the previous element gets moved to a free adjacent position. shifting the entirety of the previous string up two locations to join it to the previous element. It selects the best possible pull move based on the stability. If the pull move decreased the stability the new state is automatically accepted, if the pull move increases the stability the new state is accepted based on an acceptance probability according to the simulated annealing protocol. The entire process is repeated 10000 and the temperature of the acceptance probability is decreased every by 0.01 every 100 iterations.

## References
1: Traykov, Metodi, et al. "Algorithm for protein folding problem in 3D lattice HP model." International Journal of Biology and Biomedicine 3 (2018).
2: Chira, Camelia. "Hill-climbing search in evolutionary models for protein folding simulations." Stud Univ Babe s-Bolyai Inform 55 (2010): 29-40.
