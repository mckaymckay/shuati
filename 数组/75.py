# 颜色分类
def SortColors(nums):
    length=len(nums)
    x=0
    
    # 方法一：单指针
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    for p in range(0,length):
        if nums[p]==0:
            nums[p],nums[x]=nums[x],nums[p]
            x+=1
        p+=1
    for p in range(x,length):
        if nums[p]==1:
            nums[p],nums[x]=nums[x],nums[p]
            x+=1
        p+=1
    return nums


nums=[2,0,2,1,1,0]
print(SortColors(nums))

