from queue import LifoQueue
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # i - row
        # j - column
        num_rows = len(grid)
        num_cols = len(grid[0])
        count = 0

        for i in range(num_rows):
            for j in range(num_cols):
                n = grid[i][j]

                if n == 0:
                    continue

                grid[i][j] = 0

                count += 1
                print('adding island!')

                stack = LifoQueue()
                stack.put((i, j))

                while not stack.empty():
                    node = stack.get()
                    ni, nj = node

                    neighbors = [
                        (ni, nj - 1),  # left
                        (ni, nj + 1),  # right
                        (ni - 1, nj),  # top
                        (ni + 1, nj),  # bottom
                    ]

                    neighbors = list(filter(
                        lambda nbr: 0 <= nbr[0] < num_rows and 0 <= nbr[1] < num_cols,
                        neighbors
                    ))

                    print('neighbors for {0}:'.format((ni, nj)), neighbors)

                    for ni, nj in neighbors:
                        n_val = grid[ni][nj]
                        print('grid[{0}][{1}]:'.format(ni, nj), n_val)
                        if n_val == 1:
                            print('adding neighbor to stack')
                            grid[ni][nj] == 0  # mark as visited
                            stack.put((ni, nj))

        return count


input = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
solution = Solution()
result = solution.numIslands(input)
print('number of islands', result)
