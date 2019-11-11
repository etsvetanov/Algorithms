import random
from typing import Optional


# https://www.interviewcake.com/question/python/two-egg-problem

class Building:
    def __init__(self, breaking_floor: Optional[int] = random.randint(1, 100)):
        self.breaking_floor: int = breaking_floor

    def is_it_breaking(self, floor: int) -> bool:
        return self.breaking_floor <= floor


def highest_floor(building: Building) -> (int, int):
    tries = 0
    floor = 14
    skip_floors = 14
    last_safe_floor = 1
    eggs = 2

    # first egg
    while True:
        print('trying floor:', floor)
        tries += 1
        if build.is_it_breaking(floor):
            eggs -= 1
            break
        last_safe_floor = floor
        skip_floors -= 1
        floor += skip_floors

        if floor > 100:
            floor = 100

    if eggs == 2:
        return tries

    print('second egg')

    print('last_safe_floor', last_safe_floor)

    # second egg
    for i in range(last_safe_floor + 1, floor):
        tries += 1
        print('trying floor:', i)
        if building.is_it_breaking(i):
            break
        last_safe_floor = i

    return tries, last_safe_floor


build = Building()
print('breaking_floor:', build.breaking_floor)
tries, safe_floor = highest_floor(building=build)
print('tries:', tries, 'safe_floor:', safe_floor)
# https://www.interviewcake.com/question/python/shuffle
# https://www.interviewcake.com/question/python/simulate-5-sided-die
# https://www.interviewcake.com/question/python/balanced-binary-tree
