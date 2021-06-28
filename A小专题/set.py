'''

https://www.runoob.com/python3/python3-set.html

# 集合（set）是一个无序的不重复元素序列

注意：创建一个空集合必须用set()，而不是{ }，
因为{}是创建一个字典

创建格式：
newest = { value1, value2 }
或者 
set( value1, value2)
'''

# 1.创建
newset1 = {'spring', 'summer'}
# or
newset = set({'spring', 'summer'})  # 用{}扩起来,只有一个元素的话可以不用{}
print(newset)
print(newset1)

# 2.add/update
newset.add('autumn')
newset.update({'winter'})  # 用{}扩起来
newset.update('hello')  # 查看区别,添加进了4个字母
print(newset)

# 3.remove() / discard() / pop()
newset.remove('winter')  # 不存在会发生错误
newset.discard('summer')  # 不存在不会发生错误
newset.pop()  # 会有返回值
print(newset)

# 其他
'''
x in newset
newset.clear()
len(newset)
'''