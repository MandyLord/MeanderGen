from math import cos,sin,radians
import random
from .geometry import Point
from .path import Path
from .state import State
from .edge_steering import EdgeSteering
from .self_avoidance import SelfAvoidance
from .flow_steering import FlowSteering

class PathFinder:
    def __init__(self,movement_model,step_length=5.0,seed=None,boundary_guide=None):
        self.model=movement_model
        self.step=step_length
        self.rng=random.Random(seed)
        self.steering_behaviours = [
            EdgeSteering(),
            SelfAvoidance(
                avoid_radius=120,
                max_turn=6,
                strength=0.08,
            ),
            FlowSteering(strength=0.15),
        ]

        if boundary_guide is not None:
            self.steering_behaviours.append(boundary_guide)

    def generate(self,start:Point,heading:float,steps:int)->Path:
        path=Path()
        current=start
        h=heading
        path.add_point(current)
        previous_turn = 0.0
        
        for i in range(steps):
            state = State(
                current,
                h,
                i,
                path,
                previous_turn
            )
            raw_turn = self.model.next_turn(self.rng)
            smoothed_turn = previous_turn * 0.7 + raw_turn * 0.3
            turn = smoothed_turn
            for behaviour in self.steering_behaviours:
                turn += behaviour.steering_adjustment(state)

            previous_turn = smoothed_turn
            h += turn
            current=Point(
                current.x+self.step*cos(radians(h)),
                current.y+self.step*sin(radians(h))
            )
            path.add_point(current)
        return path

