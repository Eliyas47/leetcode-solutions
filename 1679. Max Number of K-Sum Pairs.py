class Solution:
    def maxOperations(self, nums, k):
        seen = {}
        operations = 0

        for num in nums:
            complement = k - num

            if seen.get(complement, 0) > 0:
                operations += 1
                seen[complement] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1

        return operations
