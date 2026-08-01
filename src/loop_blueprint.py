from .traveller import Traveller
from .move_away_segment import MoveAwaySegment
from .turn_segment import TurnSegment
from .return_segment import ReturnSegment
from .leave_segment import LeaveSegment
from .rectangle_boundary import RectangleBoundary
from .turn_profile import TurnProfile


class LoopBlueprint:

    def build(self):

        traveller = Traveller(
            x=60.0,
            y=40.0,
            heading=105.0,
        )

        boundary = RectangleBoundary(
            left=0,
            top=0,
            right=120,
            bottom=80,
        )

        points = []

        for _ in range(1):

            loop_intent = traveller.patch_builder.choose_loop(
                traveller,
            )

            points.extend(
                self.build_loop(
                    traveller,
                    loop_intent,
                    boundary,
                )
            )
        return points
    
    def build_loop(
        self,
        traveller,
        loop_intent,
        boundary,
    ):

        points = []

        move_away = MoveAwaySegment()
        turn = TurnSegment()
        return_segment = ReturnSegment()
        leave = LeaveSegment()

        segments = [
            move_away,
            turn,
            return_segment,
            leave,
        ]

        turn_profile = TurnProfile(
            style="tight",
            direction=loop_intent.direction,
        )

        for segment in segments:

            if isinstance(segment, TurnSegment):
                segment.start(
                    traveller,
                    turn_profile,
                )
            else:
                segment.start(traveller)

            while not segment.finished:

                x, y = segment.next_point()

                traveller.update_awareness(boundary)

                points.append((x, y))

            # Experiment: give Return a few companion
            # points from the end of Turn.
                if isinstance(segment, TurnSegment):
                    traveller.outward_points.extend(
                        segment.turn_points
                    )

        return points