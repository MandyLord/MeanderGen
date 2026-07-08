class BoundaryScore:
    """
    Encourage candidates to remain safely
    inside the drawing boundary.
    """

    def __init__(
        self,
        boundary,
        safe_distance: float = 25.0,
        weight: float = 1.0,
    ):
        self.boundary = boundary
        self.safe_distance = safe_distance
        self.weight = weight

    def score(
        self,
        candidate,
        state,
    ):
        distance = self.boundary.distance_to(
            candidate.position,
        )

        if distance <= 0:
            return -1000.0 * self.weight

        if distance >= self.safe_distance:
            return 0.0

        penalty = (
            self.safe_distance - distance
        ) / self.safe_distance

        return -penalty * self.weight