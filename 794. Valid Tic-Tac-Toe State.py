class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(player: str) -> bool:
            # Check rows and columns
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False

        countX = sum(row.count('X') for row in board)
        countO = sum(row.count('O') for row in board)

        # Rule 1: X always goes first
        if not (countX == countO or countX == countO + 1):
            return False

        xWin, oWin = win('X'), win('O')

        # Rule 2: Both cannot win
        if xWin and oWin:
            return False
        # Rule 3: If X wins, must have one more move
        if xWin and countX != countO + 1:
            return False
        # Rule 4: If O wins, must have equal moves
        if oWin and countX != countO:
            return False

        return True
