class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        unordered_set<int> ans;

        for (long long a = 1; a <= bound; a *= x) {
            for (long long b = 1; a + b <= bound; b *= y) {
                ans.insert(a + b);

                if (y == 1)
                    break;
            }

            if (x == 1)
                break;
        }

        return vector<int>(ans.begin(), ans.end());
    }
};
