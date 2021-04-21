# 自己写的答案：两次遍历
# 时间复杂度:O(n)
# 空间复杂度:O(1)
def removeZeros(nums):
    length = len(nums)
    if length != 0:
        i = 0
        j = 0
        while j < length:
            if nums[j]:
                nums[i] = nums[j]
                # if i!=j:
                #     nums[j]=0
                i += 1
            j += 1
        # 第二次遍历把末尾的元素都赋值为0
        for a in range(i, length):
            nums[a] = 0
        return nums
    return 0


# 官方答案:一次遍历
# 时间复杂度:O(n)
# 空间复杂度:O(1)
def removeZeros1(nums):
    length = len(nums)
    if length != 0:
        i = 0
        j = 0
        while j < length:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums
    return 0


arr = [0, 1, 0, 3, 0, 3]
print(removeZeros(arr))