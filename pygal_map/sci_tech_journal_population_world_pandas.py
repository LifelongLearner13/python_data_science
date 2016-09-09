"""
Script uses data downloaded from The World Book to graph the number of
Scientific and technical journal articles published during 2013 onto a world
map. This version uses Pandas Dataframe to store and manipulate the data.

CSV file downloaded from:
http://data.worldbank.org/indicator/IP.JRN.ARTC.SC

Author: Sierra Gregg
Date: September 2016
"""

# Import required moduals
import pygal
import csv
import pandas as pd
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal.style import LightGreenStyle as LG
from convert_country_codes import get_country_code

# CSV file where data is stored
JOURNAL_PUP = 'scientific_and_technical_journal_articles.csv'

# Load and convert CSV to Pandas Dataframe
dataframe = pd.read_csv(JOURNAL_PUP)

# Select two columns and remove any rows containing NAN values
dataframe = dataframe[['\ufeff"Country Name"', '2013']].dropna()

# Convert country names to Pygals country codes
dataframe['\ufeff"Country Name"'] = dataframe['\ufeff"Country Name"'].map(get_country_code)
dataframe = dataframe[dataframe['\ufeff"Country Name"'].notnull()]

# Divide the dataframe into groups
pubs_low = dataframe[dataframe['2013'] < 100]
pubs_med = dataframe[(dataframe['2013'] >= 100) & (dataframe['2013'] < 1000)]
pubs_high = dataframe[dataframe['2013'] >= 1000]

# Convert Dataframes back to dictionaries, because Pygal expects data to be
# in a dictionary.
pubs_low = dict(zip(pubs_low['\ufeff"Country Name"'], pubs_low['2013']))
pubs_med = dict(zip(pubs_med['\ufeff"Country Name"'], pubs_med['2013']))
pubs_high = dict(zip(pubs_high['\ufeff"Country Name"'], pubs_high['2013']))

# Setup the Pygal map
wm = World(style=LCS)
wm.force_uri_protocol = 'http'
wm.title = 'Publication of Scientific and Technical Journal\nArticles in 2013, by Country\nData from: The World Bank'
wm.add('0-100', pubs_low)
wm.add('100-1,000', pubs_med)
wm.add('> 1,000', pubs_high)

wm.render_to_file('world_journal_publication_pd.svg')
