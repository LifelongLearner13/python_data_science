"""
Class to generate a random walk

Author: Sierra Gregg
Date: September 2016
"""

import numpy as np
from random import choice

# Sytax is compatibable with Python 2 and Python 3
# New style class
class RandomWalk(object):
    # Constructor
    def __init__(self, num_points=5000):
        """Constructor. Default number of points is 5,000"""

        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction.
            # A positive result on the x-axis means move right, a negative means
            # move left. A positive result on the y-axis means move up, a
            # negative result means move down.
            x_step = self._getStep()
            y_step = self._getStep()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


    def _getStep(self):
        """Calculate a step"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance
