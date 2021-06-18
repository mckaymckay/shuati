## 字典

### 概念分析

* 1.键一般是唯一的，值不需要唯一

```python
dict1={'a': 1, 'b': 2, 'b': '3'}
>>> dict1['b']
'3'
>>> dict1
'a': 1, 'b': '3'
```

* 2.键必须是不变的，如字符串、数字或元组；值可以是任何数据

```python
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }
```

* 3.字典无序：遍历字典元素时，与添加元素的顺序是无关的！

### 操作

#### 1.获取值

```python
dict1={'animal':'dog','girl':'mckay','boy':'bear',55:'aha'}
print(dict1['boy'])
print(dict1[55])
print(dict1[6])
>>> bear
aha
>>> Traceback (most recent call last):
  File "/Users/mckay/Desktop/VsCodeProject/刷题/shuati/小专题/dictionary.py", line 5, in <module>
    print(dict1[44])
    KeyError: 44
```

#### 2.增

* 1）使用[]

```python
dict1['hello']='word'

>>> {'animal': 'dog', 'girl': 'mckay', 'boy': 'bear', 55: 'aha', 'hello': 'word'}
```

* 2）使用update() (update()函数还有其他变种)
[参考](<https://blog.csdn.net/cadi2011/article/details/85857917>)

```python
dict1.update({'country':'china'})

>>> {'animal': 'dog', 'girl': 'mckay', 'boy': 'bear', 55: 'aha', 'hello': 'word', 'country': 'china'}
```

#### 3.删

* 1）pop()：找不到对应的key，会抛出异常KeyError
* 2）pop(,''):增加容错
* 3）popitem()：随即删除一个Entry
* 4）del():找不到对应的key，会抛出异常KeyError
* 5）clear():清空全部元素

```python  
dict1.pop('hello')  #返回值是'word'
smart_girl.pop("animal", "容错方案")  #找不到key，返回指定的默认值
dict1.popitem() #返回被删除的Entry
del dict1['55]
dict1.clear()
del dict1
```

* 6）del:清空字典对象

#### 4.改

* 1) 直接修改，key不存在时添加key-value到字典中

```python
dict1['animal']='cat'
```

* 2) update():key不存在时添加key-value到字典中

```python
dict1.update({'hello':'dameng'})
```

#### 5.查

* 1）直接查找:找不到对应的key，会抛出异常KeyError

```python
dict1['hello]  
```

* 2）get（）

```python
dict1.get('hello')
# 或者
dict1.get('hello','not avaliable')
```

* 3）setdefault（）:同get()方法

```python
dict1.setdefault('hello')
# 或者
dict1.setdefault('hello','not avaliable')
```

### 6.遍历

* 1) for in

```python
dict1={'animal':'dog','girl':'mckay','boy':'bear'}
for i in dict1:
    print(i,aa[i])
>>> animal dog
girl mckay
boy bear
```

* 2)dict的keys()方法 : 可以得到dict的所有**key**值

```python
for i in dict1.keys():
    print(i)
>>>animal
girl
boy
```

* 3)dic的values()方法：可以得到dict的所有**value**值

```python
for i in dict1.values():
    print(i)
>>>dog
mckay
bear
```

* 4) dict的items()方法：遍历dict中的每一个key-value

```python
for i in dict1.items():
    print(i)
>>>('animal', 'dog')
('girl', 'mckay')
('boy', 'bear')
```

# 如果把每个元组的元素都分别取出来，就能输出key和value

```python
print(i[0]+':'+i[1])
>>>animal:dog
girl:mckay
boy:bear
```
