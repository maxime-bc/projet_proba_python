def int_input() -> int:

    while True:
        value = input()

        try:
            my_int = int(value)
            return my_int

        except ValueError:
            print('Enter an integer to continue.\n')


def float_input(fail_message: str = None):

    value = input()

    try:
        my_float = float(value)
        return my_float

    except ValueError:

        if fail_message is not None:
            print(fail_message)





