str1=input("Enter a string ")

str2=""

l1=list(str1.split())
# print(l1)

l1.reverse()
# print(l1)

str2=" ".join(l1)
print(str2)
