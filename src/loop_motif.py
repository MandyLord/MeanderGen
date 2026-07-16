from dataclasses import dataclass
import math
import random


@dataclass
class LoopMotif:
    """
    Generates one open quilting loop.

    The motif does not decide where the quilt is
    travelling. It only controls the shape of one
    loop by returning a turn amount.
    """

    steps: int = 40

    def __post_init__(self):
        self.age = 0
        self.direction = random.choice((-1, 1))

        # Every loop has a slightly different character.
        self.strength = random.uniform(0.8, 1.2)

    @property
    def finished(self):
        return self.age >= self.steps

    def next_turn(self):

        progress = self.age / self.steps

        # Four simple phases of an open quilting loop.

        if progress < 0.20:
            # Grow away gently.
            amount = 2.0
        elif progress < 0.45:
            # Form the rounded end.
            amount = 8.0
        elif progress < 0.65:
            # Ease the turn so we come back beside ourselves.
            amount = 4.0
        else:
            # Leave the loop naturally.
            amount = 0.0

        self.age += 1

        return amount * self.strength * self.direction