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

