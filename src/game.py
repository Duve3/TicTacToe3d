import pygame
import ui
from ui import CUColor
from enum import Enum

class PossibleObjects(Enum):
    X = "x",
    O = "o",
    EMPTY = "blank"





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

    def completed_game(self):
        # TODO: figure out how to check if anyone has won the game
        pass


class Game:
    def __init__(self, screen: ui.CScreen):
        self.screen = screen
        
        self.game_list = [
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()]
                      ]

        # TODO: make a working game

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.screen.close(kill=True)

            self.screen.fill(CUColor.BLACK())

            pygame.display.flip()

