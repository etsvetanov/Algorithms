def coins(n):
    result = 0
    coin = [0] * (n + 1)
    op_count = 0
    for i in range(1, n + 1):
        k = i
        while k <= n:
            coin[k] = (coin[k] + 1) % 2
            k += 1

        op_count += 1
        result += coin[i]

    print('op_count:', op_count)
    return result


coins(10)

