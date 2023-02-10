import json
import os
from os import system, name
from views import view
from models import player


class Controler:

    def __init__(self, view):

        self.view = view

    def run(self):
        pass

    def synchroniser():
        pass

    def get_player():
        pass

    def JSONserialiser(Object):

        objet = Object.serializer()

        name = Object.__class__.__name__ + ".json"
        directory = "\data"
        directory_name = os.path.join(directory, name)
        path = os.getcwd() + directory_name

        with open(path, 'a') as f:
            json.dump(objet, f, indent=2)

    def cleaner(function):
        def wrapper(*args, **kwargs):

            ClearTerminal()
            result = function(*args, **kwargs)

            return result

        wrapper.__doc__ = function.__doc__
        return wrapper

    @cleaner
    def coordinate_input(user_data, title, base):

        print(base)

        for x in range(len(user_data)):

            user_data[x] = input(title[x])
            line = Controler.proper_line(x, user_data, title)
            base += "\n"
            base += line
            ClearTerminal()
            print(base)

        return user_data

    def proper_line(x, user_data, title):
        """get 2 strings, return 1 string
        by additionning them second value first"""

        text = title[x] + user_data[x]
        return text



class CreateTournament:

    def __init__(self):
        pass


class CreatePlayer:

    def __init__(self):
        # initialise the attributes from the view
        user_data, title, base = view.CreatePlayerView.view()
        # store the input into data
        data = Controler.coordinate_input(user_data, title, base)
        # unpack data and create a new player object
        name, first_name, birthday, note = [*data]
        new_player = player.Player(name, first_name, birthday, note)
        Controler.JSONserialiser(new_player)


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


class CreateTournament:
    pass
