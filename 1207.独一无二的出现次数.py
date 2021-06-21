#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count={}
        res=[]
        for i in arr:
            count[i]=count.get(i,0)+1

        for j in count:
            res.append(count[j])
            
        res=list(set(res))
        return len(count)==len(res)

        

        
# @lc code=end

