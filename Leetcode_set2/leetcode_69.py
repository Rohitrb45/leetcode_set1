class Solution:
    def mySqrt(self, x: int) -> int:
        result=0
        low=0
        high=x
        if x==1 or x==0:
            return x
        while low<=high:
            mid=(low+high)//2
            sq=mid*mid
            print(sq)
            if sq==x:
                return mid
            elif sq>x:
                high=mid-1 
            else:
                low=mid+1
                result=mid
                


        return result