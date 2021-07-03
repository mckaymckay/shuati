#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, num in enumerate(nums):
            count[num] = i
        for i, num in enumerate(nums):
            j = count.get(target - num)
            if j and i != j:
                return [i, j]
        return []


# @lc code=end
