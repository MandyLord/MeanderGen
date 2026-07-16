from dataclasses import dataclass


@dataclass
class RectangleBoundary:
    left: float
    top: float
    right: float
    bottom: float

    def contains(self, traveller):

        return (
            self.left <= traveller.x <= self.right
            and
            self.top <= traveller.y <= self.bottom
        )
    
    def distance_to(self, traveller):

        left = traveller.x - self.left
        right = self.right - traveller.x
        top = traveller.y - self.top
        bottom = self.bottom - traveller.y

        return min(
            left,
            right,
            top,
            bottom,
        )