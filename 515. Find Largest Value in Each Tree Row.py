class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level_max = float('-inf')
            next_level = []
            
            for node in queue:
                level_max = max(level_max, node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            result.append(level_max)
            queue = next_level
        
        return result
