from src.geometry import Point
from src.pathfinder import PathFinder
from src.movement_models import Wander
from src.svg_writer import SVGWriter

finder = PathFinder(
    movement_model=Wander(max_turn_degrees=4.0, memory=0.85),
    step_length=5.0,
    seed=42,
)

path = finder.generate(
    start=Point(50, 50),
    heading=0.0,
    steps=250,
)

SVGWriter.write(path, "examples/first_wander.svg", 300, 300)
print("Created examples/first_wander.svg")

