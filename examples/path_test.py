from src.geometry import Point
from src.path import Path

path = Path()

path.add_point(Point(0, 0))
path.add_point(Point(10, 0))
path.add_point(Point(10, 10))

point = Point(5, 4)

distance = path.nearest_distance(point)

print(f"Nearest distance: {distance:.2f}")