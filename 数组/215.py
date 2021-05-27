# 基于快排:
def quick_partition(nums, i, j):
    if i >= j:
        return nums
    pivot = nums[i]
    low, high = i, j
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]
    nums[i] = pivot
    quick_partition(nums, low, i - 1)
    quick_partition(nums, i + 1, high)
    


nums = [3, 2, 1, 5, 6, 4]
length = len(nums)
quick_partition(nums, 0, length - 1)
print(nums)