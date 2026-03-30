class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Push children in reverse order so leftmost is processed first
            stack.extend(reversed(node.children))
        
        return result
