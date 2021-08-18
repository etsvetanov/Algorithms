def create_peaks(A):
    N = len(A)
    peaks = [False] * N

    for i in range(1, N - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks[i] = True

    return peaks


def gen_next_peak(A):
    N = len(A)

    peaks = create_peaks(A)

    next = [0] * N
    next[N - 1] = -1

    for i in range(N-2, -1, -1):
        if peaks[i]:
            next[i] = i
        else:
            next[i] = next[i + 1]

    return next


def flags(A):
    N = len(A)
    next_peak_at = gen_next_peak(A)
    i = 1

    max_flags = 0

    # in N length we can only put sqrt(N) flags, i.e. i*i, because i flags need to have i space between them
    # e.g. putting 4 flags, 4 spaces (at least) between, means 4x4 = 16 spaces
    # but we only need space between the flags, not after every flag (i.e not after the last flag)
    # so it's actually (i-1)*i
    # Below you can see that for 4 flags, with 4 spaces between, we can actually put 4 flags,
    #   that take 3*4 space
    #
    #    P <-4-> P <-4-> P <---4--> P
    # [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
    #
    while (i - 1) * i <= N:
        pos = 0
        flag_count = 0

        while pos < N and flag_count < i:
            # we advance the position to the next peak
            pos = next_peak_at[pos]
            if pos == -1:
                break

            flag_count += 1
            # we skip i positions because we are trying to put i flags
            # so we might go past a peak but that peak will be too close to the previous
            pos += i

        max_flags = max(max_flags, flag_count)
        i += 1

    return max_flags


test = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]

print(flags(test))