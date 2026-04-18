class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            for ch in str(num):
                d = int(ch)
                if d == 0 or num % d != 0:
                    return False
            return True
        
        result = []
        for n in range(left, right + 1):
            if is_self_dividing(n):
                result.append(n)
        return result
