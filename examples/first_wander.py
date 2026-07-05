from src.geometry import Point
from src.pathfinder import PathFinder
from src.movement_models import Wander
finder=PathFinder(Wander(),seed=42)
path=finder.generate(Point(50,50),0,25)
print(path.point_count())
