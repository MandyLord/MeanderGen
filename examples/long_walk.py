from src.geometry import Point
from src.pathfinder import PathFinder
from src.movement_models import Wander
from src.svg_writer import SVGWriter

finder=PathFinder(Wander(),step_length=5.0,seed=42)
path=finder.generate(Point(150,150),0.0,1000)

SVGWriter.write(path,"examples/long_walk.svg",800,800)
print("Long Walk complete")
