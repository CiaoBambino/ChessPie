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
                 rounds_list=None,
                 number_of_rounds=4):
        
        Tournament.TOURNAMENT_ID += 1
        self.tournament_id = Tournament.TOURNAMENT_ID
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.endingdate = ending_date
        self.number_of_rounds = 
        self.description = description
        self.registered_players = []
