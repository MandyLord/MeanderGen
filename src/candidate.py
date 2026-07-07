from dataclasses import dataclass

from src.geometry import Point


from dataclasses import dataclass


@dataclass
class Candidate:
    heading: float
    position: Point
    score: float = 0.0

    def __repr__(self):
        return (
            f"Candidate("
            f"heading={self.heading}, "
            f"score={self.score:.2f}, "
            f"position={self.position}"
            f")"
        )