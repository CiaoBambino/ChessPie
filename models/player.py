class Player:

    def __init__(self, name=None,
                 first_name=None,
                 birthday=None,
                 note=None,
                 player_id=None,
                 total_score=None,
                 tournament_score=None):

        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.note = note
        self.player_id = player_id
        self.total_score = 0
        self.tournament_score = 0

    def __call__(self):
        return self.serializer()

    def serializer(self):
        """Serialize the Object Player into a dictionnary"""

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
        """Deserialize the Object Player from a dictionnary"""

        name = player_data['name']
        first_name = player_data['first_name']
        birthday = player_data['birthday']
        note = player_data['note']
        player_id = player_data['player_id']
        total_score = player_data['total_score']
        tournament_score = player_data['tournament_score']

        return Player(name,
                      first_name,
                      birthday,
                      note,
                      player_id,
                      total_score,
                      tournament_score)

    def __str__(self) -> str:
        return self.first_name, self.name, self.player_id, self.note

    def __repr__(self) -> str:
        return "Utilisateur(prenom='{}', nom='{}')".format(self.first_name, self.name)
