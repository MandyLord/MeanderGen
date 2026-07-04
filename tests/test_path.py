from src.geometry import Point
from src.path import Path

def test_path():
    p=Path()
    p.add_point(Point(0,0))
    p.add_point(Point(3,4))
    assert p.point_count()==2
    assert p.total_length()==5.0

