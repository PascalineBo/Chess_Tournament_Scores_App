from itertools import permutations
from view import ROUNDS_NUMBER, NOMBRE_DE_JOUEURS


class Tournament:
    """Stocke les données du tournoi du jour"""

    def __init__(self, name_tournament, location, date, rounds_number = ROUNDS_NUMBER):
        self.name_tournament = name_tournament
        self.location = location
        self.date = date

class Player:
    """Stocke les données d'un joueur"""

    def __init__(self, fullname_player, birth_date, gender, ranking):
        self.fullname_player = fullname_player
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

class PossibleMatchsList:
    """Détermine les appariements possibles"""
    def __init__(self, players): # vérifier si ce constructeur est utile
        self.players = players # vérifier si j'ai besoin de cette ligne
        self.players = []

    def permutations_cleaning (self, players):
        self.matchs_list = list(permutations(players, 2))
        """efface de la liste des permutations possibles,
         les appariements de la première ronde"""
        del self.matchs_list[NOMBRE_DE_JOUEURS // 2 - 1]
        del self.matchs_list[((NOMBRE_DE_JOUEURS - 1) - 1 - 1)+ (NOMBRE_DE_JOUEURS // 2 + 1) ]
        return self.matchs_list

class Matchs:
    pass

class Ronde:
    """stocke les données d'une ronde"""

    def __init__(self, matchs_list, round_name, round_number,
                 start_date_time, end_date_time):
        self.round_name = round_name
        self.round_number = round_number
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matchs_list = matchs_list

class TimeControl:
    """qu'est-ce que c'est?"""
    pass

class Match:
    pass


