# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        result = []

        def dfs(node, current_path, current_sum):
            if not node:
                return

            # include current node
            current_path.append(node.val)
            current_sum += node.val

            # check if it's a leaf and sum matches
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))  # copy path

            # explore children
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)

            # backtrack
            current_path.pop()

        dfs(root, [], 0)
        return result
