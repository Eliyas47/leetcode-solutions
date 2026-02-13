class Solution:
    def gameOfLife(self, board):
        rows, cols = len(board), len(board[0])

        def count_live_neighbors(r, c):
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)
            ]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                    count += 1
            return count

        # Step 1: Apply rules with temporary states
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)

                # Rule 1 or 3: Live cell dies
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # -1 means cell was alive but will die

                # Rule 4: Dead cell becomes alive
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2   # 2 means cell was dead but will live

        # Step 2: Finalize states
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
