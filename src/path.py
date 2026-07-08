"""
MeanderGen - path.py

Sprint 1.2A - The First Path
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .geometry import Point
from .line_segment import LineSegment


@dataclass
class Path:
    """A continuous ordered collection of Point objects."""

    _points: List[Point] = field(default_factory=list)

    def add_point(self, point: Point) -> None:
        self._points.append(point)

    def point_count(self) -> int:
        return len(self._points)

    def points(self) -> tuple[Point, ...]:
        return tuple(self._points)
    
    def segments(self) -> tuple[LineSegment, ...]:
        """
        Return the path as a sequence of line segments.
        """
        if len(self._points) < 2:
            return ()

        return tuple(
            LineSegment(
                self._points[i - 1],
                self._points[i],
            )
            for i in range(1, len(self._points))
        )
    
    def nearest_segment(
        self,
        point: Point,
        ignore_last: int = 0,
    ) -> LineSegment | None:
        
        """
        Return the line segment nearest to the supplied point.
        """
        segments = self.segments()

        if ignore_last > 0:
            segments = segments[:-ignore_last]

        if not segments:
            return None

        nearest = None
        nearest_distance = float("inf")

        for segment in segments:
            distance = segment.distance_to(point)

            if distance < nearest_distance:
                nearest_distance = distance
                nearest = segment

        return nearest
    
    def nearest_distance(
        self,
        point: Point,
        ignore_last: int = 0,
    ) -> float:
        """
        Return the distance from the supplied point
        to the nearest line segment.
        """
        segment = self.nearest_segment(
            point,
            ignore_last=ignore_last,
        )

        if segment is None:
            return float("inf")

        return segment.distance_to(point)

    def clear(self) -> None:
        self._points.clear()

    def total_length(self) -> float:
        if len(self._points) < 2:
            return 0.0
        return sum(
            self._points[i-1].distance_to(self._points[i])
            for i in range(1, len(self._points))
        )

    def bounding_box(self):
        if not self._points:
            return None
        xs=[p.x for p in self._points]
        ys=[p.y for p in self._points]
        return (min(xs), min(ys), max(xs), max(ys))

