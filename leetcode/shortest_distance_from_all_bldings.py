import collections


class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])

        distance = [[0 for _ in range(w)] for _ in range(h)]
        reach = [[0 for _ in range(w)] for _ in range(h)]

        buildingNum = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    buildingNum += 1
                    q = [(i, j, 0)]

                    isVisited = [[False for _ in range(w)] for _ in range(h)]

                    for y, x, d in q:
                        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                            r = y + dy
                            c = x + dx

                            if 0 <= r < h and 0 <= c < w and grid[r][c] == 0 and not isVisited[r][c]:
                                distance[r][c] += d + 1
                                reach[r][c] += 1

                                isVisited[r][c] = True
                                q.append((r, c, d + 1))

        shortest = float("inf")
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    shortest = min(shortest, distance[i][j])

        if shortest < float("inf"):
            return shortest
        else:
            return -1