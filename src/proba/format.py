from math import fabs


def format_quadratic_equation(a: float, b: float, c: float) -> str:

    formatted_equation: str = 'f(x) = {:0.1f}x²'.format(a)

    if b == 1:
        formatted_equation += '+x'
    else:
        if b > 0.0:
            formatted_equation += '+{:0.1f}x'.format(b)
        elif b < 0.0:
            formatted_equation += '{:0.1f}x'.format(b)

    if c > 0.0:
        formatted_equation += '+{:0.1f}'.format(c)
    elif c < 0.0:
        formatted_equation += '{:0.1f}'.format(c)

    return formatted_equation


def format_pow(c: float, d: float, alpha: float) -> str:

    formatted_equation: str = ''

    if c == 1.0:
        formatted_equation += 'f(x) = (x'

    else:
        formatted_equation += 'f(x) = ({:0.1f}x'.format(c)

    if d < 0.0:
        tmp: float = fabs(d)
        formatted_equation += '+{:0.1f})^{:0.1f}\n'.format(tmp, alpha)

    else:
        formatted_equation += '-{:0.1f})^{:0.1f}\n'.format(d, alpha)

    return formatted_equation


def format_inverse(c: float) -> str:

    formatted_equation: str = 'f(x) = 1/'

    if c == 0.0:
        formatted_equation += 'x\n'

    else:
        if c < 0.0:
            tmp: float = fabs(c)
            formatted_equation += '(x+{:0.1f})\n'.format(tmp)

        else:
            formatted_equation += '(x-{:0.1f})\n'.format(c)

    return formatted_equation


def format_cos(c: float) -> str:

    formatted_equation: str = 'f(x) = cos('

    if c == 1:
        formatted_equation += 'x)\n'
        
    elif c == -1:
        formatted_equation += '-x)\n'

    else:
        formatted_equation += '{:0.1f}x)\n'.format(c)
    
    return formatted_equation


def format_sin(c: float) -> str:

    formatted_equation: str = 'f(x) = sin('

    if c == 1:
        formatted_equation += 'x)\n'

    elif c == -1:
        formatted_equation += '-x)\n'

    else:
        formatted_equation += '{:0.1f}x)\n'.format(c)

    return formatted_equation


def format_tan(c: float) -> str:

    formatted_equation: str = 'f(x) = tan('

    if c == 1:
        formatted_equation += 'x)'

    elif c == -1:
        formatted_equation += '-x)'

    else:
        formatted_equation += '{:0.1f}x)\n'.format(c)

    return formatted_equation


def format_log(c: float) -> str:

    formatted_equation: str = 'f(x) = ln('

    if c == 1:
        formatted_equation += 'x)\n'

    elif c == -1:
        formatted_equation += '-x)\n'

    else:
        formatted_equation += '{:0.1f}x)\n'.format(c)

    return formatted_equation
