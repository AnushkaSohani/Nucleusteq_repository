import string
import random

s=input("Enter a string ")
n=len(s)
pr=string.printable

res=""
count=0
while(res!=s):
    res=random.choices(pr,k=n)
    res="".join(res)
    print(res)
    count=count+1

print(count)