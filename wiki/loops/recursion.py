"""
5! = 5 * 4 * 3 * 2 * 1
"""


def factorial(n: int) -> int:
    if n < 0:
        raise AttributeError(f"Cannot compute factorial of a negative number - {n}")

    # Iterative method - Using loops
    # result = 1
    # for number in range(1, n + 1):
    #     result = result * number
    # return result

    # Recursion/Recursive method - Be careful with overflowing the stack.
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Tail recursion
def factorial_using_tail_recursion(n: int, accumulator: int = 1):
    if n < 0:
        raise AttributeError(f"Cannot compute factorial of a negative number - {n}")
    if n <= 1:
        return accumulator
    return factorial_using_tail_recursion(n - 1, n * accumulator)


""" 
    TODO: Try the above approaches for finding:
     1. The sum on n numbers.
     2. The value of pi - https://en.wikipedia.org/wiki/Leibniz_formula_for_π.
"""