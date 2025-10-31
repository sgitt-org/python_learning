#!/usr/bin/env python3


def print_message(message):
    """Just prints a message
    :param message:
    :return:
    """
    print(message)


print_message("Hi!!!")

NAME_CONST = "John"
print_message(NAME_CONST)

print(print_message.__doc__)  # print docstring
help(print_message)
