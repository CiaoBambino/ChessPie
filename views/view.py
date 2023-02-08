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
        
        while True:
            
            user_choice = input("\n Entrez votre choix : ")
            
            match user_choice:
                case "1":
                    print("option1")
                case "2":
                    print("option2")
                case "3":
                    print("option3")
                case "4":
                    print("option4")
                case "q" | "Q" | "quit" | "quitt" | "quitter" | "Quitter":
                    exit()
                case "n":
                    print("option56")
                case "s":
                    print("otoion7")
                case _:
                    print("Cette option n'existe pas")
                
    def __call__(self, *args, **kwargs):
        pass  
    

class TournamentMenu:
    pass

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
       