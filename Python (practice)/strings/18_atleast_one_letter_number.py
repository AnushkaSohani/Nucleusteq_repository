def alpha(str1):
    n=len(str1)
    for i in range(n):
        resALpha=str1[i].isalpha()
        if(resALpha==True):
            return resALpha
        
def num(str1):
    n=len(str1)
    for i in range(n):
        resNum=str1[i].isnumeric()
        if(resNum==True):
            return resNum



str1=input("Enter a string ")

resAlpha=alpha(str1)
resNum=num(str1)

if(resAlpha ==True and resNum==True):
    print("True")
else:
    print("False")

