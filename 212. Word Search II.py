class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store complete word at end node

class Solution:
    def findWords(self, board, words):
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word  # mark end of word

        rows, cols = len(board), len(board[0])
        result = []

        # Step 2: DFS backtracking
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None  # avoid duplicates

            board[r][c] = "#"  # mark visited
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = ch  # restore

        # Step 3: Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
