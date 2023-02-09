import json
import os
from os import system, name
from views import view


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

        name = Object.__name__ + ".json"
        directory = "data"
        directory_name = os.path.join(directory, name)
        path = os.getcwd() + directory_name
        print(path)

        print(Object())
        with open("path", 'a') as f:
            json.dump(Object, f)


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
