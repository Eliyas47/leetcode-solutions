class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        def dfs(node, current_depth):
            if not node:
                return
            if current_depth == depth - 1:
                old_left, old_right = node.left, node.right
                node.left = TreeNode(val, old_left, None)
                node.right = TreeNode(val, None, old_right)
            else:
                dfs(node.left, current_depth + 1)
                dfs(node.right, current_depth + 1)
        
        dfs(root, 1)
        return root
