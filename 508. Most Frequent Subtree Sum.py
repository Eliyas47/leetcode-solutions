from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root):
        if not root:
            return []
        
        freq = defaultdict(int)
        
        def dfs(node):
            if not node:
                return 0
            # Compute subtree sum
            s = node.val + dfs(node.left) + dfs(node.right)
            freq[s] += 1
            return s
        
        dfs(root)
        
        # Find max frequency
        max_freq = max(freq.values())
        
        # Collect all sums with max frequency
        return [s for s, count in freq.items() if count == max_freq]
