def specialChar(s):
    a=0
    for char in s:
        if char.isalnum()==False and char!=" ":
            a=-1

    return a


s=input("Enter a string ")
a=specialChar(s)
if(a==0):
    print("Accepted")
else:
    print("Not accepted")

