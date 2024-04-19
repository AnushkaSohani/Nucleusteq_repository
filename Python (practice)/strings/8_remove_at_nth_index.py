str1=input("Enter a string ")
ind=int(input("Enter an index to remove a character from string "))
n=len(str1)

if(ind>n):
    print("Enter valid index ")
else:
    str1=str1[0:ind]+str1[ind+1:]
    print(str1)
