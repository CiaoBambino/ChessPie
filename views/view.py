from os import system, name
from controllers import controler


class MainMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --MENU PRINCIPAL-- \n")
        print("[1] TOURNOIS")
        print("[2] JOUEURS")
        print("[3] RAPPORTS")
        print("[4] REGLAGES")
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
                case "4":
                    ClearTerminal()
                    SettingMenu()
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
        print("[1] -TOURS-")
        print("[2] CREER UN TOURNOI")
        print("[3] CHARGER UN TOURNOI")
        print("[4] MODIFIER UN TOURNOI")
        print("[5] SUPPRIMER UN TOURNOI")
        print("[6] RETOUR")
        print("[q] quitter" + "      " +
              "[n]nettoyer" + "      " +
              "[s]sauvegarder")

        self.has_decided = False

        while not self.has_decided:

            user_choice = input("\n Entrez votre choix : ")

            match user_choice:
                case "1":
                    print("option1")
                    self.has_decided = True
                case "2":
                    print("option2")
                    controler.CreateTournament()
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

    def __init__(self) -> None:
        pass


class CreateTournamentView:

    def view():
        # user_data and title must have same amount of elements
        user_data = ["name", "place", "starting_date", "ending_date", "description"]
        title = ["nom : ", "lieu : ", "date de début : ", "date de fin : ", "description : "]
        base = " --CREER UN TOURNOIS--\n"
        base += "Pour créer un Tournoi veuillez entrer ces informations."
        return user_data, title, base


class SelectPlayerView:

    def __init__(self, player_list):
        pass

    def view():
        # user_data and title must have same amount of elements
        user_data = ["name", "place", "starting_date", "description"]
        title = ["nom : ", "lieu : ", "date de début : ", "description : "]
        base = " --CREER UN TOURNOIS--\n"
        base += "Ensuite veuillez choisir les joueurs."
        return user_data, title, base


class RoundMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --TOURS-- \n")
        print("[1] AFFICHER LES TOURS")
        print("[2] AFFICHER LES MATCH")
        print("[3] CHARGER UN TOUR")
        print("[4] MODIFIER UN TOUR")
        print("[5] SUPPRIMER UN TOUR")
        print("[6] RETOUR")
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


class MatchMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --MATCH-- \n")
        print("[1] AFFICHER LES MATCH")
        print("[2] MODIFIER UN MATCH")
        print("[3] SUPPRIMER UN MATCH")
        print("[4] CREER UN MATCH")
        print("[5] RETOUR")
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
                    ClearTerminal()
                    RoundMenu()
                    self.has_decided = True
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    MatchMenu()
                    self.has_decided = True
                case "s":
                    print("option7")
                case _:
                    print("Cette option n'existe pas")


class PlayerMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --JOUEURS-- \n")
        print("[1] LISTE COMPLETE")
        print("[2] MODIFIER UN JOUEUR")
        print("[3] SUPPRIMER UN JOUEUR")
        print("[4] CREER UN PROFIL")
        print("[5] RETOUR")
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
                    controler.CreatePlayer()
                    self.has_decided = True
                    PlayerMenu()
                case "5":
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


class SettingMenu:

    def __init__(self):

        ClearTerminal()
        print("\n --REGLAGES-- \n")
        print("[1] REGLAGE 1")
        print("[2] REGLAGE 2")
        print("[3] REGLAGE 3")
        print("[4] REGLAGE 4")
        print("[5] REGLAGE 5")
        print("[6] REGLAGE 6")
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
                    SettingMenu()
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
