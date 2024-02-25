class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out=[]
        quad=[]
        nums.sort()
        #print(nums)
        def ksum(start,target,k):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if(i>start and nums[i]==nums[i-1]):
                        continue
                    quad.append(nums[i])
                    ksum(i+1,target-nums[i],k-1)
                    quad.pop()
                return
            l=start
            r=len(nums)-1
            for i in range(start, len(nums)-1):
                while(l<r):
                    if nums[l]+nums[r]> target:
                        r-=1
                    elif nums[l]+nums[r]<target:
                        l+=1
                    else:
                        out.append(quad+[nums[l],nums[r]])
                        l+=1
                        while r>l and nums[l-1]==nums[l]:
                            l+=1
        ksum(0,target,4)
        return out