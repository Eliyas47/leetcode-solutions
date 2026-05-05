class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        index = {x: i for i, x in enumerate(arr)}
        
        for x in arr:
            dp[x] = 1  # single-node tree
            for a in arr:
                if a >= x:  # no need to check larger factors
                    break
                if x % a == 0:  # a is a factor
                    b = x // a
                    if b in dp:
                        dp[x] += dp[a] * dp[b]
            dp[x] %= MOD
        
        return sum(dp.values()) % MOD
