from wiki.utils import graph
from wiki.utils.time_it import time_it_in_milliseconds


@time_it_in_milliseconds
def square_numbers_using_for_loop(numbers: list) -> list:
    squared_numbers = list()
    for number in numbers:
        squared_numbers.append(number * number)
    return squared_numbers


@time_it_in_milliseconds
def square_numbers_using_list_comprehension(numbers: list) -> list:
    return [number * number for number in numbers]


@time_it_in_milliseconds
def square_numbers_using_map(numbers: list) -> list:
    return list(map(lambda number: number * number, numbers))


def generate_a_list_of_numbers(n):
    # Generate a list of numbers
    numbers = list()
    for number in range(n):
        numbers.append(number)
    return numbers


if __name__ == "__main__":
    n_values = list()
    for_loop_duration_in_ms = list()
    list_comprehension_duration_in_ms = list()
    map_duration_in_ms = list()
    for n in range(0, 1000000, 10000):
        numbers = generate_a_list_of_numbers(n)

        n_values.append(n)
        for_loop_duration_in_ms.append(
            '{0:.2E}'.format(square_numbers_using_for_loop(numbers))
        )
        list_comprehension_duration_in_ms.append(
            '{0:.2E}'.format(square_numbers_using_list_comprehension(numbers))
        )
        map_duration_in_ms.append(
            '{0:.2E}'.format(square_numbers_using_map(numbers))
        )

    graph_info = {
        'title': '"for loop" vs "list comprehension" for squaring n numbers',
        'x': {
            'values': n_values,
            'label': 'Size of input (n)'
        },
        'y': [
            {
                'values': for_loop_duration_in_ms,
                'title': "Using for loop",
                'label': "Duration (ms)",
            },
            {
                'values': list_comprehension_duration_in_ms,
                'title': "Using list comprehension",
                'label': "Duration (ms)",
            },
            {
                'values': map_duration_in_ms,
                'title': "Using map()",
                'label': "Duration (ms)",
            }
        ]
    }

    graph.plot_on_same_line_graph(graph_info)
