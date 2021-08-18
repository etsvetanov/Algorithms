# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
    lowest_dip = A[0]
    max_profit = 0



    for n in A[1:]:
        max_profit = max(max_profit, n - lowest_dip)
        lowest_dip = min(lowest_dip, n)

    return max_profit

print(solution([0, 2000000]))
print(solution([]))