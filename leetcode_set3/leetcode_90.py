class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out=[]
        #lst=[]
        nums.sort()
        def rec(i,lst):
            if(i==len(nums)):
                out.append(lst[::])
                return
            
            lst.append(nums[i])
            rec(i+1,lst)
            lst.pop()

            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1
            rec(i+1,lst)

        rec(0,[])
        return out