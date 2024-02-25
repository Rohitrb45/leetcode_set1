class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        num=0
        sign=1
        while(i<len(s) and s[i].isspace()):
            i+=1
        if(i<len(s)and (s[i]=='-' or s[i]=='+')):
            sign = -1 if s[i] == '-' else 1
            i += 1
        while(i<len(s) and s[i].isdigit()):
            num=num*10+int((s[i]))
            print(int(s[i]))
            i+=1
        num=sign*num
        num=max(min(num, 2**31 - 1), -2**31)
        #min(max(-2**31-1,num),2**31)
        return num