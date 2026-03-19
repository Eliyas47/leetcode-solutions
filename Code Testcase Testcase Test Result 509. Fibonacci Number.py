class Solution:
    def fib(self, n: int) -> int:
        for i in range n:
             F(0)=0
             F(1)=1
             F(n)=F(n-1)+F(n-2)
        return F(n)
