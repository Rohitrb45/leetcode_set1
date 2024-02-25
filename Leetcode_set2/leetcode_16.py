import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        close_sum=0
        ind=sys.maxsize-1
        nums.sort()
        for i in range(len(nums)):
            sum=0
            left=i+1
            right=len(nums)-1
            if(i>0 and nums[i]==nums[i-1]):
                continue
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if(sum==target):
                    return sum
                elif sum>target:
                    right-=1
                else:
                    left+=1
                diff=abs(sum-target)
                #print(diff)
                if(diff<ind):
                    ind=diff
                    close_sum=sum
                    #print(close_sum)
        return close_sum