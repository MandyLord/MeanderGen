from src.geometry import Point
from src.pathfinder import PathFinder
from src.movement_models import Wander
def test_points():
    p=PathFinder(Wander(),seed=42).generate(Point(0,0),0,5)
    assert p.point_count()==6

