from menu import Menu
from game import Game
import ui

def main(skip=False, debug=False):
    ui.init()

    screen = ui.CScreen((600, 600), caption="TicTacToe4D", clock=True, fps=60)  # intentionally slowing

    menu = Menu(screen, debug=debug)
    game = Game(screen, debug=debug)
    if not skip:
        menu.run()

    game.run()


if __name__ == "__main__":
    main(skip=True, debug=True)
