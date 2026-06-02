from collections import Counter

class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count)
        ans = 0
        
        for i in range(len(keys)):
            a = keys[i]
            for j in range(i, len(keys)):
                b = keys[j]
                c = target - a - b
                if c < b:
                    continue
                if c not in count:
                    continue

                # Case 1: all distinct
                if a < b < c:
                    ans += count[a] * count[b] * count[c]
                # Case 2: a == b != c
                elif a == b and b < c:
                    ans += (count[a] * (count[a] - 1) // 2) * count[c]
                # Case 3: a < b == c
                elif a < b and b == c:
                    ans += count[a] * (count[b] * (count[b] - 1) // 2)
                # Case 4: a == b == c
                elif a == b == c:
                    ans += count[a] * (count[a] - 1) * (count[a] - 2) // 6
        
        return ans % MOD
