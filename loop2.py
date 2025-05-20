while(True):
    ch=int(input("enter your choice"))
    if(ch==1):
        n=int(input("enter the no."))
        i=1
        cnt=0
        while(i<=n):
            if(n%i==0):
                cnt+=1
            if(cnt==2):
                print("prime")
            else:
                print("not prime")
    elif(ch==2):
        n=int(input("enter the no."))
        i=1
        while(i<=10):
            print(n,"*",i,"=",n*i)
            i+=1
    elif(ch==3):
           n=int(input("enter the no."))
           i=1
           a=-1
           b=1
           while(i<=n):
               c=a+b
               a=b
               b=c
               print(c)
               i+=1
    elif(ch==4):
        n=int(input("enter the no."))
        p=len(str(n))
        asum=0
        temp=n
        while(n>0):
            r=n%10
            asum=asum+r**p
            n=n//10
        if(asum==temp):
            print("armstrong")
        else:
            print("Not armstrong")
    elif(ch==5):
        print("Palendrpm")
    elif(ch==6):
        print("Program close")
        break
    else:
        print("Wrong choice")

            