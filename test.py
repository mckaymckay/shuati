


def find():
    A = "this apple is sweet"
    B = "this apple is sour"
    C=A.split()+B.split()
    print(C)
    count={}
    for i in C:
        count[i]=count.get(i,0)+1
    return [i for i in count if count[i]==1]


print(find())
        
