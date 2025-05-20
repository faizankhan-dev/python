# i=1
# while(i<=10):
#     print("faizan",i)
#     i+=1
#     print(i)

# n=int(input("Enter the number"))
# i=1
# ans=0
# while(i<=n):
#     ans=ans+i
#     i+=1
# print(ans)

n=int(input("Enter the number"))
i=1
even=0
odd=0
while(i<=n):
    if(n%2==0):
        even=even+i
    else:
        odd=odd+i
        i+=1
        
        print("even ",even)
        print("odd ",odd)