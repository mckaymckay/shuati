# 移除元素
def removeElement(nums, item):
    length = len(nums)
    if length != 0:
        return 0
    i = 0
    j = 0
    while j < length:
        if nums[j] != item:
            if i != j:
                nums[i] = nums[j]
            i += 1
        j += 1
    return i, nums[:i]


nums = [1, 2, 6, 3, 3, 4, 3, 5, 3, 6, 7]
item = 3
print(removeElement(nums, item))

#class Solution:
# def removeElement(self, nums: List[int], val: int) -> int:
#     length=len(nums)
#     if length!=0:
#         a = 0
#         b=0
#         while a<length:
#             if nums[a]!=val:
#                 nums[b]=nums[a]
#                 b+=1
#             a+=1
#         return b
#     return 0