class Solution:
    def flipgame(self, fronts, backs):
        # Step 1: Identify forbidden numbers (same on both sides of a card)
        forbidden = {f for f, b in zip(fronts, backs) if f == b}
        
        # Step 2: Collect candidates from both arrays
        candidates = set(fronts + backs) - forbidden
        
        # Step 3: Find the minimum good integer
        return min(candidates) if candidates else 0
