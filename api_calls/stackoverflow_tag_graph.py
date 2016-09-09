"""
Uses Pygal to graph the top 30 tags on Stackoverflow from January 1, 2016 -
September 9, 2016.

Uses the `/tags` endpoint of the Stackoverflow API:
https://api.stackexchange.com/docs/tags

Code adapted from examples in Chapter 17 of Python Crash Course by Eric Matthes

Author: Sierra Gregg
Date: September 2016
"""

import requests
import pygal
from pygal.style import DarkStyle

# Send HTTP GET request to Stackoverflow API
URL = 'https://api.stackexchange.com/2.2/tags?pagesize=30&fromdate=1451606400&todate=1473379200&order=desc&sort=popular&site=stackoverflow'
sf_response = requests.get(URL)

# Store tag information in a dictionary
tag_dicts = sf_response.json()['items']

# Loop through tags to retrieve their name and count
tags, popularity = [], []
for tag_dict in tag_dicts:
    tags.append(tag_dict['name'])
    popularity.append(tag_dict['count'])


# Congigure the chart
chart_config = pygal.Config()
chart_config.legend_at_bottom = True
chart_config.x_label_rotation = 45
chart_config.title_font_size = 24
chart_config.label_font_size = 14
chart_config.major_label_font_size = 18
chart_config.truncate_label = 15
chart_config.show_y_guides = False

# Create chart and save to file
chart = pygal.Bar(chart_config, style=DarkStyle)
chart.title = 'Top 30 Tags on stackoverflow\nin 2016, So Far'
chart.x_labels = tags
chart.add('Number of Question', popularity)
chart.render_to_file('tag_popularity.svg')
