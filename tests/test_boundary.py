from src.boundary import Rectangle
from src.geometry import Point

def test_distances():
    r=Rectangle(0,0,100,100)
    d=r.distances(Point(25,40))
    assert d["left"]==25
    assert d["right"]==75
    assert d["top"]==40
    assert d["bottom"]==60
