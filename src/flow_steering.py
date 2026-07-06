from .steering import SteeringBehaviour


class FlowSteering(SteeringBehaviour):
    """
    Encourage long, flowing curves by gently reinforcing
    the previous turn direction.
    """

    def __init__(self, strength=0.15):
        self.strength = strength

    def steering_adjustment(self, state):

        previous_turn = state.previous_turn

        if previous_turn > 0:
            return self.strength

        if previous_turn < 0:
            return -self.strength

        return 0.0