class FlowScore:
    """
    Reward smooth, flowing changes in direction.
    """

    def __init__(
        self,
        weight: float = 0.1,
    ):
        self.weight = weight

    def score(
        self,
        candidate,
        state,
    ):
        """
        Reward headings that continue the previous turn smoothly.
        """
        candidate_turn = (
            candidate.heading
            - state.heading
        )

        difference = abs(
            candidate_turn
            - state.previous_turn
        )

        return (
            -difference
            * self.weight
        )