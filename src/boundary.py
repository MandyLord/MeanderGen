"""
Boundary mathematics and steering behaviour.
"""
from dataclasses import dataclass
from .geometry import Point
from .steering import SteeringBehaviour

@dataclass(frozen=True)
class Rectangle:
    left: float
    top: float
    right: float
    bottom: float

    def distances(self, point: Point)->dict[str,float]:
        return {
            "left": point.x-self.left,
            "right": self.right-point.x,
            "top": point.y-self.top,
            "bottom": self.bottom-point.y,
        }

    def contains(
        self,
        point: Point,
    ) -> bool:
        """
        Return True if the supplied point lies
        inside or on the rectangle.
        """

        return (
            self.left <= point.x <= self.right
            and
            self.top <= point.y <= self.bottom
        )
    def closest_point(
        self,
        point: Point,
    ) -> Point:
        """
        Return the closest point on the rectangle
        to the supplied point.
        """

        x = min(
            max(point.x, self.left),
            self.right,
        )

        y = min(
            max(point.y, self.top),
            self.bottom,
        )

        return Point(x, y)
    def distance_to(
        self,
        point: Point,
    ) -> float:
        """
        Return the signed distance from the supplied
        point to the rectangle.

        Positive values are inside the rectangle.
        Zero is on the boundary.
        Negative values are outside.
        """

        closest = self.closest_point(point)

        distance = point.distance_to(closest)

        if self.contains(point):

            distances = self.distances(point)

            return min(distances.values())

        return -distance  
     
class BoundaryGuide(SteeringBehaviour):
    """
    Suggest a gentle steering correction as a path approaches
    the edge of the drawing area.
    """
    def __init__(self, rectangle: Rectangle, margin: float=25.0, max_correction: float=6.0):
        self.rectangle=rectangle
        self.margin=margin
        self.max=max_correction

    def steering_adjustment(self, state) -> float:
        point = state.position
        d=self.rectangle.distances(point)
        adjust=0.0
        if d["left"]<self.margin:
            adjust += self.max*(1-d["left"]/self.margin)
        if d["right"]<self.margin:
            adjust -= self.max*(1-d["right"]/self.margin)
        return adjust

