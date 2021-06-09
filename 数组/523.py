# 连续的子数组和
def subarray(nums, k):
    length = len(nums)
    i, j, sub_len = 0, 0, length + 1
    sum = 0
    res = False
    res_array=[]
    while j < length:
        sum += nums[j]
        while j - i >0:
            if sum % k == 0:
                res = True
                sub_len = j - i
                sum-=nums[i]
            i += 1
        j += 1
    return res
 
nums=[5,0,0,0,3]
k=6
res=subarray(nums,k)
print(res)
