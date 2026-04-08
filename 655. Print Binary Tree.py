class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHeight(node):
            if not node:
                return -1
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        height = getHeight(root)
        rows, cols = height + 1, (1 << (height + 1)) - 1
        res = [["" for _ in range(cols)] for _ in range(rows)]
        
        def fill(node, r, c, h):
            if not node:
                return
            res[r][c] = str(node.val)
            if node.left:
                fill(node.left, r+1, c - (1 << (h-r-1)), h)
            if node.right:
                fill(node.right, r+1, c + (1 << (h-r-1)), h)
        
        fill(root, 0, (cols-1)//2, height)
        return res
