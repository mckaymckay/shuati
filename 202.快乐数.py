#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)
        while slow != fast and fast != 1:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        return fast == 1

    def get_next(self, n):
        while n > 0:
            res = 0
            n, b = divmod(n, 10)
            res += b**2
        return res


# @lc code=end
