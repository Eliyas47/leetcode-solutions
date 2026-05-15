class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        runs = []
        count = 1
        
        # Count consecutive runs
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                runs.append(count)
                count = 1
        runs.append(count)
        
        # Count valid substrings
        result = 0
        for i in range(1, len(runs)):
            result += min(runs[i-1], runs[i])
        
        return result
