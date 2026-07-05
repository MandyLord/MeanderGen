"""Improved Wander movement model with turn memory."""

from __future__ import annotations
import random

class Wander:
    NAME = "Wander"
    PERSONALITY = "Curious and relaxed"

    def __init__(self, max_turn_degrees: float = 4.0, memory: float = 0.85):
        self.max_turn = max_turn_degrees
        self.memory = memory
        self._previous_turn = 0.0

    def next_turn(self, rng: random.Random) -> float:
        noise = rng.uniform(-self.max_turn, self.max_turn)
        turn = self.memory * self._previous_turn + (1.0 - self.memory) * noise
        self._previous_turn = turn
        return turn

