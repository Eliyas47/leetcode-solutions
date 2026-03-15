# __define-ocg__: Sum of Left Leaves solution

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        def dfs(node, is_left):
            if not node:
                return 0
            # Check if it's a leaf
            if not node.left and not node.right:
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)
        
        varOcg = dfs(root, False)
        return varOcg
