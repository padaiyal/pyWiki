# Generator - Used for lazy evaluation. Much more efficient memory wise.
import collections


def even_numbers() -> collections.Iterable:
    number = 1
    while True:
        if number % 2 == 0:
            yield number
        number += 1


# Be careful! Infinite loop detected.
for even_number in even_numbers():
    print(even_number)