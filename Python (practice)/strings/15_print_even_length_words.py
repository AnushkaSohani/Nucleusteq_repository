def evenWord(str1):
    l1=list(str1.split())
    for i in l1:
        if(len(i)%2==0):
            print(i,end=" ")

str1=input("Enter a string ")
evenWord(str1)