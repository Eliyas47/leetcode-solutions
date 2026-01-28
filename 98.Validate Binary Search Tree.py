# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Helper function with min and max boundaries
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            # The current node's value must be within the range
            if node.val <= low or node.val >= high:
                return False
            
            # Left subtree must be < node.val
            # Right subtree must be > node.val
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)


# Example usage:
# Constructing a simple BST
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

solution = Solution()
print(solution.isValidBST(root))  # Output: True
