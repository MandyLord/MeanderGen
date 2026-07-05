from math import cos,sin,radians
import random
from .geometry import Point
from .path import Path
from .state import State

class PathFinder:
    def __init__(self,movement_model,step_length=5.0,seed=None):
        self.movement_model=movement_model
        self.step_length=step_length
        self.rng=random.Random(seed)
    def generate(self,start:Point,heading:float,steps:int)->Path:
        p=Path()
        current=start
        p.add_point(current)
        h=heading
        for i in range(steps):
            _=State(current,h,i)
            h+=self.movement_model.next_turn(self.rng)
            current=Point(current.x+self.step_length*cos(radians(h)),
                          current.y+self.step_length*sin(radians(h)))
            p.add_point(current)
        return p
