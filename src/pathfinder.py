from math import cos,sin,radians
import random
from .geometry import Point
from .path import Path
from .state import State

class PathFinder:
    def __init__(self,movement_model,step_length=5.0,seed=None,boundary_guide=None):
        self.model=movement_model
        self.step=step_length
        self.rng=random.Random(seed)
        self.boundary_guide=boundary_guide

    def generate(self,start:Point,heading:float,steps:int)->Path:
        path=Path()
        current=start
        h=heading
        path.add_point(current)
        for i in range(steps):
            _=State(current,h,i)
            turn=self.model.next_turn(self.rng)
            if self.boundary_guide is not None:
                turn += self.boundary_guide.steering_adjustment(current)
            h += turn
            current=Point(
                current.x+self.step*cos(radians(h)),
                current.y+self.step*sin(radians(h))
            )
            path.add_point(current)
        return path

