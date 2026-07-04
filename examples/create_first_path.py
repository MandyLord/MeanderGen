from src.geometry import Point
from src.path import Path
from src.svg_writer import SVGWriter

path = Path()
path.add_point(Point(10,10))
path.add_point(Point(25,20))
path.add_point(Point(45,30))
path.add_point(Point(70,55))
path.add_point(Point(90,80))

SVGWriter.write(path, "examples/first_path.svg", 100, 100)
print("Created examples/first_path.svg")

