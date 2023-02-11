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

    def get_path(Object):
        """find the absolute path with the name of the object called"""

        name = Object.__class__.__name__ + ".json"
        directory = "\data"
        directory_name = os.path.join(directory, name)
        path = os.getcwd() + directory_name

        return path

    def check_path(path):
        """Check if the path contain a file,
        if not create a file with a List inside"""

        check = os.path.isfile(path)
        if check:
            return
        else:
            objet = [{"Objet": "premier",
                     "ne pas ": "supprimer", "don't": "delete"}]

            with open(path, 'a') as f:
                json.dump(objet, f)

    def json_serialiser(Object):
        """serialise an object at the end of a json file"""

        # create a list to stock the upcoming file
        new_file = []
        # Use class method of the object to get a dictionnary
        objet = Object.serializer()
        path = Controler.get_path(Object)
        Controler.check_path(path)

        with open(path, 'r') as rf:
            file = json.load(rf)

        for elements in file:
            new_file.append(elements)

        new_file.append(objet)

        # Serialise the final file with the new Object inside
        with open(path, 'w') as f:
            json.dump(new_file, f)

    def json_deserialiser(Object):

        file = []
        # find the object file.json with his class name
        name = Object.__class__.__name__ + ".json"
        directory = "\data"
        directory_name = os.path.join(directory, name)
        path = os.getcwd() + directory_name

        # open store the file into a variable
        with open(path, 'r') as rf:
            file = json.load(rf)

        for objet in file:
            file.append(Object.deserializer(objet))

        print(file)
        time.sleep(10)
        return file

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
        Player = player.Player()
        players = Controler.JSONunserializer(Player)
        # select player to participate tournament
        view.SelectPlayerView(players)
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
        Controler.json_serialiser(new_player)


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
