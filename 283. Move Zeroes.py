class Solution:
    def moveZeroes(self, nums):
        # Pointer for the position of the next non-zero element
        last_non_zero = 0

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1

        # Fill the remaining positions with zeros
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0
