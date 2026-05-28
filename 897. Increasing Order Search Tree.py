class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.curr.right = TreeNode(node.val)
            self.curr = self.curr.right
            inorder(node.right)
        
        dummy = TreeNode(-1)
        self.curr = dummy
        inorder(root)
        return dummy.right
