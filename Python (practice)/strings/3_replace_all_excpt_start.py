str=input("Enter a string ")

first=str[0]
str=str.replace(first,'$')
str=first+str[1:]

print(str)