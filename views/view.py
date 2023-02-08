from os import system, name

class MainMenu:

    def __init__(self):

        ClearTerminal()
        print("\n MENU PRINCIPAL \n")
        print("[1] TOURNOIS")
        print("[2] JOUEURS")
        print("[3] RAPPORTS")
        print("[4] REGLAGES")
        print("[q] quitter" + "      " + 
              "[n]nettoyer" + "      " +
              "[s]sauvegarder")
        
        has_decided = False
        
        while not has_decided:
            
            user_choice = input("\n Entrez votre choix : ")
            
            match user_choice:
                case "1":
                    print("option1")
                    has_decided = True
                case "2":
                    print("option2")
                    has_decided = True
                case "3":
                    print("option3")
                    has_decided = True
                case "4":
                    print("option4")
                    has_decided = True
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    print("option6")
                    has_decided = True
                case "s":
                    print("option7")
                    has_decided = True
                case _:
                    print("Cette option n'existe pas")
                
    def __call__(self, *args, **kwargs):
        pass  
    

class TournamentMenu:
    
    def __init__(self):

        ClearTerminal()
        print("\n TOURNOIS \n")
        print("[1] AFFICHER LES TOURS")
        print("[2] CREER UN TOURNOI")
        print("[3] CHARGER UN TOURNOI")
        print("[4] MODIFIER UN TOURNOI")
        print("[5] SUPPRIMER UN TOURNOI")
        print("[6] RETOUR")
        print("[q] quitter" + "      " + 
              "[n]nettoyer" + "      " +
              "[s]sauvegarder")
        
        has_decided = False

        while not has_decided:
            
            user_choice = input("\n Entrez votre choix : ")
            
            match user_choice:
                case "1":
                    print("option1")
                    has_decided = True
                case "2":
                    print("option2")
                    has_decided = True
                case "3":
                    print("option3")
                    has_decided = True
                case "4":
                    print("option4")
                    has_decided = True
                case "5":
                    print("option5")
                    has_decided = True
                case "6":
                    print("retour")
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    print("option6")
                case "s":
                    print("option7")
                case _:
                    print("Cette option n'existe pas")

class RoundMenu:
    pass

class MatchMenu:
    pass

class PlayerMenu:
    pass

class RapportMenu:
    pass

class SettingMenu:
    pass

class ClearTerminal:
    """Clear the terminal"""

    def __call__(self):
        
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
       