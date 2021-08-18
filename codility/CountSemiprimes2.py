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
#
# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
# from math import sqrt
#
#
# def get_primes_up_to(N: int):
#     is_prime = [True] * (N + 1)
#     is_prime[0] = is_prime[1] = False
#
#     for i in range(2, int(sqrt(N)) + 1):
#         # if i is marked as not prime then we know it's multiples are not prime either
#         # and already been marked as sucj
#         if is_prime[i]:
#             for k in range(i ** 2, N + 1, i):
#                 is_prime[k] = False
#
#     return [i for i, v in enumerate(is_prime) if v]
#
#
# def solution(N, P, Q):
#     # write your code in Python 3.6
#     primes_up_to_N = get_primes_up_to(N // 2)
#     semi_primes = set()
#
#     for i, p1 in enumerate(primes_up_to_N):
#         for j in range(i + 1, len(primes_up_to_N)):
#             p2 = primes_up_to_N[j]
#             semi_prime = p1 * p2
#             if semi_prime <= N:
#                 semi_primes.add(semi_prime)
#
#     semi_primes_count_up_to = [0] * (N + 1)
#
#     for i in range(1, N + 1):
#         is_semi_prime = int(i in semi_primes)
#         print(f'setting: [{i}] to {semi_primes_count_up_to[i - 1] + is_semi_prime}')
#         semi_primes_count_up_to[i] = semi_primes_count_up_to[i - 1] + is_semi_prime
#
#     print(f'N: {N} semi_primes: {semi_primes}, semi_primes_count_up_to {semi_primes_count_up_to}')
#
#     return [semi_primes_count_up_to[q] - semi_primes_count_up_to[p] for p, q in zip(P, Q)]
#







































