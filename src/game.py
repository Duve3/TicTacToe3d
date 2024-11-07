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
    def __init__(self):
        self.state = [
            [PossibleObjects.EMPTY, PossibleObjects.EMPTY, PossibleObjects.EMPTY],
            [PossibleObjects.EMPTY, PossibleObjects.EMPTY, PossibleObjects.EMPTY],
            [PossibleObjects.EMPTY, PossibleObjects.EMPTY, PossibleObjects.EMPTY]
        ]

        self.victory = PossibleObjects.EMPTY

    def update_state(self, row, col, result):
        self.state[row][col] = result

    def __repr__(self):
        return f"""
{self.state[0][0].value} {self.state[0][1].value} {self.state[0][2].value}
{self.state[1][0].value} {self.state[1][1].value} {self.state[1][2].value}
{self.state[2][0].value} {self.state[2][1].value} {self.state[2][2].value}                
                """
    def completed_game(self) -> PossibleObjects:
        # TODO: figure out how to check if anyone has won the game
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

        self.game_list = self.game_list = [
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()]
                      ]


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
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.screen.close(kill=True)

            self.screen.fill(CUColor.BLACK())

            pygame.display.flip()

