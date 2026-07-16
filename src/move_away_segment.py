from .segment import Segment


class MoveAwaySegment(Segment):
    """
    Leaves the previous stitching and opens
    towards a new loop.
    """

    def start(self, traveller):
        self.points = []
        self.traveller = traveller

        self.step_number = 0
        self.step_length = 3.5

        self.turns = [
            8.0,
            8.0,
            8.0,
            8.0,
            8.0,
        ]

        self.record_position(traveller)

    def modify_turn(self, turn):

            if self.traveller.near_boundary:
                return turn * 0.5

            return turn

    def next_point(self):

        turn = self.current_turn()

        turn = self.modify_turn(turn)

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