def add(a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    print('a:', x, 'b:', y)

    while y:
        print('x:', bin(x), 'y:', bin(y))
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry


    return bin(x)[2:]


result = add('11111', '1111')
print('answer:', result, '({0})'.format(int(result, 2)))