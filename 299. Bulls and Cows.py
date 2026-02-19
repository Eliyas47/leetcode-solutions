class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        # Frequency maps for non-bull digits
        secret_count = {}
        guess_count = {}

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] = secret_count.get(s, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1

        # Count cows by matching frequencies
        for digit in guess_count:
            if digit in secret_count:
                cows += min(secret_count[digit], guess_count[digit])

        return f"{bulls}A{cows}B"
