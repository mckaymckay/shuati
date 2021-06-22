#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#


# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        twofound, notfound=-1,-1
        for j in range(1, length + 1):
            if j not in count:
                notfound = j
            elif count[j] == 2:
                twofound = j
            if twofound>0 and notfound>0:
                break
        return [twofound, notfound]


# @lc code=end
