from dataclasses import dataclass


@dataclass
class Traveller:
    x: float
    y: float
    heading: float

    distance_to_boundary: float = 0.0
    near_boundary: bool = False