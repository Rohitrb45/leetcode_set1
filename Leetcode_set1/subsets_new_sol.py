def subsets(nums):
        ar=[[]]
        for j in nums:
            ar+=[i+[j] for i in ar]
        return ar
nums = [1,2,3]
result = subsets(nums)
print(result)