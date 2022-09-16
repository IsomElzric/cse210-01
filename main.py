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
        self.grid = []

        self.build_grid()
        self.run()

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

    def update_grid(self):
        pass

    def prompt_action(self):
        print()
        i = input("{} turn to choose a square (1-9): ".format(Text().colored("red", "x's")))

    def check_win(self):
        return True

    def run(self):
        while self.run:
            self.draw_grid()
            self.update_grid()
            if self.check_win() == True:
                break

def main():
    print("Tic-Tac-Toe\n")
    Game()

if __name__=="__main__":
    main()