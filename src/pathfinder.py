from math import cos,sin,radians
import random
from .geometry import Point
from .path import Path
from .state import State

class PathFinder:
    def __init__(self,movement_model,step_length=5.0,seed=None):
        self.model=movement_model
        self.step=step_length
        self.rng=random.Random(seed)

    def generate(self,start:Point,heading:float,steps:int)->Path:
        path=Path()
        current=start
        h=heading
        path.add_point(current)
        for i in range(steps):
            _=State(current,h,i)
            h+=self.model.next_turn(self.rng)
            current=Point(
                current.x+self.step*cos(radians(h)),
                current.y+self.step*sin(radians(h))
            )
            path.add_point(current)
        return path

