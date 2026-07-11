from enum import Enum, auto


class PlannerPhase(Enum):
    """
    High-level stages of path generation.
    """

    SEED = auto()
    GROWTH = auto()
    FILL = auto()