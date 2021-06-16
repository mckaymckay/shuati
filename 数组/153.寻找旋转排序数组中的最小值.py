#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        length=len(nums)
        if length!=0:
            left,right=0,length-1
            while left <right:
                target=nums[right]
                mid=(left+right)//2
                if nums[mid]>target:
                    left=mid+1
                else:
                    right=mid
            return nums[left]
# @lc code=end

