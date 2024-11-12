"""
game.py

the game
i plan to make it so in the top left it says whose turn it currently is
i plan to make it zoom in on whatever is tile is being actively used
^ this zoom in feature means we have to implement a camera now... sigh.
"""
import pygame
import ui
from ui import CUColor
from enum import Enum

class PossibleObjects(Enum):
    X = "x"
    O = "o"
    EMPTY = "b"
    TIE = "t"


class TicTacToe:
    """
    TicTacToe Object
    Handles the micro TicTacToe parts, simplifies coding
    """
    def __init__(self):  # TODO: put more data in the __init__ class rather than the draw class
        # TODO: switch to surfaces? it would be better for scaling than images and would allow more features than raw images (hit boxes, etc)
        self.state = [
            [PossibleObjects.EMPTY, PossibleObjects.EMPTY, PossibleObjects.EMPTY],
            [PossibleObjects.EMPTY, PossibleObjects.EMPTY, PossibleObjects.EMPTY],
            [PossibleObjects.EMPTY, PossibleObjects.EMPTY, PossibleObjects.EMPTY]
        ]

        self.victory = PossibleObjects.EMPTY

        self.last_drawn = (-1, -1)
        self.size = (-1, -1)

    def update_state(self, row, col, result):
        self.state[row][col] = result

    def draw(self, screen: pygame.Surface, image_tictactoe: pygame.Surface, image_x, image_o, pos_x, pos_y):
        screen.blit(image_tictactoe, (pos_x, pos_y))
        for y, row in enumerate(self.state):
            for x, obj in enumerate(row):
                if obj == PossibleObjects.EMPTY:
                    continue

                if obj == PossibleObjects.X:
                    screen.blit(image_x, (x * 100, y * 100))

                elif obj == PossibleObjects.O:
                    screen.blit(image_o, (x * 100, y * 100))

        self.last_drawn = (pos_x, pos_y)
        self.size = image_tictactoe.size

    def in_hitbox(self, offset, mx, my):
        hitbox = pygame.Rect(self.last_drawn[0] - offset, self.last_drawn[1] - offset, self.size[0], self.size[1])

    def __repr__(self):
        """
        Useful for debugging, prints the current values exactly
        """
        return f"""
{self.state[0][0].value} {self.state[0][1].value} {self.state[0][2].value}
{self.state[1][0].value} {self.state[1][1].value} {self.state[1][2].value}
{self.state[2][0].value} {self.state[2][1].value} {self.state[2][2].value}                
                """
    def completed_game(self) -> PossibleObjects:
        """
        There is only four/five possible ways to win, either you have a row up, row down, row left, row right, or row diagonal

        we can check first if there is more than three of either type to check for win

        we then should check for rows, check eahc one to see if there is a winning row

        now we will do a column check which just checks top row to see if there is one of each type, then checks downwards

        next we will do a diagonal check, there is two ways for diagonals, left to right, or right to left
        ^ all diagonals require a center piece, check if there is a center piece of that type, then check up and down

        now we have the ability to check for all types of possibilities in a tic tac toe game
        :return PossibleObjects: The object who won, PossibleObject.EMPTY if none
        """
        num_x = sum([row.count(PossibleObjects.X) for row in self.state])
        num_o = sum([row.count(PossibleObjects.O) for row in self.state])

        # below minimums check
        if num_x < 3 and num_o < 3:
            return PossibleObjects.EMPTY

        # tie check
        if num_x + num_o == 9:
            return PossibleObjects.TIE

        # ROW CHECK
        for row in self.state:
            if row.count(PossibleObjects.X) == 3:
                return PossibleObjects.X

            elif row.count(PossibleObjects.O) == 3:
                return PossibleObjects.O

        # COL CHECK
        # if there is a column victory then there must be one in the top row
        for x, value in enumerate(self.state[0]):
            if value == PossibleObjects.X:
                if self.state[1][x] == PossibleObjects.X and self.state[2][x] == PossibleObjects.X:
                    return PossibleObjects.X

            elif value == PossibleObjects.O:
                if self.state[1][x] == PossibleObjects.O and self.state[2][x] == PossibleObjects.O:
                    return PossibleObjects.O

        # DIA CHECK
        if self.state[1][1] == PossibleObjects.X:
            if self.state[0][0] == PossibleObjects.X and self.state[2][2] == PossibleObjects.X:
                return PossibleObjects.X

            if self.state[0][2] == PossibleObjects.X and self.state[2][0] == PossibleObjects.X:
                return PossibleObjects.X

        elif self.state[1][1] == PossibleObjects.O:
            if self.state[0][0] == PossibleObjects.O and self.state[2][2] == PossibleObjects.O:
                return PossibleObjects.O

            if self.state[0][2] == PossibleObjects.O and self.state[2][0] == PossibleObjects.O:
                return PossibleObjects.O

        return PossibleObjects.EMPTY




