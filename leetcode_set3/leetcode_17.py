class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out=[]
        lettertochar={"2":"abc",
                      "3":"def",
                      "4":"ghi",
                      "5":"jkl",
                      "6":"mno",
                      "7":"pqrs",
                      "8":"tuv",
                      "9":"wxyz" }
        def lc(l,s):
            if len(digits)==len(s):
                out.append(s)
                return
            
            for c in lettertochar[digits[l]]:
                #s+=c
                lc(l+1,s+c)
        
        if digits:
            lc(0,"")
        return out