class Solution:
    def surfaceArea(self, grid):
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    # Each cube contributes 6 faces
                    area += grid[i][j] * 6
                    # Subtract hidden vertical faces
                    area -= (grid[i][j] - 1) * 2
                    # Subtract hidden faces with neighbors
                    if i > 0:
                        area -= 2 * min(grid[i][j], grid[i-1][j])
                    if j > 0:
                        area -= 2 * min(grid[i][j], grid[i][j-1])
        return area
