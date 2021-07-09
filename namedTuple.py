from collections import namedtuple

Point = namedtuple('Point', ['x','y'])

pt1 = Point(1, 3)

print(pt1.x)
print(pt1.y)