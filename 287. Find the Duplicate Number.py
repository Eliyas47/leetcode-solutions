class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Detect intersection point in cycle
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find entrance to cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
