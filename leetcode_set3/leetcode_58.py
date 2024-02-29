class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)-1
        count=0
        while(s[n]==" "):
            n-=1
        for i in range(n,-1,-1):
            if(s[i]==" "):
                break
            count+=1
        return count