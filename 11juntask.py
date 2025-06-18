

# a=input("Enter a character to check =")
# fk=a.lower()
# if(fk=="a"or fk=="e"or fk=="i" or fk=="o" or fk=="u"):
#     print("VOWEL")
    
# else:
#     print("CONSONET")

#TO FIND ARMSTRONG
n=int(input("Enter the 3 digit no. "))
r=n
a=n%10
n=n//10
b=n%10
n=n//10

s=(n**3)+(b**3)+(a**3)
if r==s:
    print("This no. is Armstrong ",s)
else:
    print("Not armstrong ",r)

#To find febonachi series
