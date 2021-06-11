#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length != 0:
            # arr=[]
            # for i in range(length):
            #     if target==nums[i]:
            #         arr.append(i)
            # len_arr=len(arr)
            # return [min(arr),max(arr)] if len_arr!=0 else [-1,-1]
            low = 0, high = length - 1
            while low <= high:
                mid = (low + high) // 2
                arr=[]
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    arr.append(mid)
                    
        else:
            return [-1, -1]


# @lc code=end
