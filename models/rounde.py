from models.tournament import Tournament


class Round:

    def __init__(self, actual_round=None,
                 match_list=None,
                 starting_time=None,
                 ending_time=None,
                 note=None):

        self.actual_round = actual_round
        self.name = "Round %s" % actual_round
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.match_list = match_list
        self.note = note

    def __str__(self) -> str:
        return "ROUND N°" + self.actual_round

    def __repr__(self) -> str:
        return "ROUND ({})".format(self.actual_round)
