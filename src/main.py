from menu import Menu
import ui

def main():
    ui.init()

    screen = ui.CScreen((600, 600), caption="TicTacToe4D", clock=True, fps=60)  # intentionally slowing

    menu = Menu(screen)

    menu.run()




if __name__ == "__main__":
    main()
