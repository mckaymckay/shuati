#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        for i in range(length - 1):
            for j in range(i + 1, length - 1):
                if 0 - nums[i] - nums[j] in nums[j + 1:]:
                    pass


# @lc code=end
