# arr = [1,2,2,4,5]
# length=len(arr)
# nums=list.copy(arr)
# for i in range(1,length+1):
#     if i in arr:
#         arr.remove(i)
#     else:
#         notfound=i
# print((arr[0],notfound))
# print(nums)

# print('----------------------------------')
# arr = [1,2,2,4,5]
# count={}
# for i in arr:
#     count[i]=count.get(i,0)+1
# print(count)
# print(list(count.keys()))
# # aa for aa in list(count.keys() if )
# for j in range(1,length+1):
#     if j not in count:
#         notfound=j
#     elif count[j]==2:
#         twofound=j
# print(twofound,notfound)

# print('----------------------------------')
# nums=[2,2,9,4,4,5,5,6,6]
# res=nums[0]
# for i in range(1,len(nums)):
#     res ^= nums[i]
# print('res=',res)
# a=10
# b=100
# print(a^b)

# print('----------------------------------')

# newset=set()
# newset.add(9)

# print(9 in newset)
# print(newset.pop())
# nums=[2,2,9,4,4,5,5,6,6]
# for i in nums:
#     # print(i)
#     pass
# res=set({'1','2'})
# res1={'1','2'}
# print(res)

# print('----------------------------------')
# nums=[2,2,3,2]
# res_set=set()
# res_sum=0
# set_sum=0
# for i in nums:
#     res_sum+=i

# for j in nums:
#     res_set.add(j)

# for k in res_set:
#     set_sum+=k
# print((3*set_sum-res_sum)//2)

print('----------------------------------')
nums = [2, 2, 3, 4, 3, 5, 6, 6, 7, 7]
res = 0
a, b = 0, 0
# 所有数字的异或结果
for i in nums:
    res ^= i
    print(res)
# 找到res第一个不为0的位置
# h = 1
# while(res & h == 0):
#     h << 1
h = res & -res
print(h)

for j in nums:
    if j & h == 0:
        a ^= j
    else:
        b ^= j
print([a, b])

print('----------------------------------')
s = 'anagram'
count2 = {}
for i in s:
    count2[i] = count2.get(i, 0) + 1
print(count2)
t = 'nagaram'
count1 = {}
for j in t:
    count2[j] = count2.get(j) - 1
print(count2)
print(set(s))
record = [{0} for _ in range(26)]
record[1] = 1
print(record)

print('----------------------------------')
nums = [1, 2, 3, 4, 3, 2, 1, 4, 5, 6]
res = set(nums)
print(res)

print('----------------------------------')
test = list()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

print('----------------------------------')
count = {}
nums = [1, 2, 3]
for i in nums:
    count[i] = count.get(i, 0) + 1
print(count)
nums1 = [1, 2, 2, 4]
for j in nums1:
    count[j] = count.get(j, 0) - 1
print(count)

print('----------------------------------')
nums = [1, 2, 2, 2, 3, 4, 5]
print(list(set(nums)))

print('----------------------------------')
div = divmod(19, 10)
res = 0
for i in div:
    print(i * i)
    res += i * i

print(res)
a, b = divmod(19, 10)
print(a, b)

print('----------------------------------')


def get_next(n):

    if n > 0:
        res = 0
        a, b = divmod(n, 10)
        print(a, b)
        res += b**2
    return res


print(get_next(19))
print('----------------------------------')

res = str(19)
a = 0
for i in res:
    a += int(i)**2
print(a)

print('----------------------------------')
randsom = 'a'
magezine = 'b'
count = {}
for i in magezine:
    count[i] = count.get(i, 0) + 1

print(count)
for j in randsom:
    count[j] = count.get(j, 0) - 1
    if count.get(j) < 0:
        print(11)
print(count)
from collections import Counter
h = Counter(magezine)
print(h[9])
dict1 = Counter()
nums = [1, 2, 3]
dict2 = {}
print('count_dict:', dict1[2])
print('hash_dict:', dict2.get(2))

print('----------------------------------')
nums = [1, 2, 2]
count = {}
for i, num in enumerate(nums):
    count[num] = i
print(count)

print('*' * 100)
nums = "ab"
nums1 = "aa"
count = {}
for i in nums:
    count[i] = count.get(i, 0) + 1
for j in nums1:
    count[j] = count.get(j, 0) - 1
    print(count[j])
print(count.get(9))

from collections import Counter
res = Counter(nums)
print(res[9])

print('----------------------------------')
nums = [-1, 0, 1, 2, -1, -4]
for i in range(5):
    for j in range(i + 1, 5):
        if 0 - nums[i] - nums[j] in nums[j + 1:]:
            print(11)

print('----------------------------------')
arr = ["h", "e", "l", "l", "o"]
arr.reverse()
print(arr)

left, right = 0, len(arr)-1
while left <right:
    print(left)
    arr[left],arr[right]=arr[right],arr[left]
    left += 1
    right -= 1
print(arr)

print('----------------------------------')
nums = [3,5,2,3]
nums.sort()
res=[]
length=len(nums)
i,j=0,length-1
while i<j:
    res.append(nums[i]+nums[j])
    i+=1
    j-=1
rr=max(res)
print(rr)