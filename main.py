"""
Tic-Tac-Toe
A simple game of tic-tac-toe.

for CSE210 w01 
by Alexander Turner
"""


import os


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

        print("{}{}{}".format(c, text, self.colors["default"]))

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
        self.grid = []

        self.run()

    def draw_grid(self):
        pass

    def update_grid(self):
        pass

    def prompt_action(self):
        pass

    def check_win(self):
        return True

    def run(self):
        while self.run:
            self.draw_grid()
            self.update_grid()
            self.run == self.check_win()


def main():
    print("Tic-Tac-Toe\n")
    Game()

if __name__=="__main__":
    main()