#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i, j = 0, 1
        if length==0:
            return 0
        for j in range(1,length):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1


# @lc code=end
