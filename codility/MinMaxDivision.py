def get_num_blocks_for_target_sum(arr, max_sum):
    blocks_num = 1

    block_sum = 0
    for n in arr:
        if block_sum + n > max_sum:
            block_sum = n  # move n value to next block
            blocks_num += 1
        else:
            block_sum += n

    return blocks_num


# K - number of blocks
# A[i] < M
def solution(K, M, A):
    # K is fixed so we are looking on how To distribute these K blocks such that the sum of each block is minimal

    lower_bound = max(A)  # best case we have max(A) in a single block and other blocks' sum is lower than max(A)
    upper_bound = sum(A)  # 1 block contains all numbers, and other blocks are empty

    min_max_sum = 0

    if K == 1: return upper_bound
    if K >= len(A): return lower_bound  # each A[i] will be contained in its own block

    while lower_bound <= upper_bound:
        # the number we are looking for is between the lower and upper bound so we are going to split it in half
        candidate_sum = (lower_bound + upper_bound) // 2
        candidate_blocks = get_num_blocks_for_target_sum(A, max_sum=candidate_sum)

        if candidate_blocks <= K:
            # we got blocks to spare or these blocks can accommodate lower min_max_sum
            upper_bound = candidate_sum - 1  # [lower ------ mid(new_upper) ------ upper]
            min_max_sum = candidate_sum
        else:
            # we need a solution with less blocks (i.e. min_max_sum must be larger than lower_bound)
            lower_bound = candidate_sum + 1  # [lower ------ mid(new_lower) ------ upper]

    return min_max_sum


