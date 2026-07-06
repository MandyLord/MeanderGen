from math import hypot, atan2, degrees

from .steering import SteeringBehaviour

class SelfAvoidance(SteeringBehaviour):
    """
    Steering behaviour that will gently avoid previous parts
    of the path.
    """

    def steering_adjustment(self, state):

        path = state.path
        point = state.position
        heading = state.heading
        step = state.step_number

        points = path.points()
        # Ignore the first few steps and the most recent points
        if len(points) < 50:
            return 0.0

        nearest_distance = float("inf")
        nearest_point = None

        for old_point in points[:-20]:
            distance = hypot(
                point.x - old_point.x,
                point.y - old_point.y
            )

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_point = old_point



        if nearest_point is None:
            return 0.0

        escape_heading = degrees(
            atan2(
                point.y - nearest_point.y,
                point.x - nearest_point.x
            )
        )
        delta = escape_heading - heading
        while delta > 180:
            delta -= 360

        while delta < -180:
            delta += 360
        max_turn = 8.0

        if delta > max_turn:
            delta = max_turn
        elif delta < -max_turn:
            delta = -max_turn

        if nearest_distance < 75:
            strength = (75 - nearest_distance) / 75.0
            return delta * strength * 0.1

        return 0.0

