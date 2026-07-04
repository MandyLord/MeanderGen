from src.geometry import Point
from src.path import Path
from src.svg_writer import SVGWriter

def test_svg():
    p=Path()
    p.add_point(Point(0,0))
    p.add_point(Point(10,10))
    assert "<svg" in SVGWriter.path_to_svg(p)

