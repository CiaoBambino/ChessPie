import json
import time
import os
from os import system, name
from views import view
from models import player, tournament, round, match


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
        """Clean terminal and verify if user validate his entries"""
        def wrapper(*args, **kwargs):

            condition = False
            while not condition:
                ClearTerminal()
                result = function(*args, **kwargs)
                condition = Controler.is_valid()

            return result

        wrapper.__doc__ = function.__doc__
        return wrapper

    def input_checker(x, title):

        entry = input(title[x])

        return entry

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

    def is_valid():
        """Check if answer is Yes or No and return True or False"""
        yes_list = ["Oui", "oui", "Yes", "yes", "Ou",
                    "ou", "Ye", "ye", "O", "o", "Y", "y", "ok"]
        no_list = ["Non", "non", "No", "no", "Nn", "nn", "N", "n"]
        answer_list = yes_list + no_list
        print("Souhaitez vous valider ?")

        value = True
        response = ""
        has_answered = False
        while not has_answered:
            entry = input("Oui/Non : ")
            for answer in answer_list:
                if entry == answer:
                    response = entry
                    has_answered = True

        for yes in yes_list:
            if response == yes:
                value = True
                break

            else:
                value = False

        return value


class CreateTournament:

    def __init__(self):
        # initialise the attributes from the view
        user_data, title, base = view.CreateTournamentView.view()
        # store the inputs into data
        data = Controler.coordinate_input(user_data, title, base)
        # load player from /data/player.json

        # unpack data and create a new tournament object
        name, place, starting_date, ending_date, description = [*data]
        new_tournament = tournament.Tournament(name, place,
                                               starting_date,
                                               ending_date,
                                               description)
        Controler.JSONserialiser(new_tournament)


class CreatePlayer:

    def __init__(self):
        # initialise the attributes from the view
        user_data, title, base = view.CreatePlayerView.view()
        # store the inputs into data
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
