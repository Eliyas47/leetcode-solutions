class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # Check if it's a leaf
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recurse on left and right with reduced target
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
