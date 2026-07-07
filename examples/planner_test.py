from src.direction_planner import DirectionPlanner
from src.geometry import Point

planner = DirectionPlanner()

point = Point(100, 100)

candidates = planner.candidates(
    point,
    90,
    10,
)

planner.score_candidates(
    candidates,
    None,
)

for candidate in candidates:
    print(candidate)