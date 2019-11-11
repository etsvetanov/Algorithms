# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    block_height = H[0]
    block_counter = 1
    filled_height = [0] * len(H)
    filled_height[0] = block_height

    for i in range(1, len(H)):
        if H[i] == filled_height[i]:
            continue

        if H[i] > block_height:
            filled_height[i] = block_height

            for j in range(i + 1, len(H)):
                if H[j] >= block_height:
                    filled_height[j] = block_height
                else:
                    block_counter += 1  # finalize current block
                    break

            block_height = H[i]  # create a new block (we don't know how wide yet)

        elif H[i] < block_height:
            block_height = H[i]  # create a new block (we don't know how wide yet)
            block_counter += 1  # finilize current block

    return block_counter

# k = 2, 3, 4, 5, 6
# size = 0, 1, 0, 1, 2, 3, 2, 1
# value = 4, 6,