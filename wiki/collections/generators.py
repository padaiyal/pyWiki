import sys
from wiki.utils import graph

if __name__ == '__main__':
    n_values = list()
    numbers_lists_size = list()
    numbers_generators_size = list()
    for n in range(1, 1000, 20):
        numbers_list = [number for number in range(n)]
        numbers_generator = (number for number in range(n))

        n_values.append(n)
        numbers_lists_size.append(sys.getsizeof(numbers_list))
        numbers_generators_size.append(sys.getsizeof(numbers_generator))

    graph_info = {
        'title': 'Size occupied by lists vs generators of n values.',
        'x': {
            'values': n_values,
            'label': 'Number of values (n)'
        },
        'y': [
            {
                'values': numbers_lists_size,
                'title': "Using a list",
                'label': "Size (bytes)",
            },
            {
                'values': numbers_generators_size,
                'title': "Using a generator",
                'label': "Size (bytes)",
            }
        ]
    }
    graph.plot_on_same_line_graph(graph_info)
