import time

class Player:

    CLASS_NAME = "player"
    TOTAL_PLAYER_NUMBER = 0
    TOTAL_PLAYER_LIST = []
    PLAYER_ID_INCREMENT = 0

    def __init__(self, name,
                 first_name,
                 birthday,
                 note,
                 player_id=None,
                 total_score=None,
                 tournament_score=None):

        Player.PLAYER_ID_INCREMENT += 1
        Player.TOTAL_PLAYER_NUMBER += 1
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.player_id = self.PLAYER_ID_INCREMENT
        self.total_score = 0
        self.tournament_score = 0
        self.note = note
        self.TOTAL_PLAYER_LIST.append(self)

        if len(self.TOTAL_PLAYER_LIST) > 1:
            print(self.TOTAL_PLAYER_LIST[1])
            time.sleep(10)

    def __call__(self):
        return self.serializer()
    
    def serializer(self):

        player_data = {}
        player_data['name'] = self.name
        player_data['first_name'] = self.first_name
        player_data['birthday'] = self.birthday
        player_data['note'] = self.note
        player_data['player_id'] = self.player_id
        player_data['total_score'] = self.total_score
        player_data['tournament_score'] = self.tournament_score

        return player_data

    def unserializer(self, player_data):

        name = player_data['name']
        first_name = player_data['first_name']
        birthday = player_data['birthday']
        note = player_data['note']
        player_id = player_data['player_id']
        total_score = player_data['total_score']
        tournament_score = player_data['tournament_score']

        return PLayer(name,
                      first_name,
                      birthday,
                      note,
                      player_id,
                      total_score,
                      tournament_score)

    def __str__(self) -> str:
        return self.first_name + " " + self.name + " " + self.player_id + " " + self.note

    def __repr__(self) -> str:
        return "Utilisateur(prenom='{}', nom='{}')".format(self.first_name, self.name)
