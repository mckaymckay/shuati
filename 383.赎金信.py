#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        count = {}
        for i in magazine:
            count[i] = count.get(i, 0) + 1
        for j in ransomNote:
            count[j] = count.get(j, 0) - 1  # 这一步很重要
            if count[j] < 0:
                return False
        return True  # return的位置


# @lc code=end
