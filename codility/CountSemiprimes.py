# IDEA 1: Factorize and check if prime factors are more than 2 for each number in the range
# IDEA 2: Remember the number of divisors in the sieve and then if

def solution(N, P, Q):
    M = len(P)

    F = [0] * (N + 1)
    i = 2

    while i * i <= N:
        if F[i] == 0:
            k = i * i
            while k <= N:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1

    semiprime_counts = [0] * M

    for j, (p, q) in enumerate(zip(P, Q)):

        for x in range(p, q + 1):  # [x, y)
            if F[x] > 0 and F[x // F[x]] == 0:
                semiprime_counts[j] += 1

    return semiprime_counts


print(solution(26, [1, 4, 16], [26, 10, 20]))
