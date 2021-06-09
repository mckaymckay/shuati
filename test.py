# 283
def findzero(nums):
    length = len(nums)
    if length <= 1:
        return nums
    i, j = 0,0
    while j < length:
        if  nums[j] != 0:
            nums[i]=nums[j]
            i += 1
        j += 1
    for p in range(i,length):
        nums[p]=0

    return nums

nums=[0,0,0]
res=findzero(nums)
print(res)

def findzero2()