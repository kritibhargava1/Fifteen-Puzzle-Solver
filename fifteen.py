# assignment: Programming Assignment 5
# author: Kriti Bhargava
# date: 03/17/23
# file: fifteen.py
# input: a number the user want to move on the board to an empty square
# output: an updated board with the correct number on the correct square

# Import the necessary functions from the existing code
import numpy as np
from random import choice

#uses a NumPy array to represent the tiles on the board and has methods to shuffle the board, make moves, and check if the puzzle is solved
#
class Fifteen:
    #initialize new instance of fifteen game
    def __init__(self, size=4):
        self.size = size
        self.tiles = np.array(
            [i for i in range(1, size ** 2)] + [0])  # creates an array of tiles from 1 to size**2-1 and 0 at the end
        self.adj = [  # list of all adjacent tiles for each tile in the array, in the order of the array
            [1, 4],  # adjacent tiles of tile 0
            [0, 2, 5],  # adjacent tiles of tile 1
            [1, 3, 6],  # adjacent tiles of tile 2
            [2, 7],  # adjacent tiles of tile 3
            [0, 5, 8],  # adjacent tiles of tile 4
            [1, 4, 6, 9],  # adjacent tiles of tile 5
            [2, 5, 7, 10],  # adjacent tiles of tile 6
            [3, 6, 11],  # adjacent tiles of tile 7
            [4, 9, 12],  # adjacent tiles of tile 8
            [5, 8, 10, 13],  # adjacent tiles of tile 9
            [6, 9, 11, 14],  # adjacent tiles of tile 10
            [7, 10, 15],  # adjacent tiles of tile 11
            [8, 13],  # adjacent tiles of tile 12
            [9, 12, 14],  # adjacent tiles of tile 13
            [10, 13, 15],  # adjacent tiles of tile 14
            [11, 14]  # adjacent tiles of tile 15
        ]
    # update the vector of tiles
    #This method updates the board after a move is made. It takes a move argument, which is the number of the tile to move
    def update(self, move):
        if self.is_valid_move(move):
            index = np.where(self.tiles == move)[0][0]
            empty_index = np.where(self.tiles == 0)[0][0]
            self.tiles[index], self.tiles[empty_index] = self.tiles[empty_index], self.tiles[index]

    #method swaps the position of two tiles on the board. It takes two arguments i and j, which are the indices of the tiles to swap
    def transpose(self, i, j):
        self.tiles[[i, j]] = self.tiles[[j, i]]

    def shuffle(self, steps=100):
        #shuffles tiles + empty space on board
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice(self.adj[index])
            if move_index != -1:
                self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
                index = move_index

    def is_valid_move(self, move):
        # works only if move is valid
        index = np.where(self.tiles == move)[0][0]
        row, col = index // int(np.sqrt(len(self.tiles))), index % int(np.sqrt(len(self.tiles)))
        if row > 0 and self.tiles[index - int(np.sqrt(len(self.tiles)))] == 0:
            return True
        elif row < int(np.sqrt(len(self.tiles))) - 1 and self.tiles[index + int(np.sqrt(len(self.tiles)))] == 0:
            return True
        elif col > 0 and self.tiles[index - 1] == 0:
            return True
        elif col < int(np.sqrt(len(self.tiles))) - 1 and self.tiles[index + 1] == 0:
            return True
        else:
            return False

    def is_solved(self):
        # return true if puzzle is solved
        return np.array_equal(self.tiles, np.append(np.arange(1, len(self.tiles)), 0))

    def draw(self):
        # draws current state of puzzle
        for i in range(self.size):
            print("+---" * self.size + "+")
            row = "|"
            for j in range(self.size):
                if self.tiles[i * self.size + j] != 0:
                    tile = str(self.tiles[i * self.size + j])
                else:
                    tile = " "
                if len(tile) == 2 and tile.isdigit():
                    row += "" + tile + " |"
                else:
                    row += " " + tile + " |"
                #row += " " + tile + " |"
            print(row)
        print("+---" * self.size + "+")

    def __str__(self):

        output = ""
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                if self.tiles[i * self.size + j] != 0:
                    tile = str(self.tiles[i * self.size + j]).rjust(2)
                else:
                    tile = "  "
                row += tile + " "
            output += row + "\n"
        return output


#creates an instance of the Fifteen class, and runs some tests
if __name__ == '__main__':
    game = Fifteen()
    #print(str(game))
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    '''You should be able to play the game if you uncomment the code below'''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

