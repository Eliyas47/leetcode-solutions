# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        # Push all left children onto stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop smallest node
        node = self.stack.pop()
        val = node.val
        # Push left path of right child
        if node.right:
            self._push_left(node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
