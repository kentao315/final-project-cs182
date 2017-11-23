import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCSe5CLAem2wVxoaFtvqsO6cxXSM7Jf9mY')

geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
geocode_result = geocode_result[0]
print geocode_result["geometry"]["location"]

