from math import sqrt


def find_divisors(n):
    if n == 0:
        return None

    divisors = {1, n}

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            divisors.add(divisor)
            divisors.add(n // divisor)

        divisor += 1

    return divisors


def solution(A):
    max_n = max(A)
    N = len(A)

    count = {}

    for n in A:
        count[n] = count.get(n, 0) + 1

    divisors = {n: find_divisors(n) for n in count.keys()}

    return [N - sum(count.get(divisor, 0) for divisor in divisors[n]) for n in A]


print(solution([2]))
