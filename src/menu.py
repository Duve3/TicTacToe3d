import pygame
import ui
from ui import CUColor


class Menu:
    def __init__(self, screen: ui.CScreen, debug: bool = False):
        self.screen = screen
        self.debug = debug

        # TODO: add buttons for entering game, do NOT work hard on this menu, priority is the acutal game!!

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.screen.close(kill=True)

            self.screen.fill(CUColor.WHITE())



            pygame.display.flip()

