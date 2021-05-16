from wiki.utils import graph
from wiki.utils.time_it import time_it_in_milliseconds


@time_it_in_milliseconds
def contains_using_for_loop(numbers: list, number_to_check: int) -> bool:
    for number in numbers:
        if number == number_to_check:
            return True
    return False


@time_it_in_milliseconds
def contains_using_in(numbers: list, number_to_check: int) -> bool:
    return number_to_check in numbers


if __name__ == '__main__':
    n_values = list()
    contains_using_for_loop_duration_for_match_as_milliseconds = list()
    contains_using_for_loop_duration_for_no_match_as_milliseconds = list()
    contains_using_in_for_match_as_milliseconds = list()
    contains_using_in_for_no_match_as_milliseconds = list()

    for n in range(0, 1000000, 10000):
        numbers = [number for number in range(n)]

        n_values.append(n)
        contains_using_for_loop_duration_for_match_as_milliseconds.append(
            '{0:.2E}'.format(contains_using_for_loop(numbers, 100))
        )
        contains_using_for_loop_duration_for_no_match_as_milliseconds.append(
            '{0:.2E}'.format(contains_using_in(numbers, 101))
        )
        contains_using_in_for_match_as_milliseconds.append(
            '{0:.2E}'.format(contains_using_in(numbers, 100))
        )
        contains_using_in_for_no_match_as_milliseconds.append(
            '{0:.2E}'.format(contains_using_in(numbers, 101))
        )

    graph_info = {
        'title': '"for loop" vs "in keyword" for checking if an element is in a list',
        'x': {
            'values': n_values,
            'label': 'Size of input (n)'
        },
        'y': [
            {
                'values': contains_using_in_for_match_as_milliseconds,
                'title': "Match found using 'in'",
                'label': "Duration (ms)",
            },
            {
                'values': contains_using_in_for_no_match_as_milliseconds,
                'title': "No match found using 'in'",
                'label': "Duration (ms)",
            },
            {
                'values': contains_using_for_loop_duration_for_match_as_milliseconds,
                'title': "Match found using for loop",
                'label': "Duration (ms)",
            },
            {
                'values': contains_using_for_loop_duration_for_no_match_as_milliseconds,
                'title': "No match found using for loop",
                'label': "Duration (ms)",
            },

        ]
    }

    graph.plot_on_same_line_graph(graph_info)
