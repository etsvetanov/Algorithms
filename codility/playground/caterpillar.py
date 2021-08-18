from typing import List

# is there a subsequence of A whose sum of elements equals "s"
def caterpillar(A: List[int], s: int):
    curr_sum = 0
    front = 0

    for back in range(len(A)):
        while front < len(A) and curr_sum + A[front] <= s:
            curr_sum += A[front]
            front += 1

        if curr_sum == s:
            return True

        curr_sum -= A[back]

    return False


assert(caterpillar([1, 5, 3, 9, 12, 4], 12))
assert(caterpillar([1, 5, 3, 9, 12, 4], 8))