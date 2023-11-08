from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
import numpy as np

# Function to add a button with a given label to the GUI

# GUI for the classic sliding tile puzzle game Fifteen

def add_button(pos, label):
    button = Button(gui, textvariable=label, font=font1, width=4, height=2, command=lambda pos=pos: clickButton((pos // 4, pos % 4)))
    button.grid(row=pos // 4, column=pos % 4)
    buttons[pos] = button


# Function to check if two tiles are adjacent
def is_adjacent(row1, col1, row2, col2):
    return (row1 == row2 and abs(col1 - col2) == 1) or (col1 == col2 and abs(row1 - row2) == 1)


# Function to handle button clicks
def clickButton(pos):
    global board
    row, col = pos
    empty_pos = np.where(board.tiles == 0)[0][0]  # change None to 0
    empty_row, empty_col = empty_pos // 4, empty_pos % 4
    if is_adjacent(row, col, empty_row, empty_col):
        # swap the tiles
        board.tiles[row * 4 + col], board.tiles[empty_pos] = board.tiles[empty_pos], board.tiles[row * 4 + col]
        # update the GUI
        update_gui()
        if board.is_solved():
            # show win message if the puzzle is solved
            win_label.config(text="Congratulations, you won!")


# Function to shuffle the tiles
def shuffle_tiles():
    global board
    board.shuffle()
    update_gui()


# Function to solve the puzzle
def update_gui():
    for i in range(16):
        if board.tiles[i] is None:
            labels[i].set("")
        elif board.tiles[i] == 0:
            labels[i].set("")
        else:
            labels[i].set(str(board.tiles[i]))
        buttons[i].config(textvariable=labels[i])


if __name__ == '__main__':
    # make a board with tiles
    board = Fifteen()
    empty = len(board.tiles) - 1
    # make a GUI window
    gui = Tk()
    gui.title("Fifteen")

    # make fonts
    font1 = font.Font(family='Helvetica', size='25', weight='bold')

    # make buttons with labels
    labels = [StringVar() for i in range(16)]
    buttons = [None] * 16

    for i in range(16):
        add_button(i, labels[i])

    # modify buttons
    buttons[empty].configure(bg='white')

    # add a button shuffle to shuffle the tiles
    shuffle_button = Button(gui, text="Shuffle", font=font1, width=6, height=2, command=shuffle_tiles)
    shuffle_button.grid(row=4, column=2)

    # add a label for the win message
    win_label = Label(gui, text="", font=font1)
    win_label.grid(row=5, column=0, columnspan=4)

    # arrange buttons on the grid
    gui.mainloop()
