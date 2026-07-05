"""Sprint 2.3A - Wander with drifting target turn."""

from __future__ import annotations
import random

class Wander:
    NAME = "Wander"
    PERSONALITY = "Calm and curious"

    def __init__(
        self,
        max_turn_degrees: float = 4.0,
        memory: float = 0.96,
        target_change_probability: float = 0.03,
    ):
        self.max_turn = max_turn_degrees
        self.memory = memory
        self.target_change_probability = target_change_probability
        self._turn = 0.0
        self._target_turn = 0.0

    def next_turn(self, rng: random.Random) -> float:
        if rng.random() < self.target_change_probability:
            self._target_turn = rng.uniform(-self.max_turn, self.max_turn)

        self._turn += (self._target_turn - self._turn) * (1.0 - self.memory)
        return self._turn


