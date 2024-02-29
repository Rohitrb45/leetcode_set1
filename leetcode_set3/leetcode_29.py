class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=1
        q=0
        
        if divisor<0 or dividend<0:
            sign=-1
        if divisor<0 and dividend<0:
            sign=1
        divisor=abs(divisor)
        dividend=abs(dividend)
        while(dividend>=divisor):
            count=0
            while dividend-(divisor<<1<<count)>=0:
                count+=1
                
            
            q+=1<<count
            dividend-=divisor<<count

        q=q*sign
        return min(2147483647,max(q,-2147483648))