def swap(s):
    n=len(s)

    for i in range(n):
        if s[i]=="," or s[i]==","+" ":
            s[i]="."
        elif s[i]==".":
            s[i]=", "

    new="".join(s)
    return new

s=input("Enter a string ")
s=list(s)
# print(s)
new=swap(s)
print(new)