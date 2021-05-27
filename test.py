# 27
def test(nums):
    length = len(nums)
    if length != 0:

        p, p0 = 0, 0
        while p < length:
            if nums[p] == 0:
                nums[p], nums[p0] = nums[p0], nums[p]
                p0 += 1
            p += 1

        p = p0
        while p < length:
            if nums[p] == 1:
                nums[p], nums[p0] = nums[p0], nums[p]
                p0 += 1
            p += 1
        return nums
    return None

    # shuangzhizhen
    # p, p0, p2 = 0, 0, length - 1
    # while p <= p2:
    #     while nums[p] == 2 and p <= p2:
    #         nums[p], nums[p2] = nums[p2], nums[p]
    #         p2 -= 1

    #     if nums[p] == 0:
    #         nums[p], nums[p0] = nums[p0], nums[p]
    #         p0 += 1
    #     p += 1
    # return nums
    return None


mylist = [2, 0, 2, 1, 1, 2]
val = 2
res = test(mylist)
print(res, '&&')
print(mylist)
