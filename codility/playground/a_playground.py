from math import sqrt
from typing import List, Set


def get_min_divisor_up_to(n: int) -> List[int]:
    min_divisor_by_num = [0] * (n+1)

    for i in range(2, int(sqrt(n) + 1)):
        if min_divisor_by_num[i] == 0:
            for k in range(i**2, n+1, i):
                if min_divisor_by_num[k] == 0:
                    min_divisor_by_num[k] = i

    return min_divisor_by_num


def get_prime_divisors(n: int, min_divisors: List[int]) -> Set[int]:
    prime_divisors = set()

    while min_divisors[n] != 0:
        prime_divisors.add(min_divisors[n])
        n //= min_divisors[n]

    prime_divisors.add(n)

    return prime_divisors



res = get_min_divisor_up_to(24)
print(f'> {[i for i in enumerate(res)]}')
print(f'> {get_prime_divisors(24, res)}')