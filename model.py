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

class Ronde:
    """stocke les données d'une ronde"""

    def __init__(self, list_of_matchs, round_name, round_number,
                 start_date_time): # voir comment socker aussi end_date time
        self.round_name = round_name
        self.round_number = round_number
        self.start_date_time = start_date_time
        self.list_of_matchs = list_of_matchs

class TimeControl:
    """qu'est-ce que c'est?"""
    pass

class Match:
    pass


