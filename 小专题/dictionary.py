aa={'animal':'dog','girl':'mckay','boy':'bear',55:'aha'}
print(aa['boy'])


aa['hello']='word'
aa.update({'country':'china'})
# aa.pop('hello')
# del aa['hell']
aa['hello']=22
aa.update({'hhhhhhh':'33'})
print(aa['hello'])
print(aa.get('hello'))
print(aa)
aa={'animal':'dog','girl':'mckay','boy':'bear'}
for keys in aa:
    print(keys,aa[keys])

for i in aa.items():
    print(i[0]+':'+i[1])

