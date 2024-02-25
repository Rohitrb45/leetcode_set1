class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out=[]
        unique_set=[]
        left=0
        right=len(nums)-1
        nums.sort()
        count=0
        #print(nums)
        for i in range(0, len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            sum=0
            while(left<right):
                sum=nums[i]+nums[left]+nums[right]
                if(sum==0):
                    out=[nums[i],nums[left],nums[right]]
                    if out not in unique_set:
                        unique_set.append(out)
                    #unique_set.append([nums[i],nums[left],nums[right]])
                    count+=1
                    #print(out)
                    left+=1
                    while(nums[left]==nums[left-1] and left<right):
                        left+=1
                    #right-=1
                if(sum>0):
                    right-=1
                if(sum<0):
                    left+=1

        #print(count)
        return unique_set
