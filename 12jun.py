


# n=int(input("enter the number"))
# sum=0
# for i in range(1,n+1):
#     if(i%2==0):
#         sum=sum+(i**3)
#     else:
#         sum=sum+(i**2)


#     print(sum)

    
n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum=sum-(i**2)
    else:
        sum=sum+(i**2)


print(sum)