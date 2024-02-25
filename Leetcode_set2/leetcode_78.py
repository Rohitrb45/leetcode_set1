class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out=[]
        tmp=[]
        def cset(start):
            if start>=len(nums):
                out.append(tmp.copy())
                return
            tmp.append(nums[start])
            cset(start+1)
            tmp.pop()
            cset(start+1)

        cset(0)
        return out