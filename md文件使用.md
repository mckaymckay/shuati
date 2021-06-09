
# 一级标题

## 二级标题

### 三级标题

-----------------------------------------------

## 26.删除有序数组中的重复项

### 难度:easy

[官方解析](<https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/>)

### 解题思路

### 重难点

### 解法一

---------------------------------------------

```python
def removeDuplicates(self, nums: List[int]) -> int:
    length = len(nums)
    i, j = 0, 1
    if length==0:
        return 0
    for j in range(1,length):
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
    return i + 1
```

```python
def init():
    pass
```

*文本*
__粗体文本__
***粗斜体文本***

> zuiwaiceng
>>yiceng
>>>erceng

代码地址[26](https://github.com/mckaymckay/shuati/blob/main/26.md)
