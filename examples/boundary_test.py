from src.boundary import Rectangle
from src.geometry import Point

boundary = Rectangle(
    left=0,
    top=0,
    right=100,
    bottom=100,
)

tests = [
    Point(50, 50),
    Point(-10, 50),
    Point(120, 50),
    Point(50, -20),
    Point(50, 120),
]

print("Boundary Test")
print("=" * 40)

for point in tests:

    closest = boundary.closest_point(point)

    print(
    f"{point}"
    f" -> {closest}"
    f"  distance = {boundary.distance_to(point):.2f}"
)