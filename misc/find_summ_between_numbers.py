def get_sum(a, b):
    if a == b:
        return a

    summ = 0

    lower = a if a < b else b
    higher = b if a < b else a

    while lower <= higher:
        summ += lower
        lower += 1

    return summ


print(get_sum(1, 5))
