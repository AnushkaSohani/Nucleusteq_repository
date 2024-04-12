from itertools import combinations
l=[1, 2, 3, 4]

o=combinations(l,1)
for i in o:
    print(list(i))

two=combinations(l,2)
for i in two:
    print(list(i))

three=combinations(l,3)
for i in three:
    print(list(i))

f=combinations(l,4)
for i in f:
    print(list(i))