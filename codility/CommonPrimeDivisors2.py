def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# gdc(x, y) will contain the common prime factors of x and y
# when we start dividing x and y to the greatest common divisor we will reach either 1 or a primer factor that is
# not in gdc(x, y)


def solution(A, B):
    count = 0

    for a, b in zip(A, B):
        g = gcd(a, b)

        print('\n >> gdc({a}, {b}) ='.format(a=a, b=b), g, '\n\n')

        while True:
            d = gcd(a, g)
            print('a={a:<15}  d = gcd({a}, {g}) = {d}'.format(a=a, g=g, d=d))
            if 1 == d:  # gcd(a, b) is 1, i.e. no common dividers except 1
                break

            assert(a/d == a//d)
            a //= d


        print('--------------------')

        while True:
            d = gcd(b, g)
            print('b={b:<15}  d = gcd({b}, {g}) = {d}'.format(b=b, g=g, d=d))
            if 1 == d:
                break

            assert(b//d == b/d)
            b //= d

        count += 1 if a == 1 and b == 1 else 0

    return count


solution([630, 15, 12, 210], [420, 35, 36, 60])
