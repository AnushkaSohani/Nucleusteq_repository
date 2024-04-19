def countVowel(s,vowels):
    count=0
    for i in s:
        if i in vowels:
            count=count+1
    return count


s=input("Enter a string ")
s=s.lower()

vowels=set("aeiou")

c=countVowel(s,vowels)
print(c)