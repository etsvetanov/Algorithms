# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def find_all(v, A):
    c = 0
    for x in A:
        if x == v:
            c += 1

    return c


def solution(A):
    size = 0
    n = len(A)
    candidate = None

    for x in A:
        if size == 0:
            size += 1
            candidate = x
        elif x != candidate:
            size -= 1
        else:
            size += 1

    if size == 0:
        return 0

    count = find_all(candidate, A)

    if count < n // 2:
        # no leader
        return 0
    else:
        equi_count = 0
        for i in range(1, n):
            count_left = find_all(candidate, A[:i])
            count_right = find_all(candidate, A[i:])

            size_left = i
            size_right = n - i

            if count_left > size_left // 2 and count_right > size_right // 2:
                equi_count += 1

        return equi_count

