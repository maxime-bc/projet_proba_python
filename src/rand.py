import random


def randrange_step(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start
    # TODO: same problem in C: -10 not in the interval


def randrange_exclude(excluded: float, start: float, stop: float, step: float) -> float:

    rand: float = randrange_step(start, stop, step)

    while excluded == rand:
        rand = randrange_step(start, stop, step)

    return rand
