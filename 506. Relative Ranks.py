class Solution:
    def findRelativeRanks(self, score):
        # Step 1: Sort scores with their original indices
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
        
        # Step 2: Prepare result list
        result = [""] * len(score)
        
        # Step 3: Assign ranks
        for rank, (idx, _) in enumerate(sorted_scores):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        
        return result
