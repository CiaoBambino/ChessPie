import re
import os
import json
import random
import shutil
import datetime
from views import view
from models import player, tournament, rounde, match
import time


class Controler:

    def __init__(self, view):
        self.view = view

    def json_serializer(Object, option1=None, option2=None):
        """serialize an object at the end of a json file
        parameter 'option2' is for check_path function
        'option1' is for get_path function"""
        new_file = []
        objet = Object.serializer()
        path = Controler.get_path(Object, option1)
        Controler.check_path(path, option2)
        Controler.copy_file(path)

        with open(path, 'r') as rf:
            file = json.load(rf)
        # add the opened file to the list "new_file"
        for elements in file:
            new_file.append(elements)
        # add the object to serialize at the end
        new_file.append(objet)
        # write new file into the file
        with open(path, 'w') as f:
            json.dump(new_file, f)

    def json_writer(path, liste):
        """write a given list"""
        with open(path, 'w') as f:
            json.dump(liste, f)

    def json_reader(path):
        """open to read a json"""
        file = []
        with open(path, 'r') as rf:
            file = json.load(rf)
        return file

    def remove_index(liste, index=None):
        """Get a list as entry, return it without the element.
        If no index is given it remove the first element"""
        if index is not None:
            del liste[index]
            new_list = liste
            return new_list
        else:
            del liste[0]
            new_list = liste
            return new_list

    def set_player_total_score():
        pass

    def set_tournament_score(match_list, tournament):
        """Set the score into the tournament.json"""
        path = Controler.get_path(tournament, 1)
        file = Controler.json_reader(path)

        for players in match_list:

            player_id = players[0]['player_id']
            index = Controler.get_selected_player_index(player_id, file)
            file[1]['registered_players'][index]['tournament_score'] += players[1]

        Controler.json_writer(path, file)

    def set_matchlist_score(matche, result):
        """set the score inside the tuple of a match"""

        if result == '1':
            # set the variable score of the Match object
            matche[0][1] += 1
            # set the variable score of the Player object
            matche[0][0]['tournament_score'] = matche[0][1]
        elif result == '2':
            matche[0][1] += 0.5
            matche[0][0]['tournament_score'] = matche[0][1]
            matche[1][1] += 0.5
            matche[1][0]['tournament_score'] = matche[1][1]
        else:
            matche[1][1] += 1
            matche[1][0]['tournament_score'] = matche[1][1]

        return matche

    def get_selected_player_index(player_id, file):
        """From a given player id return the player index of the dictionnary"""
        for i in range(len(file[1]['registered_players'])):
            if file[1]['registered_players'][i]["player_id"] == player_id:
                selected_player_index = i
                return selected_player_index

    def get_selected_player(player_id, player_list):
        """From a given player id return the player
           as a dictionnary"""
        for p in player_list:
            if [p["player_id"]] == [player_id]:
                selected_player = p
                return selected_player

    def get_player_list():
        """Return a list of all players"""

        player_list = []
        name = "Player.json"
        directory = "\data"
        directory_name = os.path.join(directory, name)
        path = os.getcwd() + directory_name
        check = os.path.isfile(path)
        if check:  # peut etre modifier par try except plus tard
            with open(path, 'r') as rf:
                file = json.load(rf)

            for elements in file:
                player_list.append(elements)

        return player_list

    def get_and_update_player_id():
        """return the an ID for a new user to be created,
        increment the ID counter inside the Player.json"""
        path = ".\data\Player.json"
        Controler.check_path(path, 1)
        player_list = Controler.get_player_list()
        ID = Controler.get_player_id_from_json(player_list)
        player_list[0]["player_id"] += 1
        Controler.json_writer(path, player_list)
        return ID

    def get_player_id_from_json(liste):
        """from the list of Player.json
        return the player_id of the first dictionnary"""
        for p in liste[:1]:
            return p["player_id"]

    def get_object_name(Object):
        """Return the name of the class of an object"""
        return Object.__class__.__name__

    def get_path(Object, option=None):
        """find the absolute path with the name of the object.
        Option specify that the path must be in a folder named
        with the Object name, and set the file name with the
        object attributes"""
        if option is None:
            # no option
            name = Controler.get_object_name(Object) + ".json"
            directory = "\data"
            directory_name = os.path.join(directory, name)
            path = os.getcwd() + directory_name
            return path
        else:
            # if there is an option in parameter
            name = Object.name + Object.starting_date + ".json"
            parent_directory = "\data"
            directory = Controler.get_object_name(Object)
            directory_name = os.path.join(parent_directory, directory)
            path = os.getcwd() + directory_name

            if not os.path.exists(path):
                os.mkdir(path)
                full_path = os.path.join(path, name)
                return full_path
            else:
                full_path = os.path.join(path, name)
                return full_path

    def get_actual_round(tournament):
        """get the current round of a tournament"""

        actual_round = None
        name = tournament.name + tournament.starting_date + ".json"
        directory = "\data\Tournament"
        directory_name = os.path.join(directory, name)
        path = os.getcwd() + directory_name
        check = os.path.isfile(path)
        if check:  # peut etre modifier par try except plus tard
            with open(path, 'r') as rf:
                file = json.load(rf)

            for item in file[1:]:
                actual_round = item["actual_round"]

        return actual_round

    def get_number_player(player_list):
        """Return number of player, make sur to not have the first index
        that isn't a player"""
        counter = 0
        for p in player_list:
            counter += 1
        return counter

    def get_color():
        """return a random color between black and white"""
        color = bool(random.getrandbits(1))
        if color:
            color = "blanc"
            return color
        else:
            color = "noir"
            return color

    def shuffle_list(liste):
        """shuffle a list"""
        shuffled = random.sample(liste, len(liste))
        return shuffled

    def copy_file(path):
        """Copy the file in the same directory
        adding "Save" at the end of the name of the file"""
        new_path = re.sub('.json', 'Save.json', path)
        shutil.copyfile(path, new_path)

    def check_path(path, option=None):
        """Check if the path contain a file,
        if not create a file with a List inside
        option : 1=Player, 2=Tournament"""
        check = os.path.isfile(path)
        if check:
            return
        else:
            if option == 1:
                objet = [{"total_player": 0, "player_id": 1}]
                with open(path, 'a') as f:
                    json.dump(objet, f)
            elif option == 2:
                objet = [{"total_tournament": 0}]
                with open(path, 'a') as f:
                    json.dump(objet, f)
            else:
                objet = [{"unknow": 0, "unknow": 0}]
                with open(path, 'a') as f:
                    json.dump(objet, f)

    def is_integer_in_range(value, range):
        """check if the value is an integer and in the given range"""
        if isinstance(value, int) and value <= range:
            return True
        else:
            return False

    def is_id_inlist(value, liste):
        """check is the id is in the list, return true or false"""
        for p in liste:
            if value == p['player_id']:
                return True
            else:
                continue
        return False

    def is_valid(option=1):
        """Check if answer is Yes or No and return True or False
        options : 1(default) for no message, others = message"""
        yes_list = ["Oui", "oui", "Yes", "yes", "Ou",
                    "ou", "Ye", "ye", "O", "o", "Y", "y", "ok"]
        no_list = ["Non", "non", "No", "no", "Nn", "nn", "N", "n"]
        answer_list = yes_list + no_list

        if option == 1:
            pass
        else:
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

    def is_pair(liste):
        """return a bool if it's pair or not"""
        if len(liste) % 2 == 0:
            return True
        else:
            return False

    def sort_by_score(tournament_player_list):
        """Return a list sorted by higher score"""
        def get_tscore(element):
            """return tournament_score element"""
            return element['tournament_score']

        tournament_player_list.sort(key=get_tscore, reverse=True)
        return tournament_player_list

    def concatenate_data(x, user_data, title):
        """get 2 strings, return 1 string
        by concatenating them, second value first"""
        text = title[x] + user_data[x]
        return text

    def check_match_input(result):
        """check if the input is 1, 2 or 3"""
        if result == '1' or result == '2' or result == '3':
            return True
        else:
            return False

    def check_if_valid(function):
        """Verify if the user validate his entries"""
        def wrapper(*args, **kwargs):

            condition = False
            while not condition:
                result = function(*args, **kwargs)
                condition = Controler.is_valid(2)

            return result

        wrapper.__doc__ = function.__doc__
        return wrapper

    def clean_terminal(function):
        """Clean terminal"""
        def wrapper(*args, **kwargs):
            ClearTerminal()
            result = function(*args, **kwargs)
            return result

        wrapper.__doc__ = function.__doc__
        return wrapper

    @clean_terminal
    @check_if_valid
    def get_input(user_data, title, base):
        """get the input of the user
        and return them as user_data"""
        print(base)

        for x in range(len(user_data)):

            user_data[x] = input(title[x])
            line = Controler.concatenate_data(x, user_data, title)
            base += "\n"
            base += line
            ClearTerminal()
            print(base)

        return user_data


