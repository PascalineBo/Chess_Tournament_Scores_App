
ROUNDS_NUMBER = 4

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

class TimeControl:
    """qu'est-ce que c'est?"""
    pass

class Match:
    pass


