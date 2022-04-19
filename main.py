from datetime import datetime
from model import Player
from view import View
from itertools import islice

ROUNDS_NUMBER = 4
NOMBRE_DE_JOUEURS = 8


class Tournament:
    """Stocke les données du tournoi du jour"""

    def __init__(self, name_tournament, location, date, rounds_number = ROUNDS_NUMBER):
        self.name_tournament = name_tournament
        self.location = location
        self.date = date

class TimeControl:
    """qu'est-ce que c'est?"""
    pass


class View:
    def prompt_for_tournament_name(self):
        """demande le nom du tournoi"""
        name_tournament = input("tapez le nom du tournoi : ")
        if not name_tournament:
            return None
        return name_tournament

    def prompt_for_location(self):
        """demande le lieu du tournoi"""
        location = input("tapez le lieu du tournoi : ")
        if not location:
            return None
        return location

    def prompt_for_date(self):
        """demande la date du tournoi - A VERIFIER"""
        date = input("tapez la date du tournoi en format jj/mm/aa : ")
        if not date:
            return None
        return date

    def prompt_for_fullname_player(self):
        """demande les nom et prénom du joueur ou de la joueuse"""
        full_name_player = input("tapez les NOM et prénom du joueur ou de la joueuse : ")
        if not full_name_player:
            return None
        return full_name_player

    def prompt_for_birth_date(self):
        """demande la date de naissance du joueur ou de la joueuse"""
        birth_date = input("tapez la date de naissance du joueur ou "
                           "de la joueuse en format JJ/MM/AA: ")
        if not birth_date:
            return None
        return birth_date

    def prompt_for_gender(self):
        """demande le genre du joueur ou de la joueuse"""
        gender = input("tapez le genre du joueur ou"
                           "de la joueuse en format M/F/NB: ")
        if not gender:
            return None
        return gender

    def prompt_for_ranking(self):
        """demande le classement du joueur ou de la joueuse"""
        try:
            ranking = int(input("tapez le classement du joueur ou de la joueuse: "))
            return ranking
        except ValueError:
            print("Ooups! ce n'est pas un nombre entier valide. Veuillez réessayer...")
        except not ranking:
            return None
        except not ranking > 0:
            return ("saisissez un nombre entier positif")

    def prompt_for_scores(self,player):
        """Demande les scores des joueurs"""
        print("score de " + player[0] + ":")
        score = int(input())
        return score

class Description:
    """Les remarques générales du Directeur du tournoi vont ici"""
    def prompt_for_notes(self):
        """Demande le nom du tournoi"""
        tournament_notes = input("Remarques du Directeur sur le tournoi : ")
        if not tournament_notes:
            return None
        return tournament_notes

tournament = []
view = View()

name_tournament = view.prompt_for_tournament_name()
tournament.append(name_tournament)
location = view.prompt_for_location()
tournament.append(location)
date = view.prompt_for_date()
tournament.append(date)
print(tournament)


NOMBRE_DE_JOUEURS = 5
INDICE_NOMBRE_DE_JOUEURS_MOITIE = NOMBRE_DE_JOUEURS // 2 + 1

print(INDICE_NOMBRE_DE_JOUEURS_MOITIE)

players = []
view = View()
while len(players) < NOMBRE_DE_JOUEURS:
    fullname_player = view.prompt_for_fullname_player()
    """birth_date = view.prompt_for_birth_date()
    gender = view.prompt_for_gender()"""
    ranking = view.prompt_for_ranking()
    player = Player(fullname_player, None, None, ranking)
    player_ranking = [player.fullname_player, player.ranking]
    players.append(player_ranking)
    print(players)

#sort by second element of tuple
players.sort(key = lambda x: x[1])

print(players)

ranking_list = players

for player1, player2 in zip(ranking_list, islice(ranking_list,
                                                 INDICE_NOMBRE_DE_JOUEURS_MOITIE, None)):
    print(f'les premiers matchs sont:{player1, player2}')

for player in players:
    print(player)
    score = view.prompt_for_scores(player)
    new_ranking = player[1] + score
    print(new_ranking)
    player[1] = new_ranking
    new_player_ranking = [player[0], player[1]]
    for index in range(len(players)):
        if players[index] == player_ranking:
            players[index] == new_player_ranking
print(players)

