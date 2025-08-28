class Drama:
    def __init__(self, drama):
        self.name = drama[0]
        self.rating = drama[1]
        self.actors = drama[2]
        self.viewship_rate = drama[3]
        self.genre = drama[4]
        self.director = drama[5]
        self.writer = drama[6]
        self.year = drama[7]
        self.no_of_episodes = drama[8]
        self.network = drama[9]

    def __str__(self):
        return self.name
    
    def __lt__(self, other):
        return self.rating < other.rating

    def no_of_actors(self):
        actors_list = self.actors.split(",")
        return len(actors_list)
    
    def before_2015(self):
        if int(self.year) < 2015:
            return True
        else:
            return False
        