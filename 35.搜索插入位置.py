#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length != 0:
            low, high = 0, length-1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] > target:
                    high = mid-1
                elif nums[mid] < target:
                    low = mid+1
                else:
                    return mid
            return low
            # if target<=nums[0]:
            #     return 0
            # elif target>nums[length-1]:
            #     return length
            # else:
            #     for j in range(length):
            #         if nums[j]>=target:
            #             return j
# @lc code=end
