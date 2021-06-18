


def uncommonFromSentences(s1,s2):
    C = s1.split() + s2.split()
    count = {}
    for i in C:
        count[i] = count.get(i, 0) + 1
    b=[]
    for a in count.keys():
        if count[a]==1:
            b.append(a)
    return b

s1='i am a girl'
s2='i am a boy'
print(uncommonFromSentences(s1,s2))
print(s1)
d=(s1+' '+s2).split()
print(d)
for i in d:
    print(d.count(i))