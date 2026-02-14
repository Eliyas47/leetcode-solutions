class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.prefix = []
            return
        
        m, n = len(matrix), len(matrix[0])
        # Build prefix sum matrix with extra row/col for easier calculation
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                self.prefix[i+1][j+1] = (
                    matrix[i][j] 
                    + self.prefix[i][j+1] 
                    + self.prefix[i+1][j] 
                    - self.prefix[i][j]
                )

    def sumRegion(self, row1, col1, row2, col2):
        # Use inclusion-exclusion principle
        return (
            self.prefix[row2+1][col2+1]
            - self.prefix[row1][col2+1]
            - self.prefix[row2+1][col1]
            + self.prefix[row1][col1]
        )
