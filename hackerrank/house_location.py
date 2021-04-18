import math
from typing import List

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p: 'Point'):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: 'Point'):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, c: float):
        return Point(self.x * c, self.y * c)

    def __truediv__(self, c: float):
        return Point(self.x / c, self.y / c)

    def __lt__(self, p: 'Point'):
        return self.x < p.x or (self.x == p.x and self.y < self.y)


def dot(p: Point, q: Point) -> float:
    return p.x * q.x + p.y * q.y


def dist2(p: Point, q: Point) -> float:
    return dot(p - q, p - q)


def rotate_ccw_90(p: Point) -> Point:
    return Point(-p.y, p.x)


def rotate_cw_90(p: Point) -> Point:
    return Point(p.y, -p.x)



def circleCircleIntersection(a: Point, b: Point, r: float, R: float) -> List[Point]:
    d = math.sqrt(dist2(a, b))

    ret = []

    return ret