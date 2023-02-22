class Match:

    def __init__(self, playerA, playerA_score, playerB, playerB_score):

        self.playerA = playerA
        self.playerA_score = playerA_score
        self.playerB = playerB
        self.playerB_score = playerB_score
        self.matche = ([self.playerA, self.playerA_score], [self.playerB, self.playerB_score])

    def __str__(self) -> str:
        return "Match opposant " + self.playerA['first_name'] + " à " + self.playerB['first_name']

    def __repr__(self) -> str:
        return "Match([{},{}], [{},{}])".format(self.playerA['name'], self.playerA_score, self.playerB['name'], self.playerB_score)

    def __getitem__(self, index):
        return self.matche[index]

    def __setitem__(self, key, value):
        self.matche[key] = value