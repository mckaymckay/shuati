#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#


# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s) - 1, 2 * k):
            s[i:i+k] = self.reverse(s[i:i+k])
        return (''.join(s))

    def reverse(self, s):
        x, y = 0, len(s) - 1
        while x < y:
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1
        return s


# @lc code=end
