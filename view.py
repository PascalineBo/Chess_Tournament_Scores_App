

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
        fullname_player = input("tapez les NOM et prénom du joueur ou de la joueuse : ")
        if not fullname_player:
            return None
        return fullname_player

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
            print ("saisissez un nombre entier positif")

    def prompt_for_scores(self,player):
        """Demande les scores des joueurs"""
        print("score de " + player[0] +":")
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


