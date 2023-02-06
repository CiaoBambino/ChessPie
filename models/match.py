class Match:

    def __init__(self, player_one, player_two):

        self.player_one = player_one
        self.player_two = player_two

    def __str__(self) -> str:
        return "Match opposant " + self.player_one + " à " + self.player_two
    
     def __repr__(self) -> str:
        return "Match(player 1='{}', player 2='{}')".format(self.player_one, self.player_two)