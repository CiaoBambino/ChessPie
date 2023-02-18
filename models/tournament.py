class Tournament:

    TOURNAMENT_ID = 0
    all_tournament_list = []

    def __init__(self, name,
                 place,
                 starting_date=None,
                 ending_date=None,
                 description=None,
                 registered_players=None,
                 number_of_rounds=4,
                 rounds_list=None,
                 actual_round=1):

        Tournament.TOURNAMENT_ID += 1
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.description = description
        self.tournament_id = Tournament.TOURNAMENT_ID
        self.registered_players = registered_players
        self.number_of_rounds = number_of_rounds
        self.rounds_list = rounds_list
        self.actual_round = actual_round

    def __iter__(self):
        for each in self.__dict__.values():
              yield each

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
        tournament_data['number_of_rounds'] = self.number_of_rounds
        tournament_data['rounds_list'] = self.rounds_list
        tournament_data['actual_round'] = self.actual_round

        return tournament_data

    def unserializer(self, tournament_data):
        """Deserialise the Object Tournament for the JSON file"""

        name = tournament_data['name']
        place = tournament_data['place']
        starting_date = tournament_data['starting_date']
        ending_date = tournament_data['ending_date']
        description = tournament_data['description']
        tournament_id = tournament_data['tournament_id']
        registered_players = tournament_data['registered_players']
        number_of_rounds = tournament_data['number_of_rounds']
        rounds_list = tournament_data['rounds_list']
        actual_round = tournament_data['actual_round']

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

    def __str__(self) -> str:
        return '%s %s %s'%(self.name, self.place, self.description)

    def __repr__(self) -> str:
        return "Tournois(nom='{}', lieu='{}', joueurs='{}')".format(self.name, self.place, self.registered_players)
