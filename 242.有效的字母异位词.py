#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1
        for j in t:
            count[j] = count.get(j, 0) - 1
            if count.get(j, 0) < 0:
                return False
        return True


# @lc code=end
