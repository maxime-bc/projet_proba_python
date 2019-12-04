from math import fabs


def format_quadratic_equation(a: float, b: float, c: float) -> None:

    print('f(x) = {:0.1f}x²'.format(a), end='')

    if b == 1:
        print("+x", end='')
    else:
        if b > 0.0:
            print("+{:0.1f}x".format(b), end='')
        elif b < 0.0:
            print("{:0.1f}x".format(b), end='')

    if c > 0.0:
        print("+{:0.1f}".format(c), end='')
    elif c < 0.0:
        print("{:0.1f}".format(c), end='')

    print(" = 0\n")


def format_pow1(c: float, d: float, alpha: float) -> None:

    if c == 1.0:
        print("f(x) = (x", end='')

    else:
        print("f(x) = ({:0.1f}x".format(c), end='')

    if d < 0.0:
        tmp: float = fabs(d)
        print("+{:0.1f})^{:0.1f}\n".format(tmp, alpha), end='')

    else:
        print("-{:0.1f})^{:0.1f}\n".format(d, alpha), end='')


def format_pow2(c: float) -> None:

    print("f(x) = 1/", end='')

    if c == 0.0:
        print("x\n", end='')

    else:
        if c < 0.0:
            tmp: float = fabs(c)
            print("(x+{:0.1f})\n".format(tmp), end='')

        else:
            print("(x-{:0.1f})\n".format(c), end='')


def format_trigo1(c: float):

    print("f(x) = cos(", end='')

    if c == 1:
        print("x)\n", end='')

    elif c == -1:
        print("-x)\n", end='')

    else:
        print("{:0.1f}x)\n".format(c), end='')


def format_trigo2(c: float):

    print("f(x) = sin(", end='')

    if c == 1:
        print("x)\n", end='')

    elif c == -1:
        print("-x)\n", end='')

    else:
        print("{:0.1f}x)\n".format(c), end='')


def format_trigo3(c: float):

    print("f(x) = tan(", end='')

    if c == 1:
        print("x)", end='')

    elif c == -1:
        print("-x)", end='')

    else:
        print("{:0.1f}x)\n".format(c), end='')


def format_log(c: float):

    print("f(x) = ln(", end='')

    if c == 1:
        print("x)\n", end='')

    elif c == -1:
        print("-x)\n", end='')

    else:
        print("{:0.1f}x)\n".format(c), end='')
