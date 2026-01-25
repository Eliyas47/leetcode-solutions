# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                # Generate all left and right subtrees
                left_trees = build(start, i - 1)
                right_trees = build(i + 1, end)
                
                # Combine each left and right with root i
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
            
            return all_trees
        
        return build(1, n)
