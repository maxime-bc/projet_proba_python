from math import fabs


def format_quadratic_equation(a: float, b: float, c: float) -> None:

    print('{:0.1f}x²'.format(a))

    if b == 1:
        print("+x")
    else:
        if b > 0.0:
            print("+{:0.1f}x".format(b))
        elif b < 0.0:
            print("{:0.1f}x".format(b))

    if c > 0.0:
        print("+{:0.1f}".format(c))
    elif c < 0.0:
        print("{:0.1f}".format(c))

    print(" = 0\n")


def format_pow1(c: float, d: float, alpha: float) -> None:

    if c == 1.0:
        print("(x")

    else:
        print("({:0.1f}x".format(c))

    if d < 0.0:
        tmp: float = fabs(d)
        print("+{:0.1f})^{:0.1f}\n".format(tmp, alpha))

    else:
        print("-{:0.1f})^{:0.1f}\n".format(d, alpha))


def format_pow2(c: float) -> None:

    print("f(x) = 1/")

    if c == 0.0:
        print("x\n")

    else:
        if c < 0.0:
            tmp: float = fabs(c)
            print("(x+{:0.1f})\n".format(tmp))

        else:
            print("(x-{:0.1f})\n".format(c))


def format_trigo1(c: float):

    print("f(x) = cos(")

    if c == 1:
        print("x)\n")

    elif c == -1:
        print("-x)\n")

    else:
        print("{:0.1f}x)\n".format(c))


def format_trigo2(c: float):

    print("f(x) = sin(")

    if c == 1:
        print("x)\n")

    elif c == -1:
        print("-x)\n")

    else:
        print("{:0.1f}x)\n".format(c))


def format_trigo3(c: float):

    print("f(x) = tan(")

    if c == 1:
        print("x)")

    elif c == -1:
        print("-x)")

    else:
        print("{:0.1f}x)\n".format(c))


def format_log(c: float):

    print("f(x) = ln(")

    if c == 1:
        print("x)\n")

    elif c == -1:
        print("-x)\n")

    else:
        print("{:0.1f}x)\n".format(c))