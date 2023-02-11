class Tournament:

    TOURNAMENT_ID = 0
    all_tournament_list = []

    def __init__(self, name,
                 place,
                 starting_date=None,
                 ending_date=None,
                 description=None,
                 registered_players=None,
                 tournament_id=None,
                 actual_round=None,
                 rounds_list=None,
                 number_of_rounds=4):

        Tournament.TOURNAMENT_ID += 1
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.description = description
        self.tournament_id = tournament_id
        self.registered_players = registered_players
        self.actual_round = actual_round
        self.rounds_list = rounds_list
        self.number_of_rounds = number_of_rounds

        if tournament_id is None:
            tournament_id = Tournament.TOURNAMENT_ID

    def serializer(self):
        """Serialise the Object Tournament for the JSON file"""

        tournament_data = {}
        tournament_data['name'] = self.name
        tournament_data['place'] = self.place
        tournament_data['starting_date'] = self.starting_date
        tournament_data['ending_date'] = self.ending_date
        tournament_data['description'] = self.description
        tournament_data['tournament_id'] = self.tournament_id
        tournament_data['registered_players'] = self.registered_players
        tournament_data['actual_round'] = self.actual_round
        tournament_data['rounds_list'] = self.rounds_list
        tournament_data['number_of_rounds'] = self.number_of_rounds

        return tournament_data

    def deserializer(self, tournament_data):
        """Deserialise the Object Tournament for the JSON file"""

        name = tournament_data['name']
        place = tournament_data['place']
        starting_date = tournament_data['starting_date']
        ending_date = tournament_data['ending_date']
        description = tournament_data['description']
        tournament_id = tournament_data['tournament_id']
        registered_players = tournament_data['registered_players']
        actual_round = tournament_data['actual_round']
        rounds_list = tournament_data['rounds_list']
        number_of_rounds = tournament_data['number_of_rounds']

        return Tournament(name,
                          place,
                          starting_date,
                          ending_date,
                          description,
                          tournament_id,
                          registered_players,
                          actual_round,
                          rounds_list,
                          number_of_rounds)
