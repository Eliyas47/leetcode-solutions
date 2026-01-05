from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # sort to handle duplicates easily

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])  # found a valid combination
                return
            if remaining < 0:
                return  # stop if sum exceeded

            prev = -1
            for i in range(start, len(candidates)):
                # skip duplicates
                if candidates[i] == prev:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res
