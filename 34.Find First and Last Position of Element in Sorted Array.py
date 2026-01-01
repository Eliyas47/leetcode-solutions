class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Helper to find the first index >= target
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # Helper to find the last index <= target
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_index = findLeft(nums, target)
        right_index = findRight(nums, target)

        # If target is not found, return [-1, -1]
        if left_index <= right_index and left_index < len(nums) and nums[left_index] == target:
            return [left_index, right_index]
        return [-1, -1]
