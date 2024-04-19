def charCount(s1,s2):
    s3=s1.intersection(s2)
    # print(s3)
    count=0
    print("Matching characters are: ")
    for i in s3:
        print(i)
        count=count+1
    return count


s1=input("Enter a string ")
s2=input("Enter another string ")
s1=set(s1)
s2=set(s2)
# print(s1,s2)
count=charCount(s1,s2)
print("Count = ",count)