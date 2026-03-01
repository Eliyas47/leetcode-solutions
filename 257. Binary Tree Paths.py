class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # List to store all paths
        paths = []
        
        # Helper function
        def dfs(node, path):
            if not node:
                return
            
            # append current node value
            path += str(node.val)
            
            # if leaf, add path to results
            if not node.left and not node.right:
                paths.append(path)
            else:
                # if not leaf, add separator and recurse
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)
        
        dfs(root, "")
        return paths
