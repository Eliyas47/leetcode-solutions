from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def mod_pow(x, n):
            result = 1
            x %= MOD
            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return result

        if not b:
            return 1

        last_digit = b.pop()
        part1 = mod_pow(self.superPow(a, b), 10)
        part2 = mod_pow(a, last_digit)
        return (part1 * part2) % MOD
