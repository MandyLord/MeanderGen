from math import cos, sin, radians

from .candidate import Candidate
from .geometry import Point
from .scoring.space_score import SpaceScore


class DirectionPlanner:
    """
    Evaluate candidate directions and choose
    the best one.
    """

    def __init__(
        self,
        max_turn=45,
        turn_step=5,
    ):
        self.max_turn = max_turn
        self.turn_step = turn_step
        self.scorers = [
            SpaceScore(),
        ]

    def candidate_headings(
        self,
        current_heading,
    ):
        """
        Generate candidate headings centred
        around the current heading.
        """

        headings = []

        turn = -self.max_turn

        while turn <= self.max_turn:

            headings.append(
                current_heading + turn
            )

            turn += self.turn_step

        return headings

    def future_position(
        self,
        point,
        heading,
        step_length,
    ):
        """
        Predict where the next step would end.
        """

        x = point.x + cos(radians(heading)) * step_length
        y = point.y + sin(radians(heading)) * step_length

        return Point(x, y)

    def candidates(
        self,
        point,
        current_heading,
        step_length,
    ):
        """
        Generate Candidate objects for every
        possible next move.
        """

        candidates = []

        for heading in self.candidate_headings(current_heading):

            position = self.future_position(
                point,
                heading,
                step_length,
            )

            candidates.append(
                Candidate(
                    heading=heading,
                    position=position,
                )
            )

        return candidates
    
    def score_candidates(
    self,
    candidates,
    state,
):
        """
        Score every candidate.
        """

        for candidate in candidates:

            candidate.score = 0.0

            for scorer in self.scorers:

                candidate.score += scorer.score(
                    candidate,
                    state,
                )

    def choose_turn(self, state):
        """
        Choose the highest-scoring candidate heading.
        """

        candidates = self.candidates(
            state.current,
            state.heading,
            state.step_length,
        )

        self.score_candidates(
            candidates,
            state,
        )

        best = max(
            candidates,
            key=lambda candidate: candidate.score,
        )

        return best.heading