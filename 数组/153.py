# 寻找旋转排序数组中的最小值


# 最简单的方法：遍历得到最小值
def findmin(nums):
    length = len(nums)
    if length != 0:
        min, r = nums[0], 0
        for p in range(length):
            if min > nums[p]:
                min = nums[p]
                r = p
                break
        return min, r, nums[r:] + nums[:r]
    return None


mylist = [3, 4, 5]
res = findmin(mylist)
print(res)