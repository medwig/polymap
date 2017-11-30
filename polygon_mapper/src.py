import json
from numbers import Number

BASE_URL = "https://www.keene.edu/campus/maps/tool/?coordinates="

def parse_coords(coords):
    coords = json.loads(coords)
    if not isinstance(coords[0][0], Number):
        raise TypeError('Input coordinates must be a list of integer lon/lats')
    return coords


def poly2url(polygon):
    query_string = ''
    for point in polygon:
        query_string += '%2C%20'.join(map(str, reversed(point))) + '%0A'
    query_string.rstrip('%0A')
    return BASE_URL + query_string
 

def get_url(coords):
    polygon = parse_coords(coords)
    url = poly2url(polygon)
    return url 

