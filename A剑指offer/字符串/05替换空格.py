'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

'''

s = "We are happy."
r = s.split()
res = []

for i in s:
    print(i)
    if i == ' ':
        i = "%20"
    res.append(i)
print(''.join(res))

print('--------------------------------------------------------------')




'''
最开始的想法：XXXXXXXXXX 

这个方法不得行啊 如果连续好多空格的话就不适用了

注意 s 和 ss 的type：
print(type(s))  # <class 'str'>
print(type(ss))  # <class 'list'>
'''
def xxreplace(s):  # str
    ss = s.split()  # list
    res = []
    for i in ss:
        res.append(i + "%20")
    res = ''.join(res)
    return res[:-3]


s = "We are happy."
res = xxreplace(s)
print(res)


'''
解法-：以暴制暴,遍历每个元素，遇到空格就替换成字符
'''
def replace(s):
    res = []
    for i in s:
        if i == ' ':
            i = "%20"
        res.append(i)
    return ''.join(res)

s = "We are happy."
res = replace(s)
print(res)

