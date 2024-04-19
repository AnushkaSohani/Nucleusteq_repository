def symmetric(str1):
    s=0
    n=len(str1)
    st1=str1[0:n//2]
    st2=str1[n//2:]
    if(st1==st2):
        s=1
    return s

def palindrome(str1):
    n=len(str1)
    if(n%2==0):
        p=0       
        st2=""
        st1=str1[0:n//2]
        for i in range(n-1,n//2-1,-1):
            st2=st2+str1[i]
        if(st1==st2):
            p=1
        return p
    else:
        p=0       
        st2=""
        st1=str1[0:n//2+1]
        for i in range(n-1,n//2-1,-1):
            st2=st2+str1[i]
        if(st1==st2):
            p=1
        return p



str1=input("Enter a string ")

s=symmetric(str1)
if(s==1):
    print("Symmetric")

p=palindrome(str1)
if(p==1):
    print("Palindrome")
