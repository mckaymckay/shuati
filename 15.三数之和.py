#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)<3:
            return []
        nums.sort()
        res=[]
        for i in nums:
            if nums[i]>0:
                return res

        
# @lc code=end

