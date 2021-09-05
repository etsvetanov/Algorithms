# 100% but cheating:
#
# def solution(A):
#     return(len(set(map(lambda x: abs(x), A))))

def solution(A):
    # write your code in Python 3.6

    N = len(A)
    l = 0
    r = N - 1
    count = 0
    last_l = None
    last_r = None

    while l < r:
        if abs(A[l]) < abs(A[r]):
            if A[r] != last_r:
                count += 1
                last_r = A[r]

            r -= 1

        elif abs(A[l]) > abs(A[r]):
            if A[l] != last_l:
                count += 1
                last_l = A[l]

            l += 1

        else:
            if A[l] != last_l and A[r] != last_r:
                count += 1
                last_l = A[l]
                last_r = A[r]

            l += 1
            r -= 1

    if l == r and A[l] not in (last_l, last_r):
        count += 1

    return count
