def return_with_argument(a,b,c,d):
    return a,b,c,d
x= return_with_argument(12,13,14,15)
ad=0
for i in x:
    ad=ad+i
    print(i)
print(ad)

#multiple value
def return_without_argument():
    a=13
    b=23
    c=45
    d=23

    return a,b,c,d
x= return_without_argument()
ad=0
for i in x:
    ad=ad+i
    print(i)
print(ad)



# N0 RETURN WIRH ARGUMENT
def four_factor(n1,n2):
    for i in range(n1,n2+1):
        cnt=0
        for j in range(1,i+1):
            if(i%j==0):
                cnt+=1
            if(cnt==4):
              print(i)
            
n1=int(input("enter the no.1:"))
n2=int(input("enter the no.2:"))
four_factor(n1,n2)
# TYPE OF ARGUMENT
def myfunc(a,c):
    print("a=",a)
    def myfunc(b):
        
        myfunc(12)
