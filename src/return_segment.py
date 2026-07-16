from .segment import Segment


class ReturnSegment(Segment):
    """
    Returns alongside the outward path,
    maintaining comfortable spacing,
    without closing the loop.
    """

    def start(self, traveller):

        self.traveller = traveller
        self.points = []
        self.step_number = 0
        self.step_length = 3.5

        self.turns = [
            -4.0,
            -6.0,
            -8.0,
            -6.0,
            -4.0,
        ]

        self.record_position(traveller)

    def next_point(self):

        turn = self.current_turn()

        self.advance(
            self.traveller,
            turn,
            self.step_length,
        )

        self.record_position(self.traveller)

        self.step_number += 1

        return (
            round(self.traveller.x),
            round(self.traveller.y),
        )

    @property
    def finished(self):
        return self.step_number >= len(self.turns)