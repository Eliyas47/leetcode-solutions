class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # Convert to list for easy manipulation
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters in the current 2k block
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
