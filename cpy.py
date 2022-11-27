import copy
l1=[['a',2],'sa','ra']
l2=copy.copy(l1)
l3=copy.deepcopy(l1)
print('list 1: ',l1,id(l1))
print('list 2: ',l2,id(l2))
print('list 3: ',l3,id(l3))
l3[0][0]='maa'
print(l1)
print(l2)
print(l3)
l2[0][0]='paa'
print(l2)
print(l1)