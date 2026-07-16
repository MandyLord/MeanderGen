from .geometry import Point
from .path import Path
from .svg_writer import SVGWriter
from .loop_blueprint import LoopBlueprint

blueprint = LoopBlueprint()
points = blueprint.build()

path = Path()

SCALE = 5

# Automatically centre the drawing

xs = [x for x, y in points]
ys = [y for x, y in points]

min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)

drawing_width = (max_x - min_x) * SCALE
drawing_height = (max_y - min_y) * SCALE

OFFSET_X = (200 - drawing_width) / 2 - min_x * SCALE
OFFSET_Y = (200 - drawing_height) / 2 - min_y * SCALE

for x, y in points:

    path.add_point(
        Point(
            x * SCALE + OFFSET_X,
            y * SCALE + OFFSET_Y,
        )
    )

SVGWriter.write(
    path,
    "preview_loop.svg",
    width=200,
    height=200,
    development=True,
)

from pathlib import Path

print("Created:", Path("preview_loop.svg").resolve())