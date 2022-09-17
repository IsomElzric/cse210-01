"""
Tic-Tac-Toe
A simple game of tic-tac-toe.

for CSE210 w01 
by Alexander Turner
"""


import os
from re import X


GRID_HEIGHT = 3
GRID_WIDTH = 3


# System call to make colors work
os.system("")


class Text():
    """
    Handles our custom colors for our text.
    """

    def __init__(self):
        """
        Initiates the color dictionary.
        """

        self.colors = {
            "red": '\033[31m',
            "green": '\033[32m',
            "blue": '\033[34m',
            "default": '\033[0m',
        }

    def colored(self, color, text):
        """
        Handles changing the color of text and setting it back to the default.
        """

        if self.check_color(color):
            c = self.colors[color]
        else:
            c = self.colors["default"]

        return "{}{}{}".format(c, text, self.colors["default"])

    def check_color(self, color):
        """
        Checks if the color chosen is in our dictionary.
        """

        if color in self.colors:
            return True


class Game():
    """
    Handles our game loop and the functions for it.
    """

    def __init__(self, height=GRID_HEIGHT, width=GRID_WIDTH):
        self.height = height
        self.width = width
        self.run = True
        self.grid = []
        self.turn = 0
        self.player_x = Text().colored("red", "x")
        self.player_o = Text().colored("green", "o")

        self.build_grid()
        self.game_loop()

    def build_frame(self):
        frame = []
        for i in range(self.width):
            frame.append("-")
            if i < (self.width - 1):
                frame.append("+")

        return frame

    def build_spaces(self, start=1):
        spaces = []
        for i in range(self.width):
            spaces.append("{}".format(start))
            start += 1
            if i < (self.width - 1):
                    spaces.append("|")

        return spaces

    def build_grid(self):
        self.grid.append(self.build_spaces())
        self.grid.append(self.build_frame())
        self.grid.append(self.build_spaces(self.width + 1))
        self.grid.append(self.build_frame())
        self.grid.append(self.build_spaces(self.width * 2 + 1))    

    def draw_grid(self):
        for l in range(len(self.grid)):
            print("".join(self.grid[l]))
        self.prompt_action()

    def prompt_action(self):
        self.turn += 1
        player = ""

        if self.turn % 2 == 0:
            player = self.player_o
        else:
            player = self.player_x

        print()
        if self.check_win() == True:
            self.run = False
            print("Win")
        else:
            i = input("{}'s turn to choose a square (1-9): ".format(Text().colored("red", player)))
            print()

            for l in self.grid:
                if i in l:
                    space = l.index(i)
                    l[space] = player
        
    def check_win(self):
        if self.turn >= 5:
            win = True
        else:
            win = False

        return win

    def game_loop(self):
        while self.run == True:
            self.draw_grid()
            
def main():
    print("Tic-Tac-Toe\n")
    Game()

if __name__=="__main__":
    main()