# 基于快排:
def quick_partition(nums, i, j):
    if i >= j:
        return nums
    pivot = nums[i]
    low, high = i, j
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]
    nums[i] = pivot
    quick_partition(nums, low, i - 1)
    quick_partition(nums, i + 1, high)
    


nums = [3, 2, 1, 5, 6, 4]
length = len(nums)
quick_partition(nums, 0, length - 1)
print(nums)

print('-----------------------------我是分割线-----------------------------')
def quick_sort(nums,k):
    length=len(nums)
    nums.sort()
    return nums[length-k]

nums=[2,1,9,2,4]
res=quick_sort(nums,3)
print(res)

'''
sort()函数与sorted的区别
对List排序，Python提供了两个方法
1. 用sort()函数
2. 用List的内建函数sorted()

sort函数定义：sort(cmp=None, key=None, reverse=False)
sorted函数定义：sorted(iterable, cmp=None, key=None, reverse=False)

区别: 
sort()函数对已存在的列表进行操作,调用其没有返回值;
而sorted( )函数是返回一个新的list,不在原来的list上进行操作,调用其返回一个排好序的list

例:
'''
a=[2,1,3,9,6]
a.sort()
print('a',a)

b=[2,1,3,9,6]
c=sorted(b)
print('b',b)
print('c',c)
