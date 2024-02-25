class Solution:
    def climbStairs(self, n: int) -> int:
        c=0
        a=1
        b=1
        if n==1:
            return 1
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return c