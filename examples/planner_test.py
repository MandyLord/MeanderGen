from src.direction_planner import DirectionPlanner
from src.geometry import Point
from src.path import Path
from src.boundary import Rectangle
from src.scoring.boundary_score import BoundaryScore
from src.scoring.space_score import SpaceScore

class TestState:

    def __init__(self):

        self.current = Point(190, 100)
        self.heading = 90
        self.step_length = 10

        self.path = Path()

        self.path.add_point(Point(80, 80))
        self.path.add_point(Point(90, 90))
        self.path.add_point(self.current)

boundary = Rectangle(
    left=0,
    top=0,
    right=200,
    bottom=200,
)

planner = DirectionPlanner(
    scorers=[
        SpaceScore(),
        BoundaryScore(boundary),
    ]
)

state = TestState()

candidates = planner.candidates(
    state.current,
    state.heading,
    state.step_length,
)

planner.score_candidates(
    candidates,
    state,
)

chosen_heading = planner.choose_turn(
    candidates,
    state,
)

print()
print("Planner Test")
print("=" * 40)
print(f"Current heading: {state.heading}°")
print()

print(f"{'Heading':>8} {'Score':>10}")
print("-" * 22)

for candidate in candidates:

    marker = ""

    if candidate.heading == chosen_heading:
        marker = "  <-- Selected"

    print(
        f"{candidate.heading:>8}"
        f"{candidate.score:>10.2f}"
        f"{marker}"
    )

print()
print(f"Chosen heading: {chosen_heading}°")