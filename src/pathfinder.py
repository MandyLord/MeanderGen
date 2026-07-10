from importlib.resources import path
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
            #EdgeSteering(),
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
            #print(i)
            state = State(
                current,
                h,
                i,
                path,
                previous_turn
            )
            if hasattr(self.model, "choose_turn"):

                candidates = self.model.candidates(
                    current,
                    h,
                    self.step,
                )

                chosen_heading = self.model.choose_turn(
                    candidates,
                    state,
                )
                if i == 129:
                    print()
                    print("Step 0 Scores")
                    print("-" * 40)

                    for candidate in candidates:
                        print(
                            candidate.heading,
                            candidate.breakdown,
                            candidate.score,
                )

                    print()

                if 128 <= i <=138:
                    print(
                        f"Step {i:2}: "
                        f"heading={h:6.1f}  "
                        f"chosen={chosen_heading:6.1f}"
                    )

                turn = chosen_heading - h

            else:

                raw_turn = self.model.next_turn(self.rng)

                smoothed_turn = (
                    previous_turn * 0.7
                    + raw_turn * 0.3
                )

                turn = smoothed_turn

            previous_turn = turn

            h += turn
            if 128 <= i <=138:
                print(f"    new heading = {h}")
                
            current=Point(
                current.x+self.step*cos(radians(h)),
                current.y+self.step*sin(radians(h))
            )
            path.add_point(current)
        print("Points in path:", path.point_count())
        print("Final position:", current)
        print()
        print("Last 10 points:")
        for p in path.points()[-10:]:
            print(p)
        return path

