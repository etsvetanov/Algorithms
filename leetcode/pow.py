def solution(x: int, n: int) -> int:
    if n < 0:
        x = 1 / x
        n = -n

    ans = 1
    current_product = x

    i = n
    print(
        'ans: {ans}, current_product: {current_product}, i: {i}'.format(ans=ans, current_product=current_product, i=i))
    while i:
        if i % 2 == 1:
            ans *= current_product

        current_product *= current_product

        i //= 2

        print(
            'ans: {ans}, current_product: {current_product}, i: {i}'.format(ans=ans, current_product=current_product,
                                                                            i=i))

    return ans


print(solution(2, 7))
