from datetime import datetime
from itertools import islice, permutations
from model import Player, Ronde, Tournament
from view import NOMBRE_DE_JOUEURS, INDICE_NOMBRE_DE_JOUEURS_MOITIE, ROUNDS_NUMBER
from tinydb import TinyDB


class Controller:
    """get and serializes Players Data"""
    def __init__(self, view):
        #models
        self.players = []
        self.rondes = []
        self.serialized_players = []
        #self.tournaments = []
        #self.serialized_tournaments = []
        self.tournament_name = str
        self.location = str
        self.date = str

        # views
        self.view = view

    def get_tournament_data_start(self):
        """récupère les données du tournoi au début"""
        tournament_name = self.view.prompt_for_tournament_name()
        location = self.view.prompt_for_location()
        date = self.view.prompt_for_date()
        rondes = self.rondes
        tournament_notes = str
        self.tournament = Tournament(tournament_name, location, date,rondes, tournament_notes)

    def get_tournament_data_end(self):
        """récupère les données du tournoi à la fin et les sérialise"""
        rounds_number = ROUNDS_NUMBER
        tournament_notes = self.view.prompt_for_notes()
        #tournament = Tournament(self.tournament_name, self.location, self.date, self.rondes, tournament_notes, rounds_number)
        self.tournament.tournament_notes = tournament_notes
        self.tournament.rondes = self.rondes
        #self.tournaments.append(tournament)

    def serialize_tournament(self):
        """serialise les tournois"""
        #tournaments = self.tournaments
        #for tournament in tournaments:
        serialized_tournament = {'Tournament Name': self.tournament.tournament_name,
                                     'Tournament Location': self.tournament.location,
                                     'Tournament Date': self.tournament.date,
                                     'Tournament Rondes': self.serialize_rondes(),
                                     'Tournament Notes': self.tournament.tournament_notes,
                                     'Tournament Rounds Number': self.tournament.rounds_number
                                     }
        #    self.serialized_tournaments.append(serialized_tournament)
        return serialized_tournament

    def serialize_tournaments_old(self):
        """serialise les tournois"""
        tournaments = self.tournaments
        for tournament in tournaments:
            serialized_tournament = {'Tournament Name': tournament.tournament_name,
                                     'Tournament Location': tournament.location,
                                     'Tournament Date': tournament.date,
                                     'Tournament Rondes': tournament.rondes,
                                     'Tournament Notes': tournament.tournament_notes,
                                     'Tournament Rounds Number': tournament.rounds_number
                                     }
            self.serialized_tournaments.append(serialized_tournament)
        return self.serialized_tournaments

    def serialize_rondes(self):
        """sérialise les rondes"""
        serialized_rondes = []
        for ronde in self.tournament.rondes:
            serialized_list_of_matchs = []
            for match in ronde.list_of_matchs:
                serialized_match = {'Match': match[0].fullname_player +" vs "+
                                    match[1].fullname_player}
                serialized_list_of_matchs.append(serialized_match)
            serialized_ronde = {
                'Ronde Name': ronde.round_name,
                'Ronde Number': ronde.round_number,
                'Ronde Start Time': ronde.start_date_time,
                'Ronde List of Matchs': serialized_list_of_matchs,
                'Ronde End Time': ronde.end_time
            }
            serialized_rondes.append(serialized_ronde)
        return serialized_rondes

    def get_players_data(self):
        """récupère les données des joueurs et stocke les joueurs dans une liste"""
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

    def serialize_players(self):
        """serialilse les joueurs"""
        players = self.players
        for player in players:
            serialized_player = {'Player Full Name': player.fullname_player,
                                 'Player Birth Date': player.birth_date,
                                 'Player Gender': player.gender,
                                 'Player Ranking': player.ranking,
                                 }
            self.serialized_players.append(serialized_player)
        return self.serialized_players

    def sort_players_by_ranking(self):
        """Remplit et trie une liste des joueurs avec leur classement"""
        self.players.sort(key=lambda x: x.ranking) # trie les joueurs selon leur classement
                                        # en ordre croissant
        return self.players #ranking_list

    def get_round_data(self):
        """demande les données des rondes et les stocke dans une liste"""
        round_number = int(self.view.prompt_for_new_game())
        round_name = self.view.prompt_for_round_name()
        list_of_matchs = []
        start_date_time = str(datetime.now())
        end_time = str(0)
        ronde = Ronde(list_of_matchs, round_name, round_number,
                 start_date_time, end_time)
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

    def get_round_end_time(self):
        end_time = 0
        while self.view.prompt_for_end_time() != 'O':
            end_time = str(datetime.now())
        self.rondes[-1].end_time = end_time
        return self.rondes

    def export_data_in_database(self,serialized_players,serialized_tournaments):
        """exporte les données dans une base de données TinyDB"""
        db = TinyDB("databases.json")
        players_table = db.table("players")
        players_table.truncate()  # clear the table first
        players_table.insert_multiple(serialized_players)
        tournament_table = db.table("tournament")
        tournament_table.truncate()  # clear the table first
        # tournament_table.insert_multiple(serialized_tournaments)
        try:
            print(serialized_tournaments)
            tournament_table.insert(serialized_tournaments)
        except ValueError:
            print(ValueError)
        return

    def run(self):
        self.get_tournament_data_start()
        self.get_players_data()
        self.sort_players_by_ranking()
        self.view.show_players_scores(self.players)
        self.get_round_data()
        self.view.show_round(self.matchs_list(self.players, self.rondes), self.rondes)
        self.rondes[-1].list_of_matchs = self.matchs
        self.get_round_end_time()
        self.tournament.rondes = self.rondes
        self.view.prompt_for_scores(self.matchs_list(self.players, self.rondes))
        self.sort_players_by_ranking()
        self.view.show_players_scores(self.players)

        for i in range(0,ROUNDS_NUMBER-1):
            self.get_round_data()
            self.view.show_round(self.matchs_list(self.players, self.rondes), self.rondes)
            self.rondes[-1].list_of_matchs = self.matchs_list(self.players, self.rondes)
            self.get_round_end_time()
            self.tournament.rondes = self.rondes
            self.view.prompt_for_scores(self.matchs_list(self.players, self.rondes))
            self.sort_players_by_ranking()
            self.view.show_players_scores(self.players)

        self.get_tournament_data_end()
        print(self.rondes)
        print(self.tournament)
        self.serialize_players()
        print(self.serialized_players)
        #self.export_data_in_database(self.serialized_players,self.serialized_tournaments)
        self.export_data_in_database(self.serialized_players, self.serialize_tournament())
        print(self.serialize_tournament())

