from pathlib import Path as FilePath
from .geometry import Point
from .movements import move_away_01
from .movements import grow_bulb_01
from .path import Path
from .svg_writer import SVGWriter


points1, x, y, heading = move_away_01.build(
    x=40,
    y=60,
    heading=0,
)

points2, x, y, heading = grow_bulb_01.build(
    x,
    y,
    heading,
)

points = points1 + points2

path = Path()

for x, y in points:
    path.add_point(
        Point(x, y)
    )

SVGWriter.write(
    path,
    "preview_loop.svg",
    width=200,
    height=200,
    development=True,
)

print("Created:", FilePath("preview_loop.svg").resolve())