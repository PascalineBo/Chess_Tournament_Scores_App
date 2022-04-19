from model import Player
from view import View
from itertools import islice


NOMBRE_DE_JOUEURS = 8
INDICE_NOMBRE_DE_JOUEURS_MOITIE = NOMBRE_DE_JOUEURS // 2 + 1


class TournamentData:
    """liste les données du tournoi"""
    def __init__(self,view):
        #models
        self.tournament = []

        #views
        self.view = View()

    def get_tournament_data(self):
        name_tournament = self.view.prompt_for_tournament_name()
        self.tournament.append(name_tournament)
        location = self.view.prompt_for_location()
        self.tournament.append(location)
        date = self.view.prompt_for_date()
        self.tournament.append(date)

class PlayersData:
    """serialize Players Data"""
    def __init__(self,view):
        #models
        self.players = []

        # views
        self.view = View()

    def get_players_data(self):
        while len(self.players_data) < NOMBRE_DE_JOUEURS:
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

    player = PLayer(fullname_player,birth_date,gender,ranking)
    player_ranking = [player.fullname_player, player.ranking]
    self.players.append(player_ranking)

    serialized_player = {'Player Full Name': player.fullname_player,
                         'Player Birth Date': player.birthdate,
                         'Player Gender': player.gender,
                         'Player Ranking': player.ranking,
                         }

    def get_players_scores(self):
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

class PlayersList:
    """Initie la liste des joueurs selon leur classement"""
    def get_players_and_ranking(self):
        """Remplit et trie une liste des joueurs avec leur classement"""
        players.sort(key=lambda x: x[1]) # trie les joueurs selon leur classement
                                        # en ordre croissant
        return ranking_list

class Round:
    """Règle des rondes"""
    def first_round(self):
        """Régle d'appariement pour le premier tour - tournoi Suisse"""
        for player1, player2 in zip(ranking_list, islice(ranking_list,
                                                 INDICE_NOMBRE_DE_JOUEURS_MOITIE, None)):
            print(f'les premiers matchs sont:{player1, player2}')


