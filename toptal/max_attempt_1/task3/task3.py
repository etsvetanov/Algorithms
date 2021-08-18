from heapq import heapify, heappop, heappush
from typing import List
from random import randint

def solution(a: List[int]):
    l = a.copy()
    heapify(l)

    cost = 0
    while len(l) > 1:
        a = heappop(l)
        b = heappop(l)

        res = a + b
        cost += res

        heappush(l, res)

    print(f'> cost {cost}')
    return cost




# def solution_sort_each_time(numbers: List):
#     numbers.sort()
#     total = 0
#
#     while True:
#         numbers = [numbers[0] + numbers[1], *numbers[2:]]
#         total += numbers[0]
#
#         numbers.sort()
#
#         if len(numbers) == 1:
#             break
#
#     return total
#
# def solution_min1_min2(numbers: List):


# test_cases = [
#     {
#         'input': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
#         'anwser'
#     }
# ]
#
# def run_tests():
#     for test in test:


tests = [
    ([65, 44, 1, 3, 21], 232),
    ([47, 63, 99, 1, 92], 652)
]

for test in tests:
    print(f'test: {test}')
    assert solution(test[0]) == test[1]