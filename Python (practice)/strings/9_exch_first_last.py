str1=input("Enter a string ")
n=len(str1)

# first=str1[0]
# last=str1[n-1]

# print(first)
# print(last)

str1=str1[n-1]+str1[1:n-1]+str1[0]
print(str1)