from functools import lru_cache

from wiki.utils.time_it import time_it_in_milliseconds
from wiki.utils import graph


@time_it_in_milliseconds
def fibonacci_series_with_no_cache(n) -> int:
    if n < 2:
        return n
    return fibonacci_series_with_no_cache(n - 1) + fibonacci_series_with_no_cache(n - 2)


@lru_cache(maxsize=128)
@time_it_in_milliseconds
def fibonacci_series_with_lru_cache(n) -> int:
    if n < 2:
        return n
    return fibonacci_series_with_lru_cache(n - 1) + fibonacci_series_with_lru_cache(n - 2)


if __name__ == '__main__':
    n_values = list()
    fibonacci_series_with_no_cache_duration_in_ms = list()
    fibonacci_series_with_lru_cache_duration_in_ms = list()
    for n in range(1, 30, 1):
        n_values.append(n)
        fibonacci_series_with_no_cache_duration_in_ms.append(
            '{0:.2f}'.format(fibonacci_series_with_no_cache(n))
        )
        fibonacci_series_with_lru_cache_duration_in_ms.append(
            '{0:.2f}'.format(fibonacci_series_with_lru_cache(n))
        )

    graph_info = {
        'title': 'Fibonacci series with and without LRU cache.',
        'x': {
            'values': n_values,
            'label': 'Number of terms to sum (n)'
        },
        'y': [
            {
                'values': fibonacci_series_with_no_cache_duration_in_ms,
                'title': "Without any cache",
                'label': "Duration (ms)",
            },
            {
                'values': fibonacci_series_with_lru_cache_duration_in_ms,
                'title': "With an LRU cache",
                'label': "Duration (ms)",
            }
        ]
    }
    graph.plot_on_same_line_graph(graph_info)
