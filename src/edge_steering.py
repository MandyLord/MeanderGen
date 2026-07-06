from math import atan2, degrees, cos, sin, radians

from .steering import SteeringBehaviour

class EdgeSteering(SteeringBehaviour):
    def __init__(
    self,
    width=800,
    height=800,
    margin=250,
    max_turn=10.0,
    look_ahead=60,
):
        self.width = width
        self.height = height
        self.margin = margin
        self.max_turn = max_turn
        self.look_ahead = look_ahead
    def steering_adjustment(self, state):
        point = state.position
        heading = state.heading

        future_x = point.x + self.look_ahead * cos(radians(heading))
        future_y = point.y + self.look_ahead * sin(radians(heading))
        # Distance to nearest edge
        distance = min(
        future_x,
        future_y,
        self.width - future_x,
        self.height - future_y,
        )

        if distance >= self.margin:
            return 0.0

        # Steering strength (0.0 → 1.0+)
        strength = (self.margin - distance) / self.margin
        strength = strength * strength

        # Direction back toward the centre
        centre_x = self.width / 2
        centre_y = self.height / 2

        target_heading = degrees(
            atan2(
                centre_y - point.y,
                centre_x - point.x,
            )
        )

        # Smallest angle difference (-180..180)
        delta = target_heading - heading

        while delta > 180:
            delta -= 360

        while delta < -180:
            delta += 360

        return strength * self.max_turn * (delta / 180.0)