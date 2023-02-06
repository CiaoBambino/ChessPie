class PLayer:

    TOTAL_PLAYER_NUMBER = 0
    TOTAL_PLAYER_LIST = (None)
    PLAYER_ID_INCREMENT = 0

    def __init__(self, name, first_name, birthday):
        """definition of a player"""
        
        self.Player.PLAYER_ID_INCREMENT += 1
        name = self.name
        first_name = self.first_name
        birthday = self.birthday
        player_id = PLAYER_ID_INCREMENT
        total_score = 0
        tournament_score = 0

    def __str__(self) -> str:
        return self.first_name + " " + self.name + " " + self.player_id
    
    def __repr__(self) -> str:
        return "Utilisateur(prenom='{}', nom='{}')".format(self.first_name, self.name)
