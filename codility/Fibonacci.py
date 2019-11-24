from math import sqrt

def fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    print(fib)
    return fib[n]


def fib2(n):
    return (((1 + sqrt(5))/2) ** n - ((1 - (sqrt(5))) / 2) ** n) / sqrt(5)


print(fibonacci(10))
print(fib2(10))