class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=-sys.maxsize
        print("min",max_sum)
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]

            if(sum<nums[i]):
                sum=nums[i]
            
            if(sum>max_sum):
                max_sum=sum
                
    
                

        return max_sum