#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ln, lt = len(name), len(typed)
        if ln > lt or name[0] != typed[0]: 
            return False

        i, j = 0, 0
        while j<lt :  # 一定要遍历完typed，才能判断最后一个字符
            if i < ln and name[i] == typed[j]:
                i += 1
                j += 1
            elif name[i-1] == typed[j]:
                j += 1
            else:
                return False
        return i == ln
# @lc code=end

