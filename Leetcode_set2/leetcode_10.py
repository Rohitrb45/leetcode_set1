class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem={}
        def backtrack(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            ismatch= i<len(s) and (s[i]==p[j] or p[j]==".")
            if (j+1) < len(p) and p[j+1]=="*":
                print(i,j)
                mem[(i,j)]=(backtrack(i,j+2) or
                           (ismatch and backtrack(i+1,j)))
                return mem[(i,j)]
            if ismatch:
                mem[(i,j)]=backtrack(i+1,j+1)
                return  mem[(i,j)]
            mem[(i,j)]=False
            return False
             
        return backtrack(0,0)