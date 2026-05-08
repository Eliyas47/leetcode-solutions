class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        directions = [(0,1),(1,0),(0,-1),(-1,0)]  # east, south, west, north
        steps = 1
        r, c = rStart, cStart
        result.append([r, c])
        
        while len(result) < rows * cols:
            for i in range(4):
                dr, dc = directions[i]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                if i % 2 == 1:  # after south and north, increase step length
                    steps += 1
        return result
