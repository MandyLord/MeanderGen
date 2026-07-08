from src.geometry import Point
from src.line_segment import LineSegment

segment = LineSegment(
    Point(0, 0),
    Point(10, 0),
)

point = Point(5, 4)

distance = segment.distance_to(point)

print(f"Distance: {distance:.2f}")