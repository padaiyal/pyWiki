import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.style.use('seaborn-whitegrid')


def plot_on_same_line_graph(graph_values: dict)-> None:
    fig, axes = plt.subplots(1, 1)
    axes.set_title(graph_values['title'])
    x_values = [float(x_value) for x_value in graph_values['x']['values']]
    for y_axis in reversed(graph_values['y']):
        y_values = [float(y_value) for y_value in y_axis['values']]
        axes.plot(x_values, y_values, label=y_axis['title'])
        axes.set_ylabel(y_axis['label'])
    axes.set_xlabel(graph_values['x']['label'])
    axes.legend()
    axes.yaxis.set_major_locator(MaxNLocator(5))
    plt.show()
