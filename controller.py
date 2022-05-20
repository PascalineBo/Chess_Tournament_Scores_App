from datetime import datetime
from itertools import islice
from model import Player, Ronde, Tournament
from view import NOMBRE_DE_JOUEURS, INDICE_NOMBRE_DE_JOUEURS_MOITIE, \
    ROUNDS_NUMBER
from tinydb import TinyDB
from tinydb import where


class Controller:
    """get and serializes Players Data"""
    def __init__(self, view):
        # models
        self.players = []
        self.rondes = []
        self.serialized_players = []
        self.serialized_rondes = []
        self.tournament_name = ""
        self.location = ""
        self.date = ""
        self.serialized_tournament = {}
        self.tournament_notes = ""

        # views
        self.view = view

    def get_tournament_data(self):
        """récupère les données du tournoi """
        self.tournament_count = len(self.deserialized_tournament)
        try:
            # récupère les données du tournoi à la fin
            self.search_tournament_data_in_db()  # regarde s'il y a une
            # base de données
            print(self.tournament)
            if len(self.deserialized_tournament[
                       self.tournament_count - 1]['Tournament_Notes']) == 0:
                tournament_notes = self.view.prompt_for_notes()
                self.tournament.tournament_notes = tournament_notes
                self.tournament.rondes = self.rondes
            else:
                tournament_name = self.view.prompt_for_tournament_name()
                location = self.view.prompt_for_location()
                date = self.view.prompt_for_date()
                rondes = self.rondes
                tournament_notes = ""
                self.tournament = Tournament(tournament_name, location,
                                             date, rondes, tournament_notes)
                self.export_tournament_in_database(
                    self.serialize_tournament(self.tournament))
        except IndexError:
            # récupère les données du tournoi au début
            tournament_name = self.view.prompt_for_tournament_name()
            location = self.view.prompt_for_location()
            date = self.view.prompt_for_date()
            rondes = self.rondes
            tournament_notes = ""
            self.tournament = Tournament(tournament_name, location,
                                         date, rondes, tournament_notes)
            self.export_tournament_in_database(
                self.serialize_tournament(self.tournament))

    def serialize_tournament(self, tournament):
        """serialise les tournois"""
        serialized_tournament = {
             'Tournament_Name': tournament.tournament_name,
             'Tournament_Location': tournament.location,
             'Tournament_Date': tournament.date,
             'Tournament_Rondes': self.serialized_rondes,
             'Tournament_Notes': tournament.tournament_notes,
             'Tournament_Rounds Number': tournament.rounds_number
             }
        return serialized_tournament

    def serialize_rondes(self):
        """sérialise les rondes"""
        try:
            serialized_rondes = self.deserialized_tournament[self.tournament_count - 1]['Tournament_Rondes']
        except IndexError:
            serialized_rondes = []
        try:
            ronde = self.tournament.rondes[-1]
            serialized_list_of_matchs = []
            for match in ronde.list_of_matchs:
                serialized_match = {'Match': match[0].fullname_player +
                                    " vs " + match[1].fullname_player}
                serialized_list_of_matchs.append(serialized_match)
            serialized_ronde = {
                    'Ronde_Name': ronde.round_name,
                    'Ronde_Number': ronde.round_number,
                    'Ronde_Start_Time': ronde.start_date_time,
                    'Ronde_List_of_Matchs': serialized_list_of_matchs,
                    'Ronde_End_Time': ronde.end_time
                }
            serialized_rondes.append(serialized_ronde)
        except IndexError:
            return []
        return serialized_rondes

    def get_players_data(self):
        """récupère les données des joueurs et
        stocke les joueurs dans une liste"""
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

            player = Player(fullname_player, birth_date, gender, ranking)
            self.players.append(player)

    def serialize_players(self):
        """serialise les joueurs"""
        for player in self.players:
            serialized_player = {'Player_Full_Name': player.fullname_player,
                                 'Player_Birth_Date': player.birth_date,
                                 'Player_Gender': player.gender,
                                 'Player_Ranking': player.ranking,
                                 }
            self.serialized_players.append(serialized_player)
        return self.serialized_players

    def deserialize_players(self):
        """récupère les données des joueurs dans la base de données
        pour les utiliser"""
        self.db = TinyDB("databases.json")
        players_table = self.db.table("Players")
        deserialized_players = players_table.all()  # récupère les données
        # des joueurs
        self.players = []
        for i in range(0, NOMBRE_DE_JOUEURS):
            # retransforme les objets joueurs de la base de données en
            # dictionnaires python
            try:
                fullname_player = deserialized_players[i]['Player_Full_Name']
                birth_date = deserialized_players[i]['Player_Birth_Date']
                gender = deserialized_players[i]['Player_Gender']
                ranking = float(deserialized_players[i]['Player_Ranking'])
                player = Player(fullname_player, birth_date, gender, ranking)
                print(player)
                self.players.append(player)
                print(self.players)
            except IndexError:
                return None
        return self.players  # liste des joueurs avec les données de la base de
        # données

    def sort_players_by_ranking(self):
        """Remplit et trie une liste des joueurs avec leur classement"""
        self.players.sort(key=lambda x: x.ranking)
        # trie les joueurs selon leur classement en ordre croissant
        return self.players  # ranking_list

    def get_round_data(self):
        """demande les données des rondes et les stocke dans une liste"""
        db = TinyDB("databases.json")
        self.tournament_table = db.table("tournament")
        self.deserialized_tournament = self.tournament_table.all()
        self.tournament_count = len(self.deserialized_tournament)
        print(self.tournament_count)
        if len(self.deserialized_tournament[
                   self.tournament_count - 1]['Tournament_Rondes']) == 0:
            round_number = 1
        else:
            round_number = len(self.deserialized_tournament[
                                        self.tournament_count -1][
                                   'Tournament_Rondes']) + 1
        print(len(self.deserialized_tournament[
                                        self.tournament_count -1][
                      'Tournament_Rondes']))
        round_name = "Round " + str(round_number)
        print(round_name)
        list_of_matchs = []
        start_date_time = str(datetime.now())
        end_time = str(0)
        self.ronde = Ronde(list_of_matchs, round_name, round_number,
                      start_date_time, end_time)
        self.rondes.append(self.ronde)
        print(self.rondes)
        return self.rondes

    def matchs_list(self, players, rondes):
        """détermine l'appariement des joueurs
        pour la première ronde et les suivantes"""
        matchs_round_number = 1
        for ronde in rondes:
            matchs_round_number = int(ronde.round_number)
            print(matchs_round_number)
        if matchs_round_number == 1:  # rule for the first round
            self.zip_list = zip(players,
                                islice(players,
                                       INDICE_NOMBRE_DE_JOUEURS_MOITIE,
                                       None))
            self.matchs = list(self.zip_list)
            print(self.matchs)
            return self.matchs
        elif matchs_round_number > 1:
            self.matchs = []
            self.playerslist = players[:]
            # makes a copy of the list "players"
            self.match = (self.playerslist.pop(0),
                          self.playerslist.pop(matchs_round_number - 2))
            self.matchs.append(self.match)
            if matchs_round_number == 3:
                # specific rule for the third round
                while len(self.playerslist) > 0:
                    self.match = (self.playerslist.pop(0),
                                  self.playerslist.pop())
                    self.matchs.append(self.match)
            elif matchs_round_number == 4:
                # specific rule for the fourth round
                while len(self.playerslist) > 0:
                    self.match = (self.playerslist.pop(0),
                                  self.playerslist.pop(0))
                    self.matchs.append(self.match)
            else:
                while len(self.playerslist) > 0:
                    # specific rule for the second round
                    self.match = (self.playerslist[0],
                                  self.playerslist[1])
                    self.playerslist.pop(0)
                    self.playerslist.pop(0)
                    self.matchs.append(self.match)
        return self.matchs

    def get_round_end_time(self):
        """fixe automatiquement l'heure de fin de Ronde
        quand le Directeur tape 'O'"""
        while self.view.prompt_for_end_time() != 'O':
            end_time = str(datetime.now())
        end_time = str(datetime.now())
        self.rondes[-1].end_time = end_time
        self.tournament.rondes = self.rondes
        return

    def export_players_in_database(self, serialized_players):
        """exporte les données des joueurs dans une base de données TinyDB"""
        self.db = TinyDB("databases.json")
        self.players_table = self.db.table("Players")
        self.players_table.truncate()  # clear the table first
        self.players_table.insert_multiple(serialized_players)

    def export_tournament_in_database(self, serialized_tournament):
        """exporte les données du tournoi dans une base de données TinyDB"""
        self.db = TinyDB("databases.json")
        tournament_table = self.db.table("tournament")
        """tournament_table.truncate()  # clear the table first"""
        print(serialized_tournament)
        tournament_table.insert(serialized_tournament)

    def save_players_ranking(self, players):
        """sauvegarde du classement des joueurs"""
        db = TinyDB("databases.json")
        self.players_table = db.table("Players")
        for player in players:
            self.players_table.update_multiple(
                [({'Player_Ranking': player.ranking},
                  where('Player_Full_Name') == player.fullname_player)])

    def save_notes(self, tournament):
        """sauvegarde des données des rondes, et des remarques du Directeur"""
        db = TinyDB("databases.json")
        self.tournament_table = db.table("tournament")
        self.tournament_table.update_multiple(
            [({'Tournament_Notes': tournament.tournament_notes},
              where('Tournament_Name') == tournament.tournament_name)])

    def save_rondes(self, tournament):
        """sauvegarde des données des rondes, et des remarques du Directeur"""
        db = TinyDB("databases.json")
        self.tournament_table = db.table("tournament")
        self.tournament_table.update_multiple(
            [({'Tournament_Rondes': self.serialize_rondes()},
              where('Tournament_Name') == tournament.tournament_name)])

    def search_tournament_data_in_db(self):
        """charge les données du fichier json et récupère les données de l'objet
        Tournament"""
        db = TinyDB("databases.json")
        self.tournament_table = db.table("tournament")
        self.deserialized_tournament = self.tournament_table.all()
        tournaments_number = len(self.deserialized_tournament)
        tournament_name = self.deserialized_tournament[tournaments_number - 1]['Tournament_Name']
        location = self.deserialized_tournament[tournaments_number - 1]['Tournament_Location']
        date = self.deserialized_tournament[tournaments_number - 1]['Tournament_Date']
        rondes = []
        tournament_notes = ""
        self.tournament = Tournament(tournament_name, location,
                                     date, rondes, tournament_notes)

    def complete_run(self):
        """run complet: demande toutes les données depuis le début"""
        self.get_tournament_data()  # demande les données
        # de début du tournoi
        self.get_players_data()  # demande les données
        # des joueurs du tournoi
        self.sort_players_by_ranking()  # trie les joueurs
        # selon leur classement
        self.view.show_players_scores(self.players)
        # affiche les joueurs dans l'ordre de leur classement
        self.export_players_in_database(self.serialize_players())
        # première sauvegarde des joueurs dans l'ordre de leur classement
        self.partial_run()

    def partial_run(self):
        """run actualisé: ne redemande pas les données de joueurs
        ni du début du tournoi"""
        self.get_round_data()  # récupère les données de début de la ronde
        self.view.show_round(self.matchs_list(self.players, self.rondes),
                             self.rondes[-1].round_number)
        # détermine et affiche les matchs de la ronde en cours
        self.rondes[-1].list_of_matchs = self.matchs  # enregistre
        # les matchs dans l'objet Ronde de la ronde en cours,
        # dans la liste des rondes
        self.get_round_end_time()  # si les matchs sont finis,
        # récupère automatiquement l'heure de fin de la ronde
        self.tournament.rondes = self.rondes  # enregistre
        # la liste des rondes actualisée dans l'objet tournoi en cours
        self.save_rondes(self.tournament)
        # sauvegarde les données des rondes
        self.view.prompt_for_scores(self.matchs_list
                                    (self.players, self.rondes))
        # demande la saisie des scores de la ronde pour chaque joueur
        self.sort_players_by_ranking()  # trie les joueurs
        # selon leur nouveau classement
        self.view.show_players_scores(self.players)  # affiche la liste
        # des joueurs dans l'ordre de leur nouveau classement
        self.save_players_ranking(self.players)
        # sauvegarde des joueurs dans l'ordre de leur classement
        db = TinyDB("databases.json")
        self.tournament_table = db.table("tournament")
        self.deserialized_tournament = self.tournament_table.all()
        self.tournament_count = len(self.deserialized_tournament)
        print(self.tournament_count)
        current_round_number = len(self.deserialized_tournament[
                   self.tournament_count - 1]['Tournament_Rondes'])
        # regarde dans la base de données à quel numéro de ronde
        # on est rendu
        for i in range(0, ROUNDS_NUMBER - current_round_number):
            self.get_round_data()
            self.view.show_round(self.matchs_list(self.players,
                                                  self.rondes),
                                 self.rondes[-1].round_number)
            self.rondes[-1].list_of_matchs = self.matchs_list(self.players,
                                                              self.rondes)
            self.get_round_end_time()
            self.tournament.rondes = self.rondes
            self.view.prompt_for_scores(self.matchs_list(self.players,
                                                         self.rondes))
            self.sort_players_by_ranking()
            self.view.show_players_scores(self.players)
            self.save_players_ranking(self.players)  # actualise le classement
            # des joueurs dans la base de données
            self.save_rondes(self.tournament)  # complète les données du
            # tournoi dans la base de données avec les matchs des rondes

        self.get_tournament_data()  # récupère les données
        # de fin du tournoi
        self.save_players_ranking(self.players)
        self.save_notes(self.tournament)  # complète les données du
        # tournoi dans la base de données

    def run(self):
        if self.view.prompt_for_report() == 'O':
            # demande si on veut un rapport
            db = TinyDB("databases.json")
            players_table = db.table("Players")
            tournament_table = db.table("tournament")
            print("Les données des tournois sont:")
            print(tournament_table.all())
            print("Les données des joueurs sont:")
            print(players_table.all())
        else:
            # lance l'appli
            self.deserialize_players()  # récupère les données des joueurs
            # dans la base de données
            db = TinyDB("databases.json")
            self.tournament_table = db.table("tournament")
            self.deserialized_tournament = self.tournament_table.all()
            # récupère les données des tournois dans la base de données
            if len(self.players) == 0:
                self.complete_run()
            elif len(self.deserialized_tournament[
                           len(self.deserialized_tournament) - 1]['Tournament_Notes']) != 0:
                self.complete_run()
            else:
                self.search_tournament_data_in_db()  # récupère
                # les données du tournoi dans la base de données
                self.partial_run()
