class Tournament:

    TOURNAMENT_ID = 0
    all_tournament_list = []

    def __init__(self, name,
                 place,
                 starting_date=None,
                 ending_date=None,
                 description=None,
                 tournament_id=None,
                 registered_players=None,
                 actual_round=None,
                 rounds_list=None,
                 number_of_rounds=4):

        Tournament.TOURNAMENT_ID += 1
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.endingdate = ending_date
        self.description = description
        self.tournament_id = tournament_id
        self.registered_players = registered_players
        self.actual_round = actual_round
        self.rounds_list = rounds_list
        self.number_of_rounds = number_of_rounds

        if tournament_id == None:
            tournament_id = Tournament.TOURNAMENT_ID
