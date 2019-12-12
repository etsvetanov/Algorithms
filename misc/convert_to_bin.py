def add_binary(a, b):
    summ = a + b
    tmp = summ
    bin_result = ''

    while tmp:
        remainder = tmp % 2
        bin_result = str(remainder) + bin_result
        tmp = tmp // 2

    return bin_result


print(add_binary(10, 6))


# 0 0 0 0
# 16 / 2 = 8 + 0
# 8 / 2 = 4 + 0
# 4 / 2 = 2 + 0
# 2 / 2 = 1 + 0
# 1 / 2 = 0 + 1