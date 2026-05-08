class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Top view
        top = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        
        # Front view (row max)
        front = sum(max(row) for row in grid)
        
        # Side view (column max)
        side = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        
        return top + front + side
