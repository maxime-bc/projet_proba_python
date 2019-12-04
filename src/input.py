def int_input(loop: bool = True) -> int:

    test: bool = True

    while test:
        value = input()

        try:
            my_int = int(value)
            return my_int

        except ValueError:

            if loop:
                pass

            else:
                test = False


def float_input(fail_message: str = None):

    value = input()

    try:
        my_float = float(value)
        return my_float

    except ValueError:

        if fail_message is not None:
            print(fail_message)





