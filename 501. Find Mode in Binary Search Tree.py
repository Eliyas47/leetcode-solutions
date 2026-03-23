class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict
        
        freq = defaultdict(int)
        
        def dfs(node):
            if not node:
                return
            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        max_freq = max(freq.values())
        return [val for val, count in freq.items() if count == max_freq]
