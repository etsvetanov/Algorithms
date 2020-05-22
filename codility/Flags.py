def solution(A):
    N = len(A)
    if N < 3:
        return 0

    peaks = [i for i in range(1, N - 1) if A[i] > A[i - 1] and A[i] > A[i + 1]]

    if len(peaks) <= 2:
        return len(peaks)

    first_to_last_dist = peaks[-1] - peaks[0]

    for num_flags in range(len(peaks), 1, -1):
        if (num_flags - 1) * num_flags > first_to_last_dist:
            continue

        last_flag = peaks[0]
        planted_flags = 1

        for peak in peaks[1:]:
            if peak - last_flag >= num_flags:
                planted_flags += 1
                last_flag = peak

            if planted_flags == num_flags:
                return planted_flags


assert solution([5]) == 0
assert solution([1, 2, 1]) == 1
assert solution([1, 2, 1, 2, 1]) == 2
assert solution([1, 2, 1, 2, 1, 2, 1]) == 2
assert solution([1, 2, 1, 2, 1, 2, 1, 2, 1]) == 2
assert solution([1, 2, 1, 1, 2, 1, 1, 2, 1]) == 3
