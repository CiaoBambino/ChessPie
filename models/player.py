class PLayer:

    TOTAL_PLAYER_NUMBER = 0
    TOTAL_PLAYER_LIST = []
    PLAYER_ID_INCREMENT = 0

    def __init__(self, name,
                 first_name,
                 birthday,
                 note=None):
        """definition of a player"""

        PLAYER_ID_INCREMENT += 1
        TOTAL_PLAYER_NUMBER += 1
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.player_id = PLAYER_ID_INCREMENT
        self.total_score = 0
        self.tournament_score = 0
        self.note = note
        TOTAL_PLAYER_LIST.append(self.Player)

    def __str__(self) -> str:
        return self.first_name + " " + self.name + " " + self.player_id + " " + self.note

    def __repr__(self) -> str:
        return "Utilisateur(prenom='{}', nom='{}')".format(self.first_name, self.name)
