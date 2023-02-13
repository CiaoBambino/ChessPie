from models import tournament


class Round:

    def __init__(self, actual_round,
                 starting_time,
                 ending_time,
                 note=None,
                 match_list=None):

        self.actual_round = tournament.Tournament.actual_round
        self.name = "Round %s" % actual_round
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.match_list = match_list
