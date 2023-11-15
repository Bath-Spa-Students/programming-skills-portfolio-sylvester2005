#Describe a city
def describe_city(city, country='india'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('delhi')
describe_city('cape town', 'south africa')
describe_city('dublin',"ireland")