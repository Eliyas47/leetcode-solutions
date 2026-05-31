from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        m = mass
        for x in asteroids:
            if m < x:
                return False
            m += x
        return True
