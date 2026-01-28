# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # Variables to track the two nodes that need swapping
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        # Inorder traversal to detect misplaced nodes
        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # If current node is smaller than previous, it's misplaced
            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node

            inorder(node.right)

        # Run inorder traversal
        inorder(root)

        # Swap the values of the two wrong nodes
        self.first.val, self.second.val = self.second.val, self.first.val


# Example usage:
# Constructing a BST with swapped nodes
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)  # <-- Wrong placement

solution = Solution()
solution.recoverTree(root)

# After recovery, inorder traversal should be [1, 2, 3, 4]
def inorder_print(node):
    if not node:
        return
    inorder_print(node.left)
    print(node.val, end=" ")
    inorder_print(node.right)

inorder_print(root)  # Output: 1 2 3 4
