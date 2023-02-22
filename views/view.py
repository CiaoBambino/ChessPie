from time import sleep
from os import system, name
from tabulate import tabulate
from controllers.controler import Controler, PlayerControler, TournamentControler


class MainMenu:

    def __init__(self):

        ClearTerminal()
        print("\n--MENU PRINCIPAL--\n")
        print("[1] TOURNOIS")
        print("[2] JOUEURS")
        print("[3] RAPPORTS")
        print("[q] quitter" + "      " +
              "[n] nettoyer" + "      " +
              "[s] sauvegarder")

        self.has_decided = False

        while not self.has_decided:

            user_choice = input("\n Entrez votre choix : ")

            match user_choice:
                case "1" | "&":
                    ClearTerminal()
                    TournamentMenu()
                    self.has_decided = True
                case "2" | "é":
                    ClearTerminal()
                    PlayerMenu()
                    self.has_decided = True
                case "3" | '"':
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


class TournamentMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --TOURNOIS-- \n")
        print("[1] CREER UN TOURNOI")
        print("[2] CHARGER UN TOURNOI")
        print("[3] RETOUR")
        print("[q] quitter" + "      " +
              "[n] nettoyer" + "      " +
              "[s] sauvegarder")

        self.has_decided = False

        while not self.has_decided:

            user_choice = input("\n Entrez votre choix : ")

            match user_choice:
                case "1" | "&":
                    TournamentControler()
                    self.has_decided = True
                case "2" | "é":
                    print("option2")
                    self.has_decided = True
                case "3" | '"':
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

    def create_tournament():
        # user_data and title must have same amount of elements
        user_data = ["name", "place", "starting_date",
                     "ending_date", "description", "number_of_rounds"]
        title = ["nom : ", "lieu : ", "date de début : ",
                 "date de fin : ", "description : ", "nombre de tours : "]
        ClearTerminal()
        base = "--CREER UN TOURNOIS--\n"
        base += "Pour créer un Tournoi veuillez entrer ces informations."
        return user_data, title, base

    def select_players(player_list):

        player_list = Controler.remove_index(player_list)
        selected_players = []
        base = " --CREER UN TOURNOIS--\n"
        base += "Veuillez ensuite choisir les joueurs. \n"
        player_counter = 0

        has_finished = False
        while not has_finished:

            data = [["Nom", "Prénom", "ID Joueur"]]
            for d in player_list:
                data.append([d["name"], d["first_name"], d["player_id"]])

            ClearTerminal()
            print(base)
            print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
            player_id = int(input("Entrez l'identifiant des joueurs à ajouter : "))
            condition1 = Controler.is_integer_in_range(player_id, len(player_list))
            condition2 = Controler.is_id_inlist(player_id, player_list)
            checked = False
            if condition1 and condition2:
                checked = True
            else:
                checked = False

            while not checked:
                player_id = int(input("Veuillez entrer un ID valide : "))
                condition1 = Controler.is_integer_in_range(player_id, len(player_list))
                condition2 = Controler.is_id_inlist(player_id, player_list)
                if condition1 and condition2:
                    checked = True
                else:
                    checked = False

            response = Controler.is_valid(2)
            if response:
                ClearTerminal()
                selected_player = Controler.get_selected_player(player_id, player_list)
                selected_players.append(selected_player)
                Controler.remove_index(player_list, (player_id - 1))
                player_counter += 1
                print("Le joueur n°" + str(player_id) +
                      " a été ajouté à la liste")
                print("nombre de participants : ", player_counter)
                print("Continuer d'ajouter des joueurs ?")
                has_finished = not Controler.is_valid(1)
                continue
            else:
                continue

        return selected_players

    def start_of_tournament(name, number_of_player):

        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += str(number_of_player) + " participants\n"
        base += "Lancer le tournoi ..."
        ClearTerminal()
        print(base)
        check = Controler.is_valid()
        return check

    def end_of_tournament(name):

        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += "Fin du Tournoi"
        ClearTerminal()
        print(base)
        sleep(1.8)


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
                case "1" | "&":
                    print("option1")
                    self.has_decided = True
                case "2" | "é":
                    print("option2")
                    self.has_decided = True
                case "3" | '"':
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

    def round_screen(name, actual_round, match_list):  # [1] AFFICHER LES TOURS

        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += "ROUND N°{tour}\n".format(tour=actual_round)
        ClearTerminal()
        print(base)
        print("Listes des matchs : \n")
        i = 1
        for matche in match_list:
            color = Controler.get_color()
            print(str(i), " : Match opposant", matche[0][0]['first_name'], "jouant les (%s) à"% color, matche[1][0]['first_name'])
            i += 1
        print("\nCommencer le Round ?")
        check = Controler.is_valid()
        return check

    def round_start(name, actual_round, starting_time):

        ClearTerminal()
        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += "ROUND N°{tour}\n\n".format(tour=actual_round)
        base += "Le tour à débuter le : " + starting_time
        base += "\nQuand tout les joueurs auront fini leurs parties entrez << oui >>"
        print(base)
        check = Controler.is_valid()
        return check

    def round_end(name, actual_round, ending_time, match_list):

        ClearTerminal()
        base = "--TOURNOIS--\n\n"
        base += str(name.upper()) + "\n\n"
        base += "ROUND N°{tour}\n\n".format(tour=actual_round)
        base += "Le tour à fini le : " + ending_time
        base += "\nPour chaque matches veuillez entrer le numéro du joueur gagnant :\n"
        base += "[1] pour le joueur de gauche, [2] égalité, [3] pour le joueur de droite.\n"
        print(base)

        new_match_list = []
        i = 1
        for matche in match_list:
            print(str(i), " : Match opposant", matche[0][0]['first_name'], " à", matche[1][0]['first_name'])
            result = input("Résultat : ")
            checked = Controler.check_match_input(result)
            counter = 1

            while not checked:
                if counter == 1:
                    print("Entrez 1, 2 ou 3 en fonction du résultat")
                    result = input("Résultat : ")
                    checked = Controler.check_match_input(result)
                    counter += 1
                else:
                    print("Entrez 1, 2 ou 3 en fonction du résultat,\n1 si le joueur de gauche a gagné, 2 pour un match nul, 3 si le joueur de droite a gagné")
                    result = input("Résultat : ")
                    checked = Controler.check_match_input(result)

            updated_match = Controler.set_matchlist_score(matche, result)
            new_match_list += updated_match
            i += 1
        return new_match_list


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
                case "1" | "&":
                    PlayerMenu.player_list()
                    self.has_decided = True
                case "2" | "é":
                    PlayerControler()
                    self.has_decided = True
                    PlayerMenu()
                case "3" | '"':
                    ClearTerminal()
                    MainMenu()
                    self.has_decided = True
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    PlayerMenu()
                    self.has_decided = True
                case "s":
                    print("option sauvegarder")
                case _:
                    print("Cette option n'existe pas")

    def player_list():

        player_list = Controler.get_player_list()
        data = [["Nom", "Prénom", "ID Joueur"]]

        for d in player_list[1:]:
            data.append([d["name"], d["first_name"], d["player_id"]])

        ClearTerminal()
        print("\n --JOUEURS-- \n")
        print("Liste de tout les joueurs enregistrés dans le club")
        print("Cette liste est aussi accessible dans le menu RAPPORT," 
              " trié par ordre alphabétique.")
        print("[r] retour" + "      " + "[n] nettoyer\n\n")
        print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
        print("\n[r] retour" + "      " + "[n] nettoyer")

        has_decided = False

        while not has_decided:

            user_choice = input("\nQue souhaitez vous faire : ")

            match user_choice:
                case "r" | "R" | "retour" | "rtr" | "rtour" | "return":
                    ClearTerminal()
                    PlayerMenu()
                    has_decided = True
                case "n":
                    PlayerMenu.player_list()
                    has_decided = True
                case _:
                    print("Cette option n'existe pas")

    def create_player():
        """Menu to create a player
        user_data and title must have same amount of elements"""
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
