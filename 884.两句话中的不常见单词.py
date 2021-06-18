#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#


# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        C = s1.split() + s2.split()
        count = {}
        for i in C:
            count[i] = count.get(i, 0) + 1
        return [ i for i in count.keys() if count[i]==1]

# @lc code=end
