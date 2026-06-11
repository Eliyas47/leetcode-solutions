class Solution {
public:
    string ans = "~";

    void dfs(TreeNode* node, string path) {
        if (!node) return;

        path = char('a' + node->val) + path;

        if (!node->left && !node->right) {
            if (path < ans)
                ans = path;
            return;
        }

        dfs(node->left, path);
        dfs(node->right, path);
    }

    string smallestFromLeaf(TreeNode* root) {
        dfs(root, "");
        return ans;
    }
};
