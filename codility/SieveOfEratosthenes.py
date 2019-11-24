# find all prime numbers in [2: n]
def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = False
                k += i

        i += 1

    return sieve


# find the prime factors of n
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
        x /= F[x]

    prime_factors.add(x)

    return prime_factors


print(list(enumerate(sieve(25))))
print(list(enumerate(factors_up_to_n(25))))
