import math
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, p: 'Point'):
        d_pow_2 = (self.x - p.x)**2 + (self.y - p.x)**2

        return math.sqrt(d_pow_2)

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



def rotate_ccw_90(p: Point) -> Point:
    return Point(-p.y, p.x)


def rotate_cw_90(p: Point) -> Point:
    return Point(p.y, -p.x)


def circleCircleIntersection(a: Point, b: Point, r: float, R: float) -> List[Point]:
    d = a.dist_to(b)


    ret = []

    return ret

def read_number_pair():
    return map(lambda s: int(s), input().split())

def main():
    a, b = read_number_pair()
    kim_x, kim_y = read_number_pair()
    bob_x, bob_y = read_number_pair()
    jck_x, jck_y = read_number_pair()
    jan_x, jan_y = read_number_pair()




if __name__ == "__main__":
    main()
