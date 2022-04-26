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
    def __init__(self, players):
        self.players = players
        self.players = []

    def permutations_cleaning (self, players):
        self.matchs_list = list(permutations(players, 2))
        """efface de la liste des permutations possibles,
         les appariements de la première ronde"""
        del self.matchs_list[NOMBRE_DE_JOUEURS // 2 - 1]
        del self.matchs_list[((NOMBRE_DE_JOUEURS - 1) - 1 - 1)+ (NOMBRE_DE_JOUEURS // 2 + 1) ]
        """if NOMBRE_DE_JOUEURS > 4:
            del self.matchs_list[((NOMBRE_DE_JOUEURS - 1) - 1 - 1)+
                                 ((NOMBRE_DE_JOUEURS - 1) - 1) +
                                 (NOMBRE_DE_JOUEURS // 2 + 1 + 1)]
            if NOMBRE_DE_JOUEURS > 6:
                del self.matchs_list[((NOMBRE_DE_JOUEURS - 1) - 1 - 1) +
                                     ((NOMBRE_DE_JOUEURS - 1) - 1) +
                                     ((NOMBRE_DE_JOUEURS - 1) - 1) +
                                     (NOMBRE_DE_JOUEURS // 2 + 1 + 1 + 1)]"""
        """efface les appariements inversés (redondants)"""
        """for i in range(0, NOMBRE_DE_JOUEURS - 1):
            self.matchs_list.pop()
        if NOMBRE_DE_JOUEURS > 4:
            for i in range(0, NOMBRE_DE_JOUEURS - 1):
                self.matchs_list.pop()
        if NOMBRE_DE_JOUEURS > 6:
            for i in range(0, NOMBRE_DE_JOUEURS - 1):
                self.matchs_list.pop()"""
        return self.matchs_list


class TimeControl:
    """qu'est-ce que c'est?"""
    pass

class Match:
    pass


