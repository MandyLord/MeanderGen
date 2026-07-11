from __future__ import annotations
from dataclasses import dataclass
from .geometry import Point
from .path import Path
from .planner_phase import PlannerPhase

@dataclass(frozen=True)
class State:
    position: Point
    heading: float
    step_number: int
    path: Path
    previous_turn: float
    step_length: float
    phase: PlannerPhase