class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        def modified_bs(left,right):
            if left>right:
                return -1
            mid=left+(right-left)//2
            if(nums[mid]==target):
                return mid
            if(nums[mid]>=nums[left]):
                if(target<=nums[mid] and target>=nums[left]):
                    return modified_bs(left,mid-1)
                else:
                    return modified_bs(mid+1,right)
            else:
                if(target>=nums[mid] and target<=nums[right] ):
                    return modified_bs(mid+1,right)
                else:
                    return modified_bs(left,mid-1)

        return modified_bs(0,len(nums)-1)