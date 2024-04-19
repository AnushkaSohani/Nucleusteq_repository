def capital(str1):
    str1=str1.title()
    # print(str1)

    l1=list(str1.split())
    # print(l1)

    for words in l1:
        n=len(words)
        # print(n)
        for j in range(n):
            if(j==n-1):
                words=words[0:n-1]+words[n-1].upper()
        print(words,end=" ")

str1=input("Enter a string ")
capital(str1)


