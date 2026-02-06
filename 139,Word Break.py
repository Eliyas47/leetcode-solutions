class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)   # faster lookup
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for word in word_set:
                if i >= len(word) and dp[i - len(word)] and s[i-len(word):i] == word:
                    dp[i] = True
                    break   # no need to check further words
        
        return dp[len(s)]
