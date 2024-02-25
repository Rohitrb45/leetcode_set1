class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out=[]
        def combination(start,cmb):
            if(k==len(cmb)):
                out.append(cmb.copy())
                return
            for i in range(start,n+1):
                cmb.append(i)
                combination(i+1,cmb)
                cmb.pop()

        combination(1,[])
        return out