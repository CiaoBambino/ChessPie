from views.view import MainMenu
from controllers.controler import Controler

def main():
  
    view = MainMenu()
    chess = Controler(view)



if __name__ == "__main__":
    main()