from wiki.time_it import time_it
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


@time_it
def square_numbers_using_for_loop(numbers: list) -> list:
    squared_numbers = list()
    for number in numbers:
        squared_numbers.append(number * number)
    return squared_numbers


@time_it
def square_numbers_using_list_comprehension(numbers: list) -> list:
    return [number * number for number in numbers]


def generate_a_list_of_numbers(n):
    # Generate a list of numbers
    numbers = list()
    for number in range(n):
        numbers.append(number)
    return numbers


if __name__ == "__main__":
    print("Size of input, for loop duration (ms), list comprehension duration (ms)")
    n_values = list()
    for_loop_duration_in_ms = list()
    list_comprehension_duration_in_ms = list()
    for n in range(0, 100000, 1000):
        numbers = generate_a_list_of_numbers(n)

        n_values.append(n)
        for_loop_duration_in_ms.append(
            '{0:.2f}'.format(square_numbers_using_for_loop(numbers))
        )
        list_comprehension_duration_in_ms.append(
            '{0:.2f}'.format(square_numbers_using_list_comprehension(numbers))
        )

    fig, axes = plt.subplots(1, 1)
    axes.set_title('"for loop" vs "list comprehension" for squaring n numbers')
    axes.plot(n_values, for_loop_duration_in_ms, label='Using for loop')
    axes.plot(n_values, list_comprehension_duration_in_ms, label='Using list comprehension')
    axes.set_ylabel('Duration (ms)')
    axes.set_xlabel('Size of input (n)')
    axes.legend()
    axes.yaxis.set_major_locator(MaxNLocator(5))
    plt.show()
