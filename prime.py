n1=int(input("Enter thr num1:"))
n2=int(input("Enter thr num2:"))
n3=n1+1
i=1
while(i<=n2):
    temp=n3
    count=0
    j=1
    while(j<=temp):
        if(temp%j==0):
          count+=1
    j+=1
    if(count==2):
        print("prime",temp)
        i+=1
    n3+=1