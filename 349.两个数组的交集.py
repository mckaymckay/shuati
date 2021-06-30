#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        res_set=set()
        for i in nums2:
            if i in set1:
                res_set.add(i)
        return list(res_set)
        


# @lc code=end
