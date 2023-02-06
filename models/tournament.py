class Tournament:

    actual_round = 1
    all_tournament_list = []
    rounds_list = []
    registered_players = []


    def __init__(self, name,
                 place,
                 starting_date=None,
                 ending_date=None,
                 description=None,
                 number_of_rounds=4):
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.endingdate = ending_date
        self.number_of_rounds = number_of_rounds
        self.description = description
