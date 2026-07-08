from math import hypot


class SpaceScore:
    """
    Temporary scoring function.

    Reward candidates that are further
    from the origin.
    """

    def score(
        self,
        candidate,
        state,
    ):
        return hypot(
            candidate.position.x,
            candidate.position.y,
        )