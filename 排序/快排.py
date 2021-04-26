'''
reference:https://zhuanlan.zhihu.com/p/63227573
复杂度分析:
最好的时间复杂度为：O（nlogn）
最坏的时间复杂度为：O（n**2）
平均时间复杂度为：O(nlogn)
平均空间复杂度为：O(logn)
'''


def quick_partition(lists, i, j):
    if i >= j:
        return lists
    length = len(lists)
    p = lists[i]
    low = i
    high = j
    while i<j:
        while i<j and lists[j]>=p:
            j-=1
        lists[i]=lists[j]
        while i<j and lists[i]<=p:
            i+=1
        lists[j]=lists[i]
    lists[i]=p
    quick_partition(lists,low,i-1)
    quick_partition(lists,i+1,high)
    return lists


if __name__ == '__main__':
    lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    print("排序前的序列为：")
    for i in lists:
        print(i, end=" ")
    print("\n排序后的序列为：")
    for i in quick_partition(lists, 0, len(lists) - 1):
        print(i, end=" ")
