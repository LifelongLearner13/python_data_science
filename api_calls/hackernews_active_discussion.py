"""
Uses Pygal to graph the current top 30 most popular posts on HackerNews

Uses the `//topstories.json` and `/item/{item-id}` endpoints of
the HackerNews API: https://github.com/HackerNews/API

Code adapted from examples in Chapter 17 of Python Crash Course by Eric Matthes

Author: Sierra Gregg
Date: September 2016
"""

import requests
from operator import itemgetter
import pygal
from pygal.style import DarkStyle

# Send HTTP GET request to HackerNews
url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
hn_request = requests.get(url)
print("Status code:", hn_request.status_code)

# Loop through submission_ids, so we can request information about
# each submission.
submission_ids = hn_request.json()
plot_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json?print=pretty')
    submission_request = requests.get(url)
    print(submission_request.status_code)
    response_dict = submission_request.json()

    # Formate the information so it can be displayed in the Pygal Bar graph
    submission_dict = {
        # Number of comments; zero if none, exists
        'value': response_dict.get('descendants', 0),
        # Displayed when hovering over bar
        'label': response_dict['title'],
        # When clicked each bar will open a new window containing the
        # corresponding submission
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        }

    plot_dicts.append(submission_dict)

# Sort the data by number of comments. Use itemgetter to sort by a nested value.
plot_dicts = sorted(plot_dicts, key=itemgetter('value'),
                            reverse=True)

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
chart.title = 'Top 30 Currently Most Active HackerNews Submissions'
chart.add('Number of Comments', plot_dicts)
chart.render_to_file('post_popularity.svg')
