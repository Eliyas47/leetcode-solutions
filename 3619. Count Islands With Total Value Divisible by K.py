from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        ans = 0

        def dfs(r, c):
            if (r < 0 or r >= m or c < 0 or c >= n
                    or visited[r][c] or grid[r][c] == 0):
                return 0

            visited[r][c] = True
            total = grid[r][c]

            total += dfs(r + 1, c)
            total += dfs(r - 1, c)
            total += dfs(r, c + 1)
            total += dfs(r, c - 1)

            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and not visited[i][j]:
                    if dfs(i, j) % k == 0:
                        ans += 1

        return ans
