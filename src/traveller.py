from dataclasses import dataclass, field
from math import hypot

from .boundary_query import BoundaryQuery
from .patch_builder import PatchBuilder


@dataclass
class Traveller:
    x: float
    y: float
    heading: float

    distance_to_boundary: float = 0.0
    near_boundary: bool = False
    patch_builder: PatchBuilder = field(default_factory=PatchBuilder)
    outward_points: list = field(default_factory=list)
    companion_points: list = field(default_factory=list)

    def update_awareness(self, boundary):

        self.distance_to_boundary = (
            BoundaryQuery.distance_to_boundary(
                self,
                boundary,
            )
        )

        self.near_boundary = (
            self.distance_to_boundary < 15
        )

    def distance_to_outward_path(self):

        if not self.outward_points:
            return None, float("inf")

        nearest_index = None
        nearest_distance = float("inf")

        for index, (x, y) in enumerate(self.outward_points):

            distance = hypot(
                self.x - x,
                self.y - y,
            )

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_index = index

        return nearest_index, nearest_distance