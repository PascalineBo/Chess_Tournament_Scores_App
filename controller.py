from model import Player
from itertools import islice, cycle, permutations




NOMBRE_DE_JOUEURS = 4
INDICE_NOMBRE_DE_JOUEURS_MOITIE = NOMBRE_DE_JOUEURS // 2


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
        self.matchs_list = []

        # views
        self.view = view

        # numéro de la ronde
        self.i = 1

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
            player_ranking = [player.fullname_player, player.ranking]
            self.players.append(player_ranking)

            serialized_player = {'Player Full Name': player.fullname_player,
                         'Player Birth Date': player.birth_date,
                         'Player Gender': player.gender,
                         'Player Ranking': player.ranking,
                                 }

    def sort_players_by_ranking(self):
        """Remplit et trie une liste des joueurs avec leur classement"""
        self.players.sort(key=lambda x: x[1]) # trie les joueurs selon leur classement
                                        # en ordre croissant
        return self.players #ranking_list

    def matchs_list1(self, players):
        """détermine l'appariement des joueurs pour la première ronde"""
        self.zip_list = zip(players, islice(players,
                                     INDICE_NOMBRE_DE_JOUEURS_MOITIE, None))
        self.matchs = list(self.zip_list)
        return self.matchs

    def matchs_list2(self, players):
        """détermine l'appariement des joueurs pour la partie deux"""
        self.matchs_list = list(permutations(players, 2))
        print(self.matchs_list)
        self.matchs = list(islice(self.matchs_list,0,None,2**(NOMBRE_DE_JOUEURS-1)))
        return self.matchs

    def matchs_listn(self, players):
        """détermine l'appariement des joueurs pour les parties suivantes"""
        self.matchs_list = list(permutations(players, 2))
        """efface de la liste des permutations possibles,
         les appariements de la première ronde"""
        del self.matchs_list[1],
        del self.matchs_list[NOMBRE_DE_JOUEURS]
        print(self.matchs_list)
        print(len(self.matchs_list))
        self.matchs = list(islice(self.matchs_list, 1, None, NOMBRE_DE_JOUEURS))
        return self.matchs


    def get_players_scores(self, players):
        """Liste les joueurs et leur score après une ronde"""
        for player in players:
            score = self.view.prompt_for_scores(player)
            new_ranking = player[1] + score
            player[1] = new_ranking
            player_ranking = [player[0], player[1]]
            new_player_ranking = [player[0], player[1]]
            for index in range(len(players)):
                if players[index] == player_ranking:
                    players[index] == new_player_ranking
        return players

    def run(self):
        self.get_players_data()
        self.sort_players_by_ranking()
        self.view.show_players_scores(self.players)
        self.view.show_round(self.matchs_list1(self.players))
        self.get_players_scores(self.players)
        self.sort_players_by_ranking()
        self.view.show_players_scores(self.players)
        self.view.show_round(self.matchs_list2(self.players))

        running = True

        while running:
            self.get_players_scores(self.players)
            self.sort_players_by_ranking()
            self.view.show_players_scores(self.players)
            """self.view.show_round(self.matchs_listn(self.players))"""
            self.view.show_round(self.matchs_listn(self.players))
            running = self.view.prompt_for_new_game()

