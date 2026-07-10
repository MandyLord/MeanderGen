
from dbm import error


class SpaceScore:
    """
    Score candidates according to how much
    open space surrounds them.
    """

    def __init__(
        self,
        weight: float = 1.0,
        ideal_spacing: float = 25.0,
    ):
        
        self.weight = weight
        self.ideal_spacing = ideal_spacing

    def score(
        self,
        candidate,
        state,
    ):
        """
        Reward candidates that move into open space.
        """

        distance = state.path.nearest_distance(
            candidate.position,
            ignore_last=1,
        )

        error = abs(distance - self.ideal_spacing)

        return -error * self.weight