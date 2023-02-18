from os import system, name
from controllers import controler
from tabulate import tabulate

from time import sleep


class MainMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --MENU PRINCIPAL-- \n")
        print("[1] TOURNOIS")
        print("[2] JOUEURS")
        print("[3] RAPPORTS")
        print("[q] quitter" + "      " +
              "[n]nettoyer" + "      " +
              "[s]sauvegarder")

        self.has_decided = False

        while not self.has_decided:

            user_choice = input("\n Entrez votre choix : ")

            match user_choice:
                case "1":
                    ClearTerminal()
                    TournamentMenu()
                    self.has_decided = True
                case "2":
                    ClearTerminal()
                    PlayerMenu()
                    self.has_decided = True
                case "3":
                    ClearTerminal()
                    RapportMenu()
                    self.has_decided = True
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    MainMenu()
                    self.has_decided = True
                case "s":
                    print("sauvegarder")
                    self.has_decided = True
                case _:
                    print("Cette option n'existe pas")

    def __call__(self, *args, **kwargs):
        pass


class TournamentMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --TOURNOIS-- \n")
        print("[1] CREER UN TOURNOI")
        print("[2] CHARGER UN TOURNOI")
        print("[3] RETOUR")
        print("[q] quitter" + "      " +
              "[n]nettoyer" + "      " +
              "[s]sauvegarder")

        self.has_decided = False

        while not self.has_decided:

            user_choice = input("\n Entrez votre choix : ")

            match user_choice:
                case "1":
                    controler.CreateTournament()
                    self.has_decided = True
                case "2":
                    print("option2")
                    self.has_decided = True
                case "3":
                    ClearTerminal()
                    MainMenu()
                    self.has_decided = True
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    TournamentMenu()
                    self.has_decided = True
                case "s":
                    print("option7")
                case _:
                    print("Cette option n'existe pas")


class TournamentView:

    def view(name, number_of_player):
        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += str(number_of_player) + " participants\n"
        base += "Lancer le tournoi ..."
        ClearTerminal()
        print(base)

    def end(name):
        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += "Fin du Tournoi"
        ClearTerminal()
        print(base)
        sleep(1.8)


class CreateTournamentView:

    def view():
        # user_data and title must have same amount of elements
        user_data = ["name", "place", "starting_date",
                     "ending_date", "description", "number_of_rounds"]
        title = ["nom : ", "lieu : ", "date de début : ",
                 "date de fin : ", "description : ", "nombre de tours : "]
        base = " --CREER UN TOURNOIS--\n"
        base += "Pour créer un Tournoi veuillez entrer ces informations."
        return user_data, title, base


class SelectPlayerView:

    def view(registered_players):

        base = " --CREER UN TOURNOIS--\n"
        base += "Veuillez ensuite choisir les joueurs. \n"

        data = [["Nom", "Prénom", "ID Joueur"]]

        for d in registered_players[1:]:
            data.append([d["name"], d["first_name"], d["player_id"]])

        # old version, doing the same but lesser beautiful
        """for player in range(len(registered_players)):
            for key in registered_players[player]:
                if key == 'name':
                    data_row.append(registered_players[player]['name'])
                elif key == 'first_name':
                    data_row.append(registered_players[player]['first_name'])
                elif key == 'player_id':
                    data_row.append(registered_players[player]['player_id'])
                    a = data_row.copy()
                    data += [a,]
                    data_row.clear()"""
        return base, data


class RoundMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --TOURS-- \n")
        print("[1] AFFICHER LES TOURS")
        print("[2] AFFICHER LES MATCH")
        print("[3] RETOUR")
        print("[q] quitter" + "      " +
              "[n] nettoyer" + "      " +
              "[s] sauvegarder")

        self.has_decided = False

        while not self.has_decided:

            user_choice = input("\n Entrez votre choix : ")

            match user_choice:
                case "1":
                    print("option1")
                    self.has_decided = True
                case "2":
                    print("option2")
                    self.has_decided = True
                case "3":
                    ClearTerminal()
                    TournamentMenu()
                    self.has_decided = True
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    RoundMenu()
                    self.has_decided = True
                case "s":
                    print("option7")
                case _:
                    print("Cette option n'existe pas")

    def view(name, actual_round, match_list):  # [1] AFFICHER LES TOURS
        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += "ROUND N°{tour}\n".format(tour=actual_round)
        ClearTerminal()
        print(base)
        print("Listes des matchs : \n")
        i = 1
        for matches in match_list:
            print(str(i), " : ", matches)
            i += 1
        print("\nCommencer le Round ?")

    def round_start(name, actual_round, starting_time):

        ClearTerminal()
        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += "ROUND N°{tour}\n\n".format(tour=actual_round)
        base += "Le tour à débuter le : " + starting_time
        base += "\nQuand tout les joueurs auront fini leurs parties entrez << oui >>"
        print(base)

    def round_end(name, actual_round, ending_time, match_list):

        ClearTerminal()
        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += "ROUND N°{tour}\n\n".format(tour=actual_round)
        base += "Le tour à fini le : " + ending_time
        base += "\nPour chaque matches veuillez entrer le numéro du joueur gagnant :\n"
        base += "[1] pour le joueur de gauche, [2] égalité, [3] pour le joueur de droite.\n"
        print(base)

        result_list = []
        i = 1
        for matches in match_list:
            print(str(i), " : ", matches)
            result = input("Résultat : ")
            checked = controler.Controler.check_match_input(result)
            counter = 1

            while not checked:

                if counter == 1:
                    print("Entrez 1, 2 ou 3 en fonction du résultat")
                    result = input("Résultat : ")
                    checked = controler.Controler.check_match_input(result)
                    counter += 1
                else:
                    print("Entrez 1, 2 ou 3 en fonction du résultat,\n1 si le joueur de gauche a gagné, 2 pour un match nul, 3 si le joueur de droite a gagné")
                    result = input("Résultat : ")
                    checked = controler.Controler.check_match_input(result)

            result_list += result
            i += 1

        return result_list


class PlayerMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --JOUEURS-- \n")
        print("[1] LISTE COMPLETE")
        print("[2] CREER UN PROFIL")
        print("[3] RETOUR")
        print("[q] quitter" + "      " +
              "[n] nettoyer" + "      " +
              "[s] sauvegarder")

        self.has_decided = False

        while not self.has_decided:

            user_choice = input("\n Entrez votre choix : ")

            match user_choice:
                case "1":
                    print("option1")
                    self.has_decided = True
                case "2":
                    controler.CreatePlayer()
                    self.has_decided = True
                    PlayerMenu()
                case "3":
                    ClearTerminal()
                    MainMenu()
                    self.has_decided = True
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    PlayerMenu()
                    self.has_decided = True
                case "s":
                    print("option7")
                case _:
                    print("Cette option n'existe pas")


class CreatePlayerView:

    def view():
        # user_data and title must have same amount of elements
        user_data = ["name", "first_name", "birthday", "note"]
        title = ["nom : ", "prénom : ", "Date de naissance : ", "note : "]
        base = " --CREER UN PROFIL--\n"
        base += "Pour créer un nouveau profil de joueur veuillez "
        base += "entrer ses informations personnels."
        return user_data, title, base


class RapportMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --RAPPORT-- \n")
        print("[1] LISTE DES JOUEURS")
        print("[2] LISTE DES JOUEURS D'UN TOURNOI")
        print("[3] LISTE DES TOURNOIS")
        print("[4] LISTE DES TOUR D'UN TOURNOI")
        print("[5] LISTE DES MATCH D'UN TOUR")
        print("[6] NOM/DATE D'UN TOURNOI")
        print("[7] RETOUR")
        print("[q] quitter" + "      " +
              "[n] nettoyer" + "      " +
              "[s] sauvegarder")

        self.has_decided = False

        while not self.has_decided:

            user_choice = input("\n Entrez votre choix : ")

            match user_choice:
                case "1":
                    print("option1")
                    self.has_decided = True
                case "2":
                    print("option2")
                    self.has_decided = True
                case "3":
                    print("option3")
                    self.has_decided = True
                case "4":
                    print("option4")
                    self.has_decided = True
                case "5":
                    print("option5")
                    self.has_decided = True
                case "6":
                    print("option6")
                    self.has_decided = True
                case "7":
                    ClearTerminal()
                    MainMenu()
                    self.has_decided = True
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    RapportMenu()
                    self.has_decided = True
                case "s":
                    print("option7")
                case _:
                    print("Cette option n'existe pas")


class ClearTerminal:
    """Clear the terminal"""

    def __init__(self):

        """
        if (os.name == 'posix'):
            os.system('clear')
        # else screen will be cleared for windows
        else:
             os.system('cls')
        """

        # for windows
        if name == 'nt':
            _ = system('cls')
        # others
        else:
            _ = system('clear')
