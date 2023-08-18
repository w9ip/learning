from collections import namedtuple
from operator import attrgetter
from exmp_7_13 import metro_data

Latlon = namedtuple('Latlon', 'lat lon')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [
    Metropolis(name, cc, pop, Latlon(lat, lon))
    for name, cc, pop, (lat, lon) in metro_data
]

if __name__ == '__main__':
    print(metro_areas[0])
    print(metro_areas[0].coord.lat)
    name_lat = attrgetter('name', 'coord.lat')
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        print(name_lat(city))
