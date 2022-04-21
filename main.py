from controller import Controller, TournamentData
from model import Player
from view import View

def main():
    view = View()
    tournament_data = TournamentData(view)
    game = Controller(view)
    game.run()


main()
