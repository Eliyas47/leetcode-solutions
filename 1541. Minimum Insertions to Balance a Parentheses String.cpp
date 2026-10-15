
class Solution {
public:
    int minInsertions(string s) {
        int ans = 0;
        int open = 0;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                open++;
            } else {
                // Check whether the next ')' forms a pair
                if (i + 1 < s.size() && s[i + 1] == ')') {
                    i++;
                } else {
                    // Insert the missing ')'
                    ans++;
                }

                // Match this pair with an opening '('
                if (open > 0) {
                    open--;
                } else {
                    // Insert a missing '('
                    ans++;
                }
            }
        }

        // Each unmatched '(' needs two ')'
        return ans + 2 * open;
    }
};
