def power(x, y):
    if y == 0:
        return 1

    tmp = power(x, y // 2)

    if y % 2 == 0:
        return tmp * tmp
    else:
        if y > 0:
            return x * tmp * tmp
        else:
            return (tmp * tmp) / x


















