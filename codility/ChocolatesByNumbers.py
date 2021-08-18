
def gcd(a, b):
    # Get the greatest common divisor
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)


def solution(N, M):
    lcm = N * M / gcd(N, M) # Least common multiple
    return lcm / M



print(solution(8, 3))