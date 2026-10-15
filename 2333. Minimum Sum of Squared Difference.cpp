
class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2,
                               int k1, int k2) {
        int k = k1 + k2;
        vector<int> cnt(100001, 0);
        long long total = 0;
        int mx = 0;

        for (int i = 0; i < nums1.size(); i++) {
            int d = abs(nums1[i] - nums2[i]);
            cnt[d]++;
            total += d;
            mx = max(mx, d);
        }

        if (total <= k) return 0;

        for (int d = mx; d > 0 && k > 0; d--) {
            int take = min(cnt[d], k);
            cnt[d] -= take;
            cnt[d - 1] += take;
            k -= take;
        }

        long long ans = 0;

        for (int d = 0; d <= mx; d++) {
            ans += 1LL * d * d * cnt[d];
        }

        return ans;
    }
};
