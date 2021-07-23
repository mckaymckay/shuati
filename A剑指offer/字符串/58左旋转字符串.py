
'''
题目：
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
  限制：
1 <= k < s.length <= 10000
'''


# 解法一：多次使用反转函数

class Solution():
    def reverse(self, s, x, y):
        while x < y:
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1
        return s

    def left_reverse(self, s, k):
        s = list(s)
        self.reverse(s, 0, len(s)-1)
        self.reverse(s, 0, len(s)-1-k)
        self.reverse(s, len(s)-k, len(s)-1)
        return ''.join(s)


test = Solution()
s = "abcdefg"
res = test.left_reverse(s, 2)
print(res)


print('--------------------------------------------------------------')

# 解法二：字符串切片  注意这是str切片


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


print('--------------------------------------------------------------')

# 解法三：列表遍历拼接（看的答案）


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for j in range(n):
            res.append(s[j])
        return ''.join(res)

# 还可以简化为：

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(2, len(s)+2):
            res.append(s[i % len(s)])  # 这个处理，棒啊！
        return ''.join(res)


print('--------------------------------------------------------------')

# 解法四：字符串遍历拼接（看的答案）与列表遍历拼接道理一样

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for j in range(n):
            res += s[j]
        return res

# 还可以简化为：

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(2, len(s)+2):
            res += s[i % len(s)]  # 这个处理，棒啊！
        return res
        
print('--------------------------------------------------------------')

s = "abcdefg"
s = list(s)
print(s)
n = 2
res = []
for i in range(2, len(s)+2):
    res.append(s[i % len(s)])

print(''.join(res))
res=""
for i in range(2,len(s)+2):
    res += s[i%len(s)]
print(res)

