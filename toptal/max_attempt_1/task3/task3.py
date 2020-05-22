from typing import List


def solution_sort_each_time(numbers: List):
    numbers.sort()
    total = 0

    while True:
        numbers = [numbers[0] + numbers[1], *numbers[2:]]
        total += numbers[0]

        numbers.sort()

        if len(numbers) == 1:
            break

    return total

def solution_min1_min2(numbers: List):


# test_cases = [
#     {
#         'input': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
#         'anwser'
#     }
# ]
#
# def run_tests():
#     for test in test:


print(solution_sort_each_time([100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]))
print(solution_sort_each_time([2, 4, 6, 8]))
print(solution_sort_each_time([100, 250, 1000]))
print(solution_sort_each_time([2, 4, 5, 8]))