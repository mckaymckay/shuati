# 删除数组中的重复元素


def removeElement(my_list):
    length = len(my_list)
    i = 0
    if length == 0:
        return 0
    for j in range(1, length):
        if my_list[i] != my_list[j]:
            # my_list[i + 1], my_list[j] = my_list[j], my_list[i + 1]
            my_list[i + 1] = my_list[j]
            i += 1
        j += 1
    return i + 1

mylist = [1, 2, 3, 3, 4, 4, 5]
print(removeElement(mylist))
print(mylist)

print('*******************************************************')

# 优化
# 考虑一下数组，mylist=[1,2,3,4,5],数组中没有重复元素，按照上面的写法，i和j指向的元素都不相等，
# 所以j指向的元素都会原地复制一遍，这个操作是没有必要的，
# 所以添加一个小判断，当j-i>1时，再进行复制。

def removeElement2(my_list):
    length = len(my_list)
    if length == 0:
        return 0
    i = 0
    j = 1
    while j < length:
        if my_list[i] != my_list[j]:
            if j - i > 1:
                # my_list[i+1],my_list[j]=my_list[j],my_list[i+1]
                my_list[i + 1] = my_list[j]
            i += 1  ##
        j += 1
    return i + 1

mylist1 = [1, 2, 3, 3, 4, 4, 5]
print(removeElement2(mylist1))
print(mylist1)

print('*******************************************************')

# 🚗：解题思路
# 解法： 双指针
# 首先注意数组是有序的，那么重复的元素一定会相邻。
# 要求删除重复元素，实际上就是将不重复的元素移到数组的左侧。