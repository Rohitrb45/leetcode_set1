class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        res=0
        while(i<len(s)):
           r1=roman(s[i])
           if(i+1<len(s)):
                r2=roman(s[i+1])
                if(r1>=r2):
                  res=res+r1
                  i=i+1
                else:
                  res=res+r2-r1
                  i=i+2
           else:
                 res=res+r1  
                 i=i+1
        return res
       
             
def roman(r):
    if(r=='I'):
        return 1
    if(r=='V'):
        return 5
    if(r=='X'):
        return 10
    if(r=='L'):
        return 50
    if(r=='C'):
        return 100
    if(r=='D'):
        return 500
    if(r=='M'):
        return 1000   
        
    return -1
        
        