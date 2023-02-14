import json
import time
import datetime
import os
from os import system, name
from views import view
from models import player, tournament, rounde, match
import shutil
import re
from tabulate import tabulate
import random


class Controler:

    def __init__(self, view):

        self.view = view

    def synchroniser():
        pass

    def remove_first_index(tournament_player_list):
        """Get a list as entry, 
           return it without the first element"""
        del tournament_player_list[0]
        new_list = tournament_player_list
        return new_list

    def sort_by_score(tournament_player_list):
        """Return a list sorted by higher score"""
        liste = tournament_player_list

        def get_tscore(element):
            return element['tournament_score']

        liste.sort(key=get_tscore, reverse=True)
        return liste

    def shuffle_list(liste):

        shuffled = random.sample(liste, len(liste))
        return shuffled

    def get_score(player):
        score = None
        for item in player:
            score = item["player_id"]

        return score

    def get_ids(player_list):

        id_list = []
        for p in player_list:
            id_list.append(p["player_id"])

        return id_list

    def get_selected_player(player_id):
        """From a given player id return the player
           as a dictionnary"""

        # list of all players in Player.json
        liste = Controler.get_player_list()
        for p in liste[1:]:
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

    def copy_file(Object):
        """Copy the file in the same directory
        adding Save at the end of the name"""

        path = Controler.get_path(Object)
        new_path = re.sub('.json', 'Save.json', path)
        shutil.copyfile(path, new_path)

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
        """serialize an object at the end of a json file"""

        # create a list to stock the upcoming file
        new_file = []
        # get a dictionnary
        objet = Object.serializer()
        path = Controler.get_path(Object)
        Controler.check_path(path)
        Controler.copy_file(Object)

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
        path = Controler.get_path(Object)
        print(path)
        time.sleep(5)

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

    # COORDINATE_INPUT AND SELECT PLAYER ARE GETTING THE INPUT FROM USER

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

    def coordinate_input_select_player(base, data):

        selected_players = []
        has_finished = False

        while not has_finished:

            ClearTerminal()
            print(base)
            time.sleep(0)
            print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
            player_id = int(input("Entrez l'Identifiant des joueurs à ajouter : "))
            # VERIFIER SI L'ENTREE EST UNE NOMBRE ET PAS UN STRING
            response = Controler.is_valid()

            if response:
                ClearTerminal()
                selected_player = Controler.get_selected_player(player_id)
                selected_players.append(selected_player)
                print("Le joueur n°" + str(player_id) +
                      " a été ajouté à la liste")
                print("Continuer d'ajouter des joueurs ?")
                has_finished = not Controler.is_valid()
                continue
            else:
                continue

        return selected_players

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


class CreateRounds:

    def rounds_list_generator(number_of_rounds):
        """Return an empty list
           sized for the number of rounds"""
        rounds_list = []

        for i in range(number_of_rounds):
            rounds_list.append([])

        return rounds_list

    def round_generator(liste, actual_round):
        """generate the round"""
        # A CONTINUER

        if actual_round == 1:
            player_list = Controler.shuffle_list(liste)
            match_liste, player_impair = CreateRounds.create_match_list(player_list)
            return match_liste, player_impair

        else:
            Controler.sort_by_score(player_list)
            match_liste, player_impair = CreateRounds.create_match_list(player_list)
            return match_liste, player_impair

    def create_match_list(player_list):
        """Return a list of match and the impaire player
           that is =None by default"""

        nb, is_pair = CreateTournament.calculate_player(player_list)
        match_list = []
        pair1 = []
        pair2 = []
        impaire_p = None

        if is_pair:
            for i in range(0, nb, 2):
                pair1.append(player_list[i])

            for j in range(1, nb, 2):
                pair2.append(player_list[j])

            for p1, p2 in zip(pair1, pair2):
                matche = CreateRounds.create_match(p1, p2)
                match_list.append(matche)

            return match_list, impaire_p

        else:
            for i in range(0, nb, 2):
                pair1.append(player_list[i])

            impaire_p = pair1[-1]
            del pair1[-1]

            for j in range(1, nb, 2):
                pair2.append(player_list[j])

            for p1, p2 in zip(pair1, pair2):
                paire = CreateRounds.create_match(p1, p2)
                match_list.append(paire)

            return match_list, impaire_p

    def create_match(player_one, player_two):

        p1_score = 0
        p2_score = 0

        matche = match.Match(player_one, p1_score, player_two, p2_score)
        return matche


class CreateTournament:

    def __init__(self):

        # Initialise the tournament
        name, place, starting_date, ending_date, description, tournament_player_list, number_of_rounds, rounds_list = CreateTournament.init()
        new_tournament = tournament.Tournament(name,
                                               place,
                                               starting_date,
                                               ending_date,
                                               description,
                                               tournament_player_list,
                                               number_of_rounds,
                                               rounds_list)
        Controler.json_serialiser(new_tournament)
        CreateTournament.run(new_tournament)

    def run(tournament):

        number_player, is_pair = CreateTournament.calculate_player(tournament.registered_players)
        view.TournamentView.view(tournament.name, number_player)
        check = Controler.is_valid()

        if check:
            i = tournament.actual_round
            j = i - 1
            for rounds in tournament.rounds_list[j:]:

                starting_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                liste = tournament.registered_players
                match_list, impair_p = CreateRounds.round_generator(liste, i)
                new_round = rounde.Round(i, match_list, starting_time)
                rounds.append(new_round)
                view.RoundMenu.view(tournament.name, str(i), match_list)
                check2 = Controler.is_valid()
                # afficher la vue et demander lancer ou pas
        else:
            view.TournamentMenu()

        

    def init():
        """All the variable necessary to create
           an object Tournament are collected here"""

        # initialise the attributes from the view
        user_data, title, base = view.CreateTournamentView.view()
        # store the inputs into data
        data = Controler.coordinate_input(user_data, title, base)
        # load the list of all player from /data/Player.json
        all_players = Controler.get_player_list()
        # select player to participate tournament
        SPV_base, SPV_data = view.SelectPlayerView.view(all_players)
        tournament_player_list = Controler.coordinate_input_select_player(SPV_base, SPV_data)
        # unpack data and create a new tournament object
        name, place, starting_date, ending_date, description, number_of_rounds = [*data]
        number_of_rounds = int(number_of_rounds)
        rounds_list = CreateRounds.rounds_list_generator(number_of_rounds)

        return name, place, starting_date, ending_date, description, tournament_player_list, number_of_rounds, rounds_list

    def calculate_player(player_list):
        """Return number of player in list and if it's pair"""

        counter = 0
        is_pair = None
        for p in player_list:
            counter += 1
        if counter % 2 == 0:
            is_pair = True
        else:
            is_pair = False

        return counter, is_pair


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
