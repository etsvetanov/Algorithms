from math import sqrt

from collections import Counter
from math import sqrt


def get_divisors(n: int):
    divisors = set()

    # go from 1 to sqrt(n) checking for a divisor and its reciprocal
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    return divisors


def solution(A):
    # write your code in Python 3.6
    N = len(A)
    count_by_number = Counter(A)

    non_divisors_count = [N] * N

    divisors_by_number = {}

    for i, n in enumerate(A):
        divisors = None
        if n in divisors_by_number:
            divisors = divisors_by_number[n]
        else:
            divisors = divisors_by_number[n] = get_divisors(n)

        for d in divisors:
            if d in count_by_number:
                non_divisors_count[i] -= count_by_number[d]

    return non_divisors_count


print(solution([2]))
