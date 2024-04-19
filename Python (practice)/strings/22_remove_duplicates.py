def removeDup(s):
    st=""
    for i in s:
        if i not in st:
            st=st+i

    return st

s=input("Enter a string ")
st=removeDup(s)
print(st)