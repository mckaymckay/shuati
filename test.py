arr = [1,2,2,1,1,3,3]
count={}
res=[]
for i in arr:
    count[i]=count.get(i,0)+1
print(len(count))
for j in count:
    res.append(count[j])
print(res)
print(set(res))
