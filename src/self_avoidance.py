from math import atan2, degrees

from .steering import SteeringBehaviour

class SelfAvoidance(SteeringBehaviour):
    """
    Steering behaviour that will gently avoid previous parts
    of the path.
    """
    def __init__(
        self,
        avoid_radius=75.0,
        max_turn=8.0,
        strength=0.1,
        recent_segments=10,
    ):
        self.avoid_radius = avoid_radius
        self.max_turn = max_turn
        self.strength = strength
        self.recent_segments = recent_segments

    def steering_adjustment(self, state):

        path = state.path
        point = state.position
        heading = state.heading
        step = state.step_number

        points = path.points()
      
        # Ignore the first few steps and the most recent points
        if len(points) < 50:
            return 0.0
        nearest_segment = path.nearest_segment(
            point,
            ignore_last=self.recent_segments,
        )
        
        if nearest_segment is None:
            return 0.0

        closest_point = nearest_segment.closest_point(point)

        nearest_distance = point.distance_to(closest_point)


        escape_heading = degrees(
            atan2(
                point.y - closest_point.y,
                point.x - closest_point.x
            )
        )
        delta = escape_heading - heading
        while delta > 180:
            delta -= 360

        while delta < -180:
            delta += 360
        max_turn = self.max_turn

        if delta > max_turn:
            delta = max_turn
        elif delta < -max_turn:
            delta = -max_turn

        if nearest_distance < self.avoid_radius:
            strength = (
                self.avoid_radius - nearest_distance
            ) / self.avoid_radius
            return delta * strength * self.strength 

        return 0.0

