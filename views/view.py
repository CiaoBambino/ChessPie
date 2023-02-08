import os

class MainMenu:

    def __init__(self):

        os.system('cls')
        print("\n MENU PRINCIPAL \n")
        print("[1] TOURNOIS")
        print("[2] JOUEURS")
        print("[3] RAPPORTS")
        print("[4] REGLAGES")
        print("[q] quitter" + "      " + 
              "[n]nettoyer" + "      " +
              "[s]sauvegarder")
        
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
