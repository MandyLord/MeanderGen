from src.movement_models import Wander
import random

def test_turns_are_repeatable():
    rng = random.Random(42)
    w = Wander()
    turns = [w.next_turn(rng) for _ in range(5)]
    assert len(turns) == 5
