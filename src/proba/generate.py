from typing import Tuple
from proba.rand import randrange_exclude, randrange_step, START_VALUE, STOP_VALUE, STEP_VALUE
from proba.utils import permute_bounds

# TODO: bounds a and b must be different


def generate_pow1() -> Tuple[float, float, float, float, float]:

    a: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    b: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    c: float = randrange_exclude(0.0, START_VALUE, STOP_VALUE, STEP_VALUE)
    d: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    alpha: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)

    return a, b, c, d, alpha


def generate_pow2() -> Tuple[float, float, float]:

    a: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    b: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    a, b = permute_bounds(a, b)

    c = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    while c == a or c == b:
        c = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)

    return a, b, c


def generate_trigo() -> Tuple[float, float, float]:

    a: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    b: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    c: float = randrange_exclude(0.0, START_VALUE, STOP_VALUE, STEP_VALUE)
    a, b = permute_bounds(a, b)

    return a, b, c


def generate_log() -> Tuple[float, float, float]:

    a: float = randrange_step(0.5, STOP_VALUE, STEP_VALUE)
    b: float = randrange_step(0.5, STOP_VALUE, STEP_VALUE)
    a, b = permute_bounds(a, b)

    c = randrange_exclude(0.0, START_VALUE, STOP_VALUE, STEP_VALUE)
    while c < 0.0:
        c = randrange_exclude(0.0, START_VALUE, STOP_VALUE, STEP_VALUE)

    return a, b, c
