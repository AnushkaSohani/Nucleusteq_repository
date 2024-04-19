str=input("Enter a string ")
n=len(str)

if(n>=3):
    if(str[n-3:]=='ing'):
        str=str+ 'ly'
    else:
        str=str+'ing'

    print(str)
    
else:
    print(str)




