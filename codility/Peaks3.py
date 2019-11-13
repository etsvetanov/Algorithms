def solution(A: []) -> int:
    N = len(A)

    if N < 3:
        return 0

    peaks_so_far = [0] * N

    for i in range(1, N - 1):
        prev, curr, nxt = A[i - 1: i + 2]

        peaks_so_far[i] = peaks_so_far[i - 1] + 1 if prev < curr > nxt else peaks_so_far[i - 1]

    peaks_so_far[-1] = peaks_so_far[-2]
    peaks_so_far = [0] + peaks_so_far

    for block_size in range(3, N + 1):

        if N % block_size == 0:
            # iterate over last index in block and check if:
            if all(peaks_so_far[block_end] >= block_end // block_size  # there are at least X peaks if X is current block
                   and peaks_so_far[block_end] > peaks_so_far[block_end - block_size]  # has 1 more peak than previous block
                   for block_end
                   in range(block_size, N + 1, block_size)):
                return N // block_size

    return 0


test = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
test1 = [1, 2, 1] * 10
test2 = [1, 3, 2, 1]
test3 = [0, 1000000000]
test4 = [1, 2, 3, 4, 5, 6]
test5 = [1] * 10000
test5[400] = 55
test6 = [1, 2, 3, 4, 3, 2, 1, 0] * 625
test7 = list(range(1000)) + list(reversed(range(999)))
test8 = [1, 2, 1, 2, 1, 2, 1, 1, 1]
test9 = [1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test10 = [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]

assert solution(test1) == 10
assert solution(test) == 3
assert solution(test2) == 1
assert solution(test3) == 0
assert solution(test4) == 0
assert solution(test5) == 1
assert solution(test6) == 625
assert solution(test7) == 1
assert solution(test8) == 1
assert solution(test9) == 1
assert solution(test10) == 2

for i in range(13):
    a = [1] * i
    b = [2] * i
    c = [3] * i

    assert solution(a) == 0
    assert solution(b) == 0
    assert solution(c) == 0

for i in range(100):
    a = list(range(i))

    assert solution(a) == 0
