import math
from collections import namedtuple

Point = namedtuple('Point', 'x y')

def dist(p1, p2):
    return  math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def main():
    p1 = Point(2, 4)
    p2 = Point(3, 5)
    print(dist(p1, p2) == math.sqrt((2 - 3)**2 + (4- 5)**2))


if __name__ == '__main__':
    main()