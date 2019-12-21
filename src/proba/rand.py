import random

'''This module groups functions used to generate random numbers for exercises.'''

START_VALUE: float = -10.0
STOP_VALUE: float = 10.0
STEP_VALUE: float = 0.5


def randrange_step(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start
    # TODO: same problem in C: -10 not in the interval


def randrange_exclude(excluded: float, start: float, stop: float, step: float) -> float:

    rand: float = randrange_step(start, stop, step)

    while excluded == rand:
        rand = randrange_step(start, stop, step)

    return rand


def round_float(x: float) -> float:
    return round(x * 100.0) / 100.0
