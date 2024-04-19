str1=input("Enter str1 ")
str2=input("Enter str2 ")

str3=str1.replace(str1[:2],str2[0:2])
str4=str2.replace(str2[:2],str1[0:2])

str3=str3+" "+str4
print(str3)