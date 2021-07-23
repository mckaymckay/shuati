

s = "the sky is blue"
print
s = s.split()
print(s)
left, right = 0, len(s)-1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

print(' '.join(s))

print('-------------------------------------------------------------')

s = "the sky is blue"
s = s.split()
s.reverse()
print(' '.join(s))


class Solution:
    def delete_spaces(self, s):
        length = len(s)
        left, right = 0, length-1
        # 去掉开头的空字符
        while left <= right and s[left] == ' ':  # 考虑全为空格的情况，如果是l<r，就还会留一个空格
            left += 1
        # 去掉末尾的空字符
        while left <= right and s[right] == ' ':
            right -= 1
        # 去掉中间多余的空字符
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverse_word(self, s):
        left,right=0,0
        print(len(s))
        while left<len(s):
            while  right<len(s) and s[right]!=' ':  # 注意这两个条件的先后顺序
                right+=1
            self.reverse(s,left,right-1)
            right+=1
            left=right
        return s

    def reversewords(self,s):
        s=self.delete_spaces(s)
        self.reverse(s,0,len(s)-1)
        self.reverse_word(s)
        return ''.join(s)


test = Solution()
s = " the  sky     is blue "
res = test.delete_spaces(s)
print(1,res)
res=test.reverse(res,0,len(res)-1)
print(2,res)
res=test.reverse_word(res)
print(3,res)

s = " the  sky     is blue "
re =Solution()
print(re.reversewords(s))

