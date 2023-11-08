# Fifteen Puzzle Game

Welcome to the Fifteen Puzzle Game! This Python program, `fifteen_puzzle.py`, allows you to play the classic sliding tile puzzle where the goal is to arrange the tiles in numerical order within a grid. Below, you'll find details on the program's functionality, usage, and author information.

## Program Files

- `fifteen_puzzle.py`: The main program file containing the Fifteen Puzzle game code.

## How the Game Works

The Fifteen Puzzle game is a grid-based game where you need to slide tiles in an empty space to arrange them in numerical order. The game includes the following features:

- An `Fifteen` class that represents the game board and provides methods to shuffle the board, make moves, and check if the puzzle is solved.

- You can customize the size of the game board (default size is 4x4), and the game board is initially filled with tiles numbered from 1 to `size^2 - 1`, with one empty space represented by the number 0.

- The game board is displayed as a grid, and you can make moves by entering the number of the tile you want to slide into the empty space.

- The game continues until you have successfully arranged the tiles in numerical order or choose to quit.

## How to Play

1. Run the game by executing `fifteen_puzzle.py` using a Python interpreter.

2. You can customize the board size when prompted or simply proceed with the default 4x4 board.

3. The game board is shuffled to start.

4. Enter the number of the tile you want to slide into the empty space when prompted.

5. Continue making moves until you've arranged the tiles in numerical order or decide to quit.

## Example Gameplay

Here's an example of how the game might be played:

```plaintext
Welcome to the Fifteen Puzzle Game!

Enter your move or q to quit: 2
+---+---+---+---+
| 1 | 2 | 3 | 4 |
+---+---+---+---+
| 5 | 6 | 7 | 8 |
+---+---+---+---+
| 9 | 10 | 11 | 12 |
+---+---+---+---+
| 13 |   | 14 | 15 |
+---+---+---+---+

Enter your move or q to quit: 6
+---+---+---+---+
| 1 | 2 | 3 | 4 |
+---+---+---+---+
| 5 | 6 | 7 | 8 |
+---+---+---+---+
| 9 | 10 | 11 | 12 |
+---+---+---+---+
| 13 | 14 |   | 15 |
+---+---+---+---+

Enter your move or q to quit: 11
+---+---+---+---+
| 1 | 2 | 3 | 4 |
+---+---+---+---+
| 5 | 6 | 7 | 8 |
+---+---+---+---+
| 9 | 10 |   | 12 |
+---+---+---+---+
| 13 | 14 | 11 | 15 |
+---+---+---+---+

Enter your move or q to quit: 12
+---+---+---+---+
| 1 | 2 | 3 | 4 |
+---+---+---+---+
| 5 | 6 | 7 | 8 |
+---+---+---+---+
| 9 | 10 | 11 |   |
+---+---+---+---+
| 13 | 14 |   | 15 |
+---+---+---+---+

Enter your move or q to quit: 15
+---+---+---+---+
| 1 | 2 | 3 | 4 |
+---+---+---+---+
| 5 | 6 | 7 | 8 |
+---+---+---+---+
| 9 | 10 | 11 | 12 |
+---+---+---+---+
| 13 | 14 | 15 |   |
+---+---+---+---+

Congratulations! You won! The tiles are arranged in numerical order.

Game over!
```

## Author Information

This Fifteen Puzzle Game was created by Kriti Bhargava. 

## Acknowledgments

- The Fifteen Puzzle is a classic sliding tile puzzle that has entertained people for many years.
Please feel free to contribute to or improve this game by submitting pull requests or reporting issues. Enjoy playing the Fifteen Puzzle, and happy coding!
