class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out=[]
        def csum(i,curr,total):
            if total==target:
                out.append(curr.copy())
                return
            if i>=len(candidates) or total>target:
                return
            curr.append(candidates[i])
            csum(i,curr,total+candidates[i])
            curr.pop()
            csum(i+1,curr,total)

        csum(0,[],0)
        return out