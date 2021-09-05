# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # write your code in Python 3.6
    index_by_number = {}
    n = len(A)
    left = 0
    right = 0
    count = 0


    while right < n:
        print(f'left: {left} right: {right}')
        if A[right] not in index_by_number:
            index_by_number[(A[right])] = right
            right += 1
        else:
            d = right - left
            prev_i = index_by_number[A[right]]
            count += (d*(d+1)) // 2 + (right - (prev_i + 1))
            print(f'dic: {index_by_number}, count: {count}, d: {d}')
            left = right
            index_by_number.clear()

    d = right - left
    print(f'findal d: {d}')
    count += (d*(d+1)) // 2
    return count


# res = solution(6, [1, 2, 5, 4, 5])
#
# print(f'res: {res}')
tests = [
    (6, [1, 2, 5, 4, 5], 13),
    (10, [10, 4, 7, 2, 10], 20),
    (6, [1, 2, 6, 1, 2], 18),
    (10, [1, 1, 10, 9, 5], 11),
    (8, [6, 4, 1, 8, 2], 15),
    (9, [9, 9, 8, 7, 6], 11)
]

for test in tests:
    res = solution(*test[:2])
    print(f'RESULT: {res}')
    assert(res == test[2])