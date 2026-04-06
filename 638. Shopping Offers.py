from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(needs_tuple):
            needs = list(needs_tuple)
            # Base cost: buy items individually
            cost = sum(needs[i] * price[i] for i in range(len(price)))
            
            # Try each special offer
            for offer in special:
                new_needs = []
                for i in range(len(price)):
                    if needs[i] < offer[i]:
                        break
                    new_needs.append(needs[i] - offer[i])
                else:  # valid offer
                    cost = min(cost, offer[-1] + dfs(tuple(new_needs)))
            
            return cost
        
        return dfs(tuple(needs))
