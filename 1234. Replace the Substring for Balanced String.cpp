
class Solution {
public:
    int balancedString(string s) {
        int n = s.size();
        int limit = n / 4;
        int count[128] = {};

        for (char c : s) {
            count[c]++;
        }

        // Already balanced
        if (count['Q'] == limit &&
            count['W'] == limit &&
            count['E'] == limit &&
            count['R'] == limit) {
            return 0;
        }

        int left = 0;
        int ans = n;

        for (int right = 0; right < n; right++) {
            count[s[right]]--;

            while (left <= right &&
                   count['Q'] <= limit &&
                   count['W'] <= limit &&
                   count['E'] <= limit &&
                   count['R'] <= limit) {

                ans = min(ans, right - left + 1);

                count[s[left]]++;
                left++;
            }
        }

        return ans;
    }
};
