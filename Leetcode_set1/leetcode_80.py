def merge(nums1, m, nums2, n):
    i, j, k = 0, 0, 0
    temp_nums1 = nums1[:m]  # Create a copy of the initial elements in nums1

    while i < m and j < n:
        if temp_nums1[i] <= nums2[j]:
            nums1[k] = temp_nums1[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    while i < m:
        nums1[k] = temp_nums1[i]
        i += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)
