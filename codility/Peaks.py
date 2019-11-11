def solution(A):
    if len(A) < 3:
        return 0

    peaks = []
    size = len(A)

    # O(n)
    for i in range(1, size - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)

    # O(n) ?
    for block_size in range(3, size + 1):
        num_blocks = size // block_size

        if size % block_size == 0 and len(peaks) >= num_blocks:
            every_block_contains_peak = True

            # O(n/m) ?
            for block_start in range(0, size, block_size):
                # block_indexes = [i for i in range(block_start, block_start + block_size)]
                block_end = block_start + block_size
                has_peak = False
                for p in peaks:
                    if block_start <= p <= block_end:
                        has_peak = True
                        break

                if not has_peak:
                    # this means we have a block that doesn't contain any peaks
                    every_block_contains_peak = False
                    break

            if every_block_contains_peak:
                return num_blocks

    return 0


test = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
test2 = [1, 3, 2, 1]
test3 = [0, 1000000000]
test4 = [1, 2, 3, 4, 5, 6]

assert (solution(test) == 3)
assert (solution(test2) == 1)
assert (solution(test3) == 0)
assert (solution(test4) == 0)
