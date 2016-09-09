"""
Script uses data downloaded from The World Book to graph the number of
Scientific and technical journal articles published during 2013 onto a world
map. This version uses the CSV package and loops over the data storing the
certain feilds in a dictionary.

CSV file downloaded from:
http://data.worldbank.org/indicator/IP.JRN.ARTC.SC

Author: Sierra Gregg
Date: September 2016
"""

# Import required moduals
import pygal
import csv
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS
from convert_country_codes import get_country_code

# CSV file where data is stored
JOURNAL_PUP = 'scientific_and_technical_journal_articles.csv'

# Try to open the file, if error occurs print message
try:
    with open(JOURNAL_PUP) as jp:

        # Use csv.DictReader to parse file. This will allow us to access the
        # values with their header names instead of using numeric indexes.
        reader = csv.DictReader(jp)

        # Loop over each row in the CSV file and store the required information
        # in a dictionary
        publication_numbers = {}
        for row in reader:

            # Pygal requires countries to use their country codes.
            # The get_country_code function converts the country name to the
            # corresponding Pygal code.
            code = get_country_code(row['\ufeff"Country Name"'])

            # Only store information in the dictionary when we have a
            # country code and a publication number.
            if code and row['2013']:
                publication_numbers[code] = int(float(row['2013']))

        # To improve the legibility of the graphic, we divide the data indicator
        # levels, this means we can apply a different color to each level.
        pubs_low, pubs_med, pubs_high = {}, {}, {}
        for cc, pub in publication_numbers.items():
            if pub < 100:
                pubs_low[cc] = pub
            elif pub < 1000:
                pubs_med[cc] = pub
            else:
                pubs_high[cc] = pub

        # Setup the Pygal map
        wm = World(style=LG)
        wm.force_uri_protocol = 'http'
        wm.title = 'Publication of Scientific and Technical Journal\nArticles in 2013, by Country\nData from: The World Bank'
        wm.add('0-100', pubs_low)
        wm.add('100-1,000', pubs_med)
        wm.add('> 1,000', pubs_high)

        wm.render_to_file('world_journal_publication.svg')

except IOError as e:
    print('Operation failed: %s' % e.strerror)
