#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res_set = set()
        res_sum, set_sum = 0, 0
        for i in nums:
            res_sum += i  # 所有元素的和
            res_set.add(i)

        for k in res_set:
            set_sum += k  # set中的元素的和
        return (3 * set_sum - res_sum) // 2


# @lc code=end
