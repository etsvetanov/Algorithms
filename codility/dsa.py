# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    head_count = A // K
    head_remainder = A % K
    tail_count = B // K

    result = tail_count - head_count
    result = result if head_remainder else result + 1

    return result