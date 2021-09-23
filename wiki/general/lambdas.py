from typing import Callable

square_function: Callable[[int], int] = lambda number: number * number
sum_function: Callable[[int, int], int] = lambda number1, number2: number1 + number2
is_even_function: Callable[[int], bool] = lambda number: number % 2 == 0

print(sum_function(3, 10))

"""
TODO: Try to define the functions as a part of the TODOs in the recursion.py file as lambda functions.
"""
