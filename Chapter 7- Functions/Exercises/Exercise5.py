# Cities
def describe_city(city, country='US'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('California')
describe_city('reykjavik', 'iceland')
describe_city('Boston')