"""
MeanderGen - path.py

Sprint 1.2A - The First Path
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .geometry import Point


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

