str1="mystring"
print(type(str1))
x=str1.upper()
print(x)
em="FAIZANKHAN@GMAIL.COM"
y=em.lower()
print(y)
str3="WELCOME"
print(str3[0:3:2])
print("reverse=",str3[::-1])
str1="HELLO"
rev=""
for i in str1:
    rev=i+rev
    print(rev)
    s2="hello"
    s3="bhopal"
    s4=s2+" "+s3
    print(s4)

    s=input("Enter the string")
    x=s.lower()
    vcnt=0
    ccnt=0
    for i in x:
        if(i=="a" or i=="e" or i=="i" or i=="o"or i=="u"):
            # print("Vowels",i)
            vcnt+=1
        else:
            # print("consonent",i)
            ccnt+=1
    print("vowel",vcnt)
    print("consonent",ccnt)
 