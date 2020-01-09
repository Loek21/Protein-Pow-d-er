import random
import matplotlib.pyplot as plt
import numpy as np

# hardcode in the sequence for now
hp_sequence = "HHPHHPHPP"

# convert letters to integer values
int_sequence = []
for amino in hp_sequence:
    if amino == "H":
        int_sequence.append(5)
    else:
        int_sequence.append(10)

# set dimensions for the matrix
dim = len(hp_sequence)

# define moves to make
moves = ["up", "down", "left", "right"]

# track moves history
moveslist = []

# track which tiles are occupied
tilelist = []

# set up a recursion switch for makemove
switch = []

def makemove(from_x_pos, from_y_pos):
    """defines how to move"""

    # if a move has been tried 50 times without success, return none so the last step gets deleted
    # if len(switch) > 50:
    #     print("HEYHEYYYYY")
    #     return None

    #print(switch)
    switch = []

    # keeps on trying a random move until a valid one is chosen
    while True:

        print(switch)
        if len(switch) > 3:
            print("HEYHEYYYYY")
            return None
        
        # the move is just a random choice from the list
        move = random.choice(moves)

        # if the move would move the amino acid onto an occupied tile, try again
        if move == "up":
            new_x_pos = from_x_pos
            new_y_pos = from_y_pos - 1

        elif move == "down":
            new_x_pos = from_x_pos
            new_y_pos = from_y_pos + 1
        
        elif move == "left":
            new_x_pos = from_x_pos - 1
            new_y_pos = from_y_pos
            
        elif move == "right":
            new_x_pos = from_x_pos + 1
            new_y_pos = from_y_pos

        #print(new_x_pos, new_y_pos, tilelist)
        if (new_x_pos, new_y_pos) in tilelist:
            #print("hello")
            # print("old coords", from_x_pos, from_y_pos)
            # print("new coords", new_x_pos, new_y_pos)
            # print(tilelist)
            switch.append(1)
            #makemove(from_x_pos, from_y_pos)
        
        else:
            break

    return move, new_x_pos, new_y_pos
    

def foldingmatrix(dimensions, sequence):
    """make zero-matrix and fill with sequence randomly"""

    # make the matrix
    mat = np.zeros(dimensions)

    # initiate current coordinates
    x_current = int(dim*1.5)
    y_current = int(dim*1.5)

    # first amino acid in the middle
    mat[x_current][y_current] = sequence[0]

    # add the tile to tilelist
    tilelist.append((x_current, y_current))

    # fill in the rest
    for amino in sequence[1:]:
        move = makemove(x_current, y_current)

        while (move == None) and (len(moveslist) > 0) and (len(tilelist) > 1):
            
            # going back 1 move if chain gets stuck
            moveslist.pop()
            second_last_move = tilelist.pop()
            x_current = second_last_move[0]
            y_current = second_last_move[1]
            
            # make new move
            move = makemove(x_current, y_current)

        else:
            
            # update x and y pos, add move and tile to their lists
            x_current = move[1]
            y_current = move[2]
            moveslist.append(move[0])
            tilelist.append((x_current, y_current))

            # add the value to the matrix
            mat[x_current][y_current] = amino
        
    # count the score
    score = 0

    # check for all neighbours in the matrix if H-bridges are formed
    for i in range(dimensions[0]):
        for j in range(dimensions[0]):
            if mat[i][j] == 10:
                if mat[i-1][j] == 10:
                    score -= 1
                if mat[i+1][j] == 10:
                    score -= 1
                if mat[i][j-1] == 10:
                    score -= 1
                if mat[i][j+1] == 10:
                    score -= 1
    
    # score needs to be reduced by the number of successive P's in the chain * 2 (since every coordinate pair is counted twice in the matrix)
    score_reduction = 0
    for amino in range(len(sequence) - 1):
        if (sequence[amino] == 10) and (sequence[amino + 1] == 10):
            score_reduction += 2

    # half the score (for reason see above)
    score = (score + score_reduction) / 2
    
    return mat, score

for i in range(1):
    
    # reset moves/tiles/switch lists after every iteration
    moveslist = []
    tilelist = []
    switch = []
    random_matrix = foldingmatrix((int(dim*2.5), int(dim*2.5)), int_sequence)
    score = random_matrix[1]
    
    if i % 10000 == 0:
        print(i)

    if score <= 0:
        print(f"Score is: {score}")

    plt.matshow(random_matrix[0])
    plt.show()
