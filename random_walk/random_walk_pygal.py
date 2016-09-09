"""
Uses Pygal to graph a random walk

Based on the Random Walk Theory: events are determined by random movements.
Examples/Aplications:
 * Drunken walking
 * Modeling of animals, micro-organisms and cells
 * Stock prediction

Author: Sierra Gregg
Date: September 2016
"""

import pygal
from pygal.style import Style
from random_walk_naive import RandomWalk

# Make a random walk, and calculate the points.
rw = RandomWalk(10000)
rw.fill_walk()

custom_style = Style(
  background='transparent',
  plot_background='transparent',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in',
  colors=('#E853A0', '#228b22', '#8b0000'))

# Create a scatter plot with no additional content
rw_chart = pygal.XY( show_legend=False, show_x_labels=False,
    show_y_labels=False, style=custom_style)
rw_chart.title = 'Random Walk'
xy_pairs = list(zip(rw.x_values, rw.y_values))
rw_chart.add('', xy_pairs)
rw_chart.add('', [(rw.x_values[0], rw.y_values[0])])
rw_chart.add('', [(rw.x_values[-1], rw.y_values[-1])])

rw_chart.render_to_file('rw_pygal.svg') # Save to file
