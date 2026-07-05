"""
Boundary mathematics for MeanderGen.

This module knows about the drawing rectangle but knows nothing
about Wander or SVG generation.
"""

from dataclasses import dataclass
from .geometry import Point

@dataclass(frozen=True)
class Rectangle:
    left: float
    top: float
    right: float
    bottom: float

    def width(self) -> float:
        return self.right - self.left

    def height(self) -> float:
        return self.bottom - self.top

    def contains(self, point: Point) -> bool:
        return (
            self.left <= point.x <= self.right and
            self.top <= point.y <= self.bottom
        )

    def distances(self, point: Point) -> dict[str, float]:
        return {
            "left": point.x - self.left,
            "right": self.right - point.x,
            "top": point.y - self.top,
            "bottom": self.bottom - point.y,
        }
