#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if target not in nums:
            return [-1, -1]
        # firstPos = self.findfirstPos(nums, target)
        firstPos = self.findTarget(nums, target)
        lastPos = self.findTarget(nums, target + 1) - 1
        # lastPos = self.findlastPos(nums, target)
        return [firstPos, lastPos]


    # 思路:寻找第一个等于target的位置，寻找第一个target+1的位置，再往前移动一个位置，这样一个二分查找函数就能解决。
    def findTarget(self, nums, target):
        length = len(nums)
        if length != 0:
            left, right = 0, length
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        else:
            return [-1, -1]


# @lc code=end
