

class Match:

    def __init__(self, A, A_score, B, B_score, color):

        self.A = A
        self.A_score = A_score
        self.B = B
        self.B_score = B_score
        self.matche = ([A, A_score], [B, B_score])
        self.color = color

    def __str__(self) -> str:
        return "Match opposant " + self.A['first_name'] + " ({color})".format(color=self.color) + " à " + self.B['first_name']

    def __repr__(self) -> str:
        return "Match(player 1='{}', player 2='{}')".format(self.A['name'], self.B['name'])
