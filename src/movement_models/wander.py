"""Sprint 2.1 Wander with stronger inertia."""

from __future__ import annotations
import random

class Wander:
    NAME="Wander"
    PERSONALITY="Curious and relaxed"

    def __init__(self,max_turn_degrees=3.0,memory=0.93):
        self.max_turn=max_turn_degrees
        self.memory=memory
        self._turn=0.0

    def next_turn(self,rng: random.Random)->float:
        noise=rng.uniform(-self.max_turn,self.max_turn)
        self._turn=self.memory*self._turn+(1-self.memory)*noise
        return self._turn


