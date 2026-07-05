from src.geometry import Point
from src.pathfinder import PathFinder
from src.svg_writer import SVGWriter
from src.movement_models.wander import Wander

def main():
    finder=PathFinder(Wander(),step_length=4.0,seed=42)
    path=finder.generate(
        start=Point(400,400),
        heading=0.0,
        steps=2000,
    )
    SVGWriter.write(path,"examples/tea_test.svg",800,800)
    print("="*36)
    print(" MeanderGen Tea Test")
    print("="*36)
    print("SVG written to examples/tea_test.svg")
    print(f"Points: {path.point_count()}")
    print(f"Length: {path.total_length():.1f}")

if __name__=="__main__":
    main()
