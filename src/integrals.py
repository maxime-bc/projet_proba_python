from math import log, fabs, sin, cos


def integral_pow1(a: float, b: float, c: float, d: float, alpha: float) -> float:
    return 1.0/(c*(alpha+1.0))*(pow(b*c-d, (alpha+1.0))-pow(a*c-d, (alpha+1.0)))


def integral_pow2(a: float, b: float, c: float) -> float:
    return log(fabs(b-c)) - log(fabs(a-c))


def integral_trigo1(a: float, b: float, c: float) -> float:
    return (sin(b*c) - sin(a*c))/c


def integral_trigo2(a: float, b: float, c: float) -> float:
    return (-(cos(b*c) - cos(a*c)))/c


def integral_trigo3(a: float, b: float, c: float) -> float:
    return (-(log(fabs(cos(b*c))) - log(fabs(cos(a*c)))))/c


def integral_log(a: float, b: float, c: float) -> float:
    return b*log(b*c) - a*log(a*c) - c*(b - a)