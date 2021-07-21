def quicksort(nums, i, j):
    length = len(nums)
    if i >= j:
        return nums
    pivot = nums[i]
    low, high = i, j
    while i<j:
        while i<j and nums[j]>=pivot:
            j-=1
        nums[i]=nums[j]
        while i<j and nums[i]<=pivot:
            i+=1
        nums[j]=nums[i]
    nums[i]=pivot
    quicksort(nums,0,low-1)
    quicksort(nums,i+1,high)

def findelement(nums,k):
    quicksort(nums,0,len(nums)-1)
    return nums[k-1]


if __name__ == '__main__':
    lists=[3,2,3,1,2,4,5,5,6] 
    print('排序前的序列：', lists)
    quicksort(lists, 0, len(lists)-1)
    print('\n排序后的序列：', lists)
    print(findelement(lists,4))

