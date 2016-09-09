from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Returns the Pygal 2-digit country code for the
        given country name."""

    # loops through the COUNTRIES dictionary
    for code, name in COUNTRIES.items():

        # If the name stored as a value in the COUNTRIES dictionary is
        # a substring of the user provided country name or the user provided
        # country name is a substring of the current country name, return
        # pygal's country code.
        if name in country_name or country_name in name:
            return code

    # If the country wasn't found, return None.
    return None
