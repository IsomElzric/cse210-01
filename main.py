"""
Tic-Tac-Toe
A simple game of tic-tac-toe. Originally the idea was to allow for the players
to decide how big the board would be, however time constraints didn't allow for 
that in scope of this project.

for CSE 210 w01 
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
        """
        Initate our game variables, builds the grid, and begins the game loop.
        """
        self.height = height
        self.width = width
        self.run = True
        self.grid = []
        self.turn = 0
        self.player_x = Text().colored("red", "x")
        self.player_o = Text().colored("green", "o")

        # Builds the grid elements
        self.build_grid()

        # Starts the game loop
        self.game_loop()

    def build_frame(self):
        """
        This creates the frame between the numbered spaces on rows 2 and 3.
        """
        frame = []
        for i in range(self.width):
            frame.append("-")
            if i < (self.width - 1):
                frame.append("+")

        return frame

    def build_spaces(self, start=1):
        """
        Builds the seperators between the spaces and sets the spaces to their numbers.
        """
        spaces = []
        for i in range(self.width):
            spaces.append("{}".format(start))
            start += 1
            if i < (self.width - 1):
                    spaces.append("|")

        return spaces

    def build_grid(self):
        """
        Takes the 5 seperate rows and combines them into our full grid list.
        """
        self.grid.append(self.build_spaces())
        self.grid.append(self.build_frame())
        self.grid.append(self.build_spaces(self.width + 1))
        self.grid.append(self.build_frame())
        self.grid.append(self.build_spaces(self.width * 2 + 1))    

    def draw_grid(self):
        """
        Draws our grid list to the screen in a formatted way.
        """
        for l in range(len(self.grid)):
            print("".join(self.grid[l]))

    def get_player(self):
        """
        Figures out which player's turn it is currently and returns their symbol.
        """
        player = ""
        if self.turn % 2 == 0:
            player = self.player_o
        else:
            player = self.player_x

        return player

    def prompt_action(self):
        """
        Increments the turn, prompts the player for a number, and checks if either has won.
        """
        self.turn += 1
        
        player = self.get_player()

        print()
        i = input("{}'s turn to choose a square (1-9): ".format(Text().colored("red", player)))
        print()

        # This sets each number to be the player's symbol
        for l in self.grid:
            if i in l:
                space = l.index(i)
                l[space] = player
        
        if self.check_win() == True:
            self.run = False
            self.draw_grid()
            print()

            if self.turn == 9:
                print("It's a draw!")
            
            else:
                print("{}'s win!".format(player))
        
    def check_win(self):
        """
        Checks if anyone has won or if the game has reached turn 9 without a win.
        """
        player = self.get_player()
        win = False

        left_right = [self.grid[0][0], self.grid[2][2], self.grid[4][4]]
        right_left = [self.grid[0][4], self.grid[2][2], self.grid[4][0]]

        for row in self.grid:
            # print("DEBUG: {}".format(row))
            if player in row:
                # print("DEBUG: {} found in {}".format(player, row))
                player_space = row.index(player)
                column = [self.grid[0][player_space], 
                        self.grid[2][player_space], 
                        self.grid[4][player_space]]
                
                if len(row) - len(set(row)) == 3:
                    # print("DEBUG: The row {} differs by length of {}".format(row, len(row) - len(set(row))))
                    win = True
                
                elif len(column) - len(set(column)) == 2:
                    # print("DEBUG: {} found in column {}".format(player, column))
                    win = True
                
                elif len(left_right) - len(set(left_right)) == 2:
                    # print("DEBUG: {} found in left to right diagonal {}".format(player, left_right))
                    win = True

                elif len(right_left) - len(set(right_left)) == 2:
                    # print("DEBUG: {} found in right to left diagonal {}".format(player, right_left))
                    win = True
                
                elif self.turn == 9:
                    win = True

        return win

    def game_loop(self):
        """
        Holds our game loop.
        """
        while self.run == True:
            self.draw_grid()
            self.prompt_action()
            
def main():
    """
    Prints the header and calls the game object.
    """
    print("Tic-Tac-Toe\n")
    Game()

if __name__=="__main__":
    main()