"""
sirve para hacer tuples pero se le puede dar nombres a los campos
ejemplo: 
"""

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.424, 139.23494))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])