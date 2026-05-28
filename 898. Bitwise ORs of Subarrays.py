class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res, cur = set(), set()
        for num in arr:
            cur = {num} | {x | num for x in cur}
            res |= cur
        return len(res)
