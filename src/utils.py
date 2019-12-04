# TODO : code round_double
from typing import Tuple


def round_double(x: float) -> float:
    return round(x * 100.0) / 100.0


def permute_bounds(a: float, b: float) -> Tuple[float, float]:
    tmp: float = a
    a = b
    b = tmp
    return a, b