class TournamentControler:

    def __init__(self):
        name, place, starting_date, ending_date, description, tournament_player_list, number_of_rounds, rounds_list = TournamentControler.get_values()
        new_tournament = tournament.Tournament(name,
                                               place,
                                               starting_date,
                                               ending_date,
                                               description,
                                               tournament_player_list,
                                               number_of_rounds,
                                               rounds_list)
        Controler.json_serializer(new_tournament, 1, 2)
        TournamentControler.run(new_tournament)

    def get_values():
        """All the variable necessary to create
           an object Tournament are collected here"""

        # initialise the attributes from the view
        user_data, title, base = view.TournamentMenu.create_tournament()
        # store the inputs into data
        data = Controler.get_input(user_data, title, base)
        # load the list of all player from /data/Player.json
        all_players = Controler.get_player_list()
        # select players for the tournament
        tournament_player_list = view.TournamentMenu.select_players(all_players)
        # unpack data and create a new tournament object
        name, place, starting_date, ending_date, description, number_of_rounds = [*data]
        number_of_rounds = int(number_of_rounds)
        rounds_list = RoundControler.get_rounds_list(number_of_rounds)

        return name, place, starting_date, ending_date, description, tournament_player_list, number_of_rounds, rounds_list

    def run(tournament):

        number_player = Controler.get_number_player(tournament.registered_players)
        check = view.TournamentMenu.start_of_tournament(tournament.name, number_player)

        if check:

            i = Controler.get_actual_round(tournament)
            j = i - 1

            for rounds in tournament.rounds_list[j:]:

                player_list = tournament.registered_players
                match_list, impair_player = RoundControler.get_match_list(player_list, i) # IMPAIR PLAYEER
                new_round = rounde.Round(i, match_list)
                rounds.append(new_round)
                check2 = view.RoundMenu.round_screen(tournament.name, str(i), match_list)

                if check2:
                    starting_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    check3 = view.RoundMenu.round_start(tournament.name, str(i), starting_time)
                    if check3:
                        ending_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        match_list = view.RoundMenu.round_end(tournament.name, str(i), ending_time, match_list)
                        Controler.set_tournament_score(match_list, tournament)
                        i += 1
                    else:
                        view.TournamentMenu()
                else:
                    view.TournamentMenu()

            view.TournamentMenu.end_of_tournament(tournament.name)
            view.TournamentMenu()
        else:
            view.TournamentMenu()


