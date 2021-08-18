# def gcd(a, b, res):
#     print('gcd({0}, {1}, {2})'.format(a, b, res))
#     if a == b:
#         return res * a
#     elif a % 2 == 0 and b % 2 == 0:
#         return gcd(a // 2, b // 2, 2 * res)
#     elif a % 2 == 0:
#         return gcd(a // 2, b, res)
#     elif b % 2 == 0:
#         return gcd(a, b // 2, res)
#     elif a > b:
#         return gcd(a - b, b, res)
#     else:
#         return gcd(a, b - a, res)
#

# print('gcd(24, 16):', gcd(24, 16, 1))
# print(gcd(15, 75, 1))
# print(gcd(1, 2, 1))


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(8, 3))


