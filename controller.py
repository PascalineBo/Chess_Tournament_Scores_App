from itertools import islice, permutations
from model import Player, PossibleMatchsList
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
    def __init__(self,view):
        #models
        self.players = []
        self.matchs = []

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

    def matchs_list(self, players):
        """détermine l'appariement des joueurs pour la première ronde et les suivantes"""
        round_number = int(self.view.prompt_for_new_game())
        if round_number == 1:
            self.zip_list = zip(players, islice(players,
                                         INDICE_NOMBRE_DE_JOUEURS_MOITIE, None))
            self.matchs = list(self.zip_list)
            return self.matchs
        elif round_number > 1:
                self.matchs = []
                self.playerslist = players[:]
                while len(self.playerslist) > 0:
                    self.match = (self.playerslist[0], self.playerslist[(round_number - 1)])
                    self.matchs.append(self.match)
                    self.playerslist.pop(0)
                    self.playerslist.pop(0)
                return self.matchs

    def matchs_list2(self, players):
        """détermine l'appariement des joueurs pour la partie deux"""
        self.matchs_list = list(permutations(players, 2))
        print(self.matchs_list)
        self.matchs = list(islice(self.matchs_list,
                                  0,None,2*NOMBRE_DE_JOUEURS))
        return self.matchs

    def matchs_listn(self, players, i):
        """détermine l'appariement des joueurs pour les parties suivantes"""
        possible_matchs_list = PossibleMatchsList(players)
        matchs_list = possible_matchs_list.permutations_cleaning(players)
        print(matchs_list)
        print(len(matchs_list))
        """détermine les matchs de la ronde"""
        self.matchs = list(islice(matchs_list,
                                  ((NOMBRE_DE_JOUEURS - 1 -1 -1) +
                                   (NOMBRE_DE_JOUEURS - 1 - 1)
                                   + 1
                                   + i),
                                  None, (NOMBRE_DE_JOUEURS + 2 + i)))
        return self.matchs


    def get_players_scores(self, players):
        """Liste les joueurs et leur score après une ronde"""
        for player in players:
            score = self.view.prompt_for_scores(player)
            new_ranking = player.ranking + score
            player.ranking = new_ranking
        return players

    def run(self):
        self.get_players_data()
        self.sort_players_by_ranking()
        self.view.show_players_scores(self.players)
        self.view.show_round(self.matchs_list(self.players))
        self.get_players_scores(self.players)
        self.sort_players_by_ranking()
        self.view.show_players_scores(self.players)

        for i in range(0,ROUNDS_NUMBER-1):
            self.view.show_round(self.matchs_list(self.players))
            self.get_players_scores(self.players)
            self.sort_players_by_ranking()
            self.view.show_players_scores(self.players)

