# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    assert (max(A, B) <= (min(A, B) * 2 + 2))

    big, small = ([A, 'a'], [B, 'b']) if A > B else ([B, 'b'], [A, 'a'])

    delta = big[0] - small[0]

    s = ''

    delta_or_small = min(delta, small[0])

    for _ in range(delta_or_small):
        s += (2 * big[1] + small[1])
        big[0] -= 2
        small[0] -= 1

    print(f'delta_or_small: {delta_or_small}, small: {small}')

    if small[0] == 0:
        remaining = big[0]
        char = big[1]

        return s + (remaining * char)

    for _ in range(small[0] - delta):
        s += (big[1] + small[1])

    print(f'>>> s: {s}')
    return s