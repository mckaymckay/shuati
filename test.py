arr = [1,2,2,4,5]
length=len(arr)
nums=list.copy(arr)
for i in range(1,length+1):
    if i in arr:
        arr.remove(i) 
    else:
        notfound=i
print((arr[0],notfound))
print(nums)
print('----------------------------------')

arr = [1,2,2,4,5]
count={}
for i in arr:
    count[i]=count.get(i,0)+1
print(count)
print(list(count.keys()))
# aa for aa in list(count.keys() if )
for j in range(1,length+1):
    if j not in count:
        notfound=j
    elif count[j]==2:
        twofound=j
print(twofound,notfound)

