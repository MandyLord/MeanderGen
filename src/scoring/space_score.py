
class SpaceScore:
    """
    Score candidates according to how much
    open space surrounds them.
    """

    def __init__(
        self,
        weight: float = 1.0,
    ):
        self.weight = weight

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

        return distance * self.weight