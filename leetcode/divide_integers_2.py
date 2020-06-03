def divide(dividend: int, divisor: int) -> int:
    # Constants.
    MAX_INT = 2147483647  # 2**31 - 1
    MIN_INT = -2147483648  # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    # We want to find the largest doubling of the divisor in the negative 32-bit
    # integer range that could fit into the dividend.
    # Note if it would cause an overflow by being less than HALF_INT_MIN,
    # then we just stop as we know double it would not fit into INT_MIN anyway.
    max_bit = 0
    while divisor >= HALF_MIN_INT and divisor + divisor >= dividend:
        max_bit += 1
        divisor += divisor

    quotient = 0
    # We start from the biggest bit and shift our divisor to the right
    # until we can't shift it any further.
    print('before ---- quotient: {}, divident: {}, divisor: {}'.format(quotient, dividend, divisor))
    for bit in range(max_bit, -1, -1):
        # If the divisor fits into the dividend, then we should set the current
        # bit to 1. We can do this by subtracting a 1 shifted by the appropriate
        # number of bits.
        if divisor >= dividend:
            quotient ^= (1 << bit)
            # Remove the current divisor from the dividend, as we've now
            # considered this part of it.
            dividend -= divisor

        # Shift the divisor to the right so that it's in the right place
        # for the next positon we're checking at.
        divisor = (divisor + 1) >> 1
        print('bit: {0}, quotient: {1}, divident: {2}, divisor: {3}'.format(bit, quotient, dividend, divisor))

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return -quotient if negatives != 1 else quotient


print('result:', divide(1678, 10))
# /home/evgeni/Projects/Algorithms/venv/bin/python /home/evgeni/Projects/Algorithms/leetcode/divide_integers_2.py
# before ---- quotient: 0, divident: -1678, divisor: -1280
# bit: 7, quotient: -128, divident: -398, divisor: -640
# bit: 6, quotient: -128, divident: -398, divisor: -320
# bit: 5, quotient: -160, divident: -78, divisor: -160
# bit: 4, quotient: -160, divident: -78, divisor: -80
# bit: 3, quotient: -160, divident: -78, divisor: -40
# bit: 2, quotient: -164, divident: -38, divisor: -20
# bit: 1, quotient: -166, divident: -18, divisor: -10
# bit: 0, quotient: -167, divident: -8, divisor: -5
# result: 167
#
# Process finished with exit code 0