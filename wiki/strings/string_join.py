from functools import reduce

from wiki.utils import graph
from wiki.utils.time_it import time_it_in_milliseconds


@time_it_in_milliseconds
def concatenate_with_plus_operator(strings: list) -> str:
    return reduce(lambda x, y : x + y, strings, "")


@time_it_in_milliseconds
def concatenate_with_join(strings: list) -> str:
    return "".join(strings)


if __name__ == '__main__':
    n_values = list()
    strings_concat_with_plus_operator_durations_list = list()
    strings_concat_with_join_durations_list = list()
    for n in range(1, 1000, 20):
        n_values.append(n)
        strings_generator = (str(number) for number in range(n))
        strings_concat_with_plus_operator_durations_list.append(
            '{0:.2f}'.format(concatenate_with_plus_operator(strings_generator))
        )
        strings_concat_with_join_durations_list.append(
            '{0:.2f}'.format(concatenate_with_join(strings_generator))
        )

    graph_info = {
        'title': 'Time taken to join strings via + vs join().',
        'x': {
            'values': n_values,
            'label': 'Number of strings (n)'
        },
        'y': [
            {
                'values': strings_concat_with_plus_operator_durations_list,
                'title': "Using +",
                'label': "Duration (milliseconds)",
            },
            {
                'values': strings_concat_with_join_durations_list,
                'title': "Using join()",
                'label': "Duration (milliseconds)",
            }
        ]
    }
    graph.plot_on_same_line_graph(graph_info)
