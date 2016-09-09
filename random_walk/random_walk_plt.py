"""
Uses Matplotlib to graph a random walk

Based on the Random Walk Theory: events are determined by random movements.
Examples/Aplications:
 * Drunken walking
 * Modeling of animals, micro-organisms and cells
 * Stock prediction

Author: Sierra Gregg
Date: September 2016
"""

import matplotlib.pyplot as plt
from random_walk_naive import RandomWalk

# Make a random walk, and calculate the points.
rw = RandomWalk(100000)
rw.fill_walk()

# Plot the points using a Scatter plot. Use a color map to emphasize
# the path from start to finish.
plt.scatter(rw.x_values, rw.y_values, c=list(range(rw.num_points)),
        cmap=plt.cm.PuRd, edgecolor='none', s=1)

# Emphasize the first and last points.
plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
        edgecolors='none', s=100)

# Remove the axes, so they do not distract from the visualization.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# Save the plot to a file
plt.savefig('rw_plt.png', bbox_inches='tight')
