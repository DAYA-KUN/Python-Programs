#Union, intersection,difference,symmetric difference, subset & superset

set1={1,2,3,4}
set2={3,4,5,6}

print(set1 | set2)#union
print(set1 & set2)#inter
print(set1 - set2)#diff
print(set1 ^ set2)#sym diff

a={1,2}
b={1,2,3}

print(a <= b) #subset
print(b >= a) #superset
