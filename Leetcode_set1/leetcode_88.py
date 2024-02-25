class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j,k=0,0
        temp_nums=nums1[:m]
        while(i<=m-1 and j<=n-1):
            if(temp_nums[i]>=nums2[j]):
                nums1[k]=nums2[j]
                k+=1
                j+=1
            else:
                nums1[k]=temp_nums[i]
                i+=1
                k+=1
                

        while i<=m-1:
            nums1[k]=temp_nums[i]
            i+=1
            k+=1
        while j<=n-1: 
            nums1[k]=nums2[j]
            j+=1
            k+=1 