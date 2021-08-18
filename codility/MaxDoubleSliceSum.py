# Observations:
# 1. The 0-th idx is always excluded, i.e. A[0] cannot be a part of a sum, i.e. if X=0 then sum can only begin at X+1,
#       but if X=1 then sum can only begin at X+2... thus 0-th idx can never be part of a sum
# 1.1  Following the same logic the last element cannot be a part of a sum
#       Below is an illustration of why first and last cannot be (ever) a part of the slices
#       [ X <--- left-slice ---> Y <--- right-slice ---> Z ]
#       [ 0 X <--- left-slice ---> Y <--- right-slice ---> Z -1]
#
# 2. We don't really care where (exactly) the slices begin and end so we can look at the problem, as following:
#       - we have a number Y satisfying 1 <= Y <= N-2 (following the requirements 0 <= X < Y < Z < N,
#           i.e. only X can be the 0-th and only Z can be the last one, Y has to be in between
#       - we want to know what is the maximum sum ending at the index before Y (i.e. Y-1) and what is the maximum sum
#           starting after Y (i.e. Y+1)
# 3. even though some slices sum may be negative (e.g. we only have negative numbers in the whole array), we can always
#       count a 0-length slice with sum of 0 thus we the max slice can never be negative (e.g. X=0, Y=1, Z=2 and even
#       if we have only negative numbers the max slice sum will still be 0

#                  Y      Z
# [3, 2, 6, -1, 4, 5, -1, 2]

def solution(A):
    # write your code in Python 3.6
    max_ending = 0
    max_ending_at = [0] * len(A)

    # we leave A[0] = 0 and start from A[1] so A[0] is never counted for the slice sum
    # not crucial, but we also don't care about the last two elements because they will never be needed for the
    # left-slice, they may only be occupied by Y and Z:
    # [ ... X <--- left-slice ---> Y Z]     - here the right-slice is a 0-length slice between Y Z (last 2 elements)
    for i in range(1, len(A) - 2):
        max_ending = max(0, max_ending + A[i])
        max_ending_at[i] = max_ending

    max_starting = 0
    max_starting_at = [0] * len(A)

    # same as above,
    # we leave the last one A[-1] = 0 and start from A[-2] so that the last one can never be counted for the slice sum
    # and (not crucial) but we don't care about A[0] and A[1] so we calculate A[2] and stop
    for i in range(len(A) - 2, 1, -1):  # we leave
        max_starting = max(0, max_starting + A[i])
        max_starting_at[i] = max_starting

    max_slice = 0
    for i in range(1, len(A) - 1):
        max_slice = max(max_slice, max_ending_at[i - 1] + max_starting_at[i + 1])

    return max_slice


print(solution([3, 2, 6, -1, 4, 5, -1, 2]))