class Game:
    def __init__(self, screen: ui.CScreen, debug: bool = False):
        self.screen = screen
        self.debug = debug

        self.game_list = [
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()]
                      ]

        # TODO: fix how the images aren't scaled correctly, find good values, also make image bliting work for X's and O's
        current = '\\'.join(__file__.split('\\')[:-1])
        self.IMAGE_TicTacToe = pygame.transform.scale(pygame.image.load(f"{current}/assets/TicTacToeBoard.png"), (150, 150))
        self.IMAGE_TicTacToeMegaBoard = pygame.transform.scale(pygame.image.load(f"{current}/assets/TicTacToeBoard.png"), (600, 600))
        self.IMAGE_TicX = pygame.transform.scale(pygame.image.load(f"{current}/assets/TicTacToeX.png"), (100, 100))
        self.IMAGE_TicO = pygame.transform.scale(pygame.image.load(f"{current}/assets/TicTacToeO.png"), (100, 100))

        # debug stuff, tests if tictactoe board works
        if self.debug:
            import random  # to optimize we will NOT important random unless debug
            self.reset_game()

            chosen = random.choice([PossibleObjects.X, PossibleObjects.O])

            print("Checking for row victory on", chosen)

            row = random.randint(0, 2)

            self.game_list[0][0].update_state(row, 0, chosen)
            self.game_list[0][0].update_state(row, 1, chosen)
            self.game_list[0][0].update_state(row, 2, chosen)

            print("Who won:", self.game_list[0][0].completed_game())
            print(self.game_list[0][0])


            print("Checking for Col victory on", chosen)

            col = random.randint(0, 2)

            self.reset_game()

            self.game_list[0][0].update_state(0, col, chosen)
            self.game_list[0][0].update_state(1, col, chosen)
            self.game_list[0][0].update_state(2, col, chosen)

            print("Who won:", self.game_list[0][0].completed_game())
            print(self.game_list[0][0])


            print("Checking for Dia victory on", chosen)

            row_top = random.choice([0, 2])
            row_bottom = 0 if row_top == 2 else 2

            self.reset_game()

            self.game_list[0][0].update_state(0, row_top, chosen)
            self.game_list[0][0].update_state(1, 1, chosen)
            self.game_list[0][0].update_state(2, row_bottom, chosen)

            print("Who won:", self.game_list[0][0].completed_game())
            print(self.game_list[0][0])


            print("Checking for TIE")

            opposite = PossibleObjects.O if chosen == PossibleObjects.X else PossibleObjects.X

            self.reset_game()

            self.game_list[0][0].update_state(0, 0, chosen)
            self.game_list[0][0].update_state(1, 0, opposite)
            self.game_list[0][0].update_state(2, 0, chosen)
            self.game_list[0][0].update_state(0, 1, chosen)
            self.game_list[0][0].update_state(1, 1, opposite)
            self.game_list[0][0].update_state(2, 1, chosen)
            self.game_list[0][0].update_state(0, 2, chosen)
            self.game_list[0][0].update_state(1, 2, opposite)
            self.game_list[0][0].update_state(2, 2, chosen)

            print("Who won:", self.game_list[0][0].completed_game())
            print(self.game_list[0][0])



    def reset_game(self):
        self.game_list = [
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()]
                      ]

    def run(self):
        while True:
            self.screen.tick()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.screen.close(kill=True)

            self.screen.fill(CUColor.WHITE())

            offset = 15

            for y, row in enumerate(self.game_list):
                for x, obj in enumerate(row):
                    # we are using self.screen.surface rather than self.screen.draw() bc
                    # I would rather not implement that in the UI lib and implement it in the actual code
                    print(x * 50, y * 50)
                    obj.draw(self.screen.surface, self.IMAGE_TicTacToe, self.IMAGE_TicX, self.IMAGE_TicO, offset + x * 210, offset + y * 210)

            self.screen.draw(self.IMAGE_TicTacToeMegaBoard, (0, 0))

            pygame.display.flip()

