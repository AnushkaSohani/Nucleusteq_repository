from itertools import combinations_with_replacement
l=["GFG", [5, 4], "is",["best", "good", "better", "average"]] 

# o=combinations(l,1)
# for i in o:
#     print(list(i))

two=combinations_with_replacement(l,2)
for i in two:
    print(list(i))

# three=combinations(l,3)
# for i in three:
#     print(list(i))