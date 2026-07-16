from abc import ABC, abstractmethod
from math import cos, sin, radians

class Segment(ABC):
    """
    Base class for every procedural motif segment.
S
    A segment produces one continuous piece
    of local geometry.

    The engine requests points one at a time,
    allowing it to react to boundaries,
    spacing and empty space while stitching.
    """

    def advance(self, traveller, turn, step_length):

        traveller.heading += turn

        traveller.x += cos(radians(traveller.heading)) * step_length
        traveller.y += sin(radians(traveller.heading)) * step_length

    def current_turn(self):
        return self.turns[self.step_number]
    
    def modify_turn(self, turn):
        return turn

    def record_position(self, traveller):

        self.points.append((
            round(traveller.x),
            round(traveller.y),
        ))    

    @abstractmethod
    def start(self):
        """Prepare the segment."""
        pass

    @abstractmethod
    def next_point(self):
        """Return the next local point."""
        pass

    @property
    @abstractmethod
    def finished(self):
        """True when the segment has completed."""
        pass