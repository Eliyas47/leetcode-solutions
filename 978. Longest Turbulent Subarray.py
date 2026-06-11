class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int n = arr.size();
        if (n == 1) return 1;

        int ans = 1;
        int cur = 1;
        int prev = 0;

        for (int i = 1; i < n; i++) {
            int cmp = 0;

            if (arr[i] > arr[i - 1])
                cmp = 1;
            else if (arr[i] < arr[i - 1])
                cmp = -1;

            if (cmp == 0) {
                cur = 1;
            } else if (cmp * prev == -1) {
                cur++;
            } else {
                cur = 2;
            }

            ans = max(ans, cur);
            prev = cmp;
        }

        return ans;
    }
};
