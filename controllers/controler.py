import json
import os
from models.player import PLayer

class Controler:

    def __init__(self, view):

        self.view = view

    def run(self):
        pass

    def synchroniser():
        pass

    def get_player():
        pass

    def create_player():
        pass

    def JSONserialiser(Object):
        
        name = Object.__name__ + ".json"
        directory = "\data"
        directory_name = os.path.join(directory, name)
        path = os.getcwd() + directory_name
        print(path)

        print(Object())
        with open("path", 'a') as f:
            json.dump(Object, f)


class CreateTournament:
    pass
