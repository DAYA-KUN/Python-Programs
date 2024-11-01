l=[1,2,3,4,5,[6,7]]
l2=l.copy()
l2[5].append(8)
l2[2]=4
print(l)
print(l2)


l1=[1,2,3,[4,5]]
l2=l1.copy()
l2[3]=[4,5,6]
print(l2)
print(l1)