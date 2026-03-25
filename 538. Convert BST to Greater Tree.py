# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.running_sum = 0
        
        def reverse_inorder(node):
            if not node:
                return
            # Traverse right subtree first
            reverse_inorder(node.right)
            
            # Update running sum and node value
            self.running_sum += node.val
            node.val = self.running_sum
            
            # Traverse left subtree
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root
