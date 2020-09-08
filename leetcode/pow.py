def my_pow(x, n):
    if n < 0:
        x = 1/x
        n = -n

    ans = 1

    for _ in range(n):
        ans *= x

    return ans

