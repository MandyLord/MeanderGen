from .state import State


class SteeringBehaviour:
    """
    Base class for steering behaviours.

    Subclasses return an angle adjustment (degrees).
    """

    def steering_adjustment(self, state: State):
        return 0.0