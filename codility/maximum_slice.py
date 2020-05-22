from setuptools.command.saveopts import saveopts


def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)

        max_slice = max(max_slice, max_ending)
    return max_slice


def quadratic_max_slice(A):
    n, result = len(A), 0
    for p in range(n):
        sum = 0
        for q in range(p, n):
            sum += A[q]
            result = max(result, sum)

    return result


def quadratic_max_slice2(A, pref):
    n, result = len(A), 0
    for p in range(n):
        for q in range(p, n):
            sum = pref[q + 1] - pref[p]
            result = max(result, sum)
    return result


def get_prefixes(A):
    sum = 0
    prefixes = [0]

    for n in A:
        sum += n
        prefixes.append(sum)

    return prefixes


sample_1 = [-1, -5, -2, -8, -4, -1, -1]
print('golden_max_slice(sample_1):', golden_max_slice(sample_1))
print('quadratic_max_slice(sample_1):', quadratic_max_slice(sample_1))
print('quadratic_max_slice2(sample_1):', quadratic_max_slice2(sample_1, get_prefixes(sample_1)))
