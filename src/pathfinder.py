from math import cos,sin,radians
import random
from .geometry import Point
from .path import Path
from .state import State
from .edge_steering import EdgeSteering
from .self_avoidance import SelfAvoidance

class PathFinder:
    def __init__(self,movement_model,step_length=5.0,seed=None,boundary_guide=None):
        self.model=movement_model
        self.step=step_length
        self.rng=random.Random(seed)
        self.steering_behaviours = [
            EdgeSteering(),
            SelfAvoidance(),
        ]

        if boundary_guide is not None:
            self.steering_behaviours.append(boundary_guide)

    def generate(self,start:Point,heading:float,steps:int)->Path:
        path=Path()
        current=start
        h=heading
        path.add_point(current)
        
        for i in range(steps):
            state = State(current, h, i, path)
            turn=self.model.next_turn(self.rng)
            for behaviour in self.steering_behaviours:
                turn += behaviour.steering_adjustment(state)
            
            h += turn
            current=Point(
                current.x+self.step*cos(radians(h)),
                current.y+self.step*sin(radians(h))
            )
            path.add_point(current)
        return path

