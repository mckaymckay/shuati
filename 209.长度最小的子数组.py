#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        if length != 0:
            i, j = 0, 0
            sublen = length + 1
            total = 0
            while j < length:
                total += nums[j]
                while total >= target:
                    sublen = min(j - i + 1,sublen)
                    total -= nums[i]
                    i += 1
                j += 1
            return 0 if sublen==length+1 else sublen
        return 0


# @lc code=end
