import random
class Wander:
    NAME="Wander"
    PERSONALITY="Curious and relaxed"
    def __init__(self,max_turn_degrees=6.0):
        self.max_turn_degrees=max_turn_degrees
    def next_turn(self,rng: random.Random)->float:
        return rng.uniform(-self.max_turn_degrees,self.max_turn_degrees)
