## 26.删除有序数组中的重复项

[官方解析](<https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/>)

### 1.难度:easy

### 2.重难点

* 看清楚return的是index，还是nums
* 注意**for**循环和**while**的使用区别，以及在两种循环上'+1'与否

### 3.解法

* #### 解法一

解题思路:双指针+for

```python
class Solution:
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
