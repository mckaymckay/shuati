#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        count1 = set(nums1)
        count2 = set(nums2)
        if len(count1) > len(count2):
            return self.intersection(nums2, nums1)
        res = []
        return [i for i in count1 if i in count2]


# @lc code=end
