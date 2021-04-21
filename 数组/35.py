# 搜索插入位置


def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if item == my_list[mid]:
            return mid
        elif item < my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
        print(low, high, mid)

    return low


my_list1 = [1, 2, 3, 5, 7]
obj = 8
print(binary_search(my_list1, obj))
print(-3 // 2)

print('*******************************************************')

# 📒：考点总结
# 注意1:定义变量的时候避开关键词
# 注意2:13行的return和while的位置
# 注意3:当插入值等于数组中的某一个元素时，两个return哪个是有用的
# python3地板除是向下取整，而不是向0取整

# 🚗：解题思路
# 首先注意数组是有序的
# 「只要看到面试题里给出的数组是有序数组，都可以想一想是否可以使用二分法。」
# 同时题目还强调数组中无重复元素，因为一旦有重复元素，使用二分查找法返回的元素下表可能不是唯一的。