#
# @lc app=leetcode.cn id=1877 lang=python3
#
# [1877] 数组中最大数对和的最小值
#


# @lc code=start
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        length = len(nums)

        if len(nums) % 2 != 0:
            return

        nums.sort()
        res = 0
        for i in range(length // 2):
            res = max(res, nums[i] + nums[length - i - 1])
        return res


# @lc code=end
