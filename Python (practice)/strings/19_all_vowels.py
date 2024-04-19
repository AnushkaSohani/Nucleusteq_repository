def allVowels(s,vowels):
    
    if vowels.issubset(s):
        print("Accepted")
    else:     
        diff=vowels.difference(s)
        print("Vowels",end=" ")
        for i in diff:
            print(i,",", end=" ")
        print("are not present")
        print("Not accepted")
    


s=input("Enter a string ")
s=s.lower()
s=set(s)

vowels={'a','e','i','o','u'}
allVowels(s,vowels)