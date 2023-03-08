class Requirements:
    def __init__(self):
        # intinerary style
        self.num_member = {'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0}
        self.select_set = {'attractions': 0, 'food': 0, 'entertainment': 0}
        # attractions 
        self.attractions = {'景點一': 0, '景點二': 0}
        # food 
        self.food = {'taiwanese': 0, 'japanese': 0, 'italian': 0, 'french': 0, 'fast_food': 0, 'exotic': 0, 'vegetarian': 0}
        # price
        self.price = {'low': 0, 'mormal': 0, 'medium': 0, 'high': 0}
        # entertainment
        self.entertainment = {'movie': 0, 'shopping': 0, 'romance': 0, 'sports': 0, 'party': 0}
        # distance
        self.geo_distance = {'close': 0, 'middle': 0, 'far': 0}
        self.transport_distance = {'short': 0, 'half': 0, 'long': 0, 'hourup': 0}

    def modify(self, reqiurement):
        pass