import collections
from collections import namedtuple

Point = namedtuple('Point', ['red', 'green', 'blue'])
newP = Point(55, 155, 255)

print(newP.red)
