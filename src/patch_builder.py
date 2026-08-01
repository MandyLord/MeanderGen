from .loop_intent import LoopIntent


class PatchBuilder:
    """Builds a quilting patch from one or more loops."""

    def __init__(self):
        self.preferred_loop_size = "medium"
        self.last_loop = None
        self.loop_count = 0

    def choose_loop(self, traveller):

        if traveller.near_boundary:
            pass

        if self.last_loop is None:
            direction = "left"

        elif self.last_loop.direction == "left":
            direction = "right"

        else:
            direction = "left"

        loop = LoopIntent(
            purpose="first_loop",
            size=self.preferred_loop_size,
            direction=direction,
        )

        self.last_loop = loop

        self.loop_count += 1
        return loop