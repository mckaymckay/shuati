# 长度最小的'连续'子数组
def minSubArrayLen(nums, val):
    length = len(nums)
    if length != 0:
        i = 0
        j = 0
        res = 0  
        sub_len = length + 1  #存放结果数组的长度##################
        while j < length:
            res += nums[j]
            while res >= val:
                sub_len = min(j - i + 1, sub_len)
                res -= nums[i]
                i += 1
            j += 1
        return 0 if sub_len == length + 1 else sub_len  ####################
    return 0


nums = [2, 3, 1, 2, 4, 3]
val = 7
print(minSubArrayLen(nums, val))

nums1 = [1, 1, 1, 1, 1, 1, 1, 1]
val1 = 11
print(minSubArrayLen(nums1, val1))

# 📒：考点总结
# while循环
# return 一个‘if’语句

# 🚗：解题思路
# 注意读题：要返回一个‘连续子数组’;
# 注意‘while’循环的用法，在第二次判断的过程中可以灵活运用;
# sub_len的初始值如何设置;
# 特殊情况：如果整个数组加起来小于‘val‘，如何处理返回值;