class RoundControler:

    def get_rounds_list(number_of_rounds):
        """Return an empty list sized with the number of rounds"""
        rounds_list = []
        for i in range(number_of_rounds):
            rounds_list.append([])

        return rounds_list

    def get_match_list(player_list, actual_round):
        """generate the the match list"""
        # A CONTINUER

        if actual_round == 1:
            shuffled_list = Controler.shuffle_list(player_list)
            match_liste, player_impair = RoundControler.set_match_list(shuffled_list)
            return match_liste, player_impair

        else:
            sorted_list = Controler.sort_by_score(player_list)
            match_liste, player_impair = RoundControler.set_match_list(sorted_list)
            return match_liste, player_impair

    def set_match_list(player_list):
        """Return a list of match and the impaire player
           that is =None by default"""

        number = Controler.get_number_player(player_list)
        is_pair = Controler.is_pair(player_list)
        match_list = []
        left_player = []
        right_player = []
        last_player = None

        if is_pair:
            for i in range(0, number, 2):
                left_player.append(player_list[i])

            for j in range(1, number, 2):
                right_player.append(player_list[j])

            for p1, p2 in zip(left_player, right_player):
                matche = RoundControler.set_match(p1, p2)
                match_list.append(matche)

            return match_list, last_player

        else:
            for i in range(0, number, 2):
                left_player.append(player_list[i])

            last_player = left_player[-1]
            del left_player[-1]

            for j in range(1, number, 2):
                right_player.append(player_list[j])

            for p1, p2 in zip(left_player, right_player):
                matche = RoundControler.set_match(p1, p2)
                match_list.append(matche)

            return match_list, last_player

    def set_match(player_one, player_two):
        """create a new Object Match"""
        score = 0
        new_match = match.Match(player_one, score, player_two, score)
        matche = new_match.matche
        return matche


class PlayerControler:

    def __init__(self):
        # initialise the attributes from the view
        user_data, title, base = view.PlayerMenu.create_player()
        # store the inputs into data
        data = Controler.get_input(user_data, title, base)
        # unpack data and create a new player object
        name, first_name, birthday, note = [*data]
        player_id = Controler.get_and_update_player_id()
        # create a new player
        new_player = player.Player(name, first_name, birthday, note, player_id)
        Controler.json_serializer(new_player, 1)


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
        if os.name == 'nt':
            _ = os.system('cls')
        # others
        else:
            _ = os.system('clear')
