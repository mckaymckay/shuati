#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        i, j = 0, 0
        for j in range(length):
            if nums[j] != val:
                
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


# @lc code=end
