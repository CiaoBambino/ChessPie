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


class CreatePlayer:

    def __init__(self):

        user_data, title, base = view.CreatePlayerView.view()
        ClearTerminal()
        print(base)

        for x in range(len(user_data)):

            user_data[x] = input(title[x])
            line = CreatePlayer.proper_line(x, user_data, title)
            base += "\n"
            base += line
            ClearTerminal()
            print(base)

        name, first_name, birthday, note = [*user_data]
        new_player = player.Player(name, first_name, birthday, note)
        Controler.JSONserialiser(new_player)

    def proper_line(x, user_data, title):
        """get 2 strings, return 1 string
        by additionning them second value first"""
        text = title[x] + user_data[x]
        return text


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
