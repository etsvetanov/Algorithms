def solution(N, P, Q):
    # write your code in Python 3.6
    M = len(P)

    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False

    i = 2

    while i * i <= N:
        if sieve[i]:
            k = i * i
            while k <= N:
                sieve[k] = False
                k += i
        i += 1

    primes = [i for i, isPrime in enumerate(sieve) if isPrime]

    semiprimes = set()
    for i, prime in enumerate(primes):

        for prime2 in primes[i:]:
            if prime * prime2 > N:
                break

            semiprimes.add(prime * prime2)

    # semiprimes = sorted(semiprimes)

    semiprimes_so_far = [0] * (N + 1)

    for i in range(N + 1):
        semiprimes_so_far[i] = semiprimes_so_far[i-1] + 1 if i in semiprimes else semiprimes_so_far[i-1]


    # counts = [0] * M
    counts = [semiprimes_so_far[q] - semiprimes_so_far[p-1] for p, q in zip(P, Q)]
    # for i, (p, q) in enumerate(zip(P, Q)):
    #     for x in range(p, q + 1):
    #         if x in semiprimes:
    #             counts[i] += 1

    return counts
    # N -> less than logN prime factors
    # logN + (logN - 1) + (logN - 2)



print(solution(26, [1, 4, 16], [26, 10, 20]))

























































