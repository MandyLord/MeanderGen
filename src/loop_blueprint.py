from .traveller import Traveller
from .move_away_segment import MoveAwaySegment
from .turn_segment import TurnSegment
from .return_segment import ReturnSegment
from .leave_segment import LeaveSegment
from .motif_blueprint import MotifBlueprint
from .rectangle_boundary import RectangleBoundary
from .boundary_query import BoundaryQuery


class LoopBlueprint(MotifBlueprint):

    def build(self):

        points = []

        current_x = 0
        current_y = 0

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

        for segment in segments:

            segment.start(traveller)

            while not segment.finished:

                x, y = segment.next_point()
                # Update Traveller awareness here.

                traveller.distance_to_boundary = (
                    BoundaryQuery.distance_to_boundary(
                        traveller,
                        boundary,
                    )
                )   

                traveller.near_boundary = (
                    traveller.distance_to_boundary < 15
                )

                if traveller.near_boundary:
                    print(
                        "Near boundary:",
                        traveller.distance_to_boundary,
    )

                traveller.x = x + current_x
                traveller.y = y + current_y

                points.append((x, y))

            
            # Move the origin to the end of this segment.
            #current_x = translated[0]
            #current_y = translated[1]

            
        return points