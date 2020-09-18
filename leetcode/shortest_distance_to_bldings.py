from queue import Queue
from typing import Tuple, List

# [
#     [1, 0, 2, 0, 1],
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0]
# ]

NEIGH_DIRECTIONS = (
    (-1, 0),  # top
    (+1, 0),  # bottom
    (0, -1),  # left
    (0, +1),  # right
)

def pprint(l):
    print('\n'.join(list(map(str, l))))

class Solution:
    def __init__(self):
        self.distances_sum = None  # sun of distance to each building
        self.grid = None

    def bfs(self, root: Tuple[int, int]):
        h, w = self.h, self.w
        visited = [[False] * w for _ in range(h)]

        # we must check the current blding (root) can reach all other bldings
        bldings_reached = 1

        q = Queue()
        q.put((*root, 0))  # (i, j, distance)
        
        visited[root[0]][root[1]] = True

        while not q.empty():
            i, j, d = q.get()

            neighbors = [(i + ni, j + nj) for ni, nj in NEIGH_DIRECTIONS]
            neighbors = list(filter(lambda neigh: 0 <= neigh[0] < h and 0 <= neigh[1] < w, neighbors))

            for ni, nj in neighbors:
                if not visited[ni][nj]:
                    visited[ni][nj] = True

                    if self.grid[i][j] == 0 and self.grid[ni][nj] == 1:
                        bldings_reached += 1

                    if self.grid[ni][nj] == 0:
                        self.distances_sum[ni][nj] += d + 1
                        q.put((ni, nj, d + 1))

        return bldings_reached

    def shortestDistance(self, grid: List[List[int]]) -> int:
        self.grid = grid

        pprint(grid)

        h = len(grid)
        w = len(grid[0])
        self.distances_sum = [[0] * w for _ in range(h)]
        self.h, self.w = h, w

        self.blding_coords = [(i, j) for i in range(h) for j in range (w) if self.grid[i][j] == 1]

        for i, j in self.blding_coords:
            reached = self.bfs((i, j))  # run bfs to find distance from blding to each empty point

            if reached < len(self.blding_coords):
                return -1

        min_distance = float('inf')


        for i in range(h):
            for j in range(w):
                d = self.distances_sum[i][j]
                if d > 0:  # if distance is 0 then this point is unreachable
                    min_distance = min(d, min_distance)

        return min_distance if min_distance < float('inf') else -1

solution = Solution()
input = [[1,0,1,0,1]]
result = solution.shortestDistance(input)
print('result:', result)
