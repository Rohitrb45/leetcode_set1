def nextPermutation(nums):
       inf_point=0
       #min=sys.maxsize
     

       for i in range(len(nums)-1,-1,-1):
           if nums[i]>nums[i-1]:
               inf_point=i
               break
       if inf_point==0:
            nums.sort() 

       else:
            toswap=nums[inf_point-1]
            for j in range(inf_point,len(nums)):
                if(nums[j]>toswap):
                    temp=nums[j]
                    nums[j]=nums[inf_point-1]
                    nums[inf_point-1]=temp

            nums[inf_point:]=sorted(nums[inf_point:])

       print(nums)
nums=[7,2,5,3,1]
nextPermutation(nums)