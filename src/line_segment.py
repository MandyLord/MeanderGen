"""
Line segment geometry.
"""

from dataclasses import dataclass
from math import hypot

from .geometry import Point


@dataclass(frozen=True)
class LineSegment:
    start: Point
    end: Point
    def length(self) -> float:
        """
        Return the length of this line segment.
        """
        return hypot(
            self.end.x - self.start.x,
            self.end.y - self.start.y,
        )

    def vector(self) -> tuple[float, float]:
        """
        Return the vector from start to end.
        """
        return (
            self.end.x - self.start.x,
            self.end.y - self.start.y,
        )

    def vector_to(self, point: Point) -> tuple[float, float]:
        """
        Return the vector from the start of the segment
        to the supplied point.
        """
        return (
            point.x - self.start.x,
            point.y - self.start.y,
        )
    def dot(self, point: Point) -> float:
        """
        Return the dot product of the segment vector
        with the vector from the start of the segment
        to the supplied point.
        """
        vx, vy = self.vector()
        px, py = self.vector_to(point)

        return vx * px + vy * py
    def projection_parameter(self, point: Point) -> float:
        """
        Return the projection parameter t for the supplied point.
        """
        vx, vy = self.vector()

        length_squared = vx * vx + vy * vy

        if length_squared == 0:
            return 0.0

        return self.dot(point) / length_squared
    def closest_point(self, point: Point) -> Point:
        """
        Return the closest point on this segment to the supplied point.
        """
        t = self.projection_parameter(point)

        t = max(0.0, min(1.0, t))

        vx, vy = self.vector()

        return Point(
            self.start.x + t * vx,
            self.start.y + t * vy,
        )