# Generator - Used for lazy evaluation. Much more efficient memory wise.
import collections

# List comprehensions generate it instantly so it can end up occupying a lot of memory.
# even_numbers = [number for number in range(0, 100_000) if number % 2 == 0]
# print(even_numbers)


def even_numbers() -> collections.Iterable:
    number = 0
    while True:
        yield number
        number += 2

# Be careful! Infinite loop detected.
# for even_number in even_numbers():
#     print(even_number)


def even_numbers_lesser_than(upper_limit: int) -> collections.Iterable:
    number = 0
    while number < upper_limit:
        yield number
        number += 2


for even_number in even_numbers_lesser_than(100_000):
    print(even_number)

# Same behaviour as the even_numbers_lesser_than() function.
even_numbers_in_generator_comprehension = (number for number in range(0, 100_000) if number % 2 == 0)
print(even_numbers_in_generator_comprehension)
for even_number in even_numbers_in_generator_comprehension:
    print(even_number)

# TODO: A generator (Using function and comprehension) to generate the fibonacci sequence.
