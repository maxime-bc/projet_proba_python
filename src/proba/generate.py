from typing import Tuple
from proba.rand import randrange_exclude, randrange_step, START_VALUE, STOP_VALUE, STEP_VALUE

'''This module groups functions generating random values for each type of exercises.'''


def generate_pow1() -> Tuple[float, float, float, float, float]:

    a: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    b: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    c: float = randrange_exclude(0, START_VALUE, STOP_VALUE, STEP_VALUE)
    d: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    alpha: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)

    return a, b, c, d, alpha


def generate_pow2() -> Tuple[float, float, float]:

    a: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    b: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)

    c = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    while c == a or c == b:
        c = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)

    return a, b, c


def generate_trigo() -> Tuple[float, float, float]:

    a: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    b: float = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)
    c: float = randrange_exclude(0, START_VALUE, STOP_VALUE, STEP_VALUE)

    return a, b, c


def generate_log() -> Tuple[float, float, float]:

    a: float = randrange_step(0.5, STOP_VALUE, STEP_VALUE)
    b: float = randrange_step(0.5, STOP_VALUE, STEP_VALUE)
    c: float = randrange_step(0.5, STOP_VALUE, STEP_VALUE)

    return a, b, c
