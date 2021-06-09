# 寻找旋转排序数组中的最小值

# 🚗 1.最简单的方法：遍历得到最小值
# def findmin(nums):
#     length = len(nums)
#     if length != 0:
#         min, r = nums[0], 0
#         for p in range(length):
#             if min > nums[p]:
#                 min = nums[p]
#                 r = p
#                 break
#         return min, r, nums[r:] + nums[:r]
#     return None


# 🚗 2.二分查找方法
def findmin2(nums):
    length = len(nums)
    if length != 0:
        low, high = 0, length - 1
        while low < high:  # 注意初始条件
            pivot = (low + high) // 2
            if nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high = pivot
        return nums[low]  # 注意返回值
    return None


mylist = [6]
res = findmin2(mylist)
print(res)

# 注意 和正常二分查找初始条件的稍稍差别
# 注意二分查找循环的初始条件啊，咋还忘了呢

# 二分查找思路
# 根据二分查找的思想，pivot 位于 low-high 之间，如nums[pivot]>nums[high]，说明最小值在pivot-high之间,
# 如果nums[pivot]<nums[high],则说明最小值位于low-pivot之间
