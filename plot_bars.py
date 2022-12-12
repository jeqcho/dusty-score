import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime

from matplotlib import pyplot as plt


def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    """Draws a bar plot with multiple bars per data point.

    Parameters
    ----------
    ax : matplotlib.pyplot.axis
        The axis we want to draw our plot on.

    data: dictionary
        A dictionary containing the data we want to plot. Keys are the names of the
        data, the items is a list of the values.

        Example:
        data = {
            "x":[1,2,3],
            "y":[1,2,3],
            "z":[1,2,3],
        }

    colors : array-like, optional
        A list of colors which are used for the bars. If None, the colors
        will be the standard matplotlib color cyle. (default: None)

    total_width : float, optional, default: 0.8
        The width of a bar group. 0.8 means that 80% of the x-axis is covered
        by bars and 20% will be spaces between the bars.

    single_width: float, optional, default: 1
        The relative width of a single bar within a group. 1 means the bars
        will touch eachother within a group, values less than 1 will make
        these bars thinner.

    legend: bool, optional, default: True
        If this is set to true, a legend will be added to the axis.
    """

    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    # Draw legend if we need
    if legend:
        ax.legend(bars, data.keys())


if __name__ == "__main__":
    with open('dusty_score-7095.txt', 'r') as f:
        scores_7000 = [int(line.strip()) for line in f.readlines()]
    
    with open('dusty_score.txt', 'r') as f:
        scores_real = [int(line.strip()) for line in f.readlines()]

    with open('dusty_score-1.txt', 'r') as f:
        scores_1000 = [int(line.strip()) for line in f.readlines()]

    y = [0, 0, 0, 0]
    z = [0, 0, 0, 0]
    k = [0, 0, 0, 0]

    for score in scores_1000:
        y[score] += 1

    for score in scores_7000:
        z[score] += 1
    
    for score in scores_real:
        k[score] += 1
    
    y.pop(0)
    z.pop(0)
    k.pop(0)
    # Usage example:
    data = {
        "1000": [x/1000 for x in y],
        "7095": [x/7095 for x in z],
        "Fall 2022": [x / len(scores_real) for x in k]
    }

    fig, ax = plt.subplots()
    plt.xticks(range(3), [1, 2, 3])
    bar_plot(ax, data, total_width=.8, single_width=.9)
    plt.show()