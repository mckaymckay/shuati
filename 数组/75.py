# 颜色分类
def SortColors(nums):
    length = len(nums)

    # 方法一：单指针
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    x = 0
    for p in range(0, length):
        if nums[p] == 0:
            nums[p], nums[x] = nums[x], nums[p]
            x += 1
    for p in range(x, length):
        if nums[p] == 1:
            nums[p], nums[x] = nums[x], nums[p]
            x += 1
    return nums


print('-----------------------------------------------')

# 步骤
# 🚗：如果找到了0，将其与位置x交换，并将x向后移动一个位置；
# 🚗：如果找到了2，将其与位置y交换，并将y向前移动一个位置；
# 问题有一，如果p和y处都为2，交换位置后p+1，将会产生错误，所以需要不断的进行交换；
# 这就决定了先判断nums[]==2,并且判断==2时用‘while’
# 问题有二，终止时间，如果p>y了，程序结束。


def SortColors2(nums):
    length = len(nums)
    p, x, y = 0, 0, length - 1
    # ⬇️首先这是大的循环条件
    while p <= y:
        # 这是小循环条件，有循环就要考虑终止条件和区间
        while nums[p] == 2 and p <= y:
            nums[p], nums[y] = nums[y], nums[p]
            y -= 1
        if nums[p] == 0:
            nums[p], nums[x] = nums[x], nums[p]
            x += 1
        p += 1
    return nums


nums = [2, 0, 2, 1, 1, 0]
print(SortColors(nums))
nums = [1, 0]
print(SortColors2(nums))

# 问题： 注意 为什么要写'while p<=y',而不能写'for p in range(0,y)'!!!