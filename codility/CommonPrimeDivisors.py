# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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
        prime_factors.add(F[x])
        x //= F[x]

    prime_factors.add(x)

    return prime_factors


def solution(A, B):
    # write your code in Python 3.6
    maxN = max(max(A), max(B))

    F = factors_up_to_n(maxN)
    count = 0
    for i, j in zip(A, B):
        if factorization(i, F) == factorization(j, F):
            count += 1

    return count
