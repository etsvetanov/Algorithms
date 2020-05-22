#
# def solution(A):
#     size = len(A)
#     prefixes = [0] * (size + 1)
#
#     for i in range(1, size + 1):
#         prefixes[i] = prefixes[i - 1] + A[i - 1]
#
#     min_slice_avg = prefixes[2] / 2
#     min_index = 0
#
#     for i in range(1, size + 1):
#         for j in range(i + 1, size + 1):
#             slice_size = j + 1 - i
#             slice_sum_avg = (prefixes[j] - prefixes[i - 1]) / slice_size
#             # print('i', i, 'j', j, 'slice_size', slice_size, 'slice_sum', slice_sum_avg)
#             if slice_sum_avg < min_slice_avg:
#                 min_slice_avg = slice_sum_avg
#                 min_index = i - 1
#
#     return min_index
#
#
#
# def solution(A):
#     min_avg_value = (A[0] + A[1])/2.0   # The mininal average
#     min_avg_pos = 0     # The begin position of the first
#                         # slice with mininal average
#     for index in range(0, len(A)-2):
#         # Try the next 2-element slice
#         if (A[index] + A[index+1]) / 2.0 < min_avg_value:
#             min_avg_value = (A[index] + A[index+1]) / 2.0
#             min_avg_pos = index
#         # Try the next 3-element slice
#         if (A[index] + A[index+1] + A[index+2]) / 3.0 < min_avg_value:
#             min_avg_value = (A[index] + A[index+1] + A[index+2]) / 3.0
#             min_avg_pos = index
#     # Try the last 2-element slice
#     if (A[-1]+A[-2])/2.0 < min_avg_value:
#         min_avg_value = (A[-1]+A[-2])/2.0
#         min_avg_pos = len(A)-2
#     return min_avg_pos


def solution(A):
    min_avg = min(sum(A[0:2])/2, sum(A[0:3])/3)
    min_avg_i = 0

    for i in range(1, len(A) - 1):
        avg_a = sum(A[i:i + 2])/2
        avg_b = sum(A[i:i + 3])/3 if i < len(A) - 2 else None

        print('min_avg', min_avg, 'min_avg_i', min_avg_i, 'avg_a', avg_a, 'avg_b', avg_b)

        if avg_a < min_avg:
            min_avg = avg_a
            min_avg_i = i

        if avg_b and avg_b < min_avg:
            min_avg = avg_b
            min_avg_i = i

    return min_avg_i


print('min_avg_pos:', solution([1, 0, 3, 1, 0, 1, 0, 2, 2]))
