def checkBin(s):
    b={"0","1"}

    bin=0
    for char in s:
        if(char not in b):
            bin=-1
            return bin



s=input("Enter a string ")
binary=checkBin(s)
if(binary==-1):
    print("Not a binary string ")
else:
    print("Binary string")