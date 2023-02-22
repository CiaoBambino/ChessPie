from views.view import MainMenu
from controllers.controler import Controler


def main():

    view = MainMenu()
    Controler(view)


if __name__ == "__main__":
    main()
