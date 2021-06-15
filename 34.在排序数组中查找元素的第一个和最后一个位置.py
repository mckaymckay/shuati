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
        firstPos = self.findfirstPos(nums, target)
        lastPos = self.findlastPos(nums, target)
        return [firstPos, lastPos]

    #找到最初target出现的位置
    def findfirstPos(self, nums, target):
        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                # 小于一定不是解
                left = mid + 1 # 
            else:
                right = mid
        return left

    # 找到最后一个target出现的位置
    def findlastPos(self, nums, target):
        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right + 1) // 2  # 这里是上取整
            if nums[mid] > target:
                # 大于一定不是解
                right = mid - 1
            else:
                left = mid
        return left


# @lc code=end
