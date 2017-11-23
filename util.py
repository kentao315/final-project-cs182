import csv
from math import sin, cos, sqrt, atan2, radians

def euclideanDistance((x1, y1), (x2, y2)):
    """
    Given two latitude/longitude coordinates, in degrees, returns euclidean distance (in miles)
    """
    radius = 3959
    lat1 = radians(x1)
    long1 = radians(y1)
    lat2 = radians(x2)
    long2 = radians(y2)

    distanceLon = long2 - long1
    distanceLat = lat2 - lat1

    a = sin(distanceLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(distanceLon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = radius * c
    return distance

def tempData(file):
    """
    Temporary function to clean the test addresses, returns list of latitude longitude pairs
    """
    f = open(file, "rU")
    reader = csv.reader(f, dialect=csv.excel_tab, delimiter=",")
    locations = []
    for row in reader:
        locations.extend(row)
    return locations

def cleanData(coordinates):
    addresses = []
    for i in range(0, len(coordinates)-1):
        addresses.append((coordinates[i], coordinates[i+1]))
    return addresses



