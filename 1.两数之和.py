#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        if length:
            for i in range(length-1):
                for j in range(i+1,length):
                    if nums[i]+nums[j]==target:
                        return [i,j]
                    
                
        else:
            return []
# @lc code=end

