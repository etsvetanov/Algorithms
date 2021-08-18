from math import sqrt, floor

# coins 1..n
# initially all coins showing heads
# n people turn over coins as follows: person i flips coins with numbers that are multiples of i
# count the number of coins showing tails after all people have had a turn



def coins(n):
    count = 0
    # True - tails, False - heads
    coin = [False] * (n+1)  # ignore 0-th element and use 1..n for simplicity

    for i in range(1, n+1):
        for k in range(i, n+1, i):
            coin[k] = not coin[k]

        count += int(coin[i])

    print(f'coins: {coin[1:]}')

    return count


def faster_solution(n):
    return floor(sqrt(n))

N = 152
print(f'count: {coins(N)}')
print(f'method2: {faster_solution(N)}')