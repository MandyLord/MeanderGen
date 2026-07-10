import random
from math import cos, sin, radians

from .candidate import Candidate
from .geometry import Point
from .scoring.space_score import SpaceScore
from src import candidate

class DirectionPlanner:
    """
    Evaluate candidate directions and choose
    the best one.
    """

    def __init__(
        self,
        max_turn=45,
        turn_step=5,
        scorers=None,
    ):
        self.max_turn = max_turn
        self.turn_step = turn_step

        if scorers is None:
            scorers = [
                SpaceScore(),
            ]

        self.scorers = scorers

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
            candidate.breakdown.clear()

            for scorer in self.scorers:
                score = scorer.score(
                    candidate,
                    state,
            )

                candidate.breakdown[
                    scorer.__class__.__name__
                ] = score
                candidate.score += score


    def choose_turn(
        self,
        candidates,
        state,
    ):
        """
        Score the supplied candidates and return
        the heading of the best one.
        """

        self.score_candidates(
            candidates,
            state,
        )

        best = max(
            candidates,
            key=lambda candidate: candidate.score,
        )

        tolerance = 0.2

        good_candidates = [
            candidate
            for candidate in candidates
            if candidate.score >= best.score - tolerance
        ]

        if state.step_number == 0:
            candidates.sort(
                key=lambda candidate: candidate.score,
                reverse=True,
            )

            for candidate in candidates[:5]:
                print(
                    f"{candidate.heading:>5.1f}°  "
                    f"{candidate.score:.6f}"
                )

            print(len(good_candidates))

        return random.choice(good_candidates).heading