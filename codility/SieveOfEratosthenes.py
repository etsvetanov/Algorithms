from math import floor, sqrt


# def simple_sieve(n):
#     sieve = [True] * (n + 1)
#     sieve[0] = sieve[1] = False
#
#     for i in range(2, int(sqrt(n)) + 1):  # while i**2 <= n:
#         if sieve[i]:  # if i is still potentially composite
#             for k in range(i ** 2, n + 1, i):
#                 sieve[k] = False
#
#     return sieve
#
#
def get_smallest_factor_of(n: int):
    min_factor_of = [0] * (n+1)

    for i in range(2, int(sqrt(n)) + 1):
        if min_factor_of[i] == 0:
            for k in range(i**2, n+1, i):
                if min_factor_of[k] == 0:
                    min_factor_of[k] = i

    return min_factor_of

def find_factors(x, F):
    prime_factors_of_x = []
    print(f'F: {F}')
    tmp = x

    while F[tmp]:
        print(f'F[{tmp}] = {F[tmp]}')
        factor = F[tmp]
        prime_factors_of_x.append(factor)

        tmp //= factor

    return prime_factors_of_x


# print([i for i, v in enumerate(simple_sieve(16)) if v])

print(f'prime factors: {find_factors(24, get_smallest_factor_of(24))}')

#
#
#
#
#
#
#
#
#
#
#
#
#
# # find all prime numbers in [2: n]
# def sieve(n):
#     sieve = [True] * (n + 1)
#     sieve[0] = sieve[1] = False
#     i = 2
#     while i * i <= n:
#         if sieve[i]:
#             k = i * i
#             while k <= n:
#                 sieve[k] = False
#                 k += i
#
#         i += 1
#
#     return sieve
#
#
# # find the prime factors of n
def factors_up_to_n(n):
    F = [0] * (n + 1)

    i = 2
    while i ** 2 <= n:
        if F[i] == 0:
            k = i ** 2
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1

    return F


def factorization(x, F):
    prime_factors = set()
    while F[x] > 0:

        print(f'F[{x}] = {F[x]}')
        prime_factors.add(F[x])
        x //= F[x]

    prime_factors.add(x)

    return prime_factors


# print(list(enumerate(sieve(25))))
print(list(enumerate(factors_up_to_n(25))))
print(factorization(24, factors_up_to_n(24)))
