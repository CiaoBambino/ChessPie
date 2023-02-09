from views.view import MainMenu
from controllers.controler import Controler
from models import player


def main():

    view = MainMenu()
    chess = Controler(view)
    chess.run()
    #Controler.JSONserialiser()



if __name__ == "__main__":
    main()