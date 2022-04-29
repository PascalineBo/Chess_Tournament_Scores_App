from datetime import datetime
from itertools import islice, permutations
from model import Player, Ronde
from view import NOMBRE_DE_JOUEURS, INDICE_NOMBRE_DE_JOUEURS_MOITIE, ROUNDS_NUMBER


class TournamentData:
    """liste les données du tournoi"""
    def __init__(self,view):
        #models
        self.tournament = []

        #views
        self.view = view

    def get_tournament_data(self):
        name_tournament = self.view.prompt_for_tournament_name()
        self.tournament.append(name_tournament)
        location = self.view.prompt_for_location()
        self.tournament.append(location)
        date = self.view.prompt_for_date()
        self.tournament.append(date)

class Controller:
    """get and serializes Players Data"""
    def __init__(self, view):
        #models
        self.players = []
        self.rondes = []

        # views
        self.view = view

        # numéro de la ronde

    def get_players_data(self):
        while len(self.players) < NOMBRE_DE_JOUEURS:
            fullname_player = self.view.prompt_for_fullname_player()
            ranking = self.view.prompt_for_ranking()
            birth_date = self.view.prompt_for_birth_date()
            gender = self.view.prompt_for_gender()
            if not fullname_player:
                return
            elif not birth_date:
                return
            elif not gender:
                return
            elif not ranking:
                return

            player = Player(fullname_player,birth_date,gender,ranking)
            self.players.append(player)

            serialized_player = {'Player Full Name': player.fullname_player,
                         'Player Birth Date': player.birth_date,
                         'Player Gender': player.gender,
                         'Player Ranking': player.ranking,
                                 }

    def sort_players_by_ranking(self):
        """Remplit et trie une liste des joueurs avec leur classement"""
        self.players.sort(key=lambda x: x.ranking) # trie les joueurs selon leur classement
                                        # en ordre croissant
        return self.players #ranking_list

    def get_round_data(self):
        """demande le numéro de ronde"""
        round_number = int(self.view.prompt_for_new_game())
        round_name = self.view.prompt_for_round_name()
        list_of_matchs = []
        start_date_time = str(datetime.now())
        ronde = Ronde(list_of_matchs, round_name, round_number,
                 start_date_time)
        self.rondes.append(ronde)
        print(self.rondes)
        return self.rondes

    def matchs_list(self, players, rondes):
        """détermine l'appariement des joueurs pour la première ronde et les suivantes"""
        matchs_round_number = 1
        for ronde in rondes:
            matchs_round_number = int(ronde.round_number)
            print(matchs_round_number)
        if matchs_round_number == 1: # rule for the first round
            self.zip_list = zip(players, islice(players,
                                         INDICE_NOMBRE_DE_JOUEURS_MOITIE, None))
            self.matchs = list(self.zip_list)
            print(self.matchs)
            return self.matchs
        elif matchs_round_number > 1:
            self.matchs = []
            self.playerslist = players[:] # makes a copy of the list "players"
            self.match = (self.playerslist.pop(0), self.playerslist.pop(matchs_round_number - 2))
            self.matchs.append(self.match)
            if matchs_round_number == 3: # specific rule for the third round
                 while len(self.playerslist) > 0:
                    self.match = (self.playerslist.pop(0), self.playerslist.pop())
                    self.matchs.append(self.match)
            elif matchs_round_number == 4: # specific rule for the fourth round
                while len(self.playerslist) > 0:
                    self.match = (self.playerslist.pop(0), self.playerslist.pop(0))
                    self.matchs.append(self.match)
            else:
                while len(self.playerslist) > 0: # specific rule for the second round
                    self.match = (self.playerslist[0], self.playerslist[1])
                    self.playerslist.pop(0)
                    self.playerslist.pop(0)
                    self.matchs.append(self.match)
            return self.matchs

    def run(self):
        self.get_players_data()
        self.sort_players_by_ranking()
        self.view.show_players_scores(self.players)
        self.get_round_data()
        self.view.show_round(self.matchs_list(self.players, self.rondes), self.rondes)
        self.view.prompt_for_scores(self.matchs_list(self.players, self.rondes))
        self.sort_players_by_ranking()
        self.view.show_players_scores(self.players)

        for i in range(0,ROUNDS_NUMBER-1):
            self.get_round_data()
            self.view.show_round(self.matchs_list(self.players, self.rondes), self.rondes)
            self.view.prompt_for_scores(self.matchs_list(self.players, self.rondes))
            self.sort_players_by_ranking()
            self.view.show_players_scores(self.players)

