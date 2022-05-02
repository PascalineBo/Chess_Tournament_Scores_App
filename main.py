from controller import Controller
from model import Player
from view import View

def main():
    view = View()
    game = Controller(view)
    game.run()

main()
