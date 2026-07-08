from src.boundary import Rectangle
from src.geometry import Point
from src.scoring.boundary_score import BoundaryScore

boundary = Rectangle(
    left=0,
    top=0,
    right=100,
    bottom=100,
)

scorer = BoundaryScore(boundary)

points = [
    Point(50, 50),
    Point(90, 50),
    Point(98, 50),
    Point(100, 50),
    Point(105, 50),
]

print("Boundary Score Test")
print("=" * 40)

for point in points:

    class Candidate:
        pass

    candidate = Candidate()
    candidate.position = point

    score = scorer.score(
        candidate,
        None,
    )

    print(
        f"{point}"
        f"  score = {score:.2f}"
    )