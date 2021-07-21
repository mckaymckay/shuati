'''
准确来说，python是没有数组类型的，只有列表和元组；
数组是numpy库定义的，所以在使用数组之前要先引用numpy库
见：列表、元组、数组的区别
https://zhuanlan.zhihu.com/p/210779471

string to list & list to string
见：https://blog.csdn.net/bufengzj/article/details/90231555
'''

li = ['a', 'b', 'c', 'd', 'e']
string = "abcde"
print(type(li), type(string))  # <class 'list'> <class 'str'>

# 1.list to string

a = ''.join(li)
print(a)  # abcde <class 'str'>

b = ','.join(li)
print(b)  # a,b,c,d,e <class 'str'>

# 2.string to list
c=list(string)
print(c)  # ['a', 'b', 'c', 'd', 'e'] <class 'list'>

d='abd d'
print(list(d))  # ['a', 'b', 'd', ' ', 'd']
print(d.split()) # ['abd', 'd']
print(d.split(' ')) # ['abd', 'd']

# 3.python里字符串数组转化为整型， 用list(map(type,arr))函数
e = ['22','44','66','88']
e=map(int,e)
print(list(e))
