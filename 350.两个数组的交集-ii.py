#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#


# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        res = []
        count = {}
        for i in nums1:
            count[i] = count.get(i, 0) + 1
        for j in nums2:
            if count.get(j, 0) > 0:
                count[j] = count.get(j) - 1
                res.append(j)
        return res


# @lc code=end
