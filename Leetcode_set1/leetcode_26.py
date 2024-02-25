class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_list=[]
        for i in nums:
          if i not in unique_list:
            unique_list.append(i)
            #print(i)
        nums[:] = unique_list
        return len(nums)