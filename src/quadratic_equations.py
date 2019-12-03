from math import sqrt, fabs
from typing import Tuple

from src.utils import round_double


def two_real_root(delta: float, a: float, b: float) -> Tuple[float, float]:
    return (-b-sqrt(fabs(delta)))/(2.0*a), (-b+sqrt(fabs(delta)))/(2.0*a)


def one_real_root(a: float, b: float) -> float:
    return -b/(2*a)


def discriminant(a: float, b: float, c: float) -> float:
    return (b*b)-4.0*a*c


def solve_quadratic_equation(a: float, b: float, c: float):

    delta: float = discriminant(a, b, c)

    if delta == 0.0:
        return round_double(one_real_root(a, b)), None, 1

    elif delta < 0.0:
        return None, None, 0

    else:
        root1, root2 = two_real_root(delta, a, b, )
        return round_double(root1), round_double(root2), 2