class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, target):
            # If we have k numbers and target is 0, add to result
            if len(path) == k and target == 0:
                result.append(path[:])
                return

            # If too many numbers or target < 0, stop
            if len(path) > k or target < 0:
                return

            # Try numbers from 'start' to 9
            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, path, target - num)
                path.pop()

        backtrack(1, [], n)
        return result
