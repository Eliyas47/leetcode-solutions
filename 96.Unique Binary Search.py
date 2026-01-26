class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # Base cases

        # Fill dp array using the recursive formula
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]
