from src.direction_planner import DirectionPlanner
from src.geometry import Point
from src.path import Path
from src.boundary import Rectangle
from src.scoring.boundary_score import BoundaryScore
from src.scoring.space_score import SpaceScore
from src.scoring.flow_score import FlowScore

class TestState:

    def __init__(self):

        self.current = Point(190, 100)
        self.heading = 90
        self.step_length = 10
        self.previous_turn = 10
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
        SpaceScore(
            weight=1.0
        ),
        BoundaryScore(
            boundary,
            weight=5.0
        ),
        FlowScore(
            weight=1.0
        ),
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
scorer_names = [
    scorer.__class__.__name__.replace(
        "Score",
        "",
    )
    for scorer in planner.scorers
]

print()
print("Planner Test")
print("=" * 40)
print(f"Current heading: {state.heading}°")
print()

heading = f"{'Heading':>8}"

for name in scorer_names:
    heading += f"{name:>10}"

heading += f"{'Total':>10}"

print(heading)
print("-" * len(heading))
print("-" * 42)

for candidate in candidates:

    marker = ""

    if candidate.heading == chosen_heading:
        marker = "  <-- Selected"
    
    

    row = f"{candidate.heading:>8}"

    for scorer in planner.scorers:

        score = candidate.breakdown.get(
            scorer.__class__.__name__,
            0.0,
        )

        row += f"{score:>10.2f}"

    row += f"{candidate.score:>10.2f}"

    if candidate.heading == chosen_heading:
        row += "  <-- Selected"

    print(row)
print(f"Chosen heading: {chosen_heading}°")