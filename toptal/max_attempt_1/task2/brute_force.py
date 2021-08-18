from typing import List
from math import sqrt
from itertools import zip_longest

def get_dist_from_centre(x: int, y: int):
    return sqrt(x ** 2 + y ** 2)


def solution(s: str, x: List[int], y: List[int]) -> int:
    data = [[t, get_dist_from_centre(xx, yy)] for t, xx, yy in zip(s, x, y)]

    data.sort(key=lambda item: item[0])  # sort by tag first
    data.sort(key=lambda item: item[1])  # and then by distance, so items will be sorted by distance and then by tag

    count = 0
    included_tags = set()

    for (tag, dist), (nxt_tag, nxt_dist) in zip_longest(data, data[1:], fillvalue=(None, None)):
        # we need to check if we are not including a pt that shares the same circle and tag with another pt
        # and pts are sorted by distance and then by tag so points with same distance and tag should be next to
        # each other
        if tag in included_tags or (nxt_dist and tag == nxt_tag and dist == nxt_dist):
            break

        count += 1
        included_tags.add(tag)

    print(f'> count: {count}')
    return count



tests = [
    [("ABDCA", [2, -1, -4, -3, 3], [2, -2, 4, 1, -3]), 3],
    [("ABB", [1, -2, -2], [1, -2, 2]), 1],
    [("CCD", [1, -1, 2], [1, -1, -2]), 0],
    [("ABDCAAD", [2, -2, -2, -1, 2, -2, 1], [2, 2, -4, 1, -2, -2, 0]), 2]
]


for args, expected in tests:
    assert solution(*args) == expected

