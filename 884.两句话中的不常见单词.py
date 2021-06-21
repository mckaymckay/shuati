#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#


# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count={}
        c=s1.split()+s2.split()
        for i in c:
            count[i]=count.get(i,0)+1
        # res=[]
        # for i in count:
        #     if count[i]==1:
        #         res.append(i)
        # return res
        return [i for i in count if count[i]==1]

# @lc code=end
