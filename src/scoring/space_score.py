
class SpaceScore:
    """
    Score candidates according to how much
    open space surrounds them.
    """

    def score(
        self,
        candidate,
        state,
    ):
        """
        Reward candidates that move into open space.
        """

        return state.path.nearest_distance(
            candidate.position,
            ignore_last=1,
        )