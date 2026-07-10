from src.geometry import Point
from src.pathfinder import PathFinder
from src.svg_writer import SVGWriter
from src.direction_planner import DirectionPlanner
from src.boundary import Rectangle
from src.scoring.space_score import SpaceScore
from src.scoring.boundary_score import BoundaryScore
from src.scoring.flow_score import FlowScore

boundary = Rectangle(
    left=0,
    top=0,
    right=800,
    bottom=800,
)
planner = DirectionPlanner(
    scorers=[
        SpaceScore(),
        BoundaryScore(boundary),
        FlowScore(),
    ]
)
finder=PathFinder(planner,step_length=5.0,seed=42)
path=finder.generate(Point(150,150),0.0,1000)

SVGWriter.write(
    path,
    "examples/planner_walk.svg",
    800,
    800,
    development=True,
)
print("Planner Walk complete")