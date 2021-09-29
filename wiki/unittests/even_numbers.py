from collections import Iterable


def is_even_number(number: int) -> bool:
    if number is None:
        raise AttributeError("Input number cannot be None!")
    if type(number) != int:
        raise AttributeError("Input has to be a number!")
    return number % 2 == 0


def get_even_numbers_generator(upper_limit: int) -> Iterable:

    if upper_limit is None:
        raise AttributeError("Upper limit number cannot be None!")
    if type(upper_limit) != int:
        raise AttributeError("Upper limit number has to be a number!")

    number: int = 0
    while number < upper_limit:
        if is_even_number(number):
            yield number
        number += 1
    return
