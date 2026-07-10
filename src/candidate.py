from dataclasses import dataclass, field

from src.geometry import Point


@dataclass
class Candidate:
    heading: float
    position: Point
    score: float = 0.0
    breakdown: dict[str, float] = field(
        default_factory=dict
    )
    def __repr__(self):
        return (
            f"Candidate("
            f"heading={self.heading}, "
            f"score={self.score:.2f}, "
            f"position={self.position}"
            f")"
        )