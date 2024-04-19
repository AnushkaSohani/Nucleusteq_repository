from itertools import permutations
s=input("ENter a string ")
perSet=set()
per=permutations(s)
for i in per:
    i="".join(i)
    perSet.add(i)

for i in perSet:
    print(i)
