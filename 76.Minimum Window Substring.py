from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count characters in t
        need = Counter(t)
        missing = len(t)

        left = start = end = 0

        for right, char in enumerate(s, 1):  # right is 1-based
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            # When all chars are covered
            if missing == 0:
                # Move left to shrink window
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # Update best window
                if end == 0 or right - left < end - start:
                    start, end = left, right

                # Prepare for next window
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]
