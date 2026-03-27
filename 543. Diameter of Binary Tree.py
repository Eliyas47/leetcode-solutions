# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            # Recursively find depth of left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Update diameter at this node
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return height of subtree rooted at this node
            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.diameter
