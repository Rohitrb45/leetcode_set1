class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_var={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in dict_var:
                return [i,dict_var[complement]]
            dict_var[num]=i