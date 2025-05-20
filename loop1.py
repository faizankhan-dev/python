# n = int(input("Enter a  number: "))
# i=1
# ans=1
# fsum=0
# while(i<=n):
#     ans=ans*i
#     fsum=fsum+ans
    
#     i+=1
# print(f"factorial={ans}")
# print(f"sum={fsum}")


# n=int(input("Enter the number"))
# rev=0
# while(n>0):
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# print(rev)

# n=int(input("Enter the number"))
# rsum=0
# while(n>0):
#     r=n%10
#     rsum=rsum+r
#     n=n//10
# print(rsum)


n=int(input("Enter the number"))
cnt=0
i=1
while(i<=n):
  	if(n%i==0):
  		cnt+=1
	  
  
if(cnt==2):
  	print("prime no.")
  
else:
    print("not prime")
  