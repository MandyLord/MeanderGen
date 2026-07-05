import random
from src.movement_models.wander import Wander

def test_repeatable():
    rng1=random.Random(42)
    rng2=random.Random(42)
    w1=Wander()
    w2=Wander()
    t1=[w1.next_turn(rng1) for _ in range(20)]
    t2=[w2.next_turn(rng2) for _ in range(20)]
    assert t1==t2

def test_turns_within_limit():
    rng=random.Random(1)
    w=Wander(max_turn_degrees=4)
    for _ in range(500):
        assert abs(w.next_turn(rng))<=4.0


