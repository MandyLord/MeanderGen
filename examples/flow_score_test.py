from src.geometry import Point
from src.path import Path
from src.scoring.flow_score import FlowScore


class TestState:

    def __init__(self):

        self.heading = 90
        self.previous_turn = 10
        self.path = Path()


class TestCandidate:

    def __init__(
        self,
        heading,
    ):
        self.heading = heading


state = TestState()

scorer = FlowScore()

print("Flow Score Test")
print("=" * 30)

for heading in (
    100,
    105,
    110,
    120,
    135,
):

    candidate = TestCandidate(
        heading,
    )

    score = scorer.score(
        candidate,
        state,
    )

    print(
        f"{heading:>6}°"
        f"   score = {score:>6.2f}"
    )