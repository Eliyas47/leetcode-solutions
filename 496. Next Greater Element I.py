class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        varFiltersCg = {}   # map each number to its next greater
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                varFiltersCg[stack.pop()] = num
            stack.append(num)
        
        varOcg = [varFiltersCg.get(x, -1) for x in nums1]
        return varOcg

# Example test
print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1, 3, -1]
