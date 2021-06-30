#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        a, b = 0, 0
        # 所有数字的异或结果
        for i in nums:
            res ^= i

        # 找到res第一个不为0的位置
        # h = 1
        # while (res & h == 0):
        #     h << 1
        h = res & -res

        # 按照i进行分组
        for j in nums:
            if j & h == 0:
                a ^= j
        return [a, a ^ res]


# @lc code=